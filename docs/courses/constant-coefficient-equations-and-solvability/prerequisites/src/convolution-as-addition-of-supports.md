# Convolution as addition of supports

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

Convolution combines a measurement at one point with a measurement at another and assigns the result to their sum. This description works for point masses, functions and distributions. Its main restriction is geometric: points escaping to infinity must not keep contributing to one bounded output region. Once that restriction is understood, smoothing, differentiation and translation invariance become consequences of the same construction.

We use [Tensor products and parameter-dependent distributions](tensor-products-and-parameters.md) for independent pairings and their limits, [Local data and compatible products](local-data-and-compatible-products.md) for tests compact only on a distribution’s support, and [Order, positivity and distributional limits](order-positivity-and-limits.md) for finite-regularity tests. The last section uses [Distributions as kernels of continuous operators](distributions-as-kernels.md), [Weak equations and classical functions](weak-equations-and-classical-functions.md), and the compact approximation result in [When a kernel is smooth](when-a-kernel-is-smooth.md). Entry requirements are ordinary integration, Taylor’s formula, compact cutoffs and partitions of unity. Basic references are [Dyatlov 2026], for convolution, and [Melrose 2016] and [Schwartz 1952], for the kernel perspective.

## Which pairs can contribute to an output

All pairings are complex-linear. For a distribution on \(\mathbb R^n\), define translation by

\[
\langle\tau_pu,\phi\rangle
=\langle u,\phi(\,\cdot\,+p)\rangle.
\tag{1.1}
\]

For functions, \(\tau_pf(x)=f(x-p)\). Thus \(\tau_p\delta_0=\delta_p\).

Let \(F,G\subset\mathbb R^n\) be closed. Addition is **proper on the two supports** if, for every compact \(L\subset\mathbb R^n\), the set

\[
S_L=\{(s,t)\in F\times G:s+t\in L\}
\tag{1.2}
\]

is compact. Equivalently, for every \(R<\infty\) there is \(T<\infty\) such that

\[
s\in F,\ t\in G,\ |s+t|\le R
\quad\Longrightarrow\quad |s|,|t|\le T.
\tag{1.3}
\]

Indeed \(S_L\) is closed, so boundedness gives compactness. Condition (1.3) follows from compactness for a closed ball. If either support is compact, properness follows: \(t=s+t-s\) remains bounded when the output and \(s\) do.

Properness also makes \(F+G\) closed. If \(s_j+t_j\to x\), these outputs lie in one compact ball. A subsequence of \((s_j,t_j)\) converges in \(F\times G\), and its sum is \(x\).

**Theorem 1.1 (convolution by addition).** Suppose \(u,v\in\mathcal D'(\mathbb R^n)\), with supports contained in \(F,G\), and addition is proper on \(F\times G\). There is a canonical distribution \(u*v\) given by

\[
\langle u*v,\phi\rangle
=\langle u(s)\otimes v(t),\phi(s+t)\rangle,
\qquad\phi\in\mathcal D(\mathbb R^n).
\tag{1.4}
\]

The right side is the support-relative pairing. In particular,

\[
u*v=v*u,\qquad
\operatorname{supp}(u*v)\subset F+G.
\tag{1.5}
\]

If the factors have order at most \(r,s\), the result has order at most \(r+s\). Derivatives satisfy

\[
\partial^\alpha(u*v)
=(\partial^\alpha u)*v
=u*(\partial^\alpha v).
\tag{1.6}
\]

**Proof.** The support of \(u\otimes v\) is contained in \(F\times G\). The intersection of that set with the support of \(\phi(s+t)\) is contained in the compact set \(S_{\operatorname{supp}\phi}\). It is closed, hence compact. The support-relative test theorem therefore defines (1.4).

For all tests supported in a fixed compact \(L\), choose one smooth compact cutoff \(\chi(s,t)\) equal to one near \(S_L\). The right side becomes

\[
\langle u\otimes v,\chi(s,t)\phi(s+t)\rangle.
\tag{1.7}
\]

The tensor estimate on the compact support of \(\chi\) bounds this by a finite derivative seminorm of \(\phi\). If the factors have orders \(r,s\), the estimate differentiates the first variable at most \(r\) times and the second at most \(s\) times. The product and chain rules require at most \(r+s\) derivatives of \(\phi\). This proves continuity and the stated order bound.

Interchanging the two tensor factors and their variables leaves addition unchanged, proving commutativity. If \(\phi\) is supported outside \(F+G\), its pullback has support disjoint from \(F\times G\), so its pairing is zero. Since \(F+G\) is closed, this proves the support inclusion.

For derivatives, integration by parts in the first variable gives

\[
\begin{aligned}
\langle (\partial^\alpha u)*v,\phi\rangle
&=(-1)^{|\alpha|}
\langle u\otimes v,(\partial^\alpha\phi)(s+t)\rangle\\
&=\langle\partial^\alpha(u*v),\phi\rangle.
\end{aligned}
\]

To justify this with compact tests, choose \(\chi\) equal to one on a neighborhood of the relevant support intersections before differentiating. Every term containing a derivative of \(\chi\) vanishes near the tensor support wherever the pulled-back test is nonzero. Its distributional pairing is zero. Differentiating in the second variable proves the other equality. \(\square\)

Consequently

\[
\delta_p*u=\tau_pu,\qquad
\delta_0*u=u,\qquad
(\partial^\alpha\delta_0)*u=\partial^\alpha u.
\tag{1.8}
\]

For a constant-coefficient differential operator \(P\), the same calculation gives

\[
Pu=(P\delta_0)*u,\qquad
P(u*v)=(Pu)*v=u*(Pv).
\tag{1.9}
\]

All convolutions in these identities obey the preceding support hypotheses.

Sometimes properness holds only over part of the output space. Let \(\Omega\) be the union of open balls \(B\) for which \(S_{\overline B}\) is compact. For each compact \(L\subset\Omega\), a finite ball cover shows that \(S_L\) is compact. Formula (1.4) then defines \(u*v\) on \(\Omega\), and the proof of Theorem 1.1 applies to tests there. The set \((F+G)\cap\Omega\) is relatively closed: a sequence of sums converging to a point of \(\Omega\) eventually lies in one of these balls and has a convergent sequence of contributing pairs. Thus

\[
\operatorname{supp}_\Omega(u*v)
\subset(F+G)\cap\Omega.
\tag{1.10}
\]

This \(\Omega\) is the largest open set over which addition on these supports is proper. Properness on any other open output region gives a compact preimage of the closure of a sufficiently small ball about each of its points.

## Smoothing and the exact derivative count

**Theorem 2.1 (a regular factor).** For \(u\in\mathcal D'(\mathbb R^n)\) and \(f\in C_c^\infty(\mathbb R^n)\), the convolution is the smooth function

\[
(u*f)(x)=\langle u(s),f(x-s)\rangle.
\tag{2.1}
\]

It satisfies

\[
\partial^\alpha(u*f)
=(\partial^\alpha u)*f=u*(\partial^\alpha f).
\tag{2.2}
\]

The map \(f\mapsto u*f\) is continuous from \(\mathcal D\) to \(C^\infty\). If \(u\) is compactly supported, (2.1) also defines a continuous map \(C^\infty\to C^\infty\); it maps \(\mathcal D\) continuously into \(\mathcal D\).

More generally, let \(j,k\ge0\) be integers. If \(u\) has order at most \(j\) and \(f\in C_c^{j+k}\), (2.1) defines a \(C^k\) function representing \(u*f\). The same conclusion holds for compactly supported \(u\) of order at most \(j\) and arbitrary \(f\in C^{j+k}\).

**Proof.** For \(x\) in a compact neighborhood \(L\), the tests \(f(x-\,\cdot\,)\) have common compact support in \(L-\operatorname{supp}f\). The parameter differentiation lemma gives smoothness and derivatives for smooth \(f\). If \(u\) is compactly supported, a fixed cutoff near its support gives the same argument for every smooth \(f\).

The function formula agrees with (1.4). Pair (2.1) against \(\phi(x)\), pass the integral through the distribution, and substitute \(t=x-s\). This gives

\[
\begin{aligned}
\int\phi(x)\langle u(s),f(x-s)\rangle\,dx
&=\left\langle u(s),\int\phi(s+t)f(t)\,dt\right\rangle.
\end{aligned}
\tag{2.3}
\]

The interchange follows by approximating the compact parameter integral by Riemann sums in the finite derivative seminorm controlling \(u\). One common cutoff supplies compact support in \(s\). The tensor theorem identifies the last expression with (1.4).

For the continuity assertions, fix the input support \(M\) and output compact set \(L\). A local order \(r\) of \(u\) on a compact neighborhood of \(L-M\) gives

\[
\max_{|\alpha|\le a}\sup_{x\in L}
|\partial^\alpha(u*f)(x)|
\le C_{L,M,a}\max_{|\beta|\le r+a}\sup|\partial^\beta f|.
\tag{2.4}
\]

This proves continuity on each input support space and hence on \(\mathcal D\). For compact \(u\), its support fixes the region needed for a \(C^\infty\) input. If the input is compact, (1.5) gives one compact output support for all inputs supported in \(M\), and (2.4) proves continuity into that support space.

For finite regularity, the canonical order-\(j\) pairing acts on compact \(C^j\) tests. Difference quotients of \(f(x-\,\cdot\,)\), including all derivatives in \(s\) through order \(j\), converge in \(C^j\) to the corresponding parameter derivatives whenever their total order is at most \(j+k\). Taylor’s formula and uniform continuity of the highest derivatives on compact sets justify the last derivative. This proves \(C^k\) regularity. Formula (2.3) is still justified in the \(C^j\) seminorm, and proves equality with the distribution convolution. For compact \(u\), insert the same fixed cutoff as above. \(\square\)

**Lemma 2.2 (Riemann sums with derivatives).** If \(f\in C_c^j(\mathbb R^n)\), \(g\in C_c^0(\mathbb R^n)\), then

\[
R_h(x)=h^n\sum_{m\in\mathbb Z^n}f(x-hm)g(hm)
\longrightarrow f*g(x)
\quad\text{in }C_c^j\text{ as }h\downarrow0.
\tag{2.5}
\]

All sums and the limit have support in the same compact set \(\operatorname{supp}f+\operatorname{supp}g\).

**Proof.** Each sum is finite. Differentiate it through order \(j\). For a multi-index \(\alpha\), compare its sum to the integral of \((\partial^\alpha f)(x-y)g(y)\) by partitioning \(y\)-space into cubes \(hm+[0,h]^n\). The difference on a cube is bounded by

\[
\begin{aligned}
&\|g\|_\infty\,
\omega_{\partial^\alpha f}(\sqrt n\,h)
+\|\partial^\alpha f\|_\infty\,
\omega_g(\sqrt n\,h),
\end{aligned}
\tag{2.6}
\]

where the functions are extended by zero and \(\omega\) denotes their global modulus of continuity. Both moduli tend to zero. Only cubes meeting a fixed compact neighborhood of \(\operatorname{supp}g\) contribute; their total volume is bounded independently of small \(h\). Thus the error tends uniformly to zero in \(x\), for every \(|\alpha|\le j\). A nonzero summand requires \(hm\in\operatorname{supp}g\) and \(x-hm\in\operatorname{supp}f\), proving the common support claim. The integral has the same support by continuity or directly from its integrand. \(\square\)

In particular a finite-order distribution may be passed through these Riemann sums. Convergence of scalar Riemann sums alone would not justify that step.

## Associativity and continuity need support control

**Theorem 3.1 (associativity).** Suppose addition of three closed supports \(F,G,H\) is proper: the triples \((s,t,r)\) with \(s+t+r\) in any compact set form a compact set. For distributions supported in these sets,

\[
(u*v)*w=u*(v*w),
\tag{3.1}
\]

and both sides equal the support-relative pairing of \(u\otimes v\otimes w\) with \(\phi(s+t+r)\). In particular this applies whenever at least two factors are compactly supported.

**Proof.** If any factor is zero the assertion is immediate. Otherwise the supports are nonempty. Fixing one point of \(H\) shows that \(F\times G\) sums properly, and similarly for the other pairs. Addition on \((F+G)\times H\) is also proper. To see this, take a sequence \((a_i,r_i)\) with bounded sums and choose \(a_i=s_i+t_i\), \(s_i\in F\), \(t_i\in G\). Triple properness gives a convergent subsequence of \((s_i,t_i,r_i)\), hence of \((a_i,r_i)\). Closedness of \(F+G\) completes the argument. The other association is allowed for the same reason.

For a fixed test \(\phi\), triple properness makes all contributing triples compact. Choose separate cutoffs equal to one near their three compact projections. Replacing each factor by its cut-off version does not change either iterated pairing: the difference has support in sums where at least one contributing coordinate lies outside its cutoff-one neighborhood, and none of those triples has sum in \(\operatorname{supp}\phi\). The support inclusion in Theorem 1.1 makes each such difference vanish on the test. All three cut-off factors are now compact. Their tensor product may act on every smooth function, and the two iterated formulas of the tensor theorem give the same pairing with \(\phi(s+t+r)\). They also equal the original support-relative triple pairing. \(\square\)

For \(u\in\mathcal D'\), \(f\in C_c^\infty\), \(g\in C_c^0\), this gives the smooth-function identity

\[
(u*f)*g=u*(f*g).
\tag{3.2}
\]

Here \(f*g\) is smooth and compactly supported: each derivative differentiates \(f\), with compact ordinary integration against \(g\). The left side is also smooth. Equality as distributions from Theorem 3.1 therefore gives pointwise equality. Lemma 2.2 supplies a direct justification of the ordinary-integral interchanges, even for merely continuous \(g\).

When one of \(u,v\) is compactly supported, convolution is also characterized uniquely by

\[
(u*v)*f=u*(v*f),\qquad f\in C_c^\infty.
\]

Existence of this identity follows from Theorem 3.1, since the smooth third factor is compact. If another distribution has the same identity, its difference from \(u*v\) has zero convolution with every compact smooth \(f\). Choose shrinking nonnegative normalized \(f\)’s. Theorem 5.2 below makes these convolutions tend to the difference itself, which must therefore be zero.

**Theorem 3.2 (continuity with fixed support sets).** Fix closed \(F,G\) on which addition is proper. Convolution is separately continuous for both the weak and strong distribution topologies when the variable factors have supports in the designated sets. If \(u_i\to u\) and \(v_i\to v\) are weakly convergent sequences with supports in \(F,G\), then \(u_i*v_i\to u*v\) weakly.

**Proof.** For one fixed test, choose the compact cutoff in (1.7). Tensoring is separately weakly continuous on a fixed compact product: its inner pairing gives a fixed compact test for the varying factor. Thus separate weak convergence transfers to (1.7).

For a bounded family of output tests, all supports lie in one compact \(L\), and all derivatives are uniformly bounded. The same cutoff works for the entire family. Pairing one tensor variable produces a bounded test family in the other variable, by its local finite-order bound. Consequently a strong-dual seminorm of the convolution is bounded by a strong-dual seminorm of the varying factor. This proves separate strong continuity. For two weakly convergent sequences, apply the joint sequential tensor theorem to the single compact test \(\chi(s,t)\phi(s+t)\). \(\square\)

The fixed supports are substantive. For example,

\[
\delta_i\to0,\qquad\delta_{-i}\to0
\quad\text{in }\mathcal D'(\mathbb R),
\qquad
\delta_i*\delta_{-i}=\delta_0.
\tag{3.3}
\]

Both input masses escape every compact set, but their sums stay at the origin. Theorem 3.2 therefore makes no assertion for this pair of sequences.

**Proposition 3.3 (a cone algebra).** Let \(C\subset\mathbb R^n\) be a nonempty closed convex cone containing no nonzero line. Distributions supported in \(C\) form a commutative associative algebra under convolution, with identity \(\delta_0\).

**Proof.** For any fixed number of factors, suppose sums stay bounded while the contributing coordinates do not. Divide all coordinates by their maximum norm, which tends to infinity, and pass to a subsequence. The limits lie in \(C\), at least one has norm one, and their sum is zero. The negative of that nonzero limit is the sum of the others, hence lies in \(C\) by convexity and the cone property. This gives a nonzero line in \(C\), a contradiction. Thus addition of any fixed number of such supports is proper. Also \(C+C\subset C\). Theorems 1.1 and 3.1 prove the algebra assertions, and (1.8) supplies the identity. \(\square\)

For example, \(H=\mathbf1_{[0,\infty)}\) on \(\mathbb R\) can be convolved with itself. Ordinary integration over \(0\le t\le x\) gives

\[
H*H=x_+.
\tag{3.4}
\]

Two opposite half-lines do not sum properly. For a nonnegative test \(\phi\) positive near zero, the positive-function pairing proposed for \(H(x)*H(-x)\) would contain

\[
\int_{s\ge0}\int_{t\le0}\phi(s+t)\,dt\,ds=\infty.
\tag{3.5}
\]

Indeed for every sufficiently large \(s\), an interval of \(t\)’s near \(-s\) contributes the same positive lower bound. Formula (1.4) does not define this convolution.

## Local smoothness can come from either factor

**Theorem 4.1 (finite regularity at an output point).** Let \(u\in\mathcal D'(\mathbb R^n)\) and \(v\in\mathcal E'(\mathbb R^n)\). Fix \(x_0\) and \(k\ge0\). Suppose that for every \(t\in\operatorname{supp}v\), there are an integer \(j\ge0\) and a neighborhood \(V\) of \(t\) such that either

\[
\begin{cases}
u|_{x_0-V}\in\mathcal D'^{\,j}(x_0-V),\\
v|_V\in C^{k+j}(V),
\end{cases}
\tag{4.1}
\]

or

\[
\begin{cases}
u|_{x_0-V}\in C^{k+j}(x_0-V),\\
v|_V\in\mathcal D'^{\,j}(V).
\end{cases}
\tag{4.2}
\]

Here \(\mathcal D'^{\,j}(W)\) means distributions of order at most \(j\) on \(W\), and membership in \(C^{k+j}(W)\) means representation by a function of that regularity. Then \(u*v\) is \(C^k\) near \(x_0\).

**Proof.** Choose finitely many smaller neighborhoods whose closures lie in the corresponding \(V\)’s and cover \(\operatorname{supp}v\). A smooth partition gives

\[
v=\sum_{\ell=1}^N v_\ell,\qquad
v_\ell=\chi_\ell v,
\qquad\operatorname{supp}\chi_\ell\Subset V_\ell.
\tag{4.3}
\]

Choose \(\eta_\ell\in C_c^\infty(x_0-V_\ell)\) equal to one near \(x_0-\operatorname{supp}\chi_\ell\). Compactness gives a neighborhood \(W\) of \(x_0\) such that, for every \(x\in W\),

\[
x-\operatorname{supp}\chi_\ell
\subset\{\eta_\ell=1\}^{\circ}.
\tag{4.4}
\]

The support inclusion proves \(u*v_\ell=(\eta_\ell u)*v_\ell\) on \(W\): the missing part of \(u\) cannot add to a point in \(W\) with a point of \(\operatorname{supp}v_\ell\). In case (4.1), the first cut-off factor has order at most \(j\) and the second is compact \(C^{k+j}\). In case (4.2), those roles are reversed. Theorem 2.1 makes each convolution \(C^k\). Their finite sum proves the assertion. \(\square\)

**Corollary 4.2 (singular support).** Under the same compact-support hypothesis,

\[
\operatorname{sing\,supp}(u*v)
\subset
\operatorname{sing\,supp}u+
\operatorname{sing\,supp}v.
\tag{4.5}
\]

**Proof.** The right side is closed, since the second singular support is compact. If \(x_0\) is outside it, each \(t\in\operatorname{supp}v\) has either a smooth neighborhood for \(v\), or a neighborhood on whose reflection about \(x_0\) the distribution \(u\) is smooth. The other factor has a finite local order after shrinking to relatively compact neighborhoods. The construction in Theorem 4.1 then works for every \(k\), with smooth factors allowing all needed derivatives. On a fixed resulting neighborhood the convolution is smooth. \(\square\)

The ordinary support inclusion can be strict even for two compact distributions. With

\[
u=\delta_0-2\delta_1,\qquad
v=\delta_0+2\delta_1,
\]

the two contributions at \(1\) cancel, and

\[
u*v=\delta_0-4\delta_2.
\tag{4.6}
\]

Thus the sum of the input supports is \(\{0,1,2\}\), whereas the output support is \(\{0,2\}\).

## Smoothing inside an arbitrary open set

**Proposition 5.1 (the local convolution domain).** Let \(X\subset\mathbb R^n\) be open, \(u\in\mathcal D'(X)\), and let \(v\in\mathcal E'(\mathbb R^n)\), with \(C=\operatorname{supp}v\). Then \(u*v\) is canonically defined on the open set

\[
X_C=\{x:x-C\subset X\}.
\tag{5.1}
\]

It depends only on \(u\) near \(x-C\) at an output point \(x\). Its derivative identities remain valid there, and

\[
\operatorname{supp}_{X_C}(u*v)
\subset
(\operatorname{supp}_Xu+C)\cap X_C.
\tag{5.2}
\]

For \(v=\rho\in C_c^\infty\), the formula is the smooth local function \(u_s(\rho(x-s))\).

**Proof.** For \(x\in X_C\), the compact set \(x-C\) lies inside \(X\). Its positive distance from \(X^c\) gives a neighborhood of \(x\) still in \(X_C\), so this set is open. For a compact output set \(L\subset X_C\), the set \(L-C\) is compact in \(X\). The tensor pairing in \(X\times\mathbb R^n\), with cutoffs near these sets, defines convolution exactly as in (1.4). Different cutoffs agree by the support-relative theorem. This also proves dependence on the local data and all derivative identities.

The right side of (5.2) is relatively closed. If \(f_i+c_i\to x\in X_C\), pass to a subsequence with \(c_i\to c\in C\). Then \(f_i\to x-c\in X\); relative closedness of \(\operatorname{supp}_Xu\) puts the limit in that support. Tests outside the sum have zero pairing, proving (5.2). The parameter lemma gives the smooth function assertion. \(\square\)

If \(v=0\), take \(C=\varnothing\), so \(X_C=\mathbb R^n\) and the result is zero everywhere.

**Theorem 5.2 (shrinking smooth averages).** Let \(\rho_\lambda\in C_c^\infty(\mathbb R^n)\) satisfy

\[
\int\rho_\lambda=1,\qquad
\sup_\lambda\|\rho_\lambda\|_{L^1}<\infty,
\qquad
\operatorname{supp}\rho_\lambda\subset\overline B(0,r_\lambda),
\quad r_\lambda\to0.
\tag{5.3}
\]

For \(u\in\mathcal D'(X)\), the local smooth functions \(u*\rho_\lambda\) converge to \(u\) strongly on tests in \(X\). In particular this holds for every family of nonnegative normalized profiles whose supports shrink to zero; no single fixed rescaled profile is required.

**Proof.** On each compact test support \(L\Subset X\), the convolution is defined for all sufficiently small radii. Put \(\check\rho(t)=\rho(-t)\). The tensor formula gives

\[
\langle u*\rho_\lambda,\phi\rangle
=\langle u,\check\rho_\lambda*\phi\rangle,
\qquad
(\check\rho_\lambda*\phi)(s)
=\int\rho_\lambda(t)\phi(s+t)\,dt.
\tag{5.4}
\]

The averaged tests and \(\phi\) have support in a fixed compact neighborhood of \(L\) inside \(X\). For each integer \(m\), the mean-value estimate and normalization imply

\[
\|\check\rho_\lambda*\phi-\phi\|_{C^m}
\le C_n r_\lambda\|\rho_\lambda\|_{L^1}
\|\phi\|_{C^{m+1}}.
\tag{5.5}
\]

Apply the local order estimate of \(u\) on that common compact neighborhood. For a bounded family of tests, \(\|\phi\|_{C^{m+1}}\) is uniformly bounded. The right side therefore tends to zero uniformly over the family. This is precisely strong distribution convergence. Nonnegative normalized profiles have \(L^1\) norm one. \(\square\)

**Corollary 5.3 (compact smooth approximation).** On every open \(X\), each \(u\in\mathcal D'(X)\) is the strong distribution limit of a sequence in \(C_c^\infty(X)\).

**Proof.** Choose increasing compact sets with interiors exhausting \(X\), and compact smooth cutoffs \(\chi_i\) equal to one on neighborhoods of the \(i\)-th sets. The compact distribution \(\chi_i u\) extends by zero to \(\mathbb R^n\). Choose a nonnegative smooth profile of integral one supported in the ball of radius \(\varepsilon_i\), where

\[
0<\varepsilon_i\le1/i,\qquad
\varepsilon_i<\tfrac12
\operatorname{dist}(\operatorname{supp}\chi_i,X^c).
\tag{5.6}
\]

When \(X=\mathbb R^n\), only the first bound is needed. Put \(f_i=(\chi_i u)*\rho_i\). The compact smoothing theorem gives \(f_i\in C_c^\infty(X)\). On a fixed compact test support, \(\chi_i\) eventually equals one on the entire small neighborhood needed in (5.4). Thus the pairing of \(f_i\) is exactly the local pairing of \(u*\rho_i\) there. Theorem 5.2 proves convergence uniformly on every bounded test family. The already proved compact approximation lemma in *When a kernel is smooth* is the fixed-compact version of this construction. \(\square\)

## Translation-invariant operators have one convolution kernel

**Theorem 6.1 (translation invariance).** Let

\[
A:\mathcal D(\mathbb R^n)\longrightarrow\mathcal D'(\mathbb R^n)
\tag{6.1}
\]

be a linear weakly continuous map satisfying \(A\tau_h=\tau_hA\) for every \(h\in\mathbb R^n\). There is a unique \(u\in\mathcal D'(\mathbb R^n)\) such that

\[
A\phi=u*\phi\qquad(\phi\in\mathcal D).
\tag{6.2}
\]

In particular every output is smooth, and \(A\) is continuous into \(C^\infty\).

The conclusion also applies to a linear map \(A:\mathcal D\to C^0\) which commutes with translations and sends every sequence tending to zero in \(\mathcal D\) to a sequence tending to zero uniformly on compact output sets.

**Proof.** The kernel theorem gives a unique \(K\in\mathcal D'(\mathbb R^n_x\times\mathbb R^n_y)\) with

\[
\langle A\phi,\psi\rangle
=\langle K,\psi(x)\phi(y)\rangle.
\tag{6.3}
\]

Commutation with translations gives

\[
\begin{aligned}
\langle K,\psi(x-h)\phi(y-h)\rangle
&=\langle A\tau_h\phi,\tau_h\psi\rangle\\
&=\langle\tau_hA\phi,\tau_h\psi\rangle
=\langle A\phi,\psi\rangle.
\end{aligned}
\tag{6.4}
\]

Density of product tests transfers this to every test on the product. Change coordinates to \(s=x-y\), \(r=y\); the linear change has absolute determinant one. Define the transformed distribution by

\[
\langle J,H(s,r)\rangle
=\langle K,H(x-y,y)\rangle.
\tag{6.5}
\]

Equation (6.4) says that \(J\) is invariant under translation in \(r\). Difference quotients of compact tests converge in their test topology, so \(\partial_{r_j}J=0\) for every coordinate. Repeated application of the constant-parameter theorem in *Weak equations and classical functions* gives a unique \(u\) with \(J=u(s)\otimes1(r)\). Applying this to (6.3) yields

\[
\langle A\phi,\psi\rangle
=\left\langle u(s),\int\psi(s+r)\phi(r)\,dr\right\rangle
=\langle u*\phi,\psi\rangle,
\tag{6.6}
\]

where the last equality is (2.3). Theorem 2.1 proves smoothness and continuity into \(C^\infty\). Uniqueness follows from uniqueness of \(K\) and of the constant-parameter factor. Alternatively, after smoothness has been proved, the kernel is recovered by

\[
\langle u,\theta\rangle
=(A\check\theta)(0).
\tag{6.7}
\]

For the final assertion, regard a continuous function output as a distribution. For each fixed output test \(\psi\), the scalar functional \(\phi\mapsto\int(A\phi)\psi\) is sequentially continuous on every fixed input support space. The distribution sequential criterion makes it a continuous test functional. Thus \(A\) is weakly continuous into \(\mathcal D'\), and the first part applies. \(\square\)

This proof explains the geometry of the kernel: translation moves \(x\) and \(y\) together, leaving only their difference. The theorem requires no polynomial growth of \(u\), and no Fourier transform.

## Exercises

**Exercise 1 (basic: cancellation and derivative signs).** Let \(u=\delta_0-2\delta_1\), \(v=\delta_0+2\delta_1\) on \(\mathbb R\). Compute \(u*v\), \(u*\delta'_0\), and their pairings on a test \(\phi\). Compare the support of \(u*v\) with the sum of the two input supports.

**Solution 1.** Bilinearity and \(\delta_a*\delta_b=\delta_{a+b}\) give \(u*v=\delta_0-4\delta_2\). Its pairing is \(\phi(0)-4\phi(2)\). Formula (1.8) gives \(u*\delta'_0=u'=\delta'_0-2\delta'_1\), whose pairing is \(-\phi'(0)+2\phi'(1)\). The input-support sum is \(\{0,1,2\}\), but the output support is \(\{0,2\}\); the two terms at \(1\) cancel exactly.

**Exercise 2 (intermediate: causal integration and a delayed jump).** Put \(H=\mathbf1_{[0,\infty)}\) and \(w=\delta'_0-\delta'_1\). Compute both \(H*(H*w)\) and \((H*H)*w\), and justify associativity for these noncompact factors.

**Solution 2.** Every support lies in \([0,\infty)\), a closed cone with no line, so Proposition 3.3 applies. Since \(H'=\delta_0\), one has \(H*w=\delta_0-\delta_1\). Hence \(H*(H*w)=H-\tau_1H\), the indicator of \([0,1]\) up to irrelevant endpoint values. On the other side, \(H*H=x_+\), and differentiation gives \((H*H)*w=(x_+)'-(x-1)_+'=H-\tau_1H\). Both pair with \(\phi\) as \(\int_0^1\phi(x)\,dx\).

**Exercise 3 (advanced: normalized shrinking kernels without a norm bound).** Choose an even nonnegative \(\rho\in C_c^\infty((-1,1))\) with integral one. Let \(\rho_\varepsilon(x)=\varepsilon^{-1}\rho(x/\varepsilon)\), and set \(q_\varepsilon=\rho_\varepsilon+\rho'_\varepsilon\). Show that \(q_\varepsilon\) has integral one and shrinking support, but converges to \(\delta_0+\delta'_0\). Explain why this does not contradict Theorem 5.2.

**Solution 3.** The derivative has integral zero, so the normalization and support assertions hold. For every test,

\[
\langle q_\varepsilon,\phi\rangle
=\int\rho(y)\phi(\varepsilon y)\,dy
-\int\rho(y)\phi'(\varepsilon y)\,dy
\longrightarrow\phi(0)-\phi'(0).
\]

This is the stated limit. The \(L^1\) norms cannot be uniformly bounded: the reverse triangle inequality gives

\[
\|q_\varepsilon\|_1
\ge\varepsilon^{-1}\|\rho'\|_1-1\longrightarrow\infty.
\]

Here \(\rho'\ne0\), because a nonzero compact smooth function of integral one is not constant. The missing hypothesis is exactly the uniform \(L^1\) bound. For \(u=\delta_0\), the convolutions are these kernels themselves, so normalization and shrinking support alone do not ensure convergence to \(u\).

**Exercise 4 (intermediate: a finite-regularity threshold).** Let \(f(x)=(1-x^2)^4\) for \(|x|<1\), and \(f(x)=0\) otherwise. Show that \(\delta''_0*f\) is \(C^1\) but is not \(C^2\). Identify the values of \(j,k\) in Theorem 2.1.

**Solution 4.** The fourth-order vanishing at each endpoint makes \(f\) compact \(C^3\). Its fourth derivative from inside tends to \(384\) at either endpoint, whereas outside it is zero; hence \(f\notin C^4\). Since \(\delta''_0\) has order two, the theorem with \(j=2\), \(k=1\) gives a \(C^1\) convolution equal to

\[
f''(x)=
\begin{cases}
(1-x^2)^2(56x^2-8),&|x|<1,\\
0,&|x|\ge1.
\end{cases}
\]

Near either endpoint the interior expression vanishes to order two, with coefficient \(192\) in the inward distance squared. Its second derivative has interior limit \(384\) and exterior value zero. Thus this convolution is not \(C^2\). The threshold \(C^{j+k}=C^3\) is attained without a further derivative of regularity.

**Exercise 5 (basic: the output domain shifts).** Let \(X=(-2,2)\), let \(u\) be the restriction of \(\operatorname{pv}(1/x)\) to \(X\), and let \(v=\delta_1\). Find the local convolution domain in Proposition 5.1, its singular support there, and its test pairing.

**Solution 5.** The condition \(x-1\in(-2,2)\) gives \(X_C=(-1,3)\). Translation gives the restriction of \(\operatorname{pv}(1/(x-1))\) to this interval. Its only singular point is \(1\). For \(\phi\in C_c^\infty((-1,3))\), the function \(s\mapsto\phi(s+1)\) is compactly supported in \(X\), and

\[
\langle u*v,\phi\rangle
=\lim_{a\downarrow0}\int_{\substack{s\in(-2,2)\\|s|>a}}
\frac{\phi(s+1)}s\,ds.
\]

No values of \(u\) outside \(X\) are needed. Near \(x=1\), translation preserves the principal-value singularity; elsewhere the function \(1/(x-1)\) is smooth.

**Exercise 6 (intermediate: reflection does not commute with translation).** Consider \(A\phi(x)=\phi(-x)\). Verify that \(A\) is continuous on test functions but cannot be convolution with one distribution. Use both translation and formula (6.7).

**Solution 6.** Reflection preserves compactness and every derivative supremum, so it is continuous. But \(A\tau_h=\tau_{-h}A\), which differs from \(\tau_hA\) for a nonzero \(h\) and a test concentrated near one point. Therefore Theorem 6.1’s commutation hypothesis fails. If a convolution representation existed, (6.7) would give \(u(\theta)=\theta(0)\), so \(u=\delta_0\). Convolution with that distribution is the identity, whereas reflection sends a nonzero odd test to its negative. This is a contradiction.

**Exercise 7 (advanced: a geometric properness estimate).** In \(\mathbb R\times\mathbb R^d\), let \(C=\{(t,z):t\ge|z|\}\). Give a direct bound for every contributing coordinate when the sum of any fixed number of points of \(C\) lies in a ball of radius \(R\). Then explain the obstruction if a closed convex cone contains a nonzero line.

**Solution 7.** Each \(t_i\ge0\), and \(\sum_i t_i\le R\), so \(0\le t_i\le R\). Also \(|z_i|\le t_i\le R\). Every point therefore has Euclidean norm at most \(\sqrt2R\). Closedness gives compactness of the contributing tuples. If a cone contains \(\mathbb Re\), with \(|e|=1\), then pairs \((me,-me)\) have zero sum and unbounded coordinates. Addition is not proper. The positive locally finite distributions \(\sum_{m\ge0}\delta_{me}\) and \(\sum_{m\ge0}\delta_{-me}\) give infinitely many positive contributions at zero, so their proposed positive convolution is not locally finite. This demonstrates failure of the construction for that pair, without asserting failure for every pair supported in the cone.

**Exercise 8 (advanced: translation invariance and locality).** Assume \(A\) satisfies Theorem 6.1 and is local in the sense that \(\operatorname{supp}(A\phi)\subset\operatorname{supp}\phi\) for every test. Show that \(A\) is a finite constant-coefficient differential operator. Prove the converse.

**Solution 8.** Recover its convolution distribution by (6.7). If \(\theta\) is supported away from zero, so is \(\check\theta\). Locality and smoothness of the output imply \((A\check\theta)(0)=0\). Thus \(u\) has support in \(\{0\}\). The point-support theorem in [Jets, supported distributions and local operators](jets-supported-distributions-and-local-operators.md) gives a finite sum \(u=\sum_{|\alpha|\le m}c_\alpha\partial^\alpha\delta_0\). Equation (1.8) gives \(A\phi=\sum c_\alpha\partial^\alpha\phi\). Conversely any such operator is continuous, commutes with translations, and has output support contained in the input support, because differentiation vanishes wherever the original smooth function vanishes on a neighborhood.

## References

- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, September 28, 2026, Chapters 6 and 8. Smooth convolution, properly summing supports and singular support. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
- [Melrose 2016] Richard Melrose, *18.155 Lecture 15: Schwartz’s kernel theorem*, MIT, 2016. The kernel perspective used in the translation-invariance proof. [Open lecture](https://math.mit.edu/~rbm/18.155-F16/L15.pdf).
- [Schwartz 1952] Laurent Schwartz, *Théorie des noyaux*, Proceedings of the International Congress of Mathematicians, Cambridge, Massachusetts, 1950, volume I, American Mathematical Society, 1952. [Proceedings archive](https://www.mathunion.org/icm/proceedings).
