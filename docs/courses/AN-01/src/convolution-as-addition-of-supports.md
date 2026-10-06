# Convolution as addition of supports

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, 4 October 2026. Public domain (CC0).*

Adding two source locations explains both the power and the limitation of convolution. Two compact sources always give a distribution at their sums. Two unbounded sources do so when a bounded output can receive contributions only from a compact set of input pairs. This geometric condition will also control limits, associativity and local regularity.

Pairings are complex-linear, with no conjugation. We use [U008](order-positivity-and-limits.md), Proposition 1.2 and Theorem 5.1, for finite-order extensions and distributional limits; its formula (T1) characterizes bounded test families. The [functional prerequisite](../prerequisites/U011-free-foundations/functional-foundations-U008.md), Sections 6 and 14.1–14.2, proves Baire's theorem and completeness of fixed-support test spaces. The [scalar prerequisite](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 13.1–13.5 and 13.10, and the [integration prerequisite](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.4, supply differentiation, compact cutoffs, ordinary integration and smooth approximation. All additional distribution constructions used below are proved here. The operator theorem also uses the exact Fourier inversion proof in the [Schwartz prerequisite](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F2–F4.

## Pairings, parameters and tensor products

Write \(\mathcal D(X)=C_c^\infty(X)\) for an open subset of Euclidean space. For tests supported in a fixed compact set, write \(p_m(\phi)=\max_{|\alpha|\le m}\sup|\partial^\alpha\phi|\). A distribution is a linear form with a bound \(C p_m\) on each such space. A bounded test family has one common compact support and a uniform bound for every \(p_m\), by U008 (T1). Weak convergence means convergence on each test; strong convergence means uniform convergence on every bounded test family. The distinction concerns topologies even though U008 Theorem 5.1 proves that weakly convergent **sequences** also converge strongly.

**B0. Localization and extended pairings.** Define \(\operatorname{supp}u\) as the complement of the union of open sets where \(u\) vanishes. It is closed, and \(u(\phi)=0\) whenever the compact support of \(\phi\) misses it. Here is the localization step behind that assertion. Cover the compact support by finitely many open sets on which \(u\) vanishes. Choose nonnegative smooth bumps \(b_i\) supported in those sets with \(\sum b_i>0\) near the compact support, using smaller balls and the supplied cutoff construction. On that neighborhood divide by \(\sum b_i\), and multiply by a compact cutoff \(\eta\) supported there and equal to one near the test support. The smooth functions
\[
 \chi_i=\frac{\eta b_i}{\sum b_j}
\]
are extended by zero outside the region where the denominator is positive. They sum to one near the test support. Thus \(\phi=\sum\chi_i\phi\), and every summand pairs to zero. The same partition proves that compatible local distributions glue: evaluate a test by the finite sum of its partitioned local pairings; a common refinement proves independence, and a fixed finite partition near each compact gives continuity.

If \(h\in C^\infty(X)\) and \(S=\operatorname{supp}u\cap\operatorname{supp}h\) is compact in \(X\), set
\[
 u(h):=u(\chi h),\qquad
 \chi\in\mathcal D(X),\quad \chi=1\text{ near }S.                 \tag{B1}
\]
Two choices differ by a compact test whose support misses \(\operatorname{supp}u\): at a point in \(S\) their difference vanishes nearby, and at a point of \(\operatorname{supp}u\setminus S\) the function \(h\) vanishes nearby. B0 therefore proves independence. A common cutoff proves bilinearity whenever the finitely many relevant intersections are compact. Empty intersection gives zero. In particular a compactly supported distribution acts on every smooth function, with an estimate \(C p_m(\chi h)\) for one fixed cutoff. Multiplication by a smooth function and derivatives, defined by
\[
 (au)(\phi)=u(a\phi),\qquad
 (\partial^\alpha u)(\phi)=(-1)^{|\alpha|}u(\partial^\alpha\phi),
\]
are distributions by the finite product rule and have support contained in that of \(u\). A compactly supported distribution consequently has some finite global order. We denote the space of compactly supported distributions by \(\mathcal E'\).

A continuous function which defines the zero distribution is zero pointwise. Otherwise multiply its value at a nonzero point by a constant complex phase to make its real part positive; continuity and a nonnegative bump of positive integral in a small neighborhood contradict the zero pairing. This proves uniqueness when smooth local representatives are glued.

**B1. Differentiating and integrating parameters.** Suppose \(H(x,y)\) is smooth and, for \(x\) in each compact parameter neighborhood, its \(y\)-support lies in one compact subset of \(Y\). Then
\[
 x\longmapsto v_y(H(x,y)),\qquad
 \partial_x^\alpha v_y(H)=v_y(\partial_x^\alpha H)              \tag{B2}
\]
are smooth. Indeed a local order-\(m\) bound for \(v\) bounds the change in a pairing by the \(C^m_y\) change in its test. For each \(|\beta|\le m\), the fundamental theorem gives
\[
 \frac{\partial_y^\beta H(x+te_i,y)-\partial_y^\beta H(x,y)}t
 =\int_0^1\partial_{x_i}\partial_y^\beta H(x+\theta te_i,y)\,d\theta .
\]
Uniform continuity on a common compact gives convergence in that seminorm to the derivative, and the same estimate gives continuity of the derivative. Iterate. If \(v\) has compact support, inserting one cutoff near it gives the statement without a support condition on \(H\).

If \(H\) is compactly supported in both variables, a compact parameter integral can pass through \(v\):
\[
 \int v_y(H(x,y))\,dx=v_y\!\left(\int H(x,y)\,dx\right).         \tag{B3}
\]
To prove this, approximate the integral on a containing box by lattice Riemann sums. Every derivative in \(y\) has uniform Riemann-sum error bounded by the box volume times its modulus of continuity in \(x\) at the mesh diameter. The sums have a common compact \(y\)-support. They therefore converge in every test seminorm. Apply the continuity of \(v\), and also the scalar Riemann-sum limit to the continuous function in (B2). The same proof works with finitely many continuous \(y\)-derivatives when these control a finite-order pairing.

**B2. Density of product tests and the tensor construction.** Finite sums of \(\phi(s)\psi(t)\) are dense in \(\mathcal D(X\times Y)\), with approximating supports in a fixed compact product. To see this without a tensor theorem, extend a given \(H\) by zero and form the ordinary integral
\[
 H_\varepsilon(s,t)=\int H(a,b)\rho_\varepsilon(s-a)\sigma_\varepsilon(t-b)\,da\,db,
                                                               \tag{B4}
\]
where both profiles are smooth, nonnegative, compactly supported and normalized. For small \(\varepsilon\), the supports stay inside a fixed compact product in \(X\times Y\). Differentiating \(H\) under the averaging integral shows
\[
 p_m(H_\varepsilon-H)\le
 \max_{|\alpha|\le m}\omega_{\partial^\alpha H}(C\varepsilon)\longrightarrow0
\]
for every \(m\). Integration by parts in the ordinary compact integrals identifies these derivatives with derivatives of the kernels. For a fixed \(\varepsilon\), Riemann sums in \((a,b)\) approximate (B4) in every \(p_m\), by the proof of B1, and each summand is a product test. Choose \(\varepsilon_i\downarrow0\) and then meshes so that the two errors in \(p_i\) are at most \(1/i\). This gives one sequence converging in the test topology. The construction can keep supports in any prescribed product neighborhoods of the projections of \(\operatorname{supp}H\).

For \(u\in\mathcal D'(X)\), \(v\in\mathcal D'(Y)\), define
\[
 (u\otimes v)(H)=u_s\bigl(v_t(H(s,t))\bigr).                    \tag{B5}
\]
B1 gives a smooth inner test supported in the first projection of \(\operatorname{supp}H\). If \(H\) is supported in \(K\times L\), and the two distributions have orders \(r,s\) on those sets, then
\[
 |(u\otimes v)(H)|
 \le C\max_{\substack{|\alpha|\le r\\|\beta|\le s}}
                   \sup|\partial_s^\alpha\partial_t^\beta H|. \tag{B6}
\]
This proves that it is a distribution. On a product test its value is \(u(\phi)v(\psi)\). Reversing the pairings gives another distribution with those values; B2 proves equality and uniqueness. For three factors, apply B2 first to \((X\times Y)\times Z\), and then to each test on \(X\times Y\). Products of three tests thus determine the distribution. Both associations and every permutation have the same values on them, proving tensor associativity and permutation symmetry. The support is exactly \(\operatorname{supp}u\times\operatorname{supp}v\). Outside that product a small rectangle has one zero factor, so B2 and B0 give vanishing. At a point of the product, in every small rectangle each factor has a test with nonzero pairing, and their product has nonzero pairing. The derivative and separate multiplication identities follow either from (B5) and B1 or from their identical values on product tests.

**B3. Tensor limits.** Tensoring with a fixed distribution is separately weakly and strongly continuous. For weak continuity a fixed \(H\) gives one fixed inner test by (B5). For strong continuity a bounded family of \(H\)'s gives a bounded family of inner tests, by B1 and the local estimate for the fixed factor; its support stays in one compact projection.

If \(u_i\to u\) and \(v_i\to v\) weakly as sequences, U008 Theorem 5.1 supplies common finite orders and constants on any fixed compact projections. Thus (B6) bounds all tensor pairings uniformly in one finite seminorm. Approximate \(H\) by B2 in that seminorm. On a fixed finite sum of products the pairings converge by ordinary scalar multiplication; the uniform bound controls the approximation error for every \(i\) and the limit. Consequently
\[
 u_i\otimes v_i\longrightarrow u\otimes v
       \quad\hbox{weakly and strongly in }\mathcal D'(X\times Y). \tag{B7}
\]
The strong conclusion follows from the weak conclusion and U008 Theorem 5.1 applied on the product open set.

## Which pairs can contribute to an output

Define translation by
\[
 \langle\tau_pu,\phi\rangle=\langle u,\phi(\,\cdot\,+p)\rangle.   \tag{1.1}
\]
For a function this is \(\tau_pf(x)=f(x-p)\); for a point mass it gives \(\tau_p\delta_0=\delta_p\).

For closed \(F,G\subset\mathbb R^n\), addition is **proper on the supports** if
\[
 S_L=\{(s,t)\in F\times G:s+t\in L\}
       \quad\hbox{is compact for every compact }L.              \tag{1.2}
\]
Equivalently, for every finite \(R\) there is a finite \(T\) such that
\[
 s\in F,\ t\in G,\ |s+t|\le R\quad\Longrightarrow\quad
                         |s|,|t|\le T.                        \tag{1.3}
\]
The sets \(S_L\) are closed, so the equivalence is precisely the closed-and-bounded compactness criterion, applied to containing closed balls. A compact factor implies properness because \(t=(s+t)-s\). Properness implies that \(F+G\) is closed: a convergent sequence of sums lies in one compact ball, so its contributing pairs have a convergent subsequence in \(F\times G\).

**Theorem 1.1 (convolution by addition).** If \(\operatorname{supp}u\subset F\), \(\operatorname{supp}v\subset G\), and addition is proper on \(F\times G\), define
\[
 \langle u*v,\phi\rangle=(u\otimes v)(\phi(s+t)).                \tag{1.4}
\]
The pairing uses B0. It defines a distribution with
\[
 u*v=v*u,\qquad \operatorname{supp}(u*v)\subset F+G.             \tag{1.5}
\]
Orders at most \(r,s\) for the two factors give order at most \(r+s\). Also
\[
 \partial^\alpha(u*v)=(\partial^\alpha u)*v
                         =u*(\partial^\alpha v).              \tag{1.6}
\]

**Proof.** The intersection of the tensor support with \(\operatorname{supp}\phi(s+t)\) is closed and contained in the compact set \(S_{\operatorname{supp}\phi}\). Hence B0 applies. For all tests supported in a fixed compact \(L\), choose one compact smooth \(\chi=1\) on a neighborhood of \(S_L\). Then
\[
 \langle u*v,\phi\rangle=(u\otimes v)(\chi(s,t)\phi(s+t)).       \tag{1.7}
\]
Estimate (B6), the product rule and the chain rule bound this by a fixed finite seminorm of \(\phi\). When the factor orders are \(r,s\), no term differentiates \(\phi\) more than \(r+s\) times. Tensor symmetry proves commutativity. A test supported off \(F+G\) has zero extended pairing, proving the support assertion.

For one derivative, apply \((\partial_{s_j}u)\otimes v=\partial_{s_j}(u\otimes v)\) to the compact test in (1.7). The term with \(\partial_{s_j}\chi\) vanishes near the tensor support wherever \(\phi(s+t)\) can be nonzero, because \(\chi=1\) on a neighborhood of \(S_L\). Its pairing is zero by B0. The remaining term is \(-(u\otimes v)((\partial_j\phi)(s+t))\), which is the pairing of \(\partial_j(u*v)\). Derivatives do not enlarge supports, so the same properness hypothesis permits repetition and differentiation in either variable. \(\square\)

Evaluation at a point in (1.4) and then (1.6) give
\[
 \delta_p*u=\tau_pu,\qquad \delta_0*u=u,\qquad
 (\partial^\alpha\delta_0)*u=\partial^\alpha u.                 \tag{1.8}
\]
Thus for every constant-coefficient differential operator \(P\),
\[
 Pu=(P\delta_0)*u,\qquad
 P(u*v)=(Pu)*v=u*(Pv),                                         \tag{1.9}
\]
whenever the indicated supports sum properly.

There is also a maximal local output region. Let \(\Omega\) be the union of open balls \(B\) such that \(S_{\overline B}\) is compact. For a compact \(L\subset\Omega\), a finite such cover places \(S_L\), a closed set, inside a finite union of compact sets. Therefore (1.7) defines convolution on \(\Omega\). A convergent sequence of sums with limit in \(\Omega\) eventually lies in one of these balls; compactness of its pairs proves relative closedness of \((F+G)\cap\Omega\). Consequently
\[
 \operatorname{supp}_\Omega(u*v)\subset(F+G)\cap\Omega.         \tag{1.10}
\]
Any open region where all compact output sets have compact preimages is contained in \(\Omega\), by taking a small closed ball about each point. All preceding binary identities remain valid on this region.

## Smoothing and the exact derivative count

**Theorem 2.1 (a regular factor).** If \(u\in\mathcal D'(\mathbb R^n)\) and \(f\in\mathcal D(\mathbb R^n)\), their convolution is the smooth function
\[
 (u*f)(x)=u_s(f(x-s)),                                        \tag{2.1}
\]
and
\[
 \partial^\alpha(u*f)=(\partial^\alpha u)*f
                          =u*(\partial^\alpha f).             \tag{2.2}
\]
The map \(f\mapsto u*f\) is continuous from \(\mathcal D\) to \(C^\infty\). If \(u\) is compactly supported, it is also continuous from \(C^\infty\) to \(C^\infty\), and from \(\mathcal D\) to \(\mathcal D\).

For integers \(j,k\ge0\), an order-at-most-\(j\) distribution convolved with \(f\in C_c^{j+k}\) gives a \(C^k\) function by (2.1). If \(u\) has compact support and order at most \(j\), the same holds for every \(f\in C^{j+k}\).

**Proof.** On a compact output set \(L\), the tests in (2.1) have common support in \(L-\operatorname{supp}f\). B1 proves smoothness and parameter derivatives. Differentiating \(f(x-s)\) in \(s\) reverses the sign of differentiation in \(x\), which cancels the distributional derivative sign and proves (2.2). For compact \(u\), B0 inserts a fixed cutoff near its support and permits every smooth \(f\).

To identify the function with (1.4), pair it with a test \(\phi(x)\). Formula (B3) and the translation substitution \(t=x-s\) give
\[
 \int\phi(x)u_s(f(x-s))\,dx
    =u_s\!\left(\int\phi(s+t)f(t)\,dt\right)
    =\langle u*f,\phi\rangle.                                 \tag{2.3}
\]
All needed cutoffs can be fixed near the compact contributing projections; B0 then removes them. For \(f\) supported in a fixed compact \(M\), local order \(r\) of \(u\) on a compact neighborhood of \(L-M\) gives
\[
 \max_{|\alpha|\le a}\sup_{x\in L}|\partial^\alpha(u*f)(x)|
                      \le C_{L,M,a}p_{r+a}(f).                \tag{2.4}
\]
Every defining output seminorm therefore pulls back to an admissible input seminorm in U008's test topology. For compact \(u\), its fixed cutoff gives instead a seminorm of \(f\) on a fixed compact neighborhood of \(L-\operatorname{supp}u\), proving \(C^\infty\) continuity. With fixed compact input support, (1.5) fixes a compact output support as well. The same estimates give continuity on each input support space into that output support space, and hence into \(\mathcal D\) by the defining inductive-limit topology.

For finite regularity use U008 Proposition 1.2 to pair \(u\) with \(C_c^j\) tests. The difference-quotient calculation in B1 converges in \(C_s^j\) whenever the total number of parameter and test derivatives is at most \(j+k\). Uniform continuity of the derivatives of that last order gives continuity of the \(k\)-th output derivatives. Thus (2.1) is \(C^k\). To justify (2.3) at this regularity, approximate \(f\) in \(C^{j+k}\) on a common compact neighborhood by smooth functions. The order bound proves convergence of the function pairings locally uniformly, while the smooth tensor pairings converge distributionally by (B5), or directly by their integral in \(t\). This proves agreement with (1.4). For noncompact \(f\) and compact \(u\), apply the same approximation after a cutoff on the only compact region relevant to each output test. \(\square\)

**Lemma 2.2 (Riemann sums with derivatives).** For \(f\in C_c^j\), \(g\in C_c^0\),
\[
 R_h(x)=h^n\sum_{m\in\mathbb Z^n}f(x-hm)g(hm)
             \longrightarrow f*g(x)\quad\hbox{in }C_c^j.      \tag{2.5}
\]
All sums and the limit have support in \(\operatorname{supp}f+\operatorname{supp}g\).

**Proof.** The sums are finite. For \(|\alpha|\le j\), compare the differentiated sum with the ordinary integral of \(\partial^\alpha f(x-y)g(y)\) on the cubes \(hm+[0,h]^n\). The difference between each sampled integrand and its value at a point of that cube is at most
\[
 \|g\|_\infty\omega_{\partial^\alpha f}(\sqrt n\,h)
       +\|\partial^\alpha f\|_\infty\omega_g(\sqrt n\,h).       \tag{2.6}
\]
These are global moduli of continuity of the zero extensions, so the estimate is uniform in \(x\) and tends to zero. Only cubes meeting a fixed bounded neighborhood of \(\operatorname{supp}g\) contribute; their total volume is bounded for small \(h\). This proves uniform convergence of every indicated derivative. Differentiating the ordinary integral is justified by the same uniform difference quotients. A nonzero summand requires \(hm\in\operatorname{supp}g\) and \(x-hm\in\operatorname{supp}f\); the integral vanishes off the same compact sum. \(\square\)

## Associativity and continuity need support control

**Theorem 3.1 (associativity).** Let \(F,G,H\) be nonempty closed envelopes of the supports of \(u,v,w\). Suppose that the preimage of every compact set under addition of triples in \(F\times G\times H\) is compact. Then both iterated convolutions exist and
\[
 (u*v)*w=u*(v*w).                                             \tag{3.1}
\]
Their common value on \(\phi\) is the support-relative pairing of \(u\otimes v\otimes w\) with \(\phi(s+t+r)\). In particular, at least two compact factors suffice.

**Proof.** Fix \(h_0\in H\). Pairs in \(F\times G\) with sum in a compact \(L\), together with third coordinate \(h_0\), lie in the compact triple preimage of \(L+h_0\). They form a closed subset, so pair addition is proper. Fixing a point of each other nonempty envelope gives the other pair properness statements. The sum \(F+G\) is closed by Section 1. For a sequence \((a_i,r_i)\in(F+G)\times H\) whose sums lie in a compact set, choose \(a_i=s_i+t_i\). Triple properness gives a convergent subsequence of \((s_i,t_i,r_i)\). Thus the pairs \((a_i,r_i)\) have a convergent subsequence; their relevant preimage is closed, so addition on \((F+G)\times H\) is proper. This proves existence of both associations.

Here are the cutoffs that justify equality. Put \(L=\operatorname{supp}\phi\). Choose a compact smooth cutoff \(\zeta(a,r)\) equal to one near the preimage of \(L\) in \((F+G)\times H\). In evaluating \(((u*v)\otimes w)(\zeta(a,r)\phi(a+r))\), the inner convolution involves only \(a\) in the compact first projection of \(\operatorname{supp}\zeta\). Choose a compact cutoff \(\eta(s,t)=1\) near all pairs in \(F\times G\) with sums in that projection, using pair properness. Formula (1.7), B1 and the iterated tensor identity give the compact triple pairing
\[
 (u\otimes v\otimes w)
       \bigl(\eta(s,t)\zeta(s+t,r)\phi(s+t+r)\bigr).
\]
This test is compact: \((s,t)\) lies in \(\operatorname{supp}\eta\), and \(r\) in the second projection of \(\operatorname{supp}\zeta\). Its cutoff multiplier is one near every contributing point of the triple support with sum in \(L\). B0 identifies it with the canonical extended triple pairing. Repeating the same construction for the other association gives the same pairing, by B2's tensor associativity.

If two factors are compact, choose nonempty compact envelopes for them, using \(\{0\}\) for a zero factor, and any nonempty closed envelope for the third. Bounded sums and bounded first two coordinates bound the third. Closedness then proves triple properness. \(\square\)

The nonempty-envelope hypothesis addresses an actual intermediate-existence issue. An empty envelope forces its distribution to be zero. The canonical triple pairing is then zero, and every association whose inner convolution is defined is also defined and zero. It does not define an otherwise missing inner convolution. For example, \(u=0\), \(F=\varnothing\), \(v=\mathbf1_{[0,\infty)}\) and \(w=\mathbf1_{(-\infty,0]}\) have a proper empty triple preimage. The association \((u*v)*w\) is zero, whereas \(u*(v*w)\) has no inner convolution under this construction, as (3.5) shows.

For \(u\in\mathcal D'\), \(f\in C_c^\infty\), \(g\in C_c^0\), the theorem gives
\[
 (u*f)*g=u*(f*g).                                             \tag{3.2}
\]
Indeed both \(f,g\) are compact distributions. Differentiation under the ordinary compact integral makes \(f*g\) smooth. The left side is also a smooth function, by compact integration of the smooth \(u*f\) against \(g\). The distributional identity therefore holds pointwise by B0. Lemma 2.2 justifies the interchanges even for merely continuous \(g\).

When at least one of \(u,v\) has compact support, \(u*v\) is uniquely characterized by
\[
 (u*v)*f=u*(v*f)\qquad(f\in\mathcal D).
\]
Associativity gives existence. For uniqueness, if a difference \(T\) has \(T*f=0\) for every test \(f\), apply this to the normalized shrinking profiles of Theorem 5.2. That theorem gives \(T*f\to T\), so \(T=0\).

**Theorem 3.2 (continuity with fixed support sets).** On fixed closed \(F,G\) where addition is proper, convolution is separately continuous in both the weak and strong distribution topologies. If \(u_i\to u\), \(v_i\to v\) are weakly convergent sequences supported in \(F,G\), then \(u_i*v_i\to u*v\) weakly.

**Proof.** A limit has the designated support because every test in its complement has zero pairing with each term. For a fixed output test, use one cutoff \(\chi\) in (1.7). Separate weak continuity is then B3. A bounded family of output tests has common compact support \(L\), so one such cutoff works for the whole family. Product and chain rules show that \(\{\chi(s,t)\phi(s+t)\}\) is bounded in the product test space. B3 proves separate strong continuity. Its joint sequence conclusion (B7), applied to each such fixed compact test, proves joint weak convergence. \(\square\)

The support constraint cannot be dropped:
\[
 \delta_i\to0,\qquad \delta_{-i}\to0,\qquad
                  \delta_i*\delta_{-i}=\delta_0
                  \quad\hbox{in }\mathcal D'(\mathbb R).       \tag{3.3}
\]
The two inputs eventually miss each compact test support, but their sum stays at zero.

**Proposition 3.3 (a cone algebra).** If \(C\subset\mathbb R^n\) is a nonempty closed convex cone containing no nonzero line, distributions supported in \(C\) form a commutative associative convolution algebra with identity \(\delta_0\).

**Proof.** For any fixed number \(N\ge2\) of contributing coordinates, suppose their sums remain bounded while their maximum norm \(M_i\) tends to infinity. Divide by \(M_i\) and take a convergent subsequence in the product of closed unit balls. The limits lie in \(C\), have sum zero and include a vector \(e\) of norm one. Its negative is the sum of the other limits, which also lies in \(C\). Closure under addition follows from convexity and positive scaling. Thus \(C\) contains the line \(\mathbb R e\), a contradiction. All these additions are proper. Also \(0\in C\) by closedness and scaling, and \(C+C\subset C\). Theorems 1.1 and 3.1 give closure, commutativity, associativity and the identity. Bilinearity follows from a common cutoff in (1.7). \(\square\)

For \(H=\mathbf1_{[0,\infty)}\), ordinary integration over \(0\le t\le x\) gives
\[
 H*H=x_+.                                                     \tag{3.4}
\]
For the opposite half-lines and a nonnegative compact test positive near zero,
\[
 \int_{s\ge0}\int_{t\le0}\phi(s+t)\,dt\,ds=\infty.              \tag{3.5}
\]
In fact for all sufficiently large \(s\) a fixed-length interval of \(t\)'s about \(-s\) contributes the same positive lower bound. Tonelli applies to this nonnegative integrand and proves divergence. Hence the ordinary positive pairing does not define \(H(x)*H(-x)\).

## Sequence limits on bounded output tests

**Corollary 3.4 (strong sequence limits on proper supports).** Suppose fixed closed \(F,G\) satisfy
\[
 S_L=\{(s,t)\in F\times G:s+t\in L\}\text{ is compact}           \tag{3.4a}
\]
for every compact output \(L\). If \(u_i\to u\), \(v_i\to v\) weakly with supports in these sets, then
\[
                  u_i*v_i\longrightarrow u*v
                  \quad\hbox{strongly in }\mathcal D'.         \tag{3.4b}
\]
The same conclusion holds in \(\mathcal D'(\Omega)\) if compactness in (3.4a) is required only for \(L\Subset\Omega\).

**Proof.** The support of each limit lies in its closed envelope. For a bounded output test family \(B\), let \(L\) contain all its supports and choose \(\chi=1\) near \(S_L\). The family
\[
 B_\chi=\{\chi(s,t)\phi(s+t):\phi\in B\}                        \tag{3.4c}
\]
is bounded by the product and chain rules. Put \(T_i=u_i\otimes v_i-u\otimes v\). Formula (1.7) gives
\[
 \sup_{\phi\in B}|(u_i*v_i-u*v)(\phi)|
                   \le\sup_{Q\in B_\chi}|T_i(Q)|\longrightarrow0             \tag{3.4d}
\]
by B3. If \(S_L=\varnothing\), the zero cutoff gives zero directly. This proof uses only compact output subsets of \(\Omega\), so proves the local version too. \(\square\)

## Local smoothness can come from either factor

**Theorem 4.1 (finite regularity at an output point).** Let \(u\in\mathcal D'(\mathbb R^n)\), \(v\in\mathcal E'(\mathbb R^n)\), \(x_0\in\mathbb R^n\) and an integer \(k\ge0\). Suppose that every \(t\in\operatorname{supp}v\) has a neighborhood \(V\) and an integer \(j\ge0\) such that either
\[
 u|_{x_0-V}\text{ has order at most }j,\qquad v|_V\in C^{k+j},   \tag{4.1}
\]
or
\[
 u|_{x_0-V}\in C^{k+j},\qquad v|_V\text{ has order at most }j.   \tag{4.2}
\]
Then \(u*v\) is \(C^k\) near \(x_0\).

**Proof.** Shrink the neighborhoods and use compactness of \(\operatorname{supp}v\) and the explicit partition construction in B0 to write
\[
 v=\sum_{\ell=1}^N v_\ell,\qquad v_\ell=\chi_\ell v,\qquad
                  \operatorname{supp}\chi_\ell\Subset V_\ell. \tag{4.3}
\]
Choose \(\eta_\ell\in C_c^\infty(x_0-V_\ell)\), equal to one on a neighborhood of \(x_0-\operatorname{supp}\chi_\ell\). These are compact subsets of the indicated open sets. A single sufficiently small neighborhood \(W\) of \(x_0\) satisfies
\[
 x-\operatorname{supp}\chi_\ell\subset\{\eta_\ell=1\}^{\circ}
                 \qquad(x\in W,\ 1\le\ell\le N).              \tag{4.4}
\]
The support of \((1-\eta_\ell)u\) cannot add to a point of \(W\) with the support of \(v_\ell\). Theorem 1.1 therefore gives \(u*v_\ell=(\eta_\ell u)*v_\ell\) on \(W\). In (4.1) the first factor is compact of order at most \(j\) and the second is compact \(C^{k+j}\); in (4.2) the roles reverse. Multiplication by a fixed smooth cutoff preserves the claimed order by the product rule. Theorem 2.1 makes each term \(C^k\). Their finite sum proves the result. \(\square\)

**Corollary 4.2 (singular support).** With \(v\) compactly supported,
\[
 \operatorname{sing\,supp}(u*v)
       \subset \operatorname{sing\,supp}u+\operatorname{sing\,supp}v.         \tag{4.5}
\]
Here the singular support is the closed complement of the set where a distribution is represented by a smooth function.

**Proof.** The right side is closed because its second factor is compact: a convergent sequence of sums has a convergent subsequence of second coordinates, and hence of first coordinates. If \(x_0\) misses this sum, every \(t\in\operatorname{supp}v\) has either a neighborhood where \(v\) is smooth or one whose reflection about \(x_0\) is a smooth region for \(u\). Shrink it so the other distribution has a finite local order. Choose this finite cover and the cutoffs of Theorem 4.1 once, independently of \(k\). The selected smooth factor has every derivative, and the other factor has its fixed finite order. Thus the same finite sum on the same neighborhood \(W\) is \(C^k\) for every \(k\); it is smooth there. B0 ensures agreement of these representatives. \(\square\)

Ordinary support inclusion can be strict. For
\[
 u=\delta_0-2\delta_1,\qquad v=\delta_0+2\delta_1,
 \qquad u*v=\delta_0-4\delta_2,                                \tag{4.6}
\]
the two contributions at \(1\) cancel. The input-support sum is \(\{0,1,2\}\), and the output support is \(\{0,2\}\).

**Corollary 4.3 (singular support on the proper output domain).** For closed support envelopes \(F,G\) and the maximal local properness region \(\Omega\) of Section 1,
\[
 \operatorname{sing\,supp}_\Omega(u*v)
    \subset(\operatorname{sing\,supp}u+\operatorname{sing\,supp}v)\cap\Omega. \tag{4.7}
\]
The sum on the right is relatively closed in \(\Omega\).

**Proof.** A convergent sequence of sums of singular points, with limit in \(\Omega\), eventually lies in a compact ball inside \(\Omega\). The contributing pairs then have a convergent subsequence. Closedness of both singular supports gives the relative closedness assertion. Fix \(x_0\) outside that sum and a ball \(W\) about it with compact closure \(L\subset\Omega\). Take compact cutoffs \(\chi(s),\eta(t)\) equal to one near the two projections of \(S_L\). Formula (1.7) gives
\[
 (u*v)|_W=((\chi u)*(\eta v))|_W.                              \tag{4.8}
\]
Multiplication by a smooth cutoff introduces no singularity. Corollary 4.2 therefore places the singular support of the right side in the sum of two compact subsets of the original singular supports. That compact sum misses \(x_0\), so the right side is smooth near \(x_0\). This proves (4.7). Empty factors give the zero distribution and cause no exception. \(\square\)

## Smoothing inside an arbitrary open set

**Proposition 5.1 (the local convolution domain).** For open \(X\subset\mathbb R^n\), \(u\in\mathcal D'(X)\), and compactly supported \(v\) with \(C=\operatorname{supp}v\), convolution is canonically defined on
\[
                  X_C=\{x:x-C\subset X\}.                     \tag{5.1}
\]
It depends only on \(u\) near \(x-C\) at an output point \(x\). Derivatives transfer as in (1.6), and
\[
 \operatorname{supp}_{X_C}(u*v)
              \subset(\operatorname{supp}_Xu+C)\cap X_C.      \tag{5.2}
\]
For \(v=\rho\in C_c^\infty\), it is the smooth function \(u_s(\rho(x-s))\).

**Proof.** If \(C=\varnothing\), take \(X_C=\mathbb R^n\) and the convolution zero. Otherwise, for \(x\in X_C\), the compact set \(x-C\subset X\) has a positive distance from the closed complement, unless that complement is empty. Its sufficiently small translates stay in \(X\), proving that \(X_C\) is open. For compact \(L\subset X_C\), the continuous image \(L-C\) of \(L\times C\) is compact and contained in \(X\). The contributing part of the tensor support in \(X\times\mathbb R^n\) is contained in \((L-C)\times C\). B0 and (B6) consequently define its pairing with \(\phi(s+t)\) by fixed compact cutoffs. They prove continuity, independence of cutoffs and local dependence; the derivative argument of Theorem 1.1 is unchanged.

The set in (5.2) is relatively closed. For \(f_i+c_i\to x\in X_C\), a subsequence has \(c_i\to c\in C\), so \(f_i\to x-c\in X\). Relative closedness of \(\operatorname{supp}_Xu\) includes this limit. Tests off the sum have zero pairing, proving (5.2). B1 and the calculation (2.3), with the same local cutoffs, prove the smooth formula. \(\square\)

**Theorem 5.2 (shrinking smooth averages).** Suppose smooth compact profiles satisfy
\[
 \int\rho_\lambda=1,\qquad \sup_\lambda\|\rho_\lambda\|_1<\infty,\qquad
 \operatorname{supp}\rho_\lambda\subset\overline B(0,r_\lambda),
 \qquad r_\lambda\to0.                                       \tag{5.3}
\]
For every \(u\in\mathcal D'(X)\), the locally defined \(u*\rho_\lambda\) converge strongly on tests in \(X\) to \(u\). In particular any family of nonnegative normalized shrinking profiles works, without requiring one fixed shape.

**Proof.** Every fixed compact test support \(L\Subset X\) lies in the output domain for small enough \(r_\lambda\). Formula (B5), a translation substitution, and (B3) give
\[
 \langle u*\rho_\lambda,\phi\rangle
       =\langle u,\check\rho_\lambda*\phi\rangle,\qquad
 (\check\rho_\lambda*\phi)(s)
       =\int\rho_\lambda(t)\phi(s+t)\,dt,\quad
 \check\rho(t)=\rho(-t).                                     \tag{5.4}
\]
The averaged tests have support in \(L+\overline B(0,r_\lambda)\), hence in one compact subset of \(X\) for small radii. Subtract \(\phi\) using the normalization. The fundamental theorem on the segment from \(s\) to \(s+t\) gives
\[
 p_m(\check\rho_\lambda*\phi-\phi)
       \le C_n r_\lambda\|\rho_\lambda\|_1p_{m+1}(\phi).        \tag{5.5}
\]
Use the finite-order bound of \(u\) on that compact neighborhood. On a bounded family of \(\phi\)'s, \(p_{m+1}\) has a common bound, so the pairings tend uniformly to zero. This is exactly the stated local strong convergence. For nonnegative normalized profiles the norm is one. \(\square\)

**Corollary 5.3 (compact smooth approximation).** Every distribution on an open \(X\) is a strong distribution limit of a sequence in \(C_c^\infty(X)\).

**Proof.** Use the compact exhaustion \(K_i\subset\operatorname{int}K_{i+1}\) supplied by the integration prerequisite, and cutoffs \(\chi_i=1\) near \(K_i\), compactly supported in \(X\). Multiplication followed by zero extension makes \(\chi_i u\) a compact distribution on \(\mathbb R^n\): explicitly it acts on \(\phi\) as \(u(\chi_i\phi|_X)\). Choose nonnegative normalized profiles with support radius
\[
 0<\varepsilon_i\le1/i,\qquad
 \varepsilon_i<\tfrac12\operatorname{dist}(\operatorname{supp}\chi_i,X^c),   \tag{5.6}
\]
omitting the second bound if \(X=\mathbb R^n\); a zero cutoff requires no distance restriction. Put \(f_i=(\chi_i u)*\rho_i\). Theorems 1.1 and 2.1 put \(f_i\) in \(C_c^\infty(X)\). On a fixed compact test support and its one small compact neighborhood, \(\chi_i=1\) eventually. Formula (5.4) therefore makes its pairing with \(f_i\) exactly its pairing with the local \(u*\rho_i\). Theorem 5.2 proves convergence uniformly on every bounded test family. If \(X=\varnothing\), the only distribution is zero and the zero sequence suffices. \(\square\)

## Translation-invariant operators have one convolution kernel

We first prove the two kernel facts needed for the operator theorem.

**K1. Constructing a kernel from a separately continuous pairing.** Suppose \(B(\psi,\phi)\) is a complex bilinear form on \(\mathcal D(\mathbb R^a)\times\mathcal D(\mathbb R^b)\) which is continuous in each variable with the other fixed. There is a unique \(K\in\mathcal D'(\mathbb R^{a+b})\) satisfying \(K(\psi\otimes\phi)=B(\psi,\phi)\).

Fix compact supports \(K_x,K_y\). On the complete metric space \(\mathcal D_{K_x}\), form the closed sets
\[
 E_m=\{\psi:|B(\psi,\phi)|\le m p_m(\phi)
                          \text{ for every }\phi\in\mathcal D_{K_y}\},
                   \qquad m=1,2,\ldots .
\]
They are closed because \(B(\,\cdot\,,\phi)\) is continuous for each \(\phi\). Their union is the space: continuity of \(B(\psi,\,\cdot\,)\) gives one finite-order bound for each fixed \(\psi\), and increasing \(m\) bounds its order and constant. The complete-space and Baire proofs are in the functional prerequisite, Sections 6 and 14.1–14.2. Thus some \(E_m\) contains \(\psi_0+\{\psi:p_r(\psi)<\varepsilon\}\). Subtract the inequality at \(\psi_0\) from that at \(\psi_0+\psi\), and then rescale \(\psi\). Since \(p_r\) includes the zeroth derivative, it is zero only for the zero test. This gives
\[
 |B(\psi,\phi)|\le C p_r(\psi)p_m(\phi)
       \quad(\psi\in\mathcal D_{K_x},\ \phi\in\mathcal D_{K_y}). \tag{K1}
\]
Specifically \(C=4m/\varepsilon\) works. This is the joint estimate we need; separate continuity alone was the hypothesis.

Choose compact smooth cutoffs \(\chi_x,\chi_y\) equal to one on neighborhoods of two given closed boxes, and apply (K1) with their supports. Put \(d=a+b\). The Schwartz prerequisite F2–F4 proves the Fourier convention and inversion
\[
 \widehat H(\xi,\eta)=\int e^{-i(x\cdot\xi+y\cdot\eta)}H(x,y)\,dx\,dy,
 \qquad H(z)=(2\pi)^{-d}\int e^{iz\cdot\zeta}\widehat H(\zeta)\,d\zeta .
\]
Define
\[
 K_\chi(H)=(2\pi)^{-d}\int
       \widehat H(\xi,\eta)
       B(\chi_x e^{ix\cdot\xi},\chi_y e^{iy\cdot\eta})\,d\xi\,d\eta .
                                                               \tag{K2}
\]
The second factor depends continuously on the frequencies: the compact exponential tests depend continuously on them in every derivative seminorm, and (K1) controls the change in either argument of \(B\). This is an absolutely convergent scalar integral. Indeed (K1) bounds that factor by \(C'(1+|\xi|)^r(1+|\eta|)^m\). For \(H\) on any fixed compact support, integration by parts from F2 gives
\[
 (1+|\zeta|^2)^N\widehat H(\zeta)
       =\widehat{(1-\Delta)^N H}(\zeta),\qquad
 |\widehat{(1-\Delta)^N H}(\zeta)|\le C_L p_{2N}(H).
                                                               \tag{K3}
\]
Choose \(2N>r+m+d\). The product of these bounds is integrable: on \(2^\ell\le|\zeta|\le2^{\ell+1}\) its integral is bounded by a constant times \(2^{\ell(r+m+d-2N)}\), whose sum is geometric, and the unit ball has finite volume. Thus \(K_\chi\) has a finite test seminorm bound and is a distribution.

For \(H=\psi\otimes\phi\), Fubini gives \(\widehat H=\widehat\psi\,\widehat\phi\). Fourier inversion and (K1) show
\[
 K_\chi(\psi\otimes\phi)=B(\chi_x\psi,\chi_y\phi).              \tag{K4}
\]
To justify the passage through \(B\), truncate the frequency integrals to boxes and approximate by Riemann sums. Every derivative of \(\chi_x e^{ix\cdot\xi}\) grows at most polynomially in \(\xi\); the rapid decrease of \(\widehat\psi\) bounds the tails in every test seminorm on the one fixed support \(\operatorname{supp}\chi_x\). The same holds for \(\phi\). The truncated sums therefore converge in the fixed-support test spaces, and the bound (K1) permits both limits. This proves (K4) without a vector-valued integration theorem.

On tests supported inside the boxes where both cutoffs are one, this distribution is independent of the cutoffs: by B2 approximate such a test by finite product sums supported within those boxes, and use (K4) for each sum. Choose increasing boxes exhausting each Euclidean space. The resulting distributions agree on the smaller product boxes by this argument. For an arbitrary compact test choose one containing product box and use its functional; agreement proves independence and linearity, while its finite bound proves continuity. This constructs \(K\). Product-test density B2 proves uniqueness. No growth condition on \(B\) outside fixed compact supports has been imposed.

**K2. A distribution constant in a whole group of variables.** If \(J\in\mathcal D'(\mathbb R^a_s\times\mathbb R^b_r)\) has \(\partial_{r_j}J=0\) for every \(j\), there is a unique \(u\in\mathcal D'(\mathbb R^a)\) with \(J=u\otimes1\).

Choose one-dimensional normalized compact smooth profiles \(\rho_j\), and write \(\rho(r)=\prod_j\rho_j(r_j)\). For a test \(H(s,r)\), integrate first in \(r_1\), obtaining \(H_1(s,r_2,\ldots,r_b)\). The difference \(H-\rho_1(r_1)H_1\) has integral zero in \(r_1\), so
\[
 Q_1(s,r)=\int_{-\infty}^{r_1}
       [H(s,t,r_2,\ldots,r_b)-\rho_1(t)H_1(s,r_2,\ldots,r_b)]\,dt
\]
is a compact smooth test with \(\partial_{r_1}Q_1=H-\rho_1H_1\). Smoothness follows from ordinary differentiation under the compact integral. It vanishes below the containing interval of the two supports and above that interval by zero total integral; the other supports lie in fixed compact projections. Repeat the same construction for \(H_1\) in \(r_2\), then in every subsequent coordinate. Multiplying the new primitives by the previous profiles gives compact smooth tests \(Q_j\) with
\[
 H(s,r)=\rho(r)\int H(s,t)\,dt+\sum_{j=1}^b\partial_{r_j}Q_j(s,r).           \tag{K5}
\]
Define \(u(\psi)=J(\psi(s)\rho(r))\). The product estimate for tests makes \(u\) a distribution. Applying \(J\) to (K5) kills every derivative and gives \(J(H)=u(\int H\,dr)\), precisely \(u\otimes1\) by B5. Testing with \(\psi\rho\) also proves uniqueness.

**Theorem 6.1 (translation invariance).** Let
\[
                  A:\mathcal D(\mathbb R^n)\longrightarrow
                                      \mathcal D'(\mathbb R^n)             \tag{6.1}
\]
be a linear weakly continuous map with \(A\tau_h=\tau_hA\) for every \(h\in\mathbb R^n\). There is a unique \(u\in\mathcal D'(\mathbb R^n)\) such that
\[
                         A\phi=u*\phi\qquad(\phi\in\mathcal D).            \tag{6.2}
\]
Every output is smooth, and \(A:\mathcal D\to C^\infty\) is continuous.

The conclusion also holds for a linear translation-commuting map \(A:\mathcal D\to C^0\) which sends every sequence tending to zero in \(\mathcal D\) to a sequence tending uniformly to zero on compact output sets.

**Proof.** The bilinear form \(B(\psi,\phi)=\langle A\phi,\psi\rangle\) is separately continuous: one direction is the output being a distribution, and the other is weak continuity of \(A\). K1 gives
\[
                  \langle A\phi,\psi\rangle
                    =\langle K,\psi(x)\phi(y)\rangle.                      \tag{6.3}
\]
Translation commutation implies
\[
 \begin{aligned}
 K(\psi(x-h)\phi(y-h))
   &=\langle A\tau_h\phi,\tau_h\psi\rangle\\
   &=\langle\tau_hA\phi,\tau_h\psi\rangle
     =\langle A\phi,\psi\rangle .
 \end{aligned}                                                            \tag{6.4}
\]
By B2 this invariance holds for every test on the product. The invertible linear coordinates \(s=x-y,\ r=y\) have absolute determinant one. Define
\[
                  J(H(s,r))=K(H(x-y,y)).                                  \tag{6.5}
\]
Composition with this linear map preserves compact supports and bounds each derivative by a finite sum of derivatives, so \(J\) is a distribution. Simultaneous translation of \(x,y\) is translation of \(r\) alone. Equation (6.4) consequently gives \(J(H(s,r-h))=J(H(s,r))\). Difference quotients in \(h_j\) converge in the test topology by the fundamental theorem, with one common compact support for small \(h_j\). Hence every \(\partial_{r_j}J\) is zero. K2 gives \(J=u\otimes1\).

The test \(\psi(s+r)\phi(r)\) is compactly supported: \(r\) lies in \(\operatorname{supp}\phi\) and \(s\) lies in \(\operatorname{supp}\psi-\operatorname{supp}\phi\). Thus B5 and (2.3) give
\[
 \langle A\phi,\psi\rangle
   =u_s\!\left(\int\psi(s+r)\phi(r)\,dr\right)
   =\langle u*\phi,\psi\rangle.                                           \tag{6.6}
\]
Theorem 2.1 proves the smoothness and continuity into \(C^\infty\). After that conclusion, recover \(u\) directly by
\[
                  \langle u,\theta\rangle=(A\check\theta)(0),
                  \qquad \check\theta(x)=\theta(-x).                       \tag{6.7}
\]
This proves uniqueness as well.

For the \(C^0\) variant, regard each continuous output as a distribution. For a fixed output test \(\psi\), the linear form \(\phi\mapsto\int(A\phi)\psi\) sends test sequences tending to zero to zero, by the uniform convergence on \(\operatorname{supp}\psi\) and the bound \(\|\psi\|_1\). U008 Proposition 1.1 makes it a continuous test functional. Thus \(A\) is weakly continuous into \(\mathcal D'\), and the first part applies. The original continuous output equals the smooth representative pointwise by B0. \(\square\)

The geometry is that simultaneous translation fixes only the difference \(x-y\). The construction places no polynomial growth condition on \(u\); Fourier inversion in K1 was used only for compact tests.

## Exercises

1. **Cancellation and derivative signs.** For \(u=\delta_0-2\delta_1\), \(v=\delta_0+2\delta_1\) on the line, find \(u*v\), \(u*\delta'_0\), their test pairings and the input and output supports.
2. **Causal integration and a delayed jump.** With \(H=\mathbf1_{[0,\infty)}\), \(w=\delta'_0-\delta'_1\), compute \(H*(H*w)\) and \((H*H)*w\), justifying associativity despite the noncompact factors.
3. **Normalization without a norm bound.** Let \(\rho\in C_c^\infty((-1,1))\) be even, nonnegative and normalized. Put \(\rho_\varepsilon(x)=\varepsilon^{-1}\rho(x/\varepsilon)\) and \(q_\varepsilon=\rho_\varepsilon+\rho'_\varepsilon\). Find its integral, supports and distribution limit, and identify which hypothesis of Theorem 5.2 fails.
4. **The finite-regularity threshold.** Extend \(f(x)=(1-x^2)^4\) for \(|x|<1\) by zero. Prove that \(\delta''_0*f\) is \(C^1\) but not \(C^2\), and identify \(j,k\) in Theorem 2.1.
5. **A shifted output domain.** Let \(X=(-2,2)\), \(u=\operatorname{pv}(1/x)|_X\), \(v=\delta_1\). Find the domain in Proposition 5.1, the test pairing and the singular support of \(u*v\).
6. **Reflection and translation.** Show that \(A\phi(x)=\phi(-x)\) is continuous on tests but is not convolution with one distribution. Use both translation commutation and the recovery formula (6.7).
7. **Properness from geometry.** For \(C=\{(t,z)\in\mathbb R\times\mathbb R^d:t\ge|z|\}\), bound each coordinate of any finite contributing tuple whose sum lies in a ball of radius \(R\). Explain the obstruction for a closed convex cone containing a nonzero line.
8. **Translation invariance and locality.** If \(A\) satisfies Theorem 6.1 and \(\operatorname{supp}(A\phi)\subset\operatorname{supp}\phi\) for every test, prove that \(A\) is a finite constant-coefficient differential operator. Prove the converse.
9. **Jets and tails on a half-line.** For \(u_j=\delta'_0+\delta_j\), \(v_j=\delta_0+\delta_j\), compute the convolutions and their strong limit. Give one fixed proper pair of support sets and a direct bounded-test proof.
10. **A curved proper pair.** Let \(P=\{(t,t^2):t\in\mathbb R\}\), \(p_j=(j,j^2)\), \(q_j=(-j,j^2)\). Prove properness of addition on \(P\times P\), and compute the strong limit of
\[
              (\delta_0+\delta_{p_j})*
                         (\partial_{x_1}\delta_0+\delta_{q_j}),
\]
including all translated derivatives.

## Complete solutions

**Solution 1.** Evaluation and (1.8) give
\[
 u*v=\delta_0-4\delta_2,\qquad
 u*\delta'_0=\delta'_0-2\delta'_1.
\]
Their pairings are \(\phi(0)-4\phi(2)\) and \(-\phi'(0)+2\phi'(1)\). Each input has support \(\{0,1\}\), so their support sum is \(\{0,1,2\}\); the nonzero output masses are precisely at \(0,2\). Smooth tests supported near either point show that neither is removable from the support.

**Solution 2.** Every support lies in the pointed closed cone \([0,\infty)\), so Proposition 3.3 supplies associativity. The fundamental theorem gives
\[
 H'(\phi)=-\int_0^\infty\phi'(x)\,dx=\phi(0),
 \qquad (x_+)'(\phi)=-\int_0^\infty x\phi'(x)\,dx=\int_0^\infty\phi(x)\,dx .
\]
Thus \(H*w=\delta_0-\delta_1\), and
\[
 H*(H*w)=H-\tau_1H,\qquad
 (H*H)*w=(x_+)'-\tau_1(x_+)'=H-\tau_1H.
\]
Both pair as \(\int_0^1\phi(x)\,dx\); endpoint values of the indicator have no effect on its distribution.

**Solution 3.** The derivative of a compact smooth function has integral zero. Hence \(\int q_\varepsilon=1\), and its support lies in \([-\varepsilon,\varepsilon]\). Integration by parts and scaling give
\[
 q_\varepsilon(\phi)=\int\rho(y)\phi(\varepsilon y)\,dy
                    -\int\rho(y)\phi'(\varepsilon y)\,dy
                  \longrightarrow\phi(0)-\phi'(0).
\]
The limit is \(\delta_0+\delta'_0\), by compact uniform convergence of the two test factors. But
\[
 \|q_\varepsilon\|_1\ge
    \|\rho'_\varepsilon\|_1-\|\rho_\varepsilon\|_1
    =\varepsilon^{-1}\|\rho'\|_1-1\longrightarrow\infty .
\]
Here \(\rho'\ne0\), since a nonzero normalized compact function is not constant. The uniform \(L^1\) bound in (5.3) fails. Taking \(u=\delta_0\) shows directly why the remaining hypotheses do not suffice.

**Solution 4.** At an endpoint let \(t\ge0\) be the inward distance. Then \(f=(2t-t^2)^4=16t^4+O(t^5)\) on the inside and zero on the outside. Derivatives through order three match at the endpoint; the fourth has inside limit \(4!\,16=384\) and outside limit zero. Thus \(f\in C_c^3\), while \(f\notin C^4\). The order-at-most-two pairing of \(\delta''_0\) is \(\phi\mapsto\phi''(0)\), so Theorem 2.1 with \(j=2,k=1\) applies and gives
\[
 (\delta''_0*f)(x)=f''(x)=
 \begin{cases}(1-x^2)^2(56x^2-8),&|x|<1,\\0,&|x|\ge1.\end{cases}
\]
Near an endpoint this is \(192t^2+O(t^3)\) on the inside. Its second derivative consequently has inside limit \(384\) and outside limit zero. It is \(C^1\) and not \(C^2\). The two-derivative order is exact: with a compact \(\psi\) satisfying \(\psi''(0)\ne0\), the tests \(\varepsilon^2\psi(x/\varepsilon)\) have \(C^1\) norm tending to zero but constant nonzero second derivative at zero.

**Solution 5.** The principal value on \(X\) exists directly because
\[
 u(\phi)=\int_0^2\frac{\phi(s)-\phi(-s)}s\,ds,\qquad
 |u(\phi)|\le4\sup|\phi'|.
\]
The fundamental theorem proves the bound and integrability at zero. This is the symmetric punctured-integral limit, and away from zero it is the function \(1/x\). It cannot be smooth near zero, because uniqueness of continuous representatives on either punctured side would make such a smooth representative equal to the unbounded \(1/x\).

Now \(x-\{1\}\subset(-2,2)\) means \(x\in(-1,3)\). The convolution is the translated principal value there, with singular support exactly \(\{1\}\). Its pairing is
\[
 (u*\delta_1)(\phi)=u(\phi(\,\cdot\,+1))
   =\lim_{a\downarrow0}\int_{\substack{s\in(-2,2)\\|s|>a}}
                            \frac{\phi(s+1)}s\,ds .
\]
The translated test is compactly supported inside \(X\), so no extension of \(u\) outside \(X\) is used.

**Solution 6.** Reflection takes one fixed compact support to its reflection and preserves every derivative supremum, up to irrelevant signs. It is therefore continuous on \(\mathcal D\). However \(A\tau_h=\tau_{-h}A\); for \(h\ne0\), a small bump whose two translated centers differ shows this is not \(\tau_hA\). Every convolution operator commutes with translations: (2.1) gives \(u*(\tau_h\phi)(x)=(u*\phi)(x-h)\). Hence reflection is not convolution. Independently, (6.7) would give \(u(\theta)=\theta(0)\), so \(u=\delta_0\), whose convolution operator is the identity. Reflection changes the sign of a nonzero odd test, giving a contradiction.

**Solution 7.** For a contributing tuple \((t_i,z_i)\in C\), every \(t_i\ge0\). The sum being in a radius-\(R\) ball implies \(\sum_i t_i\le R\), hence
\[
             0\le t_i\le R,\qquad |z_i|\le t_i\le R,\qquad
                         |(t_i,z_i)|\le\sqrt2R .
\]
The contributing tuples over a compact output set are closed and bounded, so compact. If a cone contains \(\mathbb R e\) for a unit vector \(e\), the pairs \((me,-me)\) have sum zero and unbounded coordinates. More concretely the two positive distributions \(\sum_{m\ge0}\delta_{me}\) and \(\sum_{m\ge0}\delta_{-me}\) are locally finite, but their proposed positive convolution pairs to infinity with any nonnegative test positive at zero: each matching pair contributes its positive value at zero. This establishes an obstruction for that pair, without asserting that every pair supported in such a cone fails.

**Solution 8.** By (6.7), a test \(\theta\) supported away from zero satisfies \(u(\theta)=(A\check\theta)(0)=0\), because locality keeps the smooth output supported away from zero. Hence \(\operatorname{supp}u\subset\{0\}\). The complete point-support proof in the [angular prerequisite](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A3, gives
\[
                  u=\sum_{|\alpha|\le m}c_\alpha\partial^\alpha\delta_0 .
\]
That proof uses a shrinking cutoff, the finite-order estimate and the Taylor remainder to annihilate tests with zero \(m\)-jet; it then supplies the coefficients and their uniqueness. Substituting into (1.8) gives \(A\phi=\sum c_\alpha\partial^\alpha\phi\). Conversely every such finite operator is continuous on each test support space by its derivative estimate and hence on \(\mathcal D\); it commutes with translations and its derivatives vanish wherever the input vanishes locally. It is therefore local and satisfies the hypotheses of Theorem 6.1.

**Solution 9.** Choose \(F=G=[0,\infty)\). A compact output bound \(s+t\le R\) bounds both \(s,t\) between zero and \(\max(R,0)\), proving properness. The input weak limits are \(\delta'_0,\delta_0\), since the masses at \(j\) eventually miss every compact test. Bilinearity, translation and derivative transfer give
\[
                 u_j*v_j=\delta'_0+\delta'_j+\delta_j+\delta_{2j}.
\]
For a bounded family supported in \([-R,R]\), all three nonorigin terms vanish exactly once \(j>R\): the tests, including their derivatives, are zero in neighborhoods of those points. The strong limit is thus \(\delta'_0\), pairing as \(-\phi'(0)\), in agreement with Corollary 3.4.

**Solution 10.** The parabola is closed. If a compact output set has second coordinate bounded above by \(R\), a contributing pair of parameters satisfies \(s^2+t^2\le R\). Either there are no such pairs or \(|s|,|t|\le\sqrt{\max(R,0)}\). Closedness and this bound prove properness. The supports of both input sequences lie in \(P\), including the derivative at the origin. Their weak limits are \(\delta_0,\partial_{x_1}\delta_0\). Expanding gives
\[
 (\delta_0+\delta_{p_j})*(\partial_{x_1}\delta_0+\delta_{q_j})
  =\partial_{x_1}\delta_0+\delta_{q_j}
                      +\partial_{x_1}\delta_{p_j}+\delta_{(0,2j^2)} .
\]
All three nonorigin locations escape every compact set. On any one bounded output test family their point and derivative pairings therefore vanish exactly for large \(j\). The strong limit is \(\partial_{x_1}\delta_0\), pairing as \(-\partial_{x_1}\phi(0)\). Both this direct argument and Corollary 3.4 allow these noncompact fixed support envelopes.

## Programme proof locations and freely accessible sources

- [U008, Order, positivity and distributional limits](order-positivity-and-limits.md): the definition and bounded-family characterization (T1), Proposition 1.2 for finite differentiability, Proposition 1.1 for the sequential criterion, and the entire proof of Theorem 5.1 for uniform order and strong sequential convergence.
- [Functional prerequisite](../prerequisites/U011-free-foundations/functional-foundations-U008.md), Sections 6 and 14.1–14.2: the complete Baire and test-space completeness proofs used in K1. [Scalar prerequisite](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 13.1–13.5 and 13.10, and [integration prerequisite](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.4: scalar differentiation, compact cutoffs, integration, translation changes and smooth approximation.
- [Schwartz prerequisite](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F2–F4: the seminorm estimates, integration by parts and two inverse identities used in (K2)–(K4). [Angular prerequisite](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A3: the full finite point-jet proof used in Solution 8.
- Semyon Dyatlov, [*Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), freely accessible MIT notes, 2 October 2026 version. Propositions 6.3 and Lemma 6.8 provide the parameter and integral arguments; Theorems 6.4, 6.7, 6.10 and 7.1 provide smooth convolution, approximation and tensor construction. Chapter 8 gives the proper-support pairing and singular-support localization. The Fourier kernel sketch in Theorem 7.6 is expanded here into the complete compact-cutoff construction K1, with its norm bound, convergence and compatibility proofs.
- Richard Melrose, [*18.155 Lecture 15: Schwartz's kernel theorem*](https://math.mit.edu/~rbm/18.155-F16/L15.pdf), freely accessible MIT lecture, 1 November 2016. Pages 2–4 explain separate continuity, the Baire estimate and localization by cutoffs. The kernel construction here uses the supplied Fourier inversion proof and the explicit integral (K2); it does not require the lecture's additional Sobolev-space machinery.

Every distributional construction and operator identity used above has its proof here or at one of the exact programme locations listed. The freely accessible human texts support the construction of these proofs.
