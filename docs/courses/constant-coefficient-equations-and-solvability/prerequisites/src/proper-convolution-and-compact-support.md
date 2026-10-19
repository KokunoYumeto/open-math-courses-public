# Proper convolution and compact support

*Original programme exposition by GPT-6 Astra (OpenAI), October 2026. Selection by GPT-6.1 Sol (OpenAI). CC0.*

A bounded output receives contributions from a compact set of input pairs when addition is proper on the supports. The constructions below define the required tensor pairing and support integral,prove its independence of cutoffs,and establish the convolution derivative identities.

We use complex-linear distributions on smooth compact tests. On each fixed compact set their continuity is an estimate by finitely many uniform test-derivative seminorms. The [scalar calculus](../metric-foundation-bridges.html) and [integration foundations](../banach-foundation-bridges.html) supply compact cutoffs,Riemann sums and the stated approximation integrals.

## Pairings and tensor products

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

## Source and terms

The complete pairing and proper-support arguments are selected from Convolution as addition of supports, B0-B2 and Theorem 1.1. Original programme exposition is CC0 1.0. The linked scalar and integration selections retain their stated terms.
