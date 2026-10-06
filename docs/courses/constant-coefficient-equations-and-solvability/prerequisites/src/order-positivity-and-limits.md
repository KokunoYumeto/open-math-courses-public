# Order, positivity and distributional limits

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

Smooth tests can hide a rapidly growing derivative or a large cancellation between nearby masses. A finite-order estimate specifies which derivatives control the pairing. Positivity changes the situation: it prevents cancellation, gives an estimate using only function values, and lets convergence on smooth tests extend to continuous tests.

The test-space conventions and completeness used here are those of [Distributions as kernels of continuous operators](distributions-as-kernels.md). The smoothing and finite-net arguments are developed in [When a kernel is smooth](when-a-kernel-is-smooth.md). For background on distributions see [Dyatlov 2026]. Two established results supply the functional-analysis and measure foundations: the complex Hahn–Banach extension theorem in Banach estimates, quotient spaces and compact parameter arguments, “Norm-preserving complex extension and scalar detection”, and the positive Riesz representation theorem in Haar measure on locally compact groups, Theorem 2.2. We state their exact uses below.

## Local estimates and the meaning of order

Let \(X\subset\mathbb R^n\) be open. Write \(\mathcal D(X)=C_c^\infty(X)\) and

\[
p_{K,m}(\phi)=\max_{|\alpha|\le m}\sup_K|\partial^\alpha\phi|,
\qquad
\mathcal D_K=\{\phi\in\mathcal D(X):\operatorname{supp}\phi\subset K\},
\tag{1.1}
\]

where \(K\subset X\) is compact. A complex-linear form \(u\) is a distribution if, for every such \(K\), there are \(m_K\ge0\) and \(C_K\) with

\[
|u(\phi)|\le C_Kp_{K,m_K}(\phi),\qquad \phi\in\mathcal D_K.
\tag{1.2}
\]

This is continuity on the test-function inductive limit. We say \(u\) has order at most \(k\) on \(X\) when the same integer \(k\) can be used for every compact \(K\), while \(C_K\) may vary. A local order bound and a single global estimate with a constant independent of support are different assertions.

**Proposition 1.1 (the sequential test).** A linear form on \(\mathcal D(X)\) is a distribution if and only if it sends every sequence tending to zero in \(\mathcal D(X)\) to a scalar sequence tending to zero.

Here convergence in \(\mathcal D(X)\) means that the supports lie in one compact \(K\) and every derivative tends uniformly to zero.

**Proof.** Estimate (1.2) immediately gives the forward implication. Conversely, if no finite estimate holds on some \(\mathcal D_K\), choose \(\phi_j\) with \(|u(\phi_j)|>j p_{K,j}(\phi_j)\). Dividing by \(u(\phi_j)\) gives \(\psi_j\) with

\[
u(\psi_j)=1,\qquad p_{K,j}(\psi_j)<1/j.
\]

For each fixed derivative index, its supremum tends to zero as \(j\to\infty\). The supports stay in \(K\). Thus \(\psi_j\to0\) in the test space, while its images remain one, a contradiction. \(\square\)

**Proposition 1.2 (extension to finitely differentiable tests).** If \(u\) has order at most \(k\) on \(X\), it has a unique linear extension to \(C_c^k(X)\) that is continuous in the \(C^k\) norm on each common compact support.

If (1.2) holds with \(m_K=k\), the same estimate, with the same constant, holds for \(C^k\) functions supported in the interior of \(K\). For a function whose support touches the boundary of \(K\), an estimate on a larger compact neighborhood always suffices.

**Proof.** Extend \(f\in C_c^k(X)\) by zero to Euclidean space. Since its support lies compactly inside \(X\), this is \(C^k\). Convolution with smooth mollifiers produces \(f_\varepsilon\in\mathcal D(X)\) for small \(\varepsilon\), with support in one compact neighborhood \(K_1\) of \(\operatorname{supp}f\), and

\[
p_{K_1,k}(f_\varepsilon-f)\longrightarrow0.
\tag{1.3}
\]

Indeed differentiation through order \(k\) commutes with convolution, and each compactly supported continuous derivative is uniformly continuous. Estimate (1.2) makes \(u(f_\varepsilon)\) Cauchy. Define \(u(f)\) to be its limit.

Two approximating families have their supports in one larger compact and their difference tends to zero in \(C^k\), so they give the same limit. The same observation proves linearity and uniqueness. Passing to the limit in the order estimate proves continuity. If the support of \(f\) is contained in the interior of \(K\), sufficiently small mollifications remain in \(K\), and that limiting estimate keeps the original \(C_K\). Without this support margin, those mollifications need not remain in \(K\); the larger-compact formulation avoids that unjustified step. \(\square\)

Order zero therefore allows all compactly supported continuous tests. The estimate is local in their support.

## One weighted estimate for every support

The local orders \(m_K\) can grow as the support moves through \(X\). Continuous weights encode this variation without choosing a new estimate for every test.

**Theorem 2.1 (locally finite derivative weights).** A linear form \(u\) on \(\mathcal D(X)\) is a distribution if and only if there exist nonnegative continuous functions \(\rho_\alpha\) on \(X\), indexed by multi-indices, such that:

1. On each compact subset of \(X\), all but finitely many \(\rho_\alpha\) vanish identically.
2. Every test satisfies

\[
|u(\phi)|\le
\sum_\alpha\|\rho_\alpha\partial^\alpha\phi\|_\infty.
\tag{2.1}
\]

The sum is finite for each test. The weights may be chosen zero for \(|\alpha|>k\) if and only if \(u\) has order at most \(k\).

**Proof.** If the weights exist, their restrictions to a compact \(K\) have finite suprema, and only finitely many indices occur. Thus (2.1) implies (1.2). If they vanish above degree \(k\), it gives the order-\(k\) estimate.

For the converse, choose a countable locally finite smooth partition \(1=\sum_{j\ge1}\psi_j\) on \(X\), with each \(\psi_j\) compactly supported in \(X\). Such a partition follows from an exhaustion by compact subsets and ordinary smooth cutoffs. The supports meet each compact in only finitely many places. On \(K_j=\operatorname{supp}\psi_j\), choose an estimate

\[
|u(g)|\le C_jp_{K_j,m_j}(g),\qquad g\in\mathcal D_{K_j}.
\]

For \(|\beta|\le m_j\), put

\[
A_{j,\beta}(x)=
\sum_{\substack{|\alpha|\le m_j\\\beta\le\alpha}}
\binom{\alpha}{\beta}
|\partial^{\alpha-\beta}\psi_j(x)|;
\tag{2.2}
\]

otherwise put \(A_{j,\beta}=0\). Here \(\beta\le\alpha\) means coordinatewise inequality. These functions are nonnegative and continuous, with support in \(K_j\). The product rule at each point, followed by a supremum, gives

\[
p_{K_j,m_j}(\psi_j\phi)
\le\sum_\beta\|A_{j,\beta}\partial^\beta\phi\|_\infty.
\]

Define

\[
\rho_\beta(x)=\sum_{j\ge1}2^j C_j A_{j,\beta}(x).
\tag{2.3}
\]

This sum is locally finite, so \(\rho_\beta\) is continuous. On a compact set only finitely many \(K_j\) meet it; their finitely many \(m_j\) show that only finitely many derivative weights are nonzero there.

For a test \(\phi\), the partition expansion has only finitely many nonzero terms. Since \(C_jA_{j,\beta}\le2^{-j}\rho_\beta\),

\[
\begin{aligned}
|u(\phi)|
&\le\sum_j|u(\psi_j\phi)|\\
&\le\sum_j2^{-j}\sum_\beta
\|\rho_\beta\partial^\beta\phi\|_\infty\\
&\le\sum_\beta\|\rho_\beta\partial^\beta\phi\|_\infty.
\end{aligned}
\]

If \(u\) has order at most \(k\), choose every \(m_j=k\); (2.2) then has no indices above \(k\). This proves both the general result and its finite-order refinement. \(\square\)

## Distributions are locally finite derivatives of measures

The weights also give a useful representation. The two cited theorems have these precise forms:

- A bounded complex-linear functional on a subspace of a complex normed space extends to the whole space with the same norm. The subspace need not be closed, and the space need not be complete.
- A positive linear functional on \(C_c(Y)\), for a locally compact Hausdorff space \(Y\), is integration against a unique positive Radon measure. This measure is finite on compact sets, outer regular on Borel sets and inner regular on open sets.

An open Euclidean \(X\) satisfies those topological hypotheses. It is also a countable union of compact sets, so the cited regularity proposition gives inner regularity on all its Borel sets. No group structure is involved.

We first need a small passage from positive to complex functionals. Write \(C_0(X)\) for continuous functions tending to zero outside compact subsets, with the supremum norm.

**Lemma 3.1 (complex representation on \(C_0\)).** Every bounded complex-linear functional \(L\) on \(C_0(X)\) is integration against a finite complex Radon measure. One can bound its total variation by \(4\|L\|\). This nonoptimal bound is sufficient below.

**Proof.** For a bounded real-linear functional \(h\) on real \(C_0(X)\), and \(f\ge0\), define

\[
h^+(f)=\sup_{0\le g\le f}h(g).
\tag{3.1}
\]

It lies between zero and \(\|h\|\|f\|_\infty\). It is positively homogeneous. It is additive on nonnegative functions: the lower inequality follows by adding admissible \(g_1,g_2\); for the upper inequality split any \(0\le g\le f_1+f_2\) as

\[
g_1=\min(g,f_1),\qquad g_2=g-g_1,
\]

so \(0\le g_i\le f_i\). These are continuous functions in \(C_0(X)\). Taking suprema gives the reverse inequality.

Extend \(h^+\) to all real functions by positive-minus-negative parts. Additivity on the positive cone makes this well-defined and linear: if \(f=a-b\) with \(a,b\ge0\), the equality \(a+f^-=b+f^+\) shows that the assigned difference equals \(h^+(f^+)-h^+(f^-)\). Put \(h^-=h^+-h\). This is positive because \(g=f\) is admissible in (3.1). On \(f\ge0\) it also satisfies

\[
h^-(f)=\sup_{0\le g\le f}[-h(g)]
\le\|h\|\|f\|_\infty,
\]

by replacing \(g\) with \(f-g\) in (3.1). Positivity bounds the absolute value on any real \(f\) by the value on \(|f|\), so both extensions are bounded.

Apply the positive Riesz theorem to their restrictions to \(C_c(X)\). It gives two positive Radon measures \(\mu^+,\mu^-\). Their total masses are at most \(\|h\|\), because the formula for the measure of the open set \(X\) is the supremum of their functional values on compactly supported functions between zero and one. Thus \(h\) is represented there by \(\mu^+-\mu^-\). Compactly supported continuous functions are dense in \(C_0(X)\): multiplying by a cutoff equal to one on a growing compact set gives uniform convergence. The finite mass bounds extend the equality to all \(C_0(X)\).

Take \(h_1=\operatorname{Re}L\) and \(h_2=\operatorname{Im}L\) on real functions. Their norms are at most \(\|L\|\). The measure \((\mu_1^+-\mu_1^-)+i(\mu_2^+-\mu_2^-)\) represents \(L\), first on real functions and then on complex functions by complex linearity. Its total variation is bounded by the sum of these four masses, at most \(4\|L\|\). \(\square\)

**Theorem 3.2 (measure-derivative representation).** For every \(u\in\mathcal D'(X)\) there are complex Radon measures \(\nu_\alpha\), locally finite in both of these senses:

- Each measure has finite total variation on every compact subset of \(X\).
- Each compact subset has a neighborhood meeting the supports of only finitely many \(\nu_\alpha\).

They represent \(u\) by

\[
u(\phi)=\sum_\alpha\int_X\partial^\alpha\phi\,d\nu_\alpha,
\qquad
u=\sum_\alpha(-1)^{|\alpha|}\partial^\alpha\nu_\alpha.
\tag{3.2}
\]

Every test sees a finite sum. If \(u\) has order at most \(k\), only \(|\alpha|\le k\) are needed. Conversely, a finite-degree representation by locally finite Radon measures gives a distribution of that order. No uniqueness of the representing measures is asserted.

**Proof.** Choose the weights of Theorem 2.1. In the normed space

\[
B=\ell^1(\{\alpha\};C_0(X)),\qquad
\|(g_\alpha)\|_B=\sum_\alpha\|g_\alpha\|_\infty,
\]

define \(J\phi=(\rho_\alpha\partial^\alpha\phi)_\alpha\). Each component is continuous and compactly supported, and only finitely many are nonzero. Inequality (2.1) makes \(F(J\phi)=u(\phi)\) well-defined: if \(J\phi=0\), the inequality forces \(u(\phi)=0\). It also gives \(\|F\|\le1\) on the subspace \(J\mathcal D(X)\).

The cited complex Hahn–Banach theorem extends \(F\) to \(L\in B'\) of norm at most one. Restrict \(L\) to the \(\alpha\)-th coordinate. Lemma 3.1 gives a finite complex measure \(\mu_\alpha\), with total variation at most four, representing that restriction. Finite coordinate sums are dense in \(B\), and the same bound makes their integrals absolutely summable. Consequently

\[
L((g_\alpha))=\sum_\alpha\int g_\alpha\,d\mu_\alpha.
\]

Set \(\nu_\alpha=\rho_\alpha\mu_\alpha\). A continuous weight is bounded on a compact set, so this measure has locally finite total variation. Its support is contained in \(\operatorname{supp}\rho_\alpha\). Given a compact \(K\subset X\), choose a larger compact neighborhood \(K_1\subset X\). All but finitely many weights vanish identically on \(K_1\), so those supports miss its interior. This proves the stated local finiteness of the family, including its neighborhood formulation.

Apply the preceding identity to \(J\phi\), giving the first equation in (3.2). The distributional derivative convention is \((\partial^\alpha v)(\phi)=(-1)^{|\alpha|}v(\partial^\alpha\phi)\); this proves the second, with its sign.

For order at most \(k\), the weights above that degree are zero, so the corresponding measures can be zero. Conversely, on a compact \(K\), a finite-degree representation satisfies

\[
|u(\phi)|\le
\sum_{|\alpha|\le k}|\nu_\alpha|(K)
\sup_K|\partial^\alpha\phi|,
\qquad \phi\in\mathcal D_K,
\]

which is an order-\(k\) estimate. The same calculation shows that any locally finite family without a degree bound still gives a distribution, with an order depending on \(K\). \(\square\)

**Corollary 3.3 (order zero is precisely a measure).** Distributions of order zero on \(X\) are exactly the locally finite complex Radon measures, with their pairing extended to \(C_c(X)\). The representing measure is unique.

**Proof.** Take \(k=0\) in Theorem 3.2 for existence and its converse. If two such measures give the same integrals on smooth tests, uniform mollification and the compact mass bounds give the same integrals on \(C_c(X)\). Positive Riesz uniqueness applied to the real and imaginary differences identifies them locally, hence on \(X\). Here a complex measure can be expressed locally as a combination of four positive measures, so positivity uniqueness applies to the equality between the corresponding sums of positive parts. \(\square\)

## Positivity forces order zero

Call a complex-linear form on \(\mathcal D(X)\) positive if \(u(\phi)\) is real and nonnegative whenever \(\phi\) is real, smooth and nonnegative.

**Theorem 4.1 (positive forms are measures).** Every positive linear form on \(\mathcal D(X)\) is automatically a distribution of order zero. Its unique extension to \(C_c(X)\) is integration against a positive Radon measure.

**Proof.** Fix a compact \(K\subset X\) and a nonnegative smooth cutoff \(\chi\) with compact support and \(\chi=1\) on \(K\). For a real \(\phi\in\mathcal D_K\), both \(\|\phi\|_\infty\chi+\phi\) and \(\|\phi\|_\infty\chi-\phi\) are nonnegative. Positivity makes \(u(\phi)\) real and gives

\[
|u(\phi)|\le u(\chi)\|\phi\|_\infty.
\tag{4.1}
\]

For complex \(\phi\), take a unit scalar \(\theta\) with \(\theta u(\phi)=|u(\phi)|\), unless its value is zero. Reality on real functions and complex linearity give

\[
|u(\phi)|=u(\operatorname{Re}(\theta\phi))
\le u(\chi)\|\phi\|_\infty.
\tag{4.2}
\]

Thus the form is a distribution of order zero without any initial continuity assumption. Proposition 1.2 extends it uniquely to \(C_c(X)\).

For \(f\ge0\) continuous with compact support, zero extension followed by convolution with nonnegative mollifiers gives nonnegative smooth approximants in one compact neighborhood. Their images are nonnegative, so the extension is positive. The cited positive Riesz theorem applies and gives the measure, with uniqueness. \(\square\)

The measure can have infinite mass on all of \(X\); (4.2) controls it on compact regions. A derivative of a point mass does not satisfy positivity: its pairing with a nonnegative function can have either sign depending on that function's slope at the point.

## Limits on smooth tests

**Theorem 5.1 (weak completeness and uniform local order).** Suppose \(u_j\in\mathcal D'(X)\) and \(u_j(\phi)\) has a scalar limit for every \(\phi\in\mathcal D(X)\). Then these limits define \(u\in\mathcal D'(X)\). On every fixed compact \(K\) there are \(C_K,m_K\), independent of \(j\), such that (1.2) holds for all \(u_j\) and for \(u\).

If \(\phi_j\to\phi\) in \(\mathcal D(X)\), then \(u_j(\phi_j)\to u(\phi)\). The sequence also converges uniformly on every bounded subset of \(\mathcal D(X)\), which is convergence in its strong dual. This statement about sequences does not identify the weak and strong topologies or make the same assertion for arbitrary nets.

**Proof.** Scalar pointwise limits are linear. Fix \(K\). The space \(\mathcal D_K\), with the increasing seminorms (1.1), is Fréchet: a Cauchy sequence has uniformly convergent derivatives of every order, their limits fit differentiation, and the limit has support in \(K\).

For integers \(r\ge1\), the sets

\[
A_r=\{\phi\in\mathcal D_K:\sup_j|u_j(\phi)|\le r\}
\]

are closed and cover \(\mathcal D_K\), since a convergent scalar sequence is bounded. Baire's theorem gives an \(A_r\) with interior. Differences of two points in a sufficiently small translated neighborhood then give

\[
\sup_j|u_j(h)|\le2r
\quad\text{when }p_{K,m}(h)<\varepsilon
\]

for some \(m,\varepsilon>0\). Scaling proves \(\sup_j|u_j(h)|\le C p_{K,m}(h)\). The seminorm includes the function itself, so its zero value implies \(h=0\), covering that case. Passing to the scalar limit gives the same bound for \(u\). Doing this for every \(K\) proves \(u\) is a distribution.

For convergent moving tests, all supports are in one compact set, and

\[
u_j(\phi_j)-u(\phi)
=u_j(\phi_j-\phi)+(u_j-u)(\phi).
\tag{5.1}
\]

The first term tends to zero by the common order estimate, and the second by hypothesis.

Finally a bounded test family has common compact support and uniform bounds on all derivatives. Arzelà–Ascoli applied to derivatives through degree \(m\), using the next derivative for equicontinuity on a compact neighborhood, supplies a finite net in the \(p_{K,m}\) seminorm. The net centers can be chosen in the family. Pointwise convergence on the finitely many centers and the uniform bound for \(u_j-u\) give uniform convergence on that family. This is precisely the strong-dual conclusion. \(\square\)

Equivalently, every weakly Cauchy sequence of distributions has a weak limit: each scalar test pairing is then Cauchy and hence convergent, so the theorem applies.

**Theorem 5.2 (positive convergence reaches continuous tests).** If the \(u_j\) in Theorem 5.1 are positive, their limit \(u\) is positive, and their Radon measures satisfy

\[
u_j(f)\longrightarrow u(f)
\quad\text{for every }f\in C_c(X).
\tag{5.2}
\]

This is convergence against compactly supported continuous tests. It need not be convergence of total masses or convergence against all bounded continuous functions.

**Proof.** Positivity passes to limits on nonnegative smooth tests. Theorem 4.1 identifies the limit and every \(u_j\) as measures.

Fix a compact neighborhood \(K_1\) of the support of \(f\), contained in \(X\), and a smooth \(\chi\ge0\) equal to one on \(K_1\). The sequence \(u_j(\chi)\) converges, so it is bounded by a common \(M\); enlarge \(M\) to include \(u(\chi)\). Inequality (4.2), extended by uniform approximation, gives

\[
|u_j(g)|+|u(g)|\le2M\|g\|_\infty
\quad\text{if }\operatorname{supp}g\subset K_1.
\tag{5.3}
\]

Choose a smooth approximation \(g\) to \(f\), still supported in \(K_1\). Then

\[
|u_j(f)-u(f)|
\le2M\|f-g\|_\infty+|u_j(g)-u(g)|.
\]

First make the approximation error arbitrarily small, then let \(j\to\infty\). This proves (5.2). \(\square\)

For contrast, the signed measures

\[
v_j=j(\delta_{1/j}-\delta_0)
\tag{5.4}
\]

on the line converge on smooth tests to \(-\delta_0'\), because \(j(\phi(1/j)-\phi(0))\to\phi'(0)\). But for a continuous compactly supported \(f\) equal to \(\sqrt{|x|}\) near zero, \(v_j(f)=\sqrt j\) for all sufficiently large \(j\). Continuous-test convergence fails, and the limit is not a measure. Positivity prevents exactly this uncontrolled local cancellation.

## Exercises

1. **Order and locality — advanced.** On \(\mathbb R\), let \(w=\sum_{j\ge1}\delta_j^{(j)}\). Prove this is a distribution, and that it has no finite global order. Use tests near one chosen integer to prove the latter assertion; an infinite formal sum alone is not a proof.
2. **Cancellation — intermediate.** For (5.4), compute its distributional limit, its total variation, and its value on the continuous test in the preceding paragraph. Prove that the limiting derivative of a point mass has order exactly one.
3. **What convergence does not imply — foundation.** Show that the positive measures \(\mu_j=j\delta_j\) converge to zero against every compactly supported continuous test, although their total masses tend to infinity. Give a bounded continuous test against which they do not converge to zero.
4. **Signs and nonuniqueness — intermediate.** In one dimension, write the distributional derivative of a smooth compactly supported function \(h\) in the first pairing form of (3.2). Check its sign. Give two different measure families representing the zero distribution, using \(h\) and \(h'\).
5. **Uniform continuous tests — advanced.** Under the hypotheses of Theorem 5.2, let \(\mathcal B\subset C_c(X)\) have one common compact support, a uniform supremum bound and a common modulus of continuity after zero extension. Prove \(\sup_{f\in\mathcal B}|u_j(f)-u(f)|\to0\). Explain how the finite-net argument differs from trying to approximate every \(f\) separately with an error depending on \(f\).

## Complete solutions

**Solution 1.** Every compact interval meets only finitely many positive integers. Thus each test has a finite pairing sum, and on a fixed compact \(K\),

\[
|w(\phi)|\le
\sum_{j\in K\cap\mathbb N}\sup_K|\phi^{(j)}|.
\]

This is a finite-order local bound; when there are no integers the restriction is zero.

Suppose a global order \(k\) existed and choose an integer \(j>k\). In a compact interval \(K\) around \(j\) containing no other positive integer, \(w=\delta_j^{(j)}\). Choose a smooth compactly supported \(b\) near zero with \(b^{(j)}(0)\ne0\), and set \(\phi_\varepsilon(x)=\varepsilon^k b((x-j)/\varepsilon)\). For small \(\varepsilon\), it is supported in \(K\); its derivatives through degree \(k\) are bounded independently of \(\varepsilon\). But

\[
|w(\phi_\varepsilon)|
=\varepsilon^{k-j}|b^{(j)}(0)|\longrightarrow\infty.
\]

This contradicts an order-\(k\) estimate on that fixed \(K\). Local finiteness makes the distribution exist while allowing its local orders to grow without bound.

**Solution 2.** Taylor expansion gives \(v_j(\phi)=\phi'(0)+O(j^{-1})\) for each fixed smooth \(\phi\), so its limit is \(-\delta'_0\), since \(\delta'_0(\phi)=-\phi'(0)\). The two masses are at distinct points and have coefficients \(j,-j\), so \(|v_j|(\mathbb R)=2j\). For the specified continuous test, \(f(0)=0\) and \(f(1/j)=j^{-1/2}\), giving \(\sqrt j\).

The bound \(|\delta'_0(\phi)|\le\sup|\phi'|\) gives order at most one. It cannot have order zero: for a smooth compactly supported \(b\) with \(b'(0)\ne0\), the tests \(b(x/\varepsilon)\) have uniformly bounded values and common compact support, while their derivative at zero has magnitude \(\varepsilon^{-1}|b'(0)|\). Thus its order is exactly one. Changing its sign does not change that order.

**Solution 3.** For a fixed \(f\in C_c(\mathbb R)\), the point \(j\) lies outside its support for all sufficiently large \(j\). Hence \(\mu_j(f)=0\) eventually. But \(\mu_j(\mathbb R)=j\). The bounded continuous function \(f=1\), which is not compactly supported, gives \(\mu_j(f)=j\), and there is no convergence to zero. The positivity theorem makes no assertion about mass escaping every compact set.

**Solution 4.** Integration by parts gives

\[
(\partial h)(\phi)=-\int h\phi'\,dx.
\]

In the first form of (3.2), take \(\nu_1=-h\,dx\) and \(\nu_0=0\). In the second form the factor \((-1)^1\) gives \(-\partial(-h\,dx)=\partial(h\,dx)\), which is the same distribution.

For a nonzero compactly supported \(h\), let \(\nu_0=h'\,dx\), \(\nu_1=h\,dx\), with other measures zero. Then the first form pairs as \(\int h'\phi\,dx+\int h\phi'\,dx=0\). These measures represent zero, as does the all-zero family. This explicit cancellation proves nonuniqueness; uniqueness of an order-zero measure alone does not give uniqueness after derivative terms are introduced.

**Solution 5.** Put all supports inside a compact neighborhood \(K_1\subset X\). The uniform bound and common modulus of continuity make the family precompact in the supremum norm by Arzelà–Ascoli on \(K_1\); its zero extensions have no new boundary discontinuity. Choose a finite \(\varepsilon\)-net with centers \(f_1,\ldots,f_N\) from the family. Positivity gives a common bound \(M\) as in (5.3), for both the measures and their limit on that neighborhood. For \(f\) within \(\varepsilon\) of a center,

\[
|(u_j-u)(f)|
\le2M\varepsilon+\max_{1\le l\le N}|(u_j-u)(f_l)|.
\]

Each center tends to zero by (5.2). Taking the supremum, then the limit superior, gives at most \(2M\varepsilon\); let \(\varepsilon\downarrow0\). A separate approximation chosen for each function would not control the supremum over the whole family. The finite net and common measure bound make the error uniform.

## References

- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2026. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
- *Banach estimates, quotient spaces and compact parameter arguments*, “Norm-preserving complex extension and scalar detection.” Course lesson.
- *Haar measure on locally compact groups*, Section 2, Theorem 2.2 and Proposition 2.3. Course lesson.
