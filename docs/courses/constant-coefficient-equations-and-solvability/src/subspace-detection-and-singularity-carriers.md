# Subspace detection and singularity carriers

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A homogeneous equation can have solutions that are smooth away from an entire plane and singular at every point of that plane. The relevant algebra is measured in the perpendicular frequency directions. This lesson defines that measurement, proves its continuity and quantitative consequences, and constructs solutions with prescribed singular sets. The construction can retain any fixed finite number of continuous derivatives.

Read [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md), [Symbols at infinity](symbols-at-infinity.md), and [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md). We use the finite-dimensional polynomial norm estimates, semialgebraic projection and one-variable asymptotics established there. The other inputs are Baire's theorem for a complete metrizable vector space and the elementary complex-analysis facts of Cauchy's estimate, the argument principle and Rouché's theorem. Grubb [Grubb] supplies the distribution background; Coste [Coste] discusses the algebraic asymptotics; Hörmander [Hormander] places the construction within the theory of singularities.

Keep \(D=-i\partial\), let \(P\ne0\) be a complex polynomial on \(\mathbb R^n\), and write \(m=\deg P\). Subspaces and orthogonal projections are real Euclidean ones. Singular support is the complement of the largest open set on which a distribution is smooth.

[Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html), Sections 6 and 14.1, proves Baire for the complete metrics used here. [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md), Sections 1–2, proves maximum modulus, weighted disk root counts and their persistence under perturbation.

## Measuring a frequency subspace

For a subspace \(W\), a real frequency \(\xi\), and \(t\geq1\), set
\[
\begin{gathered}
A_{P,W}(\xi,t)=
\max_{\substack{\theta\in W\\|\theta|\leq t}}|P(\xi+\theta)|,\\
A_P(\xi,t)=A_{P,\mathbb R^n}(\xi,t),\\
\sigma_P(W)=\inf_{t\geq1}
\liminf_{|\xi|\to\infty}
\frac{A_{P,W}(\xi,t)}{A_P(\xi,t)}.
\end{gathered}
\tag{1}
\]
The full norm \(A_P\) is positive: a polynomial vanishing on a real ball is zero. Thus \(0\leq\sigma_P(W)\leq1\). A nonzero constant gives \(\sigma_P(W)=1\) for every \(W\), and \(\sigma_P(\mathbb R^n)=1\) for every nonzero \(P\).

The radius is held fixed while taking the lower limit. Its infimum is taken afterwards. A sequence whose radii also tend to infinity requires a separate argument; Lemma 2.1 below provides it.

Choose orthonormal coordinates in \(W\). Finite-dimensional polynomial norm comparison gives
\[
\begin{gathered}
A_{P,W}(\xi,t)\asymp\\
\left(\sum_{|\alpha|\leq m}
t^{2|\alpha|}|\partial_W^\alpha P(\xi)|^2\right)^{1/2}.
\end{gathered}
\tag{2}
\]
For \(W=\{0\}\) the sum is just \(|P(\xi)|^2\). For the full space this is the rescaled derivative norm proved in [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md). Apply that same result to the restriction polynomial to obtain (2). Its constants depend on degree and dimension, and not on \(\xi,t\).

**Proposition 1.1.** Let \(\pi_W,\pi_Z\) be orthogonal projections and \(g(W,Z)=\|\pi_W-\pi_Z\|\). There is \(C\), depending only on \(m,n\), such that
\[
|\sigma_P(W)-\sigma_P(Z)|\leq Cg(W,Z).
\tag{3}
\]
In particular \(\sigma_P\) is continuous on every Grassmannian of a fixed dimension.

**Proof.** Given \(\theta\in W\) with \(|\theta|\leq t\), put \(\eta=\pi_Z\theta\). Then \(|\eta|\leq t\) and \(|\theta-\eta|\leq tg(W,Z)\). The derivative norm estimate on the ball of radius \(2t\) yields
\[
\begin{gathered}
|P(\xi+\theta)-P(\xi+\eta)|\\
\leq C A_P(\xi,t)g(W,Z).
\end{gathered}
\tag{4}
\]
One can obtain this by integrating the gradient on the segment and using (2); the segment stays in the radius-\(t\) ball. Take the maximum in \(\theta\), divide by \(A_P\), and pass to the lower limit and then the infimum. This gives \(\sigma_P(W)\leq\sigma_P(Z)+Cg(W,Z)\). Reverse the subspaces. The argument includes the zero subspace, whose unit sphere is empty. \(\square\)

## Quantitative tests at large frequencies

The following estimates convert (1) into bounds usable when \(t\) grows slowly with \(|\xi|\).

**Lemma 2.1.** Fix \(W\).

1. If \(\sigma_P(W)=0\), there are \(b,\beta,p,t_0>0\) such that, for every \(t>t_0\) and every \(r>t^p\), some real \(\xi\) satisfies
\[
\begin{gathered}
|\xi|=r,\\
A_{P,W}(\xi,t)<bt^{-\beta}A_P(\xi,t).
\end{gathered}
\tag{5}
\]
2. If \(\sigma_P(W)>0\), there are \(b,p,t_0>0\) such that
\[
\begin{gathered}
A_{P,W}(\xi,t)\geq b A_P(\xi,t),\\
t>t_0,\qquad |\xi|>t^p.
\end{gathered}
\tag{6}
\]

**Proof.** Write
\[
a(t)=\liminf_{|\xi|\to\infty}
\frac{A_{P,W}(\xi,t)}{A_P(\xi,t)}.
\]
This function is semialgebraic. Indeed the graph of each maximum in (1) is specified by polynomial inequalities with quantified real variables. A lower limit is specified by eventual lower bounds and arbitrarily distant points below any larger proposed bound. Quantifier elimination therefore applies. Complex coefficients cause no difficulty: squared absolute values are real polynomials.

Polynomial dilation estimates show that on each bounded interval \(1\leq t\leq T\),
\[
a(t)\geq c_Ta(1).
\]
They also give \(a(t)\leq Ct^ma(1)\). If \(a(1)=0\), then \(a(t)=0\) for every \(t\). Otherwise a vanishing infimum must occur along \(t\to\infty\). The one-variable semialgebraic asymptotics proved in [Symbols at infinity](symbols-at-infinity.md) imply that \(a(t)\to0\) and, after increasing \(t_0\),
\[
a(t)<\tfrac b2t^{-\beta}
\]
for some \(\beta>0\); a rational \(\beta\) may be used. This also holds when \(a\) is identically zero.

For each such \(t\), consider the set of radii \(r\) for which a point on the sphere \(|\xi|=r\) satisfies (5). This is a semialgebraic subset of the line, and it is unbounded by the strict lower-limit inequality. It consequently contains a terminal interval. The infimum of the beginnings of its terminal intervals is a finite semialgebraic function \(h(t)\): its graph is again expressed by quantified inequalities. Polynomial growth gives \(h(t)<t^p\) for all sufficiently large \(t\), after enlarging \(p\). This proves (5) for every large radius.

For the second assertion choose \(0<b<\sigma_P(W)\). At each fixed \(t\), the set where the ratio is less than \(b\) is bounded. Its supremum radius, set to zero when the set is empty, is a finite semialgebraic function. Polynomial growth bounds that radius by \(t^p\) for large \(t\), proving (6). \(\square\)

In (5), any radius \(r=e^{dt}\) with fixed \(d>0\) is eventually eligible. In (6), a radius proportional to \(\log|\xi|\) is eventually eligible. These two uses will produce singular solutions and smoothing inverses respectively.

## An analytic family of solutions

We first record an elementary fact about a polynomial in one complex variable.

**Lemma 3.1.** If \(g\ne0\) has degree at most \(m\), some \(R\in[1/2,1]\) satisfies
\[
\min_{|z|=R}|g(z)|
\geq c_m\max_{|z|\leq1}|g(z)|,
\tag{7}
\]
where \(c_m>0\) depends only on \(m\).

**Proof.** For \(m\geq1\), factor \(g\) into at most \(m\) linear factors. Set \(h=1/(8(m+1))\). Avoid intervals of radius \(h\) around the moduli of roots with modulus at most two. Their total length is less than \(1/4\), so a radius remains in \([1/2,1]\). On its circle, a factor belonging to one of these roots has absolute value at least \(h\); on the unit disk it has absolute value at most three. For a root with modulus greater than two, the ratio of the circle minimum to the disk maximum is at least \(1/3\). Multiply the factor bounds to get (7), for example with \(c_m=(h/3)^m\). A constant polynomial satisfies the assertion directly. \(\square\)

Split \(x=(x',x'')\), where \(x'\in\mathbb R^k\), and let
\[
V=\{x'=0\},\qquad W=V^\perp.
\]
The same split is used in frequency space. The prime block may have dimension zero.

**Lemma 3.2.** Suppose \(m\geq1\), \(t\geq1\), and
\[
\begin{gathered}
A_{P,W}(\xi,t)\leq\varepsilon A_P(\xi,t),\\
0<\varepsilon<\varepsilon_0.
\end{gathered}
\tag{8}
\]
There are a real \(\eta\) with \(\eta-\xi\in W\), \(|\eta-\xi|\leq t\), and a function \(U(\theta,x'')\), holomorphic for complex \(|\theta|<\gamma t\) and entire in \(x''\), such that
\[
\begin{gathered}
U(\theta,0)=1,\\
P\bigl(\eta+(\theta,D'')\bigr)U(\theta,x'')=0,\\
|U(\theta,x'')|
\leq C\exp(Ct\varepsilon^{1/m}|x''|).
\end{gathered}
\tag{9}
\]
The constants depend only on degree and dimension.

**Proof.** Normalize
\[
p(z)=\frac{P(\xi+tz)}{A_P(\xi,t)}.
\]
Its real unit-ball norm is one; its restriction to the prime unit ball has norm at most \(\varepsilon\). With a fixed large \(K\), put \(\rho=(K\varepsilon)^{1/m}<1\), and set
\[
\begin{gathered}
B=\max_{|z|\leq1,\ z\text{ real}}
|p(z',\rho z'')|,\\
q(z',z'')=B^{-1}p(z',\rho z'').
\end{gathered}
\tag{10}
\]
Coefficient norm comparison gives \(B\geq c\rho^m\): shrinking the double-prime variables multiplies every coefficient by a power of \(\rho\) at most \(m\). Hence \(q\) has full unit-ball norm one and prime restriction norm at most \(C/K\).

Take a real \((v',v'')\) in that ball with \(|q(v',v'')|=1\), and apply Lemma 3.1 to \(g(z)=q(v',zv'')\). On some circle \(|z|=R\), \(g\) has absolute value at least \(c_m\). Choose \(K\) so large that \(|g(0)|<c_m\). Then \(g\) has at least one zero in the circle: otherwise the maximum-modulus principle for \(1/g\) would contradict this inequality.

The coefficient norms of \(q\) are bounded. Thus for a fixed small \(\gamma>0\),
\[
\begin{gathered}
|q(v'+\vartheta,zv'')|\geq c_m/2,\\
|\vartheta|<\gamma,\qquad |z|=R.
\end{gathered}
\tag{11}
\]
Rouché's theorem keeps the positive number \(L\) of enclosed zeros, counted with multiplicity, constant as \(\vartheta\) varies. Define
\[
\begin{gathered}
g_\vartheta(z)=q(v'+\vartheta,zv''),\\
H(\vartheta,y'')=\\
\frac1{2\pi iL}\int_{|z|=R}
e^{izv''\cdot y''}\frac{g_\vartheta'(z)}{g_\vartheta(z)}\,dz.
\end{gathered}
\tag{12}
\]
The argument principle gives \(H(\vartheta,0)=1\). Applying \(q(v'+\vartheta,D_{y''})\) cancels the denominator; the remaining integrand is entire in \(z\), so its contour integral is zero. The bounded numerator and (11) give \(|H|\leq C e^{C|y''|}\). Differentiation under the contour establishes the asserted holomorphy.

Finally take
\[
\begin{gathered}
\eta=\xi+t(v',0),\\
U(\theta,x'')=H(\theta/t,t\rho x'').
\end{gathered}
\tag{13}
\]
Equation (10) converts the equation for \(H\) into the equation in (9). The normalization and exponential bound follow at once. \(\square\)

The contour counts all enclosed roots together. No continuous choice of individual roots is needed, even at multiple roots.

## Concentrating homogeneous solutions near a plane

We will need cutoffs whose first \(N\) derivatives obey a uniform rule. For each \(N\geq1\), there is a nonnegative \(\chi_N\in C_c^\infty(\mathbb R^k)\), with integral one and support in the fixed ball \(|\theta|<\gamma/2\), such that
\[
\begin{gathered}
\|\partial^\alpha\chi_N\|_\infty\leq C(CN)^{|\alpha|},\\
|\alpha|\leq N.
\end{gathered}
\tag{14}
\]
To construct it, convolve a fixed smooth probability function supported in \(|\theta|<\gamma/4\) with \(N\) smooth probability kernels of radius \(\gamma/(4N)\). Assign each of at most \(N\) derivatives to a different small kernel. Each differentiated kernel has \(L^1\) norm at most \(CN\), and Young's inequality proves (14). Support and integral are preserved. For \(k=0\) the integral is scalar and no cutoff derivatives are needed.

Using Lemma 3.2, define
\[
\begin{gathered}
v_t(x)=e^{ix\cdot\eta}B_t(x),\\
B_t(x)=\\
\int_{\mathbb R^k}
e^{itx'\cdot\theta}U(t\theta,x'')\chi_N(\theta)\,d\theta.
\end{gathered}
\tag{15}
\]
It is globally smooth, \(P(D)v_t=0\), and \(v_t(0)=1\).

Suppose \(|\xi|=e^{dt}\), with fixed \(d>0\). Then \(|\eta|\asymp e^{dt}\). For each fixed compact \(K\) and derivative order \(r\), Cauchy's estimate in \(x''\), (9), and positivity with \(\int\chi_N=1\) give
\[
\|v_t\|_{C^r(K)}
\leq C_{K,r}|\eta|^r
e^{C_Kt\varepsilon^{1/m}}.
\tag{16}
\]
These constants are independent of \(N\). Derivatives of the envelope at zero are at most \(C_rt^r\). The product rule consequently gives
\[
\begin{gathered}
D^\alpha v_t(0)=\eta^\alpha+O_r\bigl(t|\eta|^{r-1}\bigr),\\
|\alpha|=r.
\end{gathered}
\tag{17}
\]
Indeed the terms with \(j\geq1\) envelope derivatives are bounded by \(C_r t^j|\eta|^{r-j}\), and \(t/|\eta|\to0\). A coordinate with \(|\eta_\ell|\geq|\eta|/\sqrt n\) therefore supplies an order-\(r\) derivative of size at least \(c_r|\eta|^r\) for large \(t\).

If \(K_2\) is compact outside \(V\), then \(|x'|\geq c_0>0\) there. Integrate (15) \(N\) times in the \(\theta\) direction \(x'/|x'|\). Holomorphy in \(\theta\) gives a bound \(l!C^l\) for \(l\) derivatives of \(U(t\theta,x'')\), apart from the exponential in (9). Combining this with (14), the product rule and \(l!\leq N^l\) yields
\[
\begin{gathered}
\|v_t\|_{C^r(K_2)}\\
\leq C_{K_2,r}|\eta|^r
\left(\frac{CN}{c_0t}\right)^N
e^{C_{K_2}t\varepsilon^{1/m}}.
\end{gathered}
\tag{18}
\]
Fixed extra polynomial factors introduced by the \(x\) derivatives are absorbed into \(|\eta|^r\). Choose \(N=\lfloor qt\rfloor\), with \(q>0\) so small that \(Cq/c_0<e^{-2}\). The middle factor is then at most a fixed constant times \(e^{-2qt}\).

Thus a derivative at zero can grow like \(e^{rdt}\), while arbitrarily many prescribed derivatives on a compact set off the plane decay exponentially. This separation of estimates is the mechanism behind the carrier theorem.

## Prescribing the singular set

**Theorem 5.1.** Let \(V\) be a real linear subspace with \(\sigma_P(V^\perp)=0\). Let \(F\) be a closed set satisfying \(F+V=F\), and let \(\mu\geq0\) be an integer. There is
\[
\begin{gathered}
u\in C^\mu(\mathbb R^n),\qquad P(D)u=0,\\
\operatorname{sing\,supp}u=F,
\end{gathered}
\tag{19}
\]
such that \(u\) is not \(C^{\mu+1}\) on any open set meeting \(F\). For \(F=\varnothing\), use \(u=0\); the last assertion is vacuous.

**Proof.** Suppose \(F\ne\varnothing\). Let
\[
\begin{gathered}
\mathcal H_\mu(F)=\{u\in C^\mu(\mathbb R^n)\colon\\
P(D)u=0,\quad u\in C^\infty(\mathbb R^n\setminus F)\}.
\end{gathered}
\tag{20}
\]
Give it the compact \(C^\mu\) seminorms on all space and all compact smooth seminorms off \(F\). Countable compact exhaustions give a metrizable topology. It is complete: a Cauchy sequence has compatible limits of every required derivative on every compact set, and its homogeneous equation passes to the distributional limit.

For each rational ball \(B\) meeting \(F\) and integer \(M\geq1\), let \(E_{B,M}\) consist of the elements for which every \(|\alpha|=\mu+1\) obeys
\[
\begin{gathered}
|\langle D^\alpha u,\phi\rangle|\leq M\|\phi\|_{L^1},\\
\phi\in C_c^\infty(B).
\end{gathered}
\tag{21}
\]
This set is closed, since each test pairing is continuous. We prove it has empty interior.

If it had interior, subtracting two elements in a basic translated neighborhood and then scaling would give an estimate on all globally smooth homogeneous solutions \(v\):
\[
\begin{gathered}
\sum_{|\alpha|=\mu+1}|D^\alpha v(y)|\\
\leq C\bigl(\|v\|_{C^\mu(K_1)}+\|v\|_{C^\nu(K_2)}\bigr).
\end{gathered}
\tag{22}
\]
Here \(y\in B\cap F\), \(K_1\) is compact in all space, \(K_2\) is compact off \(F\), and \(\nu\) is finite. Finitely many seminorms combine into these two norms. Inequality (21) for a smooth function bounds its derivative pointwise by testing with smooth approximate point masses. If the combined seminorm of \(v\) is zero, scaling by arbitrary constants forces the left side to be zero; otherwise divide by that seminorm to obtain (22).

Translate the packets (15) to \(y\). Because \(y+V\subset F\), \(K_2\) is a positive distance from that translated plane. Choose \(q\) as in (18). Next choose \(d>0\) small enough that \(d\nu<q/2\). Finally choose a fixed \(\varepsilon>0\) so small that all compact exponential constants needed in (16) and (18) satisfy
\[
C_K\varepsilon^{1/m}
<\min(d/2,q/2).
\tag{23}
\]
Lemma 2.1 supplies a suitable \(\xi\) on the sphere \(|\xi|=e^{dt}\) for every large \(t\), since the ratio in (5) eventually falls below this fixed \(\varepsilon\).

By (17), the left side of (22) is at least \(c e^{(\mu+1)dt}\). Its first right-hand term is at most \(C e^{(\mu d+d/2)t}\), by (16). Its second tends to zero, by (18), (23), and \(d\nu<q/2\). This contradicts (22).

Baire's theorem now gives \(u\) outside the countable union of the \(E_{B,M}\). It is smooth off \(F\) by definition. If it were \(C^{\mu+1}\) on an open set meeting \(F\), that set would contain the closure of a rational ball meeting \(F\). The relevant continuous derivatives would be bounded there, placing \(u\) in some \(E_{B,M}\). This contradiction proves the full conclusion.

When \(V=\mathbb R^n\), the only nonempty invariant closed set is all space; the off-\(F\) seminorms disappear and the same argument uses (16). When \(V=\{0\}\), the hypothesis cannot hold because \(\sigma_P(\mathbb R^n)=1\). A constant polynomial also cannot satisfy the hypothesis. \(\square\)

In particular, take \(F=a+V\) to prescribe one affine plane. The perpendicular in the hypothesis matters: \(V\) is a set of physical points, while \(V^\perp\) is where the frequency norm is being tested.

## Stability under equal strength

Two polynomials have equal strength when their full derivative norms dominate each other uniformly at every real frequency. The rescaled comparison in [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md) gives constants \(c,C>0\) such that
\[
\begin{gathered}
cA_P(\xi,t)\leq A_Q(\xi,t)\leq CA_P(\xi,t),\\
\xi\in\mathbb R^n,\qquad t\geq1.
\end{gathered}
\tag{24}
\]

**Theorem 6.1.** If \(P,Q\) have equal strength, then for every subspace \(W\),
\[
\sigma_P(W)=0\quad\Longleftrightarrow\quad\sigma_Q(W)=0.
\tag{25}
\]

**Proof.** Suppose \(\sigma_P(W)=0\). Lemma 2.1 gives \(t_j\to\infty\) and \(|\xi_j|=e^{t_j}\) with restricted ratio tending to zero. Normalize
\[
\begin{gathered}
p_j(z)=\frac{P(\xi_j+t_jz)}{A_P(\xi_j,t_j)},\\
q_j(z)=\frac{Q(\xi_j+t_jz)}{A_P(\xi_j,t_j)}.
\end{gathered}
\tag{26}
\]
Their coefficients are bounded by polynomial norm comparison. Pass to coefficientwise limits \(p,q\). The unit-ball norm of \(p\) is one; that of \(q\) lies between \(c\) and \(C\). Both are nonzero, and \(p|_W=0\).

For any fixed real \(z\) and \(s>0\), apply (24) at \(\xi_j+t_jz\) with radius \(t_js\), which is eventually at least one. The coefficient limits give
\[
cA_p(z,s)\leq A_q(z,s)\leq CA_p(z,s).
\]
Let \(s\downarrow0\). It follows that \(c|p(z)|\leq|q(z)|\leq C|p(z)|\) at every real \(z\). Hence \(q|_W=0\), and
\[
\frac{A_{Q,W}(\xi_j,t_j)}{A_Q(\xi_j,t_j)}\longrightarrow0.
\tag{27}
\]
If \(\sigma_Q(W)>0\), (6) would bound these ratios below for large \(j\), since \(e^{t_j}\) exceeds every fixed power of \(t_j\). Thus \(\sigma_Q(W)=0\). Reverse \(P,Q\). \(\square\)

The theorem preserves the zero set of the invariant. It does not assert equality of its positive numerical values.

## Transport as an exact model

Let \(P(\xi)=\xi_1\) on \(\mathbb R^n\), \(n\geq2\), and \(a=|\pi_We_1|\). Then
\[
\begin{gathered}
A_{P,W}(\xi,t)=|\xi_1|+ta,\\
A_P(\xi,t)=|\xi_1|+t.
\end{gathered}
\tag{28}
\]
Their ratio is at least \(a\). Unbounded frequencies with \(\xi_1=0\) realize \(a\) at every fixed \(t\), so \(\sigma_P(W)=a\).

For a physical plane \(V\), its perpendicular has zero invariant precisely when \(e_1\in V\). The carrier theorem therefore permits exactly these planes for solutions of \(D_1u=0\). The elementary distributional identity \(D_1u=0\Rightarrow u=1\otimes w\), proved in the AN-01 lesson *Weak equations and classical functions*, explains the same geometry: the solution is independent of the transport coordinate.

In dimension one there are no unbounded frequencies with \(\xi_1=0\). For every fixed \(t\), the ratio in (28) tends to one as \(|\xi_1|\to\infty\), even for \(W=\{0\}\). Thus every invariant equals one, consistent with ordinary differential equation regularity.

## Exercises and full solutions

**Exercise 1. Powers of transport (basic).** For \(P(\xi)=\xi_1^r\), \(r\geq1\), calculate \(\sigma_P(W)\) in dimension at least two. Explain the dimension-one answer and identify all affine-plane carriers allowed by Theorem 5.1.

**Solution.** Since the projection of the radius-\(t\) ball of \(W\) onto the first coordinate is \([-ta,ta]\), where \(a=|\pi_We_1|\),
\[
\frac{A_{P,W}(\xi,t)}{A_P(\xi,t)}
=\left(\frac{|\xi_1|+ta}{|\xi_1|+t}\right)^r.
\]
The ratio is at least \(a^r\); frequencies with \(\xi_1=0\) and another coordinate tending to infinity attain it. Hence \(\sigma_P(W)=a^r\). In dimension one the fixed-\(t\) ratio tends to one, so all invariants are one. In higher dimension the permitted affine planes \(b+V\) have \(e_1\in V\), since \(a=0\) for \(W=V^\perp\) exactly in that case.

**Exercise 2. A vanishing value at infinity (basic).** Let \(P(\xi)=1+\xi_1^2\) in dimension at least two. Determine \(\sigma_P(\{0\})\) and \(\sigma_P(\mathbb Re_1)\). Does the absence of real zeros imply hypoellipticity?

**Solution.** For \(W=\{0\}\),
\[
\frac{A_{P,W}(\xi,t)}{A_P(\xi,t)}
=\frac{1+\xi_1^2}{1+(|\xi_1|+t)^2}.
\]
Along \(\xi_1=0\) its lower limit is at most \(1/(1+t^2)\). Taking the infimum over \(t\) gives zero. For \(W=\mathbb Re_1\), varying that coordinate already obtains the full ball maximum, so the ratio is identically one. The complex zeros \(\xi_1=\pm i\), with the other coordinates arbitrarily large and real, stay at distance one from real space. The complex-zero criterion therefore rules out hypoellipticity. Real nonvanishing alone is insufficient.

**Exercise 3. Checking the cutoff estimate (intermediate).** Prove (14) with the stated common support and integral, using only scaling and Young's inequality. Why is a fixed cutoff with no dependence on \(N\) insufficient for the estimate used in (18)?

**Solution.** Choose smooth nonnegative probability functions \(\chi_0,\rho\) supported in the balls of radii \(\gamma/4\) and one. Put \(a_N=\gamma/(4N)\), \(\rho_N(\theta)=a_N^{-k}\rho(\theta/a_N)\), and \(\chi_N=\chi_0*\rho_N^{*N}\). Its support radius is less than \(\gamma/4+Na_N=\gamma/2\), and its integral is one. Write \(\alpha\) as \(|\alpha|\) coordinate derivatives and apply each to a distinct \(\rho_N\). Every differentiated factor has \(L^1\) norm at most \(C/a_N\leq CN\); undifferentiated factors have norm one. Keep \(\chi_0\) in \(L^\infty\) and apply Young repeatedly, proving (14). A fixed smooth cutoff has finite constants at each order, but they need not be bounded by \(C(CN)^N\) as \(N\) grows. Such uncontrolled growth would invalidate the exponential decay inferred by choosing \(N\) proportional to \(t\).

**Exercise 4. A non-linear singular set (intermediate).** In \(\mathbb R^3\), let \(P(\xi)=\xi_1\), \(V=\mathbb Re_1\), and let \(C\subset\mathbb R^2\) be any nonempty closed set. Apply Theorem 5.1 to \(F=\mathbb R\times C\). What regularity can be prescribed, and why must the set be invariant in the transport direction?

**Solution.** Here \(V^\perp=\{\xi_1=0\}\), so (28) gives \(\sigma_P(V^\perp)=0\). The set \(F\) is closed and satisfies \(F+V=F\). For each integer \(\mu\geq0\), the theorem gives a \(C^\mu\) solution of \(D_1u=0\) with singular support exactly \(F\), failing to be \(C^{\mu+1}\) on every open set meeting \(F\). The result applies to disconnected or fractal \(C\) as well as smooth sets. Conversely a distribution solving \(D_1u=0\) is independent of \(x_1\), so its singular support is a cylinder in that direction. An arbitrary closed set lacking that invariance cannot be its singular support.

**Exercise 5. Why growing radii need a lemma (advanced).** Explain why (27) alone does not imply \(\sigma_Q(W)=0\). Complete the contradiction using the positive half of Lemma 2.1, including the comparison of \(e^{t_j}\) with \(t_j^p\).

**Solution.** In definition (1), the lower limit is taken at a fixed radius. Formula (27) permits \(t_j\to\infty\), so it does not by itself produce a zero lower limit at any fixed radius. If \(\sigma_Q(W)>0\), Lemma 2.1 gives fixed \(b,p,t_0>0\) bounding the ratio below whenever \(t>t_0\) and \(|\xi|>t^p\). Since \(t-p\log t\to\infty\), \(e^t>t^p\) for every sufficiently large \(t\). Our sequence has \(|\xi_j|=e^{t_j}\), so its ratios are eventually at least \(b\), contradicting (27). The uniform polynomial threshold supplies the missing implication.

**Exercise 6. Local boundedness in the Baire argument (advanced).** Show that a function which is \(C^{\mu+1}\) on an open set \(N\) meeting \(F\) belongs to some \(E_{B,M}\). Explain why this proves the theorem's pointwise singular-support assertion rather than only a failure of global smoothness.

**Solution.** Choose \(y\in N\cap F\) and a rational ball \(B\) containing \(y\) with compact closure inside \(N\). Every derivative of order \(\mu+1\) is continuous and bounded on that closure. There are finitely many such derivatives, so choose an integer \(M\) above all their bounds. Their distributional pairings then satisfy (21), because integration against \(\phi\) is bounded by the supremum times \(\|\phi\|_1\). Hence the function lies in \(E_{B,M}\). A function outside all these sets cannot be \(C^{\mu+1}\) on any neighborhood of any point of \(F\). Since it is smooth off \(F\), its singular support is exactly \(F\), with no omitted regular point in that set.

## References

- **[Grubb]** Gerd Grubb, *Distributions and Operators*, open lectures, sections on distributional differentiation and Fourier transformation. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- **[Coste]** Michel Coste, *Real Algebraic Sets*, ICTP lecture notes, 2003, sections on semialgebraic projection and growth. [Lecture notes](https://indico.ictp.it/event/a02455/session/9/contribution/6/material/0/0.pdf).
- **[Hormander]** Lars Hörmander, “On the singularities of solutions of partial differential equations with constant coefficients,” *Séminaire Goulaouic–Schwartz*, 1971–1972, exposé 25, 1–6. [Original article](https://www.numdam.org/item/SEDP_1971-1972____A25_0/).
