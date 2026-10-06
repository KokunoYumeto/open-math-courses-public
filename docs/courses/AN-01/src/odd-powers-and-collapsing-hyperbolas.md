# Odd powers and collapsing hyperbolas

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition by GPT-6.1 Sol (OpenAI). Original exposition: CC0. Self-checked by the writing AI.*

The two endpoints \(t=\pm|\epsilon|\) approach the same point as \(\epsilon\to0\). With opposite weights, their singular powers have a limit at every complex order. The reason is visible on tests: an odd difference cancels the denominator produced by the square-root substitution. We prove the required smoothness, construct the entire family by ordinary integrals, and calculate the point derivatives and finite asymptotic expansions.

The full normalized-power construction is in [Finite parts of singular powers](finite-parts-of-singular-powers.md), formula (N1) and its proof. Its supplied [gamma foundations](../prerequisites/U011-free-foundations/gamma-foundations-U016.md), (G0)–(G2) and (W4a)–(W4e), prove the reciprocal Gamma function and every logarithmic bound used in parameter differentiation. The [finite-order test topology](order-positivity-and-limits.md), Definition (1.2) and Proposition 1.2, gives the distribution criterion. The [one-variable identity theorem](gluing-holomorphic-sides.md), Lemma 3.2, justifies continuation of scalar test pairings. The [angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A5, supply \(\Gamma(1/2)=\sqrt\pi\) from the fully proved Gaussian integral. All other calculus steps, including the square-variable smoothness, are proved below from these supplied inputs.

The complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the finite-order remainders used here, including signed increments, complex-valued functions, directional derivatives and uniform bounds for all required derivatives on compact neighborhoods.

## 1. Normalize before composing

A distribution pairs complex linearly with a test. We write \(T'(\phi)=-T(\phi')\), \(\delta_c(\phi)=\phi(c)\), and \(p_j(\phi)=\max_{\ell\le j}\|\phi^{(\ell)}\|_\infty\). Positive real powers use \(s^a=\exp(a\log s)\), with the real logarithm.

Let \(C_a\) be the entire family from U016. Its established identities are

\[
\begin{gathered}
C_a(s)=\frac{s_+^a}{\Gamma(a+1)}\quad(\operatorname{Re}a>-1),\\
\partial_sC_a=C_{a-1},\qquad C_0=1_{\{s>0\}},\\
C_{-k}=\delta_0^{(k-1)}\quad(k\ge1),\qquad
\operatorname{supp}C_a\subset[0,\infty).
\end{gathered}
\tag{1.1}
\]

In particular the first expression does not define a product of separately divergent objects outside its stated initial half-plane. The entire reciprocal \(G=1/\Gamma\) satisfies \(G(z)=zG(z+1)\) and \(G(1)=1\), by the complete supplied product proof.

For real \(\epsilon\ne0\), begin in the ordinary integrable region with

\[
u_{a,\epsilon}(t)=
\operatorname{sgn}(t)\,G(a+1)(t^2-\epsilon^2)_+^a,
\qquad \operatorname{Re}a>-1 .
\tag{1.2}
\]

Both boundary zeros are simple, so this function is locally integrable at the endpoints under exactly that exponent condition. It vanishes in the open gap between them. For all remaining orders, the definition will be the entire continuation constructed on tests. We use \(U_a\) for the eventual *odd* limit; this notation is local to this lesson and is different from the unnormalized one-sided family also called \(U_a\) in U016.

## 2. A descended test remains smooth

For \(\phi\in C_c^\infty(\mathbb R)\) supported in \([-R,R]\), \(R>0\), set

\[
b_\phi(t)=\frac{\phi(t)-\phi(-t)}{2t}\ (t\ne0),\qquad
b_\phi(0)=\phi'(0),\qquad
q_\phi(x)=b_\phi(\sqrt x)\quad(x\ge0).
\tag{2.1}
\]

**Lemma 2.1 (odd tests under square descent).** The function \(q_\phi\) is smooth on \([0,\infty)\), meaning that its successive right derivatives exist and are continuous at zero. It vanishes for \(x>R^2\). For every integer \(p\ge0\),

\[
\|q_\phi^{(p)}\|_\infty
 \le 2^{-p}\|\phi^{(2p+1)}\|_\infty,\qquad
q_\phi^{(p)}(0)=\frac{p!}{(2p+1)!}\phi^{(2p+1)}(0).
\tag{2.2}
\]

**Proof.** We first prove smooth division by the coordinate. If a smooth \(h\) satisfies \(h(0)=0\), the scalar FTC gives

\[
\frac{h(t)}t=\int_0^1h'(vt)\,dv,\qquad
\left(\frac ht\right)^{(j)}(t)=\int_0^1v^jh^{(j+1)}(vt)\,dv .
\tag{2.3}
\]

The integrals define the value at zero as well. They are smooth: on a compact interval, apply the FTC to the difference quotient of the integrand, whose next derivative is uniformly bounded for \(0\le v\le1\); dominated convergence then passes the derivative under the integral. Induction gives all derivatives. Thus division costs one derivative, with bound at most \(\|h^{(j+1)}\|_\infty\), and its \(j\)-th derivative at zero is \(h^{(j+1)}(0)/(j+1)\).

Apply this to \(h(t)=(\phi(t)-\phi(-t))/2\). The quotient \(b=b_\phi\) is even, smooth, zero for \(|t|>R\), and has
\(\|b^{(j)}\|_\infty\le\|\phi^{(j+1)}\|_\infty\).
For any even smooth function \(b\), \(b'(0)=0\). A second application of the proved division formula gives an even smooth function

\[
Tb(t)=\frac12\int_0^1b''(vt)\,dv,\qquad
Tb(t)=\frac{b'(t)}{2t}\ (t\ne0),\qquad
\|(Tb)^{(j)}\|_\infty\le\tfrac12\|b^{(j+2)}\|_\infty .
\tag{2.4}
\]

Iterating this integral, define \(b_p=T^pb\). Each \(b_p\) is smooth and even and satisfies \(\|b_p^{(j)}\|_\infty\le2^{-p}\|b^{(2p+j)}\|_\infty\). For \(x>0\), ordinary differentiation gives \(q_\phi^{(p)}(x)=b_p(\sqrt x)\). Each right side has a continuous limit at zero. To verify that these are actual boundary derivatives, integrate the derivative identity on \([\delta,x]\), then let \(\delta\downarrow0\). Continuity and boundedness give

\[
b_{p-1}(\sqrt x)-b_{p-1}(0)
 =\int_0^x b_p(\sqrt s)\,ds\qquad(p\ge1).
\tag{2.5}
\]

The FTC on the half-line proves the assertion at every successive derivative order. The stated norm bound now follows from the bounds on \(b_p\) and \(b\).

Evenness makes every odd derivative of \(b\) at zero vanish: differentiate \(b(-t)=b(t)\) and put \(t=0\). Its finite Taylor formula through degree \(2p\), with a remainder \(o(t^{2p})\) obtained by continuity of the highest derivative in the integral remainder, contains only even powers. Substituting \(t=\sqrt x\) and comparing with the already justified Taylor formula for the smooth half-line function gives \(q_\phi^{(p)}(0)=p!b^{(2p)}(0)/(2p)!\). Formula (2.3) gives \(b^{(2p)}(0)=\phi^{(2p+1)}(0)/(2p+1)\), proving the second identity (2.2). Compact support follows directly from (2.1); smoothness at \(R^2>0\) also follows from composition with the smooth square root there. All the operations are linear. \(\square\)

Only smoothness on the attained half-line is needed. There is no unproved extension to negative square variables and no application of a distribution to a nonsmooth test.

## 3. A formula valid at every complex order

In the initial region, let \(e=|\epsilon|\) and combine the integrals over \(t>e\) and \(t<-e\). On the positive half use \(s=t^2-e^2\). On truncated intervals away from \(e\), the ordinary substitution theorem follows from the scalar FTC; absolute integrability permits passage to the endpoints. The test factor is precisely

\[
q_\phi(s+e^2)
 =\frac{\phi(\sqrt{s+e^2})-\phi(-\sqrt{s+e^2})}
        {2\sqrt{s+e^2}} .
\tag{3.1}
\]

It follows that

\[
\langle u_{a,\epsilon},\phi\rangle
 =G(a+1)\int_0^\infty s^a q_\phi(s+e^2)\,ds
 \qquad(\operatorname{Re}a>-1).
\tag{3.2}
\]

For \(\eta\ge0\), integer \(N\ge0\), and \(\operatorname{Re}(a+N)>-1\), define

\[
I_N(a,\eta;\phi)=(-1)^N G(a+N+1)
 \int_0^\infty s^{a+N}q_\phi^{(N)}(s+\eta)\,ds .
\tag{3.3}
\]

Every integral has support in \(0\le s\le R^2\). This formula uses ordinary integrals of the smooth half-line function just constructed.

**Theorem 3.1 (entire continuation and collapse).** All allowed indices \(N\) give the same value. At \(\eta>0\) they define the unique entire continuation \(v_a(\eta)=u_{a,\sqrt\eta}\) of (1.2); at \(\eta=0\) they define an entire distribution family \(U_a\). For every \(a\in\mathbb C\),

\[
v_a(\eta)\longrightarrow U_a\quad\hbox{in }\mathcal D'(\mathbb R),
\qquad \eta\downarrow0 .
\tag{3.4}
\]

More precisely, if \(A\subset\mathbb C\) is compact and \(N\) satisfies \(\min_{a\in A}\operatorname{Re}(a+N)>-1\), then

\[
\begin{aligned}
|I_N(a,\eta;\phi)|&\le B_{A,N,R}\,p_{2N+1}(\phi),\\
|\langle v_a(\eta)-U_a,\phi\rangle|
 &\le B_{A,N,R}\,\eta\,p_{2N+3}(\phi)
\end{aligned}
\tag{3.5}
\]

for \(a\in A\), \(\eta\ge0\), and tests on the fixed support. Consequently convergence is uniform on every bounded collection of such tests and locally uniform in the complex order. Both signs of \(\epsilon\) have the same limit.

**Proof.** On the full adjacent overlap \(\operatorname{Re}(a+N)>-1\), integration by parts gives

\[
\int_0^\infty s^{a+N+1}q_\phi^{(N+1)}(s+\eta)\,ds
 =-(a+N+1)\int_0^\infty s^{a+N}q_\phi^{(N)}(s+\eta)\,ds .
\tag{3.6}
\]

The upper boundary vanishes by support. At the lower boundary the exponent \(a+N+1\) has positive real part, while \(q_\phi^{(N)}\) is bounded. Thus that boundary also vanishes. Gamma recursion proves \(I_{N+1}=I_N\) throughout this overlap; adjacent steps compare any two permitted indices.

For \(\sigma=\operatorname{Re}(a+N)>-1\), the absolute value of (3.3) is at most

\[
|G(a+N+1)|\,\frac{R^{2(\sigma+1)}}{\sigma+1}
        \|q_\phi^{(N)}\|_\infty .
\tag{3.7}
\]

Together with (2.2) this is a finite-order bound on each fixed-support test space, hence a distribution by U008's proved criterion. On compact \(A\), the exponent margin is positive and all factors in (3.7) are bounded, proving the first line of (3.5).

These pairings are holomorphic on each permitted half-plane. In fact each complex derivative differentiates \(G\) and inserts a power of \(\log s\) in the integral. The supplied gamma foundation proves
\(\int_0^1s^{\delta-1}|\log s|^j\,ds=j!/\delta^{j+1}\)
for \(\delta>0\), and proves complex differentiation by dominated difference quotients. This controls the endpoint at zero uniformly on compact parameter sets; on \([1,R^2]\), when nonempty, everything is bounded. Thus every fixed parameter derivative has the same test order \(2N+1\), with a different constant. The compatible half-planes cover \(\mathbb C\), giving an entire family. Formula (3.2) identifies the initial values at \(\eta>0\). The scalar identity theorem after each test pairing gives uniqueness.

Finally, the half-line FTC gives

\[
|q_\phi^{(N)}(s+\eta)-q_\phi^{(N)}(s)|
 \le\eta\,\|q_\phi^{(N+1)}\|_\infty .
\tag{3.8}
\]

For \(s>R^2\) both terms vanish. Apply (3.7) to their difference and then (2.2) to obtain the second line of (3.5). This proves convergence with all asserted uniformity. Dependence only on \(\eta=\epsilon^2\) proves the two-sided statement. \(\square\)

For \(\eta>0\), a test supported strictly inside \((-\sqrt\eta,\sqrt\eta)\) gives zero in every formula (3.3). Thus the entire continued family still has support outside that gap. At the critical value \(\eta=0\), its existence has been proved by these pairings rather than presumed as a general pullback.

## 4. Negative integers become odd point derivatives

**Theorem 4.1 (all negative-integer coefficients).** For every integer \(k\ge1\),

\[
\langle v_{-k}(\eta),\phi\rangle
 =(-1)^{k-1}q_\phi^{(k-1)}(\eta),\qquad
U_{-k}=\frac{(-1)^k(k-1)!}{(2k-1)!}\delta_0^{(2k-1)} .
\tag{4.1}
\]

**Proof.** At \(a=-k\), use \(N=k\) in (3.3). Since \(G(1)=1\), ordinary integration of the derivative gives

\[
(-1)^k\int_0^\infty q_\phi^{(k)}(s+\eta)\,ds
 =(-1)^{k-1}q_\phi^{(k-1)}(\eta).
\tag{4.2}
\]

The distant endpoint is zero by compact support. At \(\eta=0\), (2.2) gives
\((-1)^{k-1}(k-1)!\phi^{(2k-1)}(0)/(2k-1)!\).
An odd delta derivative pairs as the negative of that test derivative, proving the coefficient in (4.1). In particular,

\[
U_{-1}=-\delta_0',\qquad
U_{-2}=\tfrac16\delta_0''',\qquad
U_{-3}=-\tfrac1{60}\delta_0^{(5)} .
\tag{4.3}
\]

\(\square\)

**Example 4.2 (two moving point sources).** The first identity of (4.1) at \(k=1\) is an exact formula, not a formal composition rule:

\[
u_{-1,\epsilon}=\frac{\delta_e-\delta_{-e}}{2e},
\qquad e=|\epsilon|>0.
\tag{4.4}
\]

Its pairing is the central difference quotient, tending to \(\phi'(0)\). At \(k=2\), direct differentiation of (2.1) for \(x>0\), followed by \(-q_\phi'(e^2)\), gives

\[
u_{-2,\epsilon}
 =\frac{\delta_e-\delta_{-e}
             +e(\delta_e'+\delta_{-e}')}{4e^3}.
\tag{4.5}
\]

The numerator of its pairing is
\(\phi(e)-\phi(-e)-e[\phi'(e)+\phi'(-e)]\).
Finite Taylor formulas through the requisite derivatives give
\(-2e^3\phi'''(0)/3+O(e^5p_5(\phi))\).
Dividing by \(4e^3\) gives \(-\phi'''(0)/6\), the pairing of \(\delta_0'''/6\). This independently checks both the factor and the derivative sign.

## 5. Every finite even-power expansion has a controlled remainder

**Theorem 5.1 (smooth collapse and finite expansion).** Every test pairing of \(v_a(\eta)\) is smooth for \(\eta\ge0\), including its right derivatives at zero, and

\[
\partial_\eta^jv_a(\eta)=(-1)^jv_{a-j}(\eta),\qquad
v_{a-j}(0)=U_{a-j}\quad(j\ge0).
\tag{5.1}
\]

If \(M\ge1\), \(A\subset\mathbb C\) is compact, and \(N\) is chosen as in Theorem 3.1, then

\[
\begin{aligned}
v_a(\eta)&=\sum_{j=0}^{M-1}\frac{(-\eta)^j}{j!}U_{a-j}
                  +\mathcal R_{a,M}(\eta),\\
|\langle\mathcal R_{a,M}(\eta),\phi\rangle|
 &\le C_{A,N,R,M}\eta^M p_{2N+2M+1}(\phi).
\end{aligned}
\tag{5.2}
\]

For each fixed number of complex-order derivatives, the differentiated remainder obeys the same test-order estimate with another constant. These claims are uniform for \(a\in A\), \(\eta\ge0\), on the fixed test support.

**Proof.** Differentiate (3.3) \(j\) times in \(\eta\). The resulting integrand has \(q_\phi^{(N+j)}(s+\eta)\), with the same exponent and a common support interval. Bounded higher derivatives and the integrable power justify this by dominated difference quotients, also as right differences at zero. At parameter \(a-j\), use index \(N+j\) in (3.3); its Gamma argument and power are identical, and the signs differ by \((-1)^j\). This proves (5.1).

For the expansion, apply the finite Taylor formula with integral remainder on the segment \([s,s+\eta]\) to \(q_\phi^{(N)}\). Its \(j\)-th term, inserted into (3.3), is exactly \((-\eta)^jU_{a-j}(\phi)/j!\) by the same index comparison. The remainder has absolute value at most \(\eta^M\|q_\phi^{(N+M)}\|_\infty/M!\). Formula (3.7) and Lemma 2.1 give (5.2).

For explicit control of parameter derivatives, the \(\ell\)-th derivative of (3.3) is

\[
(-1)^N\sum_{j=0}^{\ell}\binom{\ell}{j}G^{(\ell-j)}(a+N+1)
 \int_0^{R^2}s^{a+N}(\log s)^j q_\phi^{(N)}(s+\eta)\,ds .
\tag{5.3}
\]

All derivatives of \(G\) are bounded on the compact parameter set. The logarithmic integrals have the uniform bounds proved in Theorem 3.1. Insert the same finite Taylor remainder in each integral to obtain the stated differentiated estimate. This also proves locally uniform convergence of every fixed complex-order derivative; it does not rely on a pointwise-limit inference. \(\square\)

Replacing \(\eta\) by \(\epsilon^2\) gives finite expansions in even powers of \(\epsilon\). A smooth test need not equal its infinite Taylor series, and no infinite-series convergence is asserted.

## 6. Identify the limit and its elementary operations

**Proposition 6.1 (ordinary region, principal value and identities).** In the region \(\operatorname{Re}a>-1/2\), the limit is the locally integrable function

\[
U_a(t)=\frac{\operatorname{sgn}(t)|t|^{2a}}{\Gamma(a+1)} .
\tag{6.1}
\]

For the larger half-plane \(\operatorname{Re}a>-1\), it is given by the absolutely convergent *paired* integral

\[
\langle U_a,\phi\rangle
 =G(a+1)\int_0^\infty t^{2a}[\phi(t)-\phi(-t)]\,dt .
\tag{6.2}
\]

In particular,

\[
U_{-1/2}=\frac1{\sqrt\pi}\operatorname{pv}\frac1t .
\tag{6.3}
\]

For every complex \(a\), \(U_a\) is odd and homogeneous of degree \(2a\), and satisfies

\[
t\partial_tU_a=2aU_a,\qquad
t^2U_a=(a+1)U_{a+1},\qquad
\partial_t^2U_a=(4a-2)U_{a-1}.
\tag{6.4}
\]

**Proof.** In (3.3) take \(N=0,\eta=0\) and substitute \(s=t^2\), first away from zero and then by absolute convergence. The resulting integral is (6.2). The FTC bounds its test difference by \(2t\|\phi'\|_\infty\), so its integrand is integrable near zero when \(\operatorname{Re}a>-1\). The function itself is locally integrable under the stronger condition \(2\operatorname{Re}a>-1\), giving (6.1). At \(a=-1/2\), use the proved \(\Gamma(1/2)=\sqrt\pi\). The symmetric truncated integral of \(\phi(t)/t\) is the integral of \([\phi(t)-\phi(-t)]/t\) over \(t>e\); its limit exists by that same bound. This is the principal-value distribution and proves (6.3).

Replacing \(\phi(t)\) by \(\phi(-t)\) changes the sign of \(q_\phi\), hence of every pairing: \(U_a\) is odd. For \(\lambda>0\),

\[
q_{\phi(\lambda\cdot)}(s)=\lambda q_\phi(\lambda^2s).
\tag{6.5}
\]

Take \(N\) derivatives and substitute \(r=\lambda^2s\) in (3.3) at \(\eta=0\). The factors are \(\lambda^{2N+1}\) and \(\lambda^{-2(a+N+1)}\), giving

\[
\langle U_a,\phi(\lambda\cdot)\rangle
 =\lambda^{-2a-1}\langle U_a,\phi\rangle .
\tag{6.6}
\]

This is the definition of homogeneous degree \(2a\) on the line. The tests for \(\lambda\) near one have one common compact support; the FTC and all test derivatives show that their derivative is \(t\phi'(t)\) in the test topology. Differentiating (6.6) at one gives \(U_a(t\phi')=-(2a+1)U_a(\phi)\). Since
\((tU_a')(\phi)=-U_a((t\phi)')\),
the Euler formula in (6.4) follows.

In the ordinary region, multiplying (6.1) by \(t^2\) and using Gamma recursion gives the middle identity in (6.4). For \(\operatorname{Re}a>1/2\), two integrations by parts on each punctured half-line justify the last one: the function tends to zero at zero, its first derivative \(2aG(a+1)|t|^{2a-1}\) also tends to zero there, and its second derivative is locally integrable. Thus there is no endpoint term. Its coefficient is \(2a(2a-1)G(a+1)=(4a-2)G(a)\). Both identities extend to the whole plane by the proved scalar identity theorem, since each side is an entire distribution family. No division by a vanishing coefficient is used. \(\square\)

**Example 6.2 (a principal-value derivative).** Substitution of \(a=-1/2\) in (6.4) gives

\[
U_{-3/2}=-\frac1{4\sqrt\pi}
              \partial_t^2\operatorname{pv}\frac1t .
\tag{6.7}
\]

Off zero this is the function \(-1/(2\sqrt\pi\,t^3)\), but the derivative formula specifies its entire distributional extension. At \(a=1/2\), by contrast, (6.1) gives \(U_{1/2}=2t/\sqrt\pi\), whose second derivative is zero. The coefficient \(4a-2\) also vanishes, so that recurrence alone cannot recover \(U_{-1/2}\). Its value is fixed by the integral construction.

## Exercises

**Exercise 1.** Find \(U_0,U_1,U_2,U_{1/2}\). Among \(a=-3/4,-1/2,-1/4\), determine which give an ordinary locally integrable function in (6.1), and explain the distributions at the others.

**Exercise 2.** Continue from the integrable region the family

\[
w_{a,\epsilon}(t)=\operatorname{sgn}(t)\,C_a(4t^2-\epsilon^2),
\qquad \epsilon\ne0 .
\tag{7.1}
\]

Find its limit at every complex order, calculate the exact coefficient at \(a=-3\), and check the scaling separately with the moving point masses at \(a=-1\).

**Exercise 3.** Compare the convergent odd family \(u_{-1/2,\epsilon}\) with

\[
z_\epsilon(t)=
\frac{1_{\{|t|>|\epsilon|\}}}{\sqrt\pi\sqrt{t^2-\epsilon^2}} .
\tag{7.2}
\]

Show that the latter has no distributional limit. Quantify its divergence on a nonnegative compact smooth test equal to one near zero.

**Exercise 4.** Check the multiplication and second-derivative identities (6.4) at \(a=-3\) using the point derivatives. Prove the finite-parameter identity

\[
\partial_t^2v_a(\eta)
 =(4a-2)v_{a-1}(\eta)+4\eta v_{a-2}(\eta),
\qquad \eta>0,
\tag{7.3}
\]

for every complex \(a\), and justify passage to the limit in the last term.

**Exercise 5.** Expand \(u_{1,\epsilon}\) through order \(\epsilon^4\), with a bounded-test \(O(\epsilon^6)\) remainder. Check the point-derivative coefficient independently by integrating the discrepancy on \((-|\epsilon|,|\epsilon|)\).

**Exercise 6.** At \(a=-1\), write all \(M\) terms of (5.2). For every \(M\ge1\), construct one fixed compact smooth test proving that the remainder cannot in general be improved to \(o(\eta^M)\).

**Exercise 7.** Put \(V_a=\partial_aU_a\) and \(\psi(z)=\Gamma'(z)/\Gamma(z)\) wherever defined. Find \(V_{1/2}\) as a locally integrable function, prove

\[
(t\partial_t-2a)V_a=2U_a,
\tag{7.4}
\]

and calculate \(\partial_t^2V_{1/2}\). Explain its relation to \(\partial_t^2U_{1/2}=0\).

**Exercise 8.** Define

\[
\begin{aligned}
A_\phi(t)&=\phi(t)+\phi(-t)-2\phi(0)1_{\{t<1\}}\quad(t>0),\\
F(\phi)&=\int_0^\infty\frac{A_\phi(t)}t\,dt .
\end{aligned}
\tag{7.5}
\]

Prove that \(F\) is a distribution and establish the renormalized limit, including its constant,

\[
z_\epsilon-\frac2{\sqrt\pi}\log\frac1{|\epsilon|}\,\delta_0
 \longrightarrow\frac{F+2\log2\,\delta_0}{\sqrt\pi}.
\tag{7.6}
\]

## Complete solutions

**Solution 1.** Formula (6.1), the Gamma recurrence and its half-integer normalization give

\[
U_0=\operatorname{sgn}(t),\qquad U_1=t|t|,\qquad
U_2=\tfrac12\operatorname{sgn}(t)t^4,\qquad
U_{1/2}=2t/\sqrt\pi .
\tag{8.1}
\]

For real \(a\), the integral of \(|t|^{2a}\) near zero is finite precisely when \(a>-1/2\): its positive-side antiderivative is \(t^{2a+1}/(2a+1)\) away from the endpoint exponent, and that endpoint has logarithmic divergence. Only \(-1/4\) in the list meets this condition. The order \(-1/2\) gives the principal value (6.3). At \(-3/4\), (6.2) has size \(O(t^{-1/2}\|\phi'\|_\infty)\) near zero, so it converges and satisfies a finite test bound. These bounds, not just values on the punctured line, establish the distributions.

**Solution 2.** Substitute \(x=2t\) in the initial pairing to get

\[
\langle w_{a,\epsilon},\phi\rangle
 =\tfrac12\langle u_{a,\epsilon},\phi(\cdot/2)\rangle .
\tag{8.2}
\]

The right side defines an entire family, so it gives the required continuation. Theorem 3.1 and (6.6) give the limit \(2^{2a}U_a\), where \(2^{2a}=\exp(2a\log2)\). At \(-3\), its value is \(-\delta_0^{(5)}/3840\). Formula (8.2) also directly gives

\[
w_{-1,\epsilon}=\frac{\delta_{e/2}-\delta_{-e/2}}{4e}
 \longrightarrow-\tfrac14\delta_0',
\qquad e=|\epsilon|.
\tag{8.3}
\]

Indeed the numerator pairs to \(e\phi'(0)+O(e^3p_3(\phi))\). This verifies the scaling without assuming a delta pullback at a critical point.

**Solution 3.** The odd limit is (6.3). Let \(\phi\ge0\) have compact support and equal one on \([-r,r]\). The scalar cutoff proof supplies such a test. For \(0<e<r\), positivity gives

\[
\langle z_\epsilon,\phi\rangle\ge
\frac2{\sqrt\pi}\int_e^r\frac{dt}{\sqrt{t^2-e^2}}
=\frac2{\sqrt\pi}\operatorname{arcosh}(r/e),\qquad
\operatorname{arcosh}(r/e)=\log(1/e)+\log(2r)+o(1).
\tag{8.4}
\]

Here \(\operatorname{arcosh}x\) denotes \(\log(x+\sqrt{x^2-1})\) for \(x\ge1\). Differentiating \(\log(t+\sqrt{t^2-e^2})\) gives \(1/\sqrt{t^2-e^2}\) for \(t>e\). The FTC on truncated intervals, followed by the finite lower endpoint \(\log e\), proves the integral identity. The asymptotic follows from
\(\log((r+\sqrt{r^2-e^2})/e)\).
The lower bound tends to infinity, so a distributional limit is impossible.

**Solution 4.** Theorem 4.1 gives \(U_{-2}=\delta_0'''/6\), \(U_{-3}=-\delta_0^{(5)}/60\), and \(U_{-4}=\delta_0^{(7)}/840\). The product rule applied at zero yields

\[
t^2\delta_0^{(j)}=j(j-1)\delta_0^{(j-2)}\qquad(j\ge2).
\tag{8.5}
\]

To check the sign, the left pairing is \((-1)^j(t^2\phi)^{(j)}(0)=(-1)^jj(j-1)\phi^{(j-2)}(0)\); the right has the same sign since \((-1)^{j-2}=(-1)^j\). Therefore \(t^2U_{-3}=-\delta_0'''/3=-2U_{-2}\), and \(\partial_t^2U_{-3}=-\delta_0^{(7)}/60=-14U_{-4}\), as required.

For \(\eta>0\), start with \(\operatorname{Re}a>1\). At each simple boundary the function and its first derivative tend to zero, while the second derivative is integrable; integrating by parts on either side therefore introduces no boundary mass. Inside the nonzero region the sign is constant, and differentiation of the powers gives

\[
\partial_t^2v_a(\eta)
 =2v_{a-1}(\eta)+4t^2v_{a-2}(\eta).
\tag{8.6}
\]

There also \((t^2-\eta)v_{a-2}(\eta)=(a-1)v_{a-1}(\eta)\), by Gamma recursion. All pairings are entire, so both identities hold for every \(a\). Substitution proves (7.3). Applied to parameter \(a-2\), the uniform bound (3.5) gives \(\eta v_{a-2}(\eta)\to0\) on bounded tests of common support, justifying the limiting recurrence.

**Solution 5.** Use (5.2) with \(a=1,N=0,M=3\):

\[
u_{1,\epsilon}=t|t|-\epsilon^2\operatorname{sgn}(t)
 -\tfrac12\epsilon^4\delta_0'
 +O_{\mathcal D'}(\epsilon^6).
\tag{8.7}
\]

Its remainder is bounded by a support-dependent constant times \(|\epsilon|^6p_7(\phi)\). For a separate calculation, the actual function minus the first two ordinary terms is \(\operatorname{sgn}(t)(e^2-t^2)\) on \((-e,e)\) and zero elsewhere. Its pairing is

\[
\int_0^e(e^2-t^2)[\phi(t)-\phi(-t)]\,dt.
\tag{8.8}
\]

Taylor's integral remainder gives the bracket \(2t\phi'(0)+O(t^3p_3(\phi))\). Integration of the first term is \(e^4\phi'(0)/2\); the remainder has size \(O(e^6p_3(\phi))\). Since \(\delta_0'(\phi)=-\phi'(0)\), the point coefficient in (8.7) is confirmed, with an even smaller test order in this particular calculation.

**Solution 6.** Take a compact smooth cutoff \(\chi\) equal to one near zero, and let \(\phi(t)=t^{2M+1}\chi(t)\). For sufficiently small \(e>0\), the exact moving-source formula gives

\[
\langle v_{-1}(e^2),\phi\rangle=e^{2M}.
\tag{8.9}
\]

All test derivatives of odd orders \(2j+1\) for \(j<M\) vanish at zero. The first \(M\) expansion terms therefore pair to zero, while the remainder divided by \(\eta^M=e^{2M}\) pairs to one. This rules out a general \(o(\eta^M)\) bound even on this fixed test. Substitution of (4.1) into the finite expansion gives

\[
v_{-1}(\eta)
 =-\sum_{j=0}^{M-1}\frac{\eta^j}{(2j+1)!}\delta_0^{(2j+1)}
      +O_{\mathcal D'}(\eta^M).
\tag{8.10}
\]

The \(j!\) in (4.1) cancels the Taylor factorial, and the product of the two signs is always negative.

**Solution 7.** In a compact neighborhood of \(a=1/2\), the ordinary integrand and its parameter derivative have a common integrable power-log bound. Differentiating (6.1) thus gives

\[
V_{1/2}(t)=\frac{2t}{\sqrt\pi}
                   [\,2\log|t|-\psi(3/2)\,].
\tag{8.11}
\]

It has continuous value zero at zero, because \(t\log|t|\to0\); for example put \(t=e^{-r}\) and use exponential domination as in gamma foundation (G1). The reciprocal derivative is \(G'(z)=-\Gamma'(z)/\Gamma(z)^2\) on the nonzero domain, explaining the sign of \(\psi\). Differentiating the entire Euler identity gives (7.4). Differentiating the last recurrence in (6.4) gives

\[
\partial_t^2V_a=4U_{a-1}+(4a-2)V_{a-1}.
\tag{8.12}
\]

All operations commute with parameter derivatives because each is a fixed continuous operation on test pairings. At \(a=1/2\), this is \(4\operatorname{pv}(1/t)/\sqrt\pi\). The coefficient \(4a-2\) vanishes at \(1/2\) but its derivative equals four. This explains why the differentiated family has a nonzero second derivative even though the single member \(U_{1/2}\) does not.

**Solution 8.** For \(0<t<1\), Taylor's integral remainder gives \(|A_\phi(t)|\le t^2p_2(\phi)\). For \(t>1\), it vanishes beyond \(\max(1,R)\), and its size is at most \(2p_0(\phi)\). The possible jump at one causes no improper integral. Consequently
\[
|F(\phi)|\le\tfrac12p_2(\phi)
             +2\log(\max(1,R))p_0(\phi).
\]
This proves both convergence and the finite-order distribution bound.

For \(0<e<1\), the exact decomposition of the even pairing is

\[
\sqrt\pi\,\langle z_\epsilon,\phi\rangle
 =\int_e^\infty\frac{A_\phi(t)}{\sqrt{t^2-e^2}}\,dt
       +2\phi(0)\operatorname{arcosh}(1/e).
\tag{8.13}
\]

On \([r,\max(1,R)]\), for any fixed \(0<r<1\) and \(e<r/2\), the reciprocal square-root kernel is bounded by a fixed multiple of \(1/t\) and tends to \(1/t\). Dominated convergence applies, including across the single jump of \(A_\phi\). Near the moving endpoint, the substitution \(w=\sqrt{t^2-e^2}\), justified first on truncated intervals, gives

\[
\int_e^r\frac{t^2}{\sqrt{t^2-e^2}}\,dt
 =\int_0^{\sqrt{r^2-e^2}}\sqrt{w^2+e^2}\,dw
 \le r^2 .
\tag{8.14}
\]

The Taylor bound therefore controls this part by \(r^2p_2(\phi)\), uniformly for \(e<r\). The limiting integral on \((0,r)\) has bound \(r^2p_2(\phi)/2\). First pass to the limit on the fixed interval, then let \(r\downarrow0\); the first term of (8.13) tends to \(F(\phi)\). The elementary logarithmic formula in Solution 3 gives
\(\operatorname{arcosh}(1/e)-\log(1/e)\to\log2\).
Subtracting the divergent point mass in (7.6) now proves the full asserted limit, including \(2\log2\).

## Programme proof locations and freely accessible sources

The programme proofs listed at the beginning supply the exact distribution and gamma inputs. [Scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 13.1–13.5 and 13.7–13.10, proves the FTC, exponential/logarithm identities and compact cutoffs. [Measure foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.4 and 16.1–16.2, supplies convergence and parameter integration. The [Gaussian proof](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F3, together with the Euler integral and positive substitution, gives the half-integer normalization stated in angular foundation A5. Each supplied prerequisite keeps its own licence.

- [Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, October 2, 2026](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), Section 5.2, pp. 61–64. These freely accessible notes supply the normalized one-sided-power and principal-value constructions. Their full required arguments, including scalar Gamma prerequisites, are proved in U016 and the supplied foundations; Sections 3–6 here construct the collapsing odd family itself.
- [Keith Conrad, *Differentiating under the integral sign*](https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf), Section 11, Theorem 11.1 and its proof, pp. 13–14. The smooth-division integral is the starting point for the complete iterative half-line square-descent proof in Lemma 2.1. No external smooth-extension theorem is assumed.
