# Hypoellipticity and complex zeros

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

An equation is hypoelliptic when its solutions are smooth wherever its data are smooth. For constant coefficients, this local property is equivalent to a geometric statement about the complex zeros of its polynomial: those zeros must retreat from real frequency space as the real frequency tends to infinity. We prove the equivalence, its quantitative version, and two criteria that test only a single local weighted solution space.

Read [Symbols at infinity](symbols-at-infinity.md) and [Wavefronts of regular kernels](wavefronts-of-regular-kernels.md). We also use the local weighted spaces from [Local regularity, sharp embeddings, and compactness](local-regularity-and-compactness.md). Grubb's lectures [Grubb] give the distribution and Fourier background; Coste [Coste] explains the algebraic asymptotics behind the power estimates; Hörmander's seminar article [Hormander] develops the broader limiting-symbol approach to singularities.

Keep \(D=-i\partial\). All polynomials may have complex coefficients. The smooth wavefront set is denoted by \(\operatorname{WF}\). We use its cutoff stability, its base projection onto singular support, and its decrease under differential operators. One further convolution fact will be used explicitly: if a distribution \(E\) is smooth off zero and \(f\) has compact support, then
\[
\operatorname{WF}(E*f)\subset\operatorname{WF}(f).
\tag{1}
\]
The convolution exists because \(f\) is compact. This is the usual wavefront estimate for convolution specialized to a kernel whose only possible singular base point is zero. We assume this exact estimate as the [planned smooth-wavefront convolution prerequisite](../prerequisites/planned-foundation-proofs.html#smooth-wavefront-convolution); its separate foundational proof is still to be written.

[Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html), Section 14.5, proves the Fréchet closed graph theorem used for the solution spaces. [Continuous functionals, test families and compact limits](continuous-functionals-and-test-families.md), Section 3, proves compact smooth subsequences. [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md), Section 1, gives uniform holomorphic limits and the Cauchy estimates used in their specialization.

## Measuring the distance to a complex zero

Let \(P\ne0\) have degree at most \(m\), and define
\[
\begin{gathered}
Z_P=\{\zeta\in\mathbb C^n:P(\zeta)=0\},\\
d_P(\xi)=\operatorname{dist}(\xi,Z_P),
\qquad \xi\in\mathbb R^n.
\end{gathered}
\tag{2}
\]
Distance uses the Euclidean norm on \(\mathbb C^n=\mathbb R^{2n}\). For a nonzero constant polynomial set \(d_P=\infty\). Every nonconstant polynomial has a complex zero: fix all but one variable at values where its leading coefficient in that variable is nonzero, and apply the fundamental theorem of algebra. Its zero set is closed, so the distance is finite and attained.

When \(P(\xi)\ne0\), put
\[
A_P(\xi)=\sum_{1\leq|\alpha|\leq m}
\left|\frac{\partial^\alpha P(\xi)}{P(\xi)}\right|^{1/|\alpha|}.
\tag{3}
\]

**Lemma 1.1.** There are constants \(c,C>0\), depending only on \(m,n\), such that
\[
\begin{gathered}
\frac c{d_P(\xi)}\leq A_P(\xi)\leq\frac C{d_P(\xi)},\\
P(\xi)\ne0.
\end{gathered}
\tag{4}
\]
For a constant polynomial both sides are zero, using \(1/\infty=0\).

**Proof.** Suppose \(P\) is nonconstant. Write \(A=A_P(\xi)>0\). Each derivative ratio is at most \(A^{|\alpha|}\). The finite Taylor formula therefore gives, for complex \(z\),
\[
\left|\frac{P(\xi+z)}{P(\xi)}-1\right|
\leq\sum_{1\leq|\alpha|\leq m}
\frac{(A|z|)^{|\alpha|}}{\alpha!}.
\tag{5}
\]
Choose \(c>0\), depending only on \(m,n\), so that the sum with \(A|z|\) replaced by \(c\) is less than one. There is no zero in \(|z|<c/A\). Hence \(d_P(\xi)\geq c/A\), which proves the first inequality.

For the second inequality let \(d=d_P(\xi)>0\). If \(|z|\leq d\), consider the one-variable polynomial \(r(s)=P(\xi+sz)\). It is nonzero at zero. If its degree is \(l\), factor it as
\[
\frac{r(s)}{r(0)}=\prod_{\nu=1}^l(1-s/s_\nu).
\]
Every root satisfies \(|s_\nu||z|\geq d\), so \(|s_\nu|\geq1\). The constant case \(l=0\) is included by the empty product. At \(s=1\) this gives
\[
|P(\xi+z)|\leq2^m|P(\xi)|
\quad(|z|\leq d).
\tag{6}
\]
Apply the several-variable Cauchy estimate on the polydisk with each radius \(d/\sqrt n\), contained in that ball:
\[
|\partial^\alpha P(\xi)|
\leq\alpha!\,2^m n^{|\alpha|/2}
|P(\xi)|d^{-|\alpha|}.
\tag{7}
\]
Taking the indicated roots and summing over the finitely many multi-indices proves \(A_P(\xi)\leq C/d\). \(\square\)

The fractional powers in (3) are needed because derivatives of different orders detect zeros at different scales.

## Retreat from real space has a polynomial rate

**Theorem 2.1.** The following conditions are equivalent:

1. \(d_P(\xi)\to\infty\) as real \(|\xi|\to\infty\).
2. For some \(a,c,R>0\), \(d_P(\xi)\geq c|\xi|^a\) when \(|\xi|>R\).
3. \(P\) has no real zeros outside a ball, and \(\partial^\alpha P(\xi)/P(\xi)\to0\) for every \(\alpha\ne0\).
4. For some \(a,C,R>0\), \(P(\xi)\ne0\) and
   \[
\begin{gathered}
\left|\frac{\partial^\alpha P(\xi)}{P(\xi)}\right|
\leq C|\xi|^{-a|\alpha|},\\
|\xi|>R,\quad\alpha\ne0.
\end{gathered}
\tag{8}
\]
5. For zeros \(\zeta\in Z_P\), \(|\operatorname{Im}\zeta|\to\infty\) whenever \(|\zeta|\to\infty\).

The nonzero constant case satisfies every condition, with the assertions about zeros vacuous. In the positive-degree case the exponent can be chosen at most one.

**Proof.** By Lemma 1.1, outside real zeros, \(A_P\to0\) if and only if \(d_P\to\infty\). The finite sum (3) tends to zero if and only if every derivative ratio does. Condition 1 also excludes real zeros outside a ball. Thus 1 and 3 are equivalent.

To obtain the power, suppose \(P\) is nonconstant and set
\[
M(r)=\min_{|\xi|=r}d_P(\xi).
\tag{9}
\]
The distance to a nonempty closed set is continuous, so the minimum exists. It is semialgebraic. Indeed the real and imaginary parts of \(P(\zeta)=0\), the squared distance, and \(|\xi|^2=r^2\) are polynomial conditions in real coordinates. A closest zero can be described by saying that it is a zero and that no zero has smaller squared distance. A minimum over the real sphere is then another quantified polynomial condition. The projection lemma from the symbols-at-infinity lesson applies.

If condition 1 holds, \(M(r)\to\infty\). The one-parameter asymptotic lemma gives
\[
\begin{gathered}
M(r)=b r^a(1+o(1)),\\
b>0,\qquad a>0.
\end{gathered}
\tag{10}
\]
Hence 2 follows. Conversely 2 immediately gives 1. A fixed zero \(\zeta_0\) gives \(d_P(\xi)\leq|\xi-\zeta_0|\leq|\xi|+|\zeta_0|\), so such a power can be taken with \(a\leq1\).

By (4), condition 2 gives \(A_P(\xi)\leq C|\xi|^{-a}\). Each summand is at most this bound; raising it to \(|\alpha|\) proves (8). Only finitely many derivatives are nonzero, so the finitely many constants can be enlarged to a common \(C\). Condition 4 gives 3, completing the first four equivalences.

If 1 fails, there are real \(\xi_j\to\infty\) and zeros \(\zeta_j\) at uniformly bounded distance from them. Then \(|\zeta_j|\to\infty\) but \(|\operatorname{Im}\zeta_j|\) stays bounded, contradicting 5. Conversely if 5 fails, choose unbounded zeros with bounded imaginary parts. Their real parts tend to infinity and have distance at most that imaginary bound from \(Z_P\). This contradicts 1. \(\square\)

The power in (8) is proportional to the derivative order. An assertion with a single decay power for all derivatives would give a weaker estimate.

## The local analytic property

Call \(P(D)\) **hypoelliptic** if, for every open set \(X\subset\mathbb R^n\) and every \(u\in\mathcal D'(X)\), smoothness of \(P(D)u\) on \(X\) implies smoothness of \(u\) on \(X\).

**Theorem 3.1.** For \(P\ne0\), each condition of Theorem 2.1 is equivalent to each of the following:

1. On every open \(X\), \(\operatorname{WF}(u)=\operatorname{WF}(P(D)u)\) for all \(u\in\mathcal D'(X)\).
2. On every open \(X\), \(u\) and \(P(D)u\) have the same singular support.
3. Every homogeneous distributional solution on every open set is smooth.
4. \(P(D)\) has a fundamental solution \(E\) with singular support exactly \(\{0\}\).

These are also equivalent to hypoellipticity as defined above.

**Proof.** Wavefront equality implies singular-support equality by projection. The latter gives both hypoellipticity and smoothness of all homogeneous solutions. Hypoellipticity itself also gives smoothness of homogeneous solutions.

Suppose every homogeneous distributional solution is smooth. Choose a regular fundamental solution \(E\). It solves the homogeneous equation off zero, so its singular support is contained in \(\{0\}\). For each normalized localization \(Q\), the lower localization theorem in the wavefronts lesson supplies a fundamental solution \(G\) of \(Q(D)\) with support contained in this singular support. Thus \(\operatorname{supp}G\subset\{0\}\). The minimal linear-support theorem in the active-directions lesson implies \(V_Q\subset\{0\}\); therefore \(Q\) is constant.

It follows that every positive-order coefficient of \(T_P(\eta)\) tends to zero as \(|\eta|\to\infty\). Otherwise a sequence with one such coefficient bounded away from zero would have a coefficient-convergent subsequence on the unit sphere, producing a nonconstant localization. Hence
\[
\begin{gathered}
\frac{\partial^\alpha P(\eta)}{S_P(\eta)}\to0
\quad(\alpha\ne0),\\
\frac{|P(\eta)|}{S_P(\eta)}\to1.
\end{gathered}
\tag{11}
\]
In particular \(P\) is eventually nonzero on real space, and all ratios \(\partial^\alpha P/P\) tend to zero. This is condition 3 of Theorem 2.1.

Conversely that condition makes every localization constant. Its active subspace is zero. The canonical wavefront upper bound in the wavefronts lesson therefore gives a fundamental solution smooth off zero. It cannot also be smooth at zero: a differential operator applied to a smooth function is smooth, whereas its value here is delta. Its singular support is exactly \(\{0\}\).

It remains to show that such an \(E\) gives wavefront equality. First let \(v\) have compact support. Convolution and differentiation commute, and
\[
v=E*P(D)v.
\tag{12}
\]
By (1), \(\operatorname{WF}(v)\subset\operatorname{WF}(P(D)v)\). The opposite inclusion follows from decrease of wavefront sets under differential operators.

For general \(u\in\mathcal D'(X)\), fix \(x_0\in X\), and choose \(\chi\in C_c^\infty(X)\) equal to one on a neighborhood of \(x_0\). Extend \(\chi u\) by zero to all of space. Equation (12) gives
\[
\begin{aligned}
\chi u&=E*(\chi P(D)u)\\
&\quad+E*([P(D),\chi]u).
\end{aligned}
\tag{13}
\]
The commutator has compact support away from \(x_0\). Because \(E\) is smooth off zero, its convolution with that commutator is smooth near \(x_0\): the test kernels and all their spatial derivatives avoid the singular base point, and their pairing with a fixed compact distribution is smooth. The first term has wavefront contained in that of \(\chi P(D)u\), by (1). Near \(x_0\), this gives \(\operatorname{WF}(u)\subset\operatorname{WF}(P(D)u)\). Differential decrease supplies the reverse inclusion. Since \(x_0\) was arbitrary, condition 1 follows. \(\square\)

The argument uses all open sets for the qualitative characterization. The next criterion requires only one nonempty open set, but restricts the solutions to a specified weighted space.

## Testing one weighted space of homogeneous solutions

Let \(k\) be a positive moderate weight and \(1\leq p\leq\infty\). On a nonempty open \(X\), write
\[
\begin{gathered}
\mathcal N_{p,k}(X)=\\
\{u\in B_{p,k}^{\mathrm{loc}}(X):P(D)u=0\}.
\end{gathered}
\tag{14}
\]
It is a closed subspace of the local weighted Fréchet space: the inclusion into distributions and application of \(P(D)\) are continuous.

**Theorem 4.1.** If every member of \(\mathcal N_{p,k}(X)\) is smooth for one such \(X,p,k\), then \(P(D)\) is hypoelliptic.

**Proof.** The inclusion \(\mathcal N_{p,k}(X)\to C^\infty(X)\) has closed graph, because convergence in either topology implies convergence to the same distribution. The Fréchet closed graph theorem makes it continuous. A sequence bounded in every local weighted seminorm must therefore be bounded in every smooth seminorm.

If the zero-escape condition of Theorem 2.1 failed, there would be complex zeros
\[
\begin{gathered}
\zeta_j=\xi_j+i\eta_j,\\
|\xi_j|\to\infty,\qquad|\eta_j|\leq B.
\end{gathered}
\tag{15}
\]
Define homogeneous smooth solutions
\[
u_j(x)=\frac{e^{ix\cdot\zeta_j}}{k(\xi_j)}.
\tag{16}
\]
For each compact cutoff \(\phi\), modulation gives
\[
\widehat{\phi u_j}(\xi_j+h)
=\frac{\widehat{\phi e^{-x\cdot\eta_j}}(h)}{k(\xi_j)}.
\tag{17}
\]
The functions \(\phi e^{-x\cdot\eta_j}\) form a bounded set in \(C_c^\infty\) with common compact support. Their transforms are uniformly Schwartz. Using \(k(\xi_j+h)\leq k(\xi_j)M_k(h)\), we obtain
\[
\begin{aligned}
&\|\phi u_j\|_{p,k}\\
&\quad\leq(2\pi)^{-n/p}
\|M_k\,\widehat{\phi e^{-x\cdot\eta_j}}\|_p\\
&\quad\leq C_\phi.
\end{aligned}
\tag{18}
\]
For \(p=\infty\), the factor \((2\pi)^{-n/p}\) is one and the norm is the supremum norm. Thus the sequence is bounded in \(\mathcal N_{p,k}(X)\).

Fix \(x_0\in X\). For every integer \(r\), smooth boundedness gives uniform bounds on all \(D_l^r u_j(x_0)\). At least one coordinate of \(\zeta_j\) has modulus at least \(|\zeta_j|/\sqrt n\). Since \(e^{-x_0\cdot\eta_j}\) is bounded below by a positive constant, these bounds imply
\[
|\xi_j|^r\leq C_r k(\xi_j).
\tag{19}
\]
Moderateness gives \(k(\xi)\leq C(1+|\xi|)^N\) for some finite \(N\). Choosing an integer \(r>N\) contradicts (19). The zero-escape condition holds, so Theorems 2.1 and 3.1 prove hypoellipticity. \(\square\)

No a priori estimate was assumed: closed graph converts the qualitative smoothness hypothesis into the estimates tested by the exponential solutions.

## Compactness of the same solution space

A Fréchet space is **Montel** here if every bounded sequence has a convergent subsequence. For Fréchet spaces this is equivalent to relative compactness of bounded sets.

**Theorem 5.1.** If \(\mathcal N_{p,k}(X)\), with its local weighted topology, is Montel for one nonempty \(X\), then \(P(D)\) is hypoelliptic. Conversely, for a hypoelliptic \(P\), these solution spaces are Montel for every \(X,p,k\). They consist of all homogeneous distributional solutions, and their weighted, smooth, and induced strong distribution topologies coincide.

**Proof of necessity.** If hypoellipticity fails, take the bounded sequence (16). It tends to zero in distributions on \(X\). Indeed for any compact test its Fourier transform at \(-\zeta_j\) decreases faster than every power of \(|\xi_j|\), uniformly for bounded \(\eta_j\), while \(k(\xi_j)^{-1}\) has at most polynomial growth. These estimates are also uniform on bounded test sets.

Montel compactness would then force \(u_j\to0\) in the local weighted topology. To justify the full-sequence conclusion, any subsequence has a further convergent subsequence; its distributional limit must be zero. If some weighted seminorm stayed bounded below on a subsequence, this would contradict that further convergence.

But the inverse moderate inequality \(k(\xi_j+h)\geq k(\xi_j)/M_k(-h)\) gives, for a fixed nonzero \(\phi\in C_c^\infty(X)\),
\[
\|\phi u_j\|_{p,k}
\geq(2\pi)^{-n/p}
\left\|\frac{\widehat{\phi e^{-x\cdot\eta_j}}}{M_k(-\cdot)}\right\|_p.
\tag{20}
\]
Take a subsequence with \(\eta_j\to\eta\). The functions on the right converge in the stated \(L^p\) norm, including the supremum endpoint. To see this, convergence of \(\phi e^{-x\cdot\eta_j}\) in \(C_c^\infty\) gives Schwartz convergence of its transform, and \(1/M_k(-h)\leq M_k(h)\) has polynomial growth. The limiting norm is positive because \(\phi e^{-x\cdot\eta}\) is nonzero and Fourier transformation is injective. Equation (20) cannot tend to zero. This contradiction proves necessity.

**Proof of sufficiency and the topology statements.** Hypoellipticity makes every homogeneous distributional solution smooth; every smooth function is locally in each of these weighted spaces. The inclusion from the weighted solution space to \(C^\infty\) is continuous by the closed graph argument of Theorem 4.1. Conversely the local weighted-space theorem gives a continuous inclusion \(C^\infty\to B_{p,k}^{\mathrm{loc}}\). Thus the smooth and weighted topologies agree.

We can also compare the induced strong distribution topology directly. Choose a fundamental solution \(E\) smooth off zero, a compact \(K\subset X\), and a cutoff \(\chi\) equal to one on a neighborhood of \(K\). For a homogeneous \(u\), the compact convolution identity gives
\[
\chi u=E*([P(D),\chi]u).
\tag{21}
\]
All coefficients of the commutator are supported at a positive distance from \(K\). For \(x\) near \(K\), move its derivatives from \(u\) onto the kernel and coefficient. The result has the form
\[
u(x)=\langle u,T_x\rangle,
\qquad T_x\in C_c^\infty(X),
\tag{22}
\]
with one common compact test support. Each family \(\{\partial_x^\beta T_x:x\in K\}\) is bounded in the test-function space: \(E(x-y)\) and every derivative are smooth on the separated compact sets. Consequently every smooth seminorm on \(K\) is bounded by a strong distribution seminorm on \(u\), the supremum of its pairings with that bounded family. The reverse inclusion from \(C^\infty\) into distributions is continuous. The two induced topologies agree.

Finally, bounded sets of smooth functions have uniformly bounded derivatives on every compact set. Arzelà–Ascoli, applied successively to all derivatives on a compact exhaustion, gives a subsequence converging in \(C^\infty(X)\). The limit still satisfies \(P(D)u=0\). Transporting this compactness through the coincident topologies proves the Montel assertion. \(\square\)

For \(P(\xi_1,\xi_2)=\xi_1+i\xi_2\), the first derivative ratios have size \(1/|\xi|\), and all higher derivatives vanish. This is hypoelliptic, and \(P(D)=-2i\partial_{\bar z}\). Using the usual Cauchy–Riemann characterization of holomorphic functions, the homogeneous solution space is the holomorphic functions on \(X\subset\mathbb C\). The compactness just proved specializes to their familiar local convergence theorem: bounded families in the local weighted topology have subsequences converging with every derivative on compact subsets. A locally uniformly bounded holomorphic family is locally bounded in \(B_{2,1}\), by Plancherel after a compact cutoff, so the same conclusion applies to it.

## Passage to reciprocal symbols

The quantitative estimate (8) supplies the hypothesis used in the [constant-coefficient interface of the symbol-calculus lesson](../prerequisites/euclidean-symbol-calculus.html#an03-euc-010--the-exact-constant-coefficient-interface). We use its proved reciprocal-symbol construction: for positive degree \(m\), choose \(\rho=\min(a,1)>0\) and a smooth cutoff \(\theta\) that vanishes on a sufficiently large ball and equals one outside a larger ball. Then
\[
\left|\partial_\xi^\alpha\left(\frac{\theta(\xi)}{P(\xi)}\right)\right|
\leq C_\alpha\langle\xi\rangle^{-m\rho-\rho|\alpha|}.
\tag{23}
\]
In the notation developed there, this is \(\theta/P\in S^{-m\rho}_{\rho,0}\). The construction uses the nonzero highest derivative to bound \(P^{-1}\), and the differentiated reciprocal identity to obtain all further bounds. The cutoff avoids real zeros; the assertion makes no claim about a reciprocal across those zeros. For a constant polynomial its reciprocal is a symbol of order zero.

This also gives a direct parametrix. Put \(K=\mathcal F^{-1}(\theta/P)\) and \(h=\mathcal F^{-1}(1-\theta)\). Then
\[
P(D)K=\delta_0-h,\qquad h\in\mathcal S.
\tag{24}
\]
The kernel \(K\) is smooth off zero. Here is the application of the frequency integration-by-parts identity proved in the same symbol-calculus lesson. For a multi-index \(\beta\), the Leibniz rule and (23) bound
\[
\left|\partial_{\xi_j}^{\,N}
\left(\xi^\beta\frac{\theta}{P}\right)\right|
\leq C_{\beta,N}
\langle\xi\rangle^{|\beta|-m\rho-N\rho}.
\tag{25}
\]
Terms where derivatives hit \(\xi^\beta\) have at least as much decay because \(\rho\leq1\). Choose \(N\) with the exponent less than \(-n\). The expression is integrable, so its inverse Fourier transform is continuous. The integration-by-parts identity identifies it, up to a constant power of \(i\), with \(x_j^N D^\beta K\). On \(x_j\ne0\) this gives a continuous representative of \(D^\beta K\). Applying this to every \(\beta\) proves smoothness there, and the sets \(x_j\ne0\) cover the complement of zero. It cannot be smooth at zero because the right side of (24) is singular there. Thus the quantitative criterion yields a parametrix with singular support exactly \(\{0\}\), without using the localization theorems for this implication.

## Exercises with complete solutions

**Exercise 1. Constants and the point singularity.** Check all the criteria for \(P=c\ne0\), including the assertion about the singular support of a fundamental solution.

**Solution.** Its zero set is empty, so \(d_P=\infty\) and all positive-order derivative ratios are zero. The unique fundamental solution is \(c^{-1}\delta_0\), with singular support \(\{0\}\). Multiplication by \(c\) preserves the wavefront set and singular support of every distribution. The homogeneous solution space is zero, so it is smooth and Montel in every stated topology. These facts also explain why (4) is written with inverse distance rather than the undefined product \(\infty\cdot0\).

**Exercise 2. The fractional powers.** For \(P(\xi)=\xi^2+1\) on the real line, compute \(d_P\) and \(A_P\). Determine their product at large \(|\xi|\).

**Solution.** The complex zeros are \(\pm i\), so \(d_P(\xi)=\sqrt{\xi^2+1}\). Its nonzero derivative ratios give
\[
A_P(\xi)=\frac{2|\xi|}{\xi^2+1}
+\sqrt{\frac2{\xi^2+1}}.
\]
Therefore \(d_PA_P\to2+\sqrt2\). The second derivative contributes at the same inverse-distance scale only after taking its square root. The operator is hypoelliptic by Theorem 2.1.

**Exercise 3. Heat and a sharp exponent.** For \(P(\tau,\xi)=i\tau+|\xi|^2\), \(\xi\in\mathbb R^d\), show that (8) holds with exponent \(a=1/2\). Show that no larger exponent works uniformly in the distance lower bound.

**Solution.** Put \(L=|\tau|+|\xi|^2\), comparable to \(|P|\), and \(R=(\tau^2+|\xi|^2)^{1/2}\). For large \(R\), \(L\geq cR\). The time derivative ratio is \(1/|P|\leq C R^{-1}\), and each nonzero second spatial derivative ratio is at most \(C R^{-1}\). For a first spatial derivative the ratio is at most \(C|\xi|/L\). If \(|\tau|\leq|\xi|^2\), then \(R\leq C|\xi|^2\) and the ratio is at most \(C/|\xi|\leq C R^{-1/2}\). If \(|\tau|>|\xi|^2\), then \(R\) is comparable to \(|\tau|\) and the ratio is at most \(C|\tau|^{-1/2}\). All other derivatives vanish. This proves (8).

At the real point \((T,0)\), \(T>0\), the complex point
\[
\zeta=\bigl(T,e^{-i\pi/4}\sqrt T,0,\ldots,0\bigr)
\]
is a zero: in complex variables the spatial polynomial is the sum of squares, and its value here is \(-iT\). Its distance from \((T,0)\) is \(\sqrt T\). Hence \(d_P(T,0)\leq\sqrt T\), so no bound \(d_P\geq cR^a\) with \(a>1/2\) can hold. This is a hypoelliptic operator whose quadratic principal part is not elliptic on spacetime.

**Exercise 4. A noncompact homogeneous solution space.** Take \(P(\xi_1,\xi_2)=\xi_1\), \(p=2\), \(k=1\), and a nonempty open rectangle \(X\). Give a bounded sequence of homogeneous solutions that tends to zero in distributions but not in the local weighted topology.

**Solution.** Let \(u_j=e^{ijx_2}\). It is independent of \(x_1\), hence homogeneous. For every compact cutoff \(\phi\), Plancherel or Fourier translation gives a norm independent of \(j\), so the sequence is locally bounded. Integration by parts against a compact test gives distributional convergence to zero. But for any fixed nonzero cutoff \(\phi\), \(\|\phi u_j\|_{2,1}=\|\phi\|_{L^2}>0\). It cannot have a convergent subsequence in the local weighted solution space: any such subsequence would have distributional limit zero and would contradict this norm identity.

**Exercise 5. Why all localizations must be constant.** For \(P(\xi)=\xi_1\xi_2\), every localization has degree less than two. Explain why that fact does not prove hypoellipticity.

**Solution.** The original inactive subspace is zero, so the degree-drop theorem applies to every nonzero escaping direction. Nevertheless the path \((0,t)\) gives the normalized localization \(\xi_1\), which is not constant. The criterion in Theorem 3.1 needs every localization to have active space zero, not just smaller degree. Equivalently the real zeros \((0,t)\) remain at zero distance from the complex zero set while tending to infinity.

**Exercise 6. Checking the topology estimate.** In (22), explain why the strong distribution topology gives every \(C^r\) seminorm on \(K\), and why merely pointwise bounds on \(\langle u,T_x\rangle\) would be insufficient.

**Solution.** For \(|\beta|\leq r\), differentiation gives \(\partial_x^\beta u(x)=\langle u,\partial_x^\beta T_x\rangle\). The union of these test families over \(x\in K\) is bounded in \(C_c^\infty(X)\), with common compact support and uniform bounds on every test derivative. The supremum over this bounded set is one continuous strong distribution seminorm. It bounds the \(C^r(K)\) norm. Separate pointwise pairings would give continuity only for each fixed \(x,\beta\); they would not control the supremum over the compact family required by that norm.

## References

- **[Grubb]** Gerd Grubb, *Distributions and Operators*, open lectures, sections on Fourier transformation, local spaces, and interior regularity. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- **[Coste]** Michel Coste, *Real Algebraic Sets*, lecture notes, 2003, §1.1 and §1.5. [ICTP notes](https://indico.ictp.it/event/a02455/session/9/contribution/6/material/0/0.pdf).
- **[Hormander]** Lars Hörmander, “On the singularities of solutions of partial differential equations with constant coefficients,” *Séminaire Goulaouic–Schwartz*, 1971–1972, exposé 25, 1–6. [Original article](https://www.numdam.org/item/SEDP_1971-1972____A25_0/).
