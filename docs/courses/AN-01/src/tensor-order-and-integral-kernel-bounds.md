# Tensor order and integral kernel bounds

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

An integral kernel can describe evaluation on a graph, differentiation of an input, or averaging over a region. Its absolute row and column integrals control all its \(L^p\) bounds. For distributional kernels, a different issue is the number of test derivatives needed to bound a pairing. Tensor products can attain the sum of two orders, but sufficiently separated frequencies can reduce that exact order to their maximum.

We pair distributions complex linearly, so \(\delta_a^{(k)}(\phi)=(-1)^k\phi^{(k)}(a)\). The test topology and local finite-order estimates are proved in [U008](order-positivity-and-limits.md), the initial test-space construction and Proposition 1.2. The complete tensor construction on arbitrary Euclidean open sets is [U021](convolution-as-addition-of-supports.md), B0–B2, especially (B5)–(B6). That proof includes density of sums of product tests, tensor uniqueness, exact product supports and three-factor associativity. These exact supplied results suffice here.

The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12, 13.1–13.5 and 13.7–13.10, proves compactness, calculus, exponential/trigonometric series and smooth cutoffs. The [finite algebra foundation](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, proves the inner-product and matrix identities. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.3 and 16, proves completed Lebesgue integration, Tonelli, Fubini, Hölder and measurable sections. All further estimates and sharpness arguments are proved below.

## Evaluation and differentiation determine a kernel

For an operator \(T:\mathcal D(Y)\to\mathcal D'(X)\), a kernel means a distribution \(K\) on \(X\times Y\) satisfying
\[
K(\psi(x)\phi(y))=\langle T\phi,\psi\rangle.
\]
There is at most one such distribution: subtract two and apply the product-test density proved in U021 B2. In the following cases we construct it explicitly.

**Theorem 1.1 (continuous graph evaluation).** For every continuous real \(f:\mathbb R\to\mathbb R\), let \(H(t)=1_{\{t>0\}}\). Then
\[
\partial_yH(y-f(x))=K_f,\qquad
K_f(\Phi)=\int_{\mathbb R}\Phi(x,f(x))\,dx.
\]
This is an order-zero positive graph measure, with exact support \(\{(x,f(x)):x\in\mathbb R\}\). Its operator is \(T_f\phi=\phi\circ f\), which is weakly continuous from tests to distributions.

**Proof.** The function \(H(y-f(x))\) is Borel and bounded. For a test supported in a compact rectangle \(I\times J\), absolute Fubini and the fundamental theorem give
\[
\begin{aligned}
\langle\partial_yH(y-f(x)),\Phi\rangle
&=-\int_I\int_{f(x)}^\infty\partial_y\Phi(x,y)\,dy\,dx\\
&=\int_I\Phi(x,f(x))\,dx.
\end{aligned}
\]
The first integrand vanishes outside \(I\times J\), so is absolutely integrable. The second pairing is bounded by \(|I|\|\Phi\|_\infty\). Thus it has order at most zero. It is integration against the pushforward of \(dx\) by the continuous map \(x\mapsto(x,f(x))\); the same estimate gives local finiteness.

The graph is closed: if \((x_j,f(x_j))\to(x,y)\), continuity forces \(y=f(x)\). Off it, the pairing vanishes on a sufficiently small neighborhood. At \((x_0,f(x_0))\), choose a nonnegative smooth test supported in any prescribed neighborhood and positive on a smaller rectangle around that point. Continuity of \(f\) places \((x,f(x))\) in that smaller rectangle for all \(x\) in a nonempty interval about \(x_0\). Its pairing is strictly positive. The support is therefore exactly the graph and the measure is nonzero, so its exact order is zero.

On product tests the formula is \(\int\psi(x)\phi(f(x))\,dx\), proving the operator identity and uniqueness. The output is continuous. For every fixed \(\psi\),
\[
|\langle T_f\phi,\psi\rangle|
\le\|\psi\|_1\|\phi\|_\infty.
\]
This bound gives continuity for the test topology and hence weak continuity into distributions. The argument has made no assumption on derivatives, injectivity or properness of \(f\). \(\square\)

**Theorem 1.2 (an input derivative fixes the sign).** Suppose \(a:\mathbb R^2\to\mathbb C\) is continuous, and define
\[
T\phi(x)=\phi(x)+\int_{\mathbb R}a(x,y)\phi'(y)\,dy.
\]
Then its unique kernel is
\[
K=\delta_{\mathrm{diag}}-\partial_y a,\qquad
\delta_{\mathrm{diag}}(\Phi)=\int_{\mathbb R}\Phi(t,t)\,dt.
\]
Here the derivative is distributional; no classical derivative of \(a\) is required.

**Proof.** Continuous \(a\) is locally integrable, so its weak derivative is a distribution. The diagonal term is the instance \(f(x)=x\) of Theorem 1.1. Thus the proposed sum exists as a distribution. On product tests,
\[
\begin{aligned}
(-\partial_y a)(\psi\otimes\phi)
&=\iint a(x,y)\psi(x)\phi'(y)\,dx\,dy,\\
\delta_{\mathrm{diag}}(\psi\otimes\phi)
&=\int\psi(x)\phi(x)\,dx.
\end{aligned}
\]
Both integrals are absolutely convergent on compact products. They give the required pairing, and product-test density proves uniqueness.

For completeness, \(T\phi\) is continuous. On a compact output interval \(I\), uniform continuity of \(a\) on \(I\) times a compact neighborhood of \(\operatorname{supp}\phi\) makes its integral continuous in \(x\). If \(\operatorname{supp}\phi\subset J\), then for a fixed output test \(\psi\) supported in \(I\),
\[
|\langle T\phi,\psi\rangle|
\le\|\psi\|_1\bigl(\|\phi\|_\infty
 +|J|\sup_{I\times J}|a|\,\|\phi'\|_\infty\bigr).
\]
Thus the operator is weakly continuous on the test space. The two minus signs, one in the proposed kernel and one in weak differentiation, explain the plus sign in the input formula. \(\square\)

**Example 1.3.** Taking \(f(x)=|x|+\sin x\) gives the exact order-zero kernel on that graph and output \(\phi(|x|+\sin x)\). Its corner at zero has no effect on the \(y\)-derivative identity. Taking \(a(x,y)=e^{-x^2-y^2}\) in Theorem 1.2 and differentiating the smooth density gives
\[
K=\delta_{\mathrm{diag}}+2y e^{-x^2-y^2}.
\]

## Row and column masses control every exponent

**Theorem 2.1 (Schur bounds, with every endpoint).** Let \(X\subset\mathbb R^m\) and \(Y\subset\mathbb R^n\) be open. Suppose the measurable complex kernel \(K\) satisfies
\[
\int_X|K(x,y)|\,dx\le A\quad\text{for a.e. }y,\qquad
\int_Y|K(x,y)|\,dy\le B\quad\text{for a.e. }x,
\]
where \(0\le A,B<\infty\). For every \(f\in L^p(Y)\), the integral
\[
T_Kf(x)=\int_Y K(x,y)f(y)\,dy
\]
converges absolutely for almost every \(x\), defines a measurable output class, and obeys
\[
\begin{cases}
\|T_Kf\|_1\le A\|f\|_1,&p=1,\\
\|T_Kf\|_p\le A^{1/p}B^{1-1/p}\|f\|_p,&1<p<\infty,\\
\|T_Kf\|_\infty\le B\|f\|_\infty,&p=\infty.
\end{cases}
\]
These bounds are valid on almost-everywhere equivalence classes and are sharp as universal bounds. If either \(A\) or \(B\) is zero, the kernel and every operator are zero almost everywhere.

**Proof: measurable representatives.** Open Euclidean sets with Lebesgue measure are sigma-finite. We first justify the choice of Borel representatives. The integration foundation, §15.0, proves that each Lebesgue measurable set differs from a Borel set inside a Borel null set. Approximate a nonnegative measurable function by the increasing finite simple functions of §16.1. Replace every level set in this countable family by its Borel version. The new simple functions agree with the old ones off one Borel null union; their pointwise limit there, extended by zero on that union, is a Borel representative. Split real and imaginary parts into positive and negative parts to treat finite complex functions. This applies on the product space as well as each factor.

Changing a representative on a null set preserves its section integrals outside a null set, by Tonelli and completion. For the input assertion directly, if \(f=\widetilde f\) off a null set \(N\), then
\[
|K(x,y)|\,|f(y)-\widetilde f(y)|=0
\quad\text{for a.e. }(x,y).
\]
Indeed \(X\times N\) is product null by a countable finite-measure exhaustion of \(X\). Tonelli gives zero integral on almost every row. The same argument applies to two versions of \(K\) which agree almost everywhere. We may take finite representatives throughout.

Integrals of nonnegative Borel functions over one variable are measurable by Tonelli. Real and imaginary parts, split into positive and negative parts, consequently give a measurable complex integral wherever it is absolutely finite. Set the output to zero on the exceptional null set.

**Proof: norm estimates.** If \(A=0\), Tonelli on \(X\times(Y\cap[-j,j]^n)\) gives integral zero for \(|K|\); exhaustion gives \(K=0\) almost everywhere. If \(B=0\), interchange the two variables in this reasoning. A zero kernel gives zero on almost every row for every input, as above.

For \(p=1\), Tonelli gives
\[
\int_X\int_Y|K(x,y)||f(y)|\,dy\,dx
\le A\|f\|_1.
\]
Thus the inner integral is finite almost everywhere and yields the first bound. For \(1<p<\infty\), put
\[
J(x)=\int_Y|K(x,y)||f(y)|^p\,dy.
\]
Its integral is at most \(A\|f\|_p^p\), so it is finite almost everywhere. Hölder in the ordinary \(dy\) measure, applied to \(|K|^{1/p}|f|\) and \(|K|^{1-1/p}\), gives on such rows
\[
\int_Y|K(x,y)||f(y)|\,dy
\le J(x)^{1/p}
       \left(\int_Y|K(x,y)|\,dy\right)^{1-1/p}.
\]
Zero rows are interpreted directly as zero; all remaining rows have finite weight. Raising to \(p\) and integrating proves
\[
\|T_Kf\|_p^p\le B^{p-1}\int_XJ(x)\,dx
\le B^{p-1}A\|f\|_p^p.
\]
This simultaneously proves absolute existence. At infinity choose a representative bounded by \(\|f\|_\infty\); the absolute row integral is at most \(B\|f\|_\infty\). Representative independence transfers the conclusion to the entire class. Linearity follows on the intersection of the full-measure sets where the finite collection of relevant integrals converges.

**Proof: sharpness.** For finite positive-volume measurable \(E\subset X,F\subset Y\), take \(K=c1_E1_F\) with \(c>0\). Its exact column and row bounds are \(A=c|E|\) and \(B=c|F|\). Input \(1_F\) gives output \(c|F|1_E\), with norm ratio
\[
c|E|^{1/p}|F|^{1-1/p}\quad(1\le p<\infty),
\qquad c|F|\quad(p=\infty).
\]
They equal the asserted constants, so a uniformly smaller bound from these hypotheses is impossible. These are universal estimates; a particular complex kernel can have a smaller interior norm. \(\square\)

**Example 2.2 (causal averaging).** On \(\mathbb R\), set
\[
K(x,y)=4e^{-4(x-y)}1_{\{y<x\}}.
\]
Integrating \(4e^{-4t}\) over \(t>0\) gives one, so both absolute marginal integrals are one. The norm is therefore at most one for every exponent. For \(p=\infty\), \(T_K1=1\) proves equality. For \(p<\infty\), use \(f_R=1_{(0,R)}\). On \(0<x<R\), direct integration gives \(T_Kf_R(x)=1-e^{-4x}\). Therefore for \(0<L<R\),
\[
\frac{\|T_Kf_R\|_p}{\|f_R\|_p}
\ge(1-e^{-4L})\left(\frac{R-L}{R}\right)^{1/p}.
\]
First let \(R\to\infty\), then \(L\to\infty\). The supremum defining the operator norm is at least one. At \(p=1\), equality also follows immediately by Tonelli for any nonzero nonnegative integrable input.

## A nonzero factor reveals its own order

For an integer \(r\ge0\), a distribution has order at most \(r\) if every compact test support \(L\) has a constant \(C_L\) such that
\[
|u(\phi)|\le C_L\max_{|\alpha|\le r}\|\partial^\alpha\phi\|_\infty,
\qquad \operatorname{supp}\phi\subset L.
\]
The same \(r\) must work for all supports; only the constants vary. The exact order is the least such nonnegative integer, when one exists. We assign zero distribution order zero.

**Theorem 3.1 (upper bound and converse).** For distributions \(u,v\) on arbitrary Euclidean open sets \(U,V\), orders at most \(k,l\) imply tensor order at most \(k+l\). If both factors are nonzero and their tensor has order at most \(N\), each factor has order at most \(N\).

**Proof.** Every compact subset of \(U\times V\) lies in the product of its compact projections. U021 (B6), with the two given order estimates, gives
\[
|(u\otimes v)(\Phi)|
\le C\max_{\substack{|\alpha|\le k\\|\beta|\le l}}
          \|\partial_x^\alpha\partial_y^\beta\Phi\|_\infty.
\]
Each derivative has total order at most \(k+l\). This proves the upper bound on every compact support.

For the converse, choose a fixed test \(\psi\) with \(v(\psi)=1\), by rescaling a nonzero pairing. On any compact \(L\subset U\), apply the tensor order bound to \(\phi(x)\psi(y)\). Each derivative of total order at most \(N\) is a product of a derivative of \(\phi\) through \(N\) and a fixed derivative of \(\psi\). Hence
\[
|u(\phi)|=|(u\otimes v)(\phi\otimes\psi)|
\le C_{L,\psi}\max_{|\alpha|\le N}\|\partial^\alpha\phi\|_\infty.
\]
The same argument with a normalized test of \(u\) gives the estimate for \(v\). It includes \(N=0\). If one factor is zero, its tensor is zero regardless of the order of the other factor, so the converse hypothesis is necessary. \(\square\)

## Concentrated jets attain the sum of orders

**Theorem 4.1 (the additive bound is attained).** For positive integers \(k,l\), the factors \(u=\delta_0^{(k)}\), \(v=\delta_0^{(l)}\) have exact orders \(k,l\), and \(u\otimes v\) has exact order \(k+l\).

**Proof.** The definitions give the factor upper bounds; Theorem 3.1 gives the tensor upper bound. Choose \(\eta\in\mathcal D(\mathbb R)\) equal to one near zero, and put
\[
h(s,t)=s^kt^l\eta(s)\eta(t),\qquad
\Phi_\varepsilon(x,y)=\varepsilon^{k+l-1}
 h(x/\varepsilon,y/\varepsilon),\quad 0<\varepsilon<1.
\]
All supports lie in one fixed compact rectangle. A derivative of total order \(j\le k+l-1\) has norm at most a fixed constant times \(\varepsilon^{k+l-1-j}\), so these norms stay bounded. But
\[
(u\otimes v)(\Phi_\varepsilon)
=(-1)^{k+l}k!l!\,\varepsilon^{-1}.
\]
Thus the tensor has no order bound \(k+l-1\). The one-variable tests
\[
\phi_\varepsilon(x)=\varepsilon^{k-1}
       (x/\varepsilon)^k\eta(x/\varepsilon)
\]
have bounded derivatives through \(k-1\) and pairing \((-1)^kk!/\varepsilon\) with \(\delta_0^{(k)}\). This proves its exact factor order; replacing \(k\) by \(l\) proves the other one. \(\square\)

## Separated frequencies attain the maximum order

We will use the elementary fact that \(\sum_{h\ge1}h^dc^{-h}<\infty\) for each integer \(d\ge0\) and real \(c>1\). The quotient of consecutive terms is \(c^{-1}(1+1/h)^d\), which tends to \(c^{-1}<1\) by the finite binomial formula. Choose \(\theta\) strictly between these numbers and one. Beyond a fixed index the terms are bounded by a fixed multiple of \(\theta^h\); the finite geometric-sum formula bounds that tail. This proves the fact without a further convergence criterion.

**Theorem 5.1 (the maximum can be the exact order).** For every integer \(N\ge1\), there are two distributions on \(\mathbb R\), each of exact order \(N\), whose tensor product also has exact order \(N\).

**Proof: defining the factors.** Let
\[
q=N+1,\qquad M_j=2^{q^j},\qquad c_j=jM_j^{N-1}\quad(j\ge1),
\]
and define the two series by pairing their even and odd modes with tests:
\[
u_0=\sum_{j\ {\rm even}}c_je^{2\pi iM_jx},
\qquad
u_1=\sum_{j\ {\rm odd}}c_je^{2\pi iM_jx}.
\]
For a test supported in an interval of length \(L\), integration by parts \(N\) times has no boundary terms and yields
\[
\left|\int e^{2\pi iM_jx}\phi(x)\,dx\right|
\le L(2\pi M_j)^{-N}\|\phi^{(N)}\|_\infty.
\]
After multiplying by \(c_j\), the summable bound is a constant times \(j/M_j\). Indeed \(q\ge2\) implies \(M_j\ge2^j\), and \(\sum j2^{-j}\) converges, for example because the ratio of consecutive terms is at most \(3/4\) for \(j\ge2\). The series therefore defines a linear functional with an order-\(N\) estimate on every compact test support. It is a distribution by the supplied test topology; tails converge in that same seminorm estimate.

**Proof: detecting the factor orders.** Choose a nonnegative smooth \(\eta\) supported compactly in \((-1,1)\) and positive on \([-3/4,3/4]\). The supplied cutoff construction gives such a function. Define
\[
S(x)=\sum_{m\in\mathbb Z}\eta(x+m),\qquad
\chi(x)=\frac{\eta(x)}{S(x)}.
\]
The sum is locally finite and smooth; a nearest integer ensures one argument lies in \([-1/2,1/2]\), so \(S>0\). Reindexing shows \(S(x+1)=S(x)\). Consequently \(\chi\) is compact smooth and \(\sum_m\chi(x+m)=1\). Splitting its integral into unit intervals gives for every integer \(n\)
\[
\int_{\mathbb R}\chi(x)e^{2\pi inx}\,dx
=\int_0^1e^{2\pi int}\,dt
=\begin{cases}1,&n=0,\\0,&n\ne0.\end{cases}
\]
The final integral follows from the scalar exponential primitive and \(e^{2\pi in}=1\). There are only finitely many contributing translated pieces.

For \(j\) of the chosen parity, put
\[
\phi_j(x)=M_j^{-(N-1)}\chi(x)e^{-2\pi iM_jx}.
\]
Leibniz's rule bounds all derivatives through \(N-1\) independently of \(j\), since every resulting power of \(M_j\) has exponent at most zero. The support is fixed. The already absolutely convergent pairing series and the integer-frequency identity give exactly
\[
u_0(\phi_j)=j\quad(j\text{ even}),\qquad
u_1(\phi_j)=j\quad(j\text{ odd}).
\]
All other frequencies have zero pairing. Both parities contain arbitrarily large \(j\), so neither factor has order at most \(N-1\).

**Proof: the tensor estimate.** Form the double mode series with even \(j\) and odd \(k\). For a two-variable test \(\Phi\) supported in a rectangle of area \(L\), integrate by parts \(N\) times in the variable with the larger frequency:
\[
\left|\iint e^{2\pi i(M_jx+M_ky)}\Phi(x,y)\,dx\,dy\right|
\le L(2\pi\max(M_j,M_k))^{-N}
          \max_{|\alpha|\le N}\|\partial^\alpha\Phi\|_\infty.
\]
The indices cannot coincide. Thus the coefficient majorant is
\[
\sum_{\substack{j\text{ even}\\ k\text{ odd}}}
       jk\,\frac{M_{\min(j,k)}^{N-1}}{M_{\max(j,k)}}.
\]
Dropping the parity restriction while retaining distinct indices bounds this by
\[
\begin{aligned}
2\sum_{h\ge2}\frac h{M_h}\sum_{t<h}tM_t^{N-1}
&\le2\sum_{h\ge2}h^3\frac{M_{h-1}^{N-1}}{M_h}\\
&=2\sum_{h\ge2}h^3\,2^{-2q^{h-1}}<\infty.
\end{aligned}
\]
The equality uses \(q=N+1\). The last convergence follows from \(q^{h-1}\ge h\) for \(h\ge2\), proved by induction using \(q\ge2\), and the elementary summability just proved for the dominating \(h^3 4^{-h}\). This supplies a finite order-\(N\) bound for the double series.

On a product test, absolute convergence of each one-variable series factors the double sum into the two pairings. U021 B2 therefore identifies the resulting distribution with \(u_0\otimes u_1\) on all tests. Each factor is nonzero and has exact order \(N\); Theorem 3.1 excludes a smaller tensor order. This proves the claim, also for \(N=1\). \(\square\)

## Exercises

**Exercise 1 (basic).** Find the operator, exact support and half-line derivative representation of the kernel
\[
K(\Phi)=\int(1+x^2)\Phi(x,x^2-1)\,dx.
\]

**Exercise 2 (intermediate).** For \(a(x,y)=e^{-x^2}|y-2|\), find the kernels of
\[
T_1\phi=\phi+\int a(x,y)\phi'(y)\,dy,\qquad
T_2\phi=\int a(x,y)\phi''(y)\,dy.
\]
Explain the bounded density in one and the line measure in the other.

**Exercise 3 (intermediate).** On \(X=(0,4)\), \(Y=(0,3)\), take
\[
K(x,y)=1_{\{\max(0,x-1)<y<\min(3,x)\}}.
\]
Calculate its exact row and column bounds, the output on \(1_Y\), and that input's norm ratio for every exponent. Find the endpoint operator norms.

**Exercise 4 (basic).** Find the exact \(L^p\) operator norms and an attaining input for
\[
K(x,y)=(2-i)1_{(0,2)}(x)1_{(1,4)}(y),\qquad 1\le p\le\infty.
\]

**Exercise 5 (advanced).** Partition \(X=(0,2)\) into two unit intervals and \(Y=(0,3)\) into three unit intervals. Let the six constant kernel values be
\[
M=\begin{pmatrix}1&2i&0\\-1&0&3\end{pmatrix}.
\]
Find the Schur bound and the exact \(L^1,L^2,L^\infty\) operator norms. Compare the \(L^2\) input and output norms for interval values \(1,i,-1\).

**Exercise 6 (intermediate).** If \(\alpha,\beta\) are real measurable functions, prove that replacing \(K\) by \(e^{i\alpha(x)}K(x,y)e^{i\beta(y)}\) preserves every \(L^p\) operator norm and both absolute marginal bounds.

**Exercise 7 (intermediate).** For
\[
u=\delta_{-1}^{(2)}+3\delta_2,\qquad v=\delta_4'-\delta_0,
\]
compute the full tensor pairing, exact support and exact order.

**Exercise 8 (advanced).** Prove that \(\sum_{j\ge1}\delta_j^{(j)}\) is a distribution with no finite global order. What does its tensor with zero show about Theorem 3.1?

**Exercise 9 (intermediate).** Determine \(x^r\delta_0^{(k)}\) for all nonnegative integers \(r,k\), then find the coefficient and exact order of
\[
x^2y(\delta_0^{(3)}\otimes\delta_0^{(2)}).
\]

**Exercise 10 (advanced).** For \(N\ge1\), take \(q=2N\), \(M_j=2^{q^j}\) and \(c_j=jM_j^{N-1}\). Divide the series \(\sum c_je^{2\pi iM_jx}\) into the three residue classes of \(j\) modulo three. Prove that each factor and their threefold tensor have exact order \(N\).

**Exercise 11 (advanced).** In Theorem 5.1 replace \(q=N+1\) by any integer \(q\ge2\). Determine exactly when the displayed absolute double coefficient majorant converges. State both the resulting order conclusion and the limit of what divergence of this majorant proves.

**Exercise 12 (advanced).** Suppose \(K\) from \(Y\) to \(X\) and \(L\) from \(Z\) to \(Y\) satisfy Theorem 2.1. Prove that
\[
C(x,z)=\int_YK(x,y)L(y,z)\,dy
\]
exists absolutely almost everywhere, has column bound \(A_KA_L\) and row bound \(B_KB_L\), and represents \(T_KT_L\) on every \(L^p\), including the endpoints and zero-bound cases.

## Complete solutions

**Solution 1.** A product test gives \(T\phi(x)=(1+x^2)\phi(x^2-1)\). Theorem 1.1, followed by multiplication by the smooth function \(1+x^2\), gives
\[
K=(1+x^2)\partial_yH(y-x^2+1).
\]
No \(x\)-derivative is taken. The kernel vanishes off the closed graph \(y=x^2-1\). At every graph point the positive-test argument of Theorem 1.1 has strictly positive weight \(1+x^2\), so it proves the exact support is that whole graph. The same compact-projection estimate proves order zero.

**Solution 2.** Splitting at \(y=2\), integration by parts gives for every test
\[
-\int|y-2|\phi'(y)\,dy
=-\int_{-\infty}^2\phi(y)\,dy+\int_2^\infty\phi(y)\,dy.
\]
The two boundary terms at \(2\) vanish because \(|y-2|=0\) there. Thus its first derivative is \(\operatorname{sgn}(y-2)\). A second integration gives
\[
-\int\operatorname{sgn}(y-2)\phi'(y)\,dy=2\phi(2),
\]
so its second derivative is \(2\delta_2\). The first input derivative contributes a minus sign to the kernel, whereas two input derivatives contribute a plus. Therefore
\[
\begin{aligned}
K_1&=\delta_{\mathrm{diag}}-e^{-x^2}\operatorname{sgn}(y-2),\\
K_2&=2e^{-x^2}\,dx\otimes\delta_2(dy).
\end{aligned}
\]
The first added density is bounded. The second kernel is supported on \(y=2\) and gives \(T_2\phi(x)=2e^{-x^2}\phi(2)\). These identities construct the kernels directly, and product-test density proves uniqueness.

**Solution 3.** For \(0<y<3\), its column has \(y<x<y+1\), of length one. Thus \(A=1\). The row length, also the output \(g=T_K1_Y\), is
\[
g(x)=
\begin{cases}
x,&0<x<1,\\
1,&1\le x\le3,\\
4-x,&3<x<4.
\end{cases}
\]
Its essential supremum is one, so \(B=1\). For finite \(p\),
\[
\|g\|_p^p=2+\frac2{p+1},\qquad
\frac{\|g\|_p}{\|1_Y\|_p}
=\left(\frac{2+2/(p+1)}3\right)^{1/p}.
\]
At infinity this ratio is one. Theorem 2.1 bounds every operator norm by one. At \(p=1\), Tonelli and the constant column integral give \(\int T_Kf=\int f\) for any nonzero nonnegative \(f\in L^1(Y)\), so the norm is exactly one. At infinity, input \(1_Y\) attains one. The computed finite-\(p\) ratio for a single input makes no additional equality assertion for the interior operator norms.

**Solution 4.** The absolute column and row bounds are \(2\sqrt5\) and \(3\sqrt5\). Theorem 2.1 therefore gives the bound
\[
\sqrt5\,2^{1/p}3^{1-1/p}\quad(1\le p<\infty),
\qquad 3\sqrt5\quad(p=\infty).
\]
Input \(1_{(1,4)}\) gives output \((6-3i)1_{(0,2)}\). The norm ratio is precisely the displayed constant for each exponent, including \(2\sqrt5\) at \(p=1\). Thus all bounds are attained.

**Solution 5.** The absolute column sums are \(2,2,3\), and the row sums \(3,4\). Hence \(A=3,B=4\), with Schur \(L^2\) bound \(\sqrt{12}\).

Let \(z_j\) be the integral of an arbitrary input on its \(j\)-th unit interval. Hölder at exponent two gives \(\sum|z_j|^2\le\|f\|_2^2\). Its two output values form \(Mz\). Conversely, the input constant at \(z_j\) on each interval realizes these three integrals with squared norm \(\sum|z_j|^2\). The integral-operator norm therefore equals the Euclidean norm of \(M\).

Here is the finite matrix argument in full. Direct multiplication gives
\[
D=MM^*=\begin{pmatrix}5&-1\\-1&10\end{pmatrix},
\qquad
\lambda_\pm=\frac{15\pm\sqrt{29}}2.
\]
The positive numbers \(\lambda_\pm\) solve \(\lambda^2-15\lambda+49=0\). For either root, the vector \(w_\pm=(1,5-\lambda_\pm)^t\) satisfies \(Dw_\pm=\lambda_\pm w_\pm\), by direct substitution. Moreover
\[
w_+^*w_-=1+(5-\lambda_+)(5-\lambda_-)
=1+25-75+49=0.
\]
Normalize these two nonzero vectors. They form an orthonormal basis of \(\mathbb C^2\). Expansion in this basis proves
\[
w^*Dw\le\lambda_+\|w\|^2,
\quad\text{with equality at a normalized }w_+.
\]
Finite-dimensional Cauchy–Schwarz and
\(\|v\|=\sup_{\|w\|=1}|w^*v|\), obtained by taking \(w=v/\|v\|\) when \(v\ne0\), give
\[
\|Mz\|\le\sup_{\|w\|=1}\|M^*w\|\,\|z\|
\le\sqrt{\lambda_+}\|z\|.
\]
For normalized \(w_+\), choose \(z=M^*w_+/\sqrt{\lambda_+}\). Then \(\|z\|=1\) and \(Mz=\sqrt{\lambda_+}w_+\). Thus
\[
\|T_K\|_{2\to2}=\sqrt{\frac{15+\sqrt{29}}2}<\sqrt{12},
\]
where the strict inequality follows from \(29<81\).

Input supported on the third interval and constant there has \(L^1\) ratio three, attaining the upper bound. At infinity, interval values \((-1,0,1)\) give a second output value four with input norm one, attaining that bound. Finally
\[
M(1,i,-1)^t=(-1,-4)^t,
\]
so the specified input and output norms are \(\sqrt3\) and \(\sqrt{17}\), with ratio \(\sqrt{17/3}\), smaller than the exact \(L^2\) norm.

**Solution 6.** Absolute kernel values are identical, so both marginal bounds agree. Multiplication by \(e^{i\alpha}\) and \(e^{i\beta}\) is an isometry on every \(L^p\), including infinity, with inverse given by the negative phase. Absolute convergence from Theorem 2.1 gives the operator identity
\[
T_{K_{\alpha,\beta}}=M_\alpha T_K M_\beta.
\]
The isometries imply that the new operator norm is at most the old one. Apply their inverses to obtain the reverse inequality. No smoothness of the phases is used.

**Solution 7.** Expanding the four tensor terms with the derivative signs gives
\[
\begin{aligned}
(u\otimes v)(\Phi)
={}&-\Phi_{xxy}(-1,4)-\Phi_{xx}(-1,0)\\
 &-3\Phi_y(2,4)-3\Phi(2,0).
\end{aligned}
\]
Each factor has exact support at its two indicated points, detected by a bump times a suitable monomial near each point. U021 B2 gives exact tensor support
\[
\{(-1,4),(-1,0),(2,4),(2,0)\}.
\]
Its order is at most three. In a fixed small rectangle about \((-1,4)\) excluding the other points, use the translated scaling test of Theorem 4.1 with \(k=2,l=1\). Derivatives through order two stay bounded, whereas the pairing has magnitude \(2/\varepsilon\). Thus the exact order is three.

**Solution 8.** On tests supported in a fixed compact set, only finitely many positive integers occur. The sum is then finite and bounded by a seminorm involving the largest derivative order among those indices. This proves it is a distribution. If it had global order at most \(r\), choose \(j>r\) and a small compact interval about \(j\) excluding other integers. On its tests the distribution equals \(\delta_j^{(j)}\). The translated tests of Theorem 4.1 have bounded derivatives through \(j-1\), hence through \(r\), but unbounded pairings. This is a contradiction. Tensoring with zero yields zero; an order-zero product therefore cannot bound the other factor's order without the nonvanishing hypothesis.

**Solution 9.** Leibniz's rule at zero gives
\[
(x^r\delta_0^{(k)})(\phi)
=
\begin{cases}
(-1)^k k!\,\phi^{(k-r)}(0)/(k-r)!,&r\le k,\\
0,&r>k.
\end{cases}
\]
Only the term differentiating \(x^r\) exactly \(r\) times survives. In distribution notation,
\[
x^r\delta_0^{(k)}
=(-1)^r\frac{k!}{(k-r)!}\delta_0^{(k-r)}
\quad(r\le k),
\]
and it is zero for \(r>k\). Applying the separate multiplication identity in U021 B2 gives
\[
x^2y(\delta_0^{(3)}\otimes\delta_0^{(2)})
=(6\delta_0')\otimes(-2\delta_0')
=-12\delta_0'\otimes\delta_0'.
\]
Its pairing is \(-12\Phi_{xy}(0,0)\). Theorem 4.1 proves exact order two.

**Solution 10.** With \(q=2N\ge2\), each residue-class series has an order-\(N\) bound from \(\sum j/M_j<\infty\), by exactly the integration-by-parts estimate in Theorem 5.1. Its same compact filter \(\chi\) gives pairing \(j\) on \(M_j^{-(N-1)}\chi e^{-2\pi iM_jx}\) for the class containing \(j\). Since each class has arbitrarily large indices and the lower-order seminorms of those tests stay bounded, every factor has exact order \(N\).

For a test on \(\mathbb R^3\), form the triple series with one index from each class. The indices are distinct. Integrate by parts \(N\) times in the variable of largest index \(h\). The coefficient bound, apart from the common support volume and \((2\pi)^{-N}\), is at most
\[
h^3\frac{M_{h-1}^{2(N-1)}}{M_h}.
\]
For each \(h\), at most \(3h^2\) ordered triples occur: choose the largest coordinate in three ways and each smaller index in fewer than \(h\) ways. The entire majorant is therefore bounded by
\[
3\sum_{h\ge3}h^5
   \frac{M_{h-1}^{2(N-1)}}{M_h}
=3\sum_{h\ge3}h^5\,2^{-2q^{h-1}}<\infty.
\]
The equality uses \(q=2N\); geometric comparison follows from \(q^{h-1}\ge h\). Thus the series defines a distribution of order at most \(N\). On triple product tests, the three absolutely convergent scalar series multiply to the three factor pairings. U021 B2's three-factor uniqueness identifies it with the tensor.

Normalize fixed tests of two nonzero factors to have pairing one. An order bound \(N-1\) for the triple tensor would then give the same bound for the remaining factor, by the product differentiation estimate used in Theorem 3.1. This contradicts its exact order. The triple order is \(N\).

**Solution 11.** The same grouping by the larger index bounds the double majorant by
\[
2\sum_{h\ge2}h^3\,2^{(N-1-q)q^{h-1}}.
\]
If \(q>N-1\), the exponent coefficient is a negative integer; comparison with a polynomial times \(2^{-h}\) proves convergence. The factor proof is unchanged for any \(q\ge2\), so Theorem 5.1 gives exact tensor order \(N\) in this range.

Conversely, adjacent indices \(h-1,h\) have opposite parity; one placement belongs to the even/odd sum. Its term equals
\[
h(h-1)\,2^{(N-1-q)q^{h-1}}.
\]
For \(q\le N-1\) these terms do not even tend to zero. Thus the majorant converges exactly when \(q>N-1\), equivalently \(q\ge\max(2,N)\) under the integer restriction. Divergence of this particular absolute estimate does not prove a higher tensor order. The two factors still exist and have exact order \(N\), so their tensor exists with order at most \(2N\) by Theorem 3.1; another argument would be needed to improve or sharpen that bound.

**Solution 12.** Choose measurable representatives as in Theorem 2.1 and put
\[
D(x,z)=\int_Y|K(x,y)||L(y,z)|\,dy\in[0,\infty].
\]
Tonelli gives for almost every \(z\)
\[
\int_X D(x,z)\,dx
\le A_K\int_Y|L(y,z)|\,dy
\le A_KA_L.
\]
The exceptional \(y\)-set in the column bound of \(K\) has measure zero and contributes zero to the \(dy\) integral; Tonelli and sigma-finiteness justify the iterated statement. In the other order it gives for almost every \(x\)
\[
\int_Z D(x,z)\,dz
\le B_L\int_Y|K(x,y)|\,dy
\le B_KB_L.
\]
Integrate the first bound on each bounded finite-measure piece of \(Z\). A countable exhaustion proves \(D<\infty\) for almost every \((x,z)\). Hence \(C\) is an absolutely defined measurable kernel there; set it to zero on the null exceptional set. The inequality \(|C|\le D\) proves both claimed marginal bounds.

For a general \(f\in L^p(Z)\), apply Theorem 2.1 to \(|L|\) and \(|f|\). The function
\[
g(y)=\int_Z|L(y,z)||f(z)|\,dz
\]
is finite almost everywhere and lies in \(L^p(Y)\). Apply the same theorem to \(|K|\) and \(g\). For almost every \(x\) this gives
\[
\int_Y\int_Z|K(x,y)||L(y,z)||f(z)|\,dz\,dy<\infty.
\]
Changing the null-set values of \(g\) has no effect by representative independence. Absolute Fubini at these \(x\) interchanges the two integrals and proves \(T_K(T_Lf)(x)=T_Cf(x)\). Both applications of the theorem include \(p=1,\infty\) and all zero-bound cases, so the proof does too.

## Free sources and exact proof dependencies

- Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, 2 October 2026 version, §7.1, pp.77–80, and Lemma 15.5, pp.200–201. [Free author notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf). The tensor pairing and \(L^2\) weighted estimate were compared with their actual proofs. Our exact supplied tensor construction is U021 B0–B2; no general Schwartz kernel existence theorem is assumed.
- Terence Tao, *Lecture Notes 2*, Math 247A, Fall 2006, §5, especially Theorem 5.6, Remark 5.7 and the sharpness calculation on pp.12–14. [Free author notes](https://www.math.ucla.edu/~tao/247a.1.06f/notes2.pdf). Theorem 2.1 above supplies the complete direct Hölder proof with all endpoints and null-set details; it does not require an interpolation theorem.
- [U008](order-positivity-and-limits.md), the test-space definitions and Proposition 1.2; [U021](convolution-as-addition-of-supports.md), B0–B2 and estimate (B6): local continuity, compact cutoffs, parameter differentiation, product-test density, tensor estimates, uniqueness and support. The linked scalar, finite algebra and integration foundations supply their stated elementary prerequisites. The frequency filters, all convergence estimates, the exact order tests and every exercise calculation are proved in this lesson.
