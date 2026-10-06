# Fixed observations, density weights and modular time

Which observations stay fixed? Which positive densities define weights? How does a density change the modular clock? These are three different questions. A matrix calculation distinguishes them immediately; the general proof then shows which finite domains, closed graphs and spectral corners each question requires.

The reference weight throughout the general argument is faithful, normal and semifinite on an arbitrary von Neumann algebra. The algebra and its Hilbert-space representation need not be separable or sigma-finite. Densities can be unbounded, can have a kernel, and need not be measurable for a trace. The modular formula belongs to the density's support corner.

Start with the [matrix calculation](#OA-MOD-CZ-12), then follow the finite-domain criterion, the construction of a weight, and the change of modular time. Four solved problems sit beside the result each tests. The final [synthesis](#OA-MOD-CZ-13) joins their conclusions. The mathematical sources are cited at the end.

## Three questions in a matrix algebra

Consider \(M_2(\mathbb C)\) and the faithful weight \(\varphi_d(x)=\operatorname{Tr}(dx)\), with \(d=\operatorname{diag}(2,5)\). Its GNS realization on Hilbert–Schmidt matrices sends \(x\) to \(xd^{1/2}\). The closed involution sends that vector to \(x^*d^{1/2}\); equivalently, on an arbitrary matrix \(\xi\), it is \(d^{-1/2}\xi^*d^{1/2}\). Its polar factors are \(J\xi=\xi^*\) and \(\Delta\xi=d\xi d^{-1}\). All domains are the whole finite-dimensional space, so this is a direct polar computation.

The modular flow and a finite-domain test are therefore

\[
 \begin{aligned}
 \sigma_t^{\varphi_d}(E_{ij})&=(d_i/d_j)^{it}E_{ij},\\
 \varphi_d(E_{12}E_{21})&=2,\\
 \varphi_d(E_{21}E_{12})&=5.
 \end{aligned}
 \tag{CZ.M1}
\]

Diagonal observations stay fixed. The observation \(E_{12}\) fails both fixedness and cyclicity against \(E_{21}\). In this model every matrix has a finite linear weight value; the first solved problem will show why this domain simplification fails for general weights.

Now choose the fixed positive density \(h=\operatorname{diag}(3,7)\). Its new weight has density \(hd=\operatorname{diag}(6,35)\). Repeating the same polar calculation changes the off-diagonal frequency from \(\log(2/5)\) to \(\log(6/35)\). The set of fixed observations is still diagonal, but the clock changes. With \(h_0=\operatorname{diag}(3,0)\), the new weight has density \(\operatorname{diag}(6,0)\) and support \(E_{11}\). It has a faithful modular theory on \(E_{11}ME_{11}\), not on all of \(M\).

These computations suggest three tests for the general argument. Fixedness should be detectable by cyclicity on the domain where the linear weight exists. Constructing the new weight should distinguish its support from boundedness of the density. Computing its clock should use a closed GNS graph first and remove invertibility by spectral corners afterwards.

## Locate the finite domain before testing an observation

The first question is fixedness. Before comparing \(\varphi(az)\) and \(\varphi(za)\), determine where these linear values exist. A finite-star GNS vector and an element with a finite linear weight value are different notions.

Fix a faithful normal semifinite weight \(\varphi\) on a von Neumann algebra \(M\). Write

\[
\mathfrak n=\{x\in M:\varphi(x^*x)<\infty\},\quad
\mathfrak a=\mathfrak n\cap\mathfrak n^*,\quad
\mathfrak m=\operatorname{span}\mathfrak m_+,
\qquad \mathfrak m_+=\{x\in M_+:\varphi(x)<\infty\}.
\tag{CZ.1}
\]

The weight has its usual linear extension to \(\mathfrak m\). The identities \(\mathfrak m=\operatorname{span}\{y^*x:x,y\in\mathfrak n\}\) and \(\mathfrak m\subseteq\mathfrak a\) are WG's finite-domain results. The latter follows first for \(x\in\mathfrak m_+\) from \(x^2\leq\|x\|x\), and then by linearity. Moreover \(\mathfrak m\) is spanned by products \(xy^*\) with \(x,y\in\mathfrak a\): use \(x=y=z^{1/2}\) for \(z\in\mathfrak m_+\).

Use the faithful normal GNS representation, write \(\Lambda=\Lambda_\varphi\), and set

\[
S=J\Delta^{1/2},\qquad \sigma_t=\sigma_t^\varphi,
\qquad \langle\Lambda(x),\Lambda(y)\rangle=\varphi(y^*x).
\tag{CZ.2}
\]

The first slot of every inner product is linear. WH and MF supply the full finite-star Hilbert algebra, its closed involution, the modular group and its GNS covariance. CX-03 supplies the following exact right-multiplier identity for an entire element \(a\):

\[
\Lambda(xa)=J\sigma_{-i/2}(a^*)J\Lambda(x),
\qquad x\in\mathfrak n.
\tag{CZ.3}
\]

It includes membership \(xa\in\mathfrak n\), not just an equality on a smaller analytic core. SK supplies spectral powers and their domains; QF and FC supply closed positive forms and their resolvent order; MA supplies Gaussian integration, bounded strips and scalar holomorphic uniqueness; KM supplies the existence and uniqueness of the modular KMS group.

Call \(a\in M\) a **two-sided multiplier of \(\mathfrak m\)** if \(a\mathfrak m\subseteq\mathfrak m\) and \(\mathfrak ma\subseteq\mathfrak m\). Then \(a^*\) is also such a multiplier. If \(x\in\mathfrak n\), the positive element

\[
(xa)^*(xa)=a^*(x^*x)a
\tag{CZ.4}
\]

belongs to \(\mathfrak m\), hence has finite weight. Thus right multiplication by either \(a\) or \(a^*\) preserves \(\mathfrak n\). Combining this with the left-ideal property and taking adjoints proves that \(\mathfrak a\) is stable under left and right multiplication by \(a,a^*\). This is the domain fact needed below. It does not assert that \(ax\in\mathfrak m\) whenever \(x\in\mathfrak a\).

## Create analytic tests without changing the real topology

We need analytic test elements to connect the finite-domain equality with the real modular orbit. Gaussian smoothing supplies them without imposing norm continuity on that orbit.

Let \(\alpha:\mathbb R\to\operatorname{Aut}(M)\) be a group for which \(t\mapsto\omega(\alpha_t(x))\) is continuous for every \(x\in M\) and \(\omega\in M_*\). An element is entire when its orbit has an \(M\)-valued entire extension, denoted \(\alpha_z(x)\). Weak-star holomorphy and norm holomorphy of this extension are equivalent: local scalar boundedness, uniform boundedness on the Banach predual, and the scalar Cauchy coefficients give a locally norm-convergent power series in \(M\), as proved in CX-03. This concerns holomorphy of the extended function; it does not impose norm continuity on all real orbits.

The entire elements form a unital *-algebra, and

\[
\alpha_z(xy)=\alpha_z(x)\alpha_z(y),\quad
\alpha_z\bigl(\alpha_w(x)\bigr)=\alpha_{z+w}(x),\quad
\alpha_z(x)^*=\alpha_{\bar z}(x^*).
\tag{CZ.5}
\]

For the product and adjoint, continue the real identities by scalar tests. For the group identity, first fix a real parameter and continue the other one, then continue the remaining parameter. The intermediate function is entire and agrees with the corresponding real orbit, so each intermediate value is itself an entire element.

There are uniformly bounded entire approximants to every \(x\in M\). For \(r>0\), define weak-star integrals

\[
x_r(z)=\sqrt{r/\pi}\int_{\mathbb R}e^{-r(t-z)^2}\alpha_t(x)\,dt.
\tag{CZ.6}
\]

The integrable kernel has norm \(e^{r(\operatorname{Im}z)^2}\), so this integral belongs to \((M_*)^*=M\) and satisfies
\(\|x_r(z)\|\leq e^{r(\operatorname{Im}z)^2}\|x\|\). Differentiating the kernel in \(L^1\), with uniform Gaussian bounds on compact subsets of \(\mathbb C\), proves norm holomorphy. Real translation identifies \(\alpha_s(x_r(0))=x_r(s)\). Thus \(x_r(0)\) is entire and has norm at most \(\|x\|\).

In fact \(x_r(0)\to x\) sigma-strongly*. First weak continuity of \(\alpha_t\) implies sigma-strong continuity of each orbit at zero: expand
\(\omega((\alpha_t(x)-x)^*(\alpha_t(x)-x))\) for \(\omega\in M_*^+\); all four terms converge by weak continuity and the automorphism identity. Apply the same argument to \(x^*\). Jensen's inequality for a Hilbert-space seminorm and the Gaussian approximate identity then give the asserted convergence of (CZ.6). Hence the entire algebra is sigma-weakly dense, with no sequential density assertion for the algebra itself.

### A real orbit that Gaussian smoothing must handle

The formula in each matrix block follows from the polar computation at the entry. The normal block-sum weight is evaluated by the supremum of finite block subsums, and its GNS construction is their Hilbert direct sum. Thus the following is a concrete real-orbit test available before the general density perturbation theorem; the later formula (CZ.40) agrees with that block computation.

**Real modular orbits need not be norm-continuous.** Let \(I\) be an arbitrary nonempty set and
\(M=\prod_{(i,n)\in I\times\mathbb N}M_2(\mathbb C)\). Give each block the density \(d_n=\operatorname{diag}(1,e^n)\), and sum the normal positive block functionals over all indices. The resulting weight is normal semifinite faithful. Formula (CZ.40), starting from the block-sum trace, yields \(\sigma_t(x)_{i,n}=d_n^{it}x_{i,n}d_n^{-it}\). For the bounded family \(a_{i,n}=E_{21}\),

\[
\sigma_t(a)_{i,n}=e^{int}E_{21}.
\tag{CZ.43}
\]

At \(t_n=\pi/n\), the norm difference is two. The orbit is still pointwise sigma-strongly* continuous. Its continuation \(e^{inz}E_{21}\) is bounded on the closed upper unit strip and weak-star continuous there, including its boundary; it is norm holomorphic in the interior. This illustrates why a closed-strip theorem for a von Neumann algebra cannot silently demand norm continuity of all boundary values.

## Keep the analytic tests in their full domains

Smoothing is useful only if the products in the calculation remain in their exact finite and graph domains. The following domain result supplies that missing connection.

For the modular group, an entire \(a\in M\) multiplies \(\mathfrak n\) on the right by (CZ.3); the left-ideal property handles the other side. Applying the same statements to \(a^*\) proves that \(\mathfrak a\) is an entire-algebra bimodule. Products \(xy^*\), \(x,y\in\mathfrak a\), then show that \(\mathfrak m\) is such a bimodule as well.

Let \(\mathcal T\subseteq\mathfrak a\) be the operator image of MF's maximal Tomita algebra. For \(x\in\mathcal T\), its modular orbit and its GNS orbit are entire, every complex translate belongs to \(\mathcal T\), and

\[
\Lambda(\sigma_z(x))=\Delta^{iz}\Lambda(x).
\tag{CZ.7}
\]

The space \(\Lambda(\mathcal T)\) is dense and is a common core for any finite collection of modular power graph norms. If \(a\) is entire and \(x\in\mathcal T\), both \(ax\) and \(xa\) belong to \(\mathcal T\). For the left product its entire GNS orbit is \(\sigma_z(a)\Delta^{iz}\Lambda(x)\). For the right product use (CZ.3) at every complex translate. Its local norm bounds follow from the local bounds on the entire operator factors and on the entire GNS vector. These formulas prove all the required graph-domain conditions, so \(\mathcal T\) is an ideal in the entire algebra.

For later computations we also need the half-power identity

\[
\Delta^{1/2}a\Lambda(x)
=\sigma_{-i/2}(a)\Delta^{1/2}\Lambda(x),
\qquad x\in\mathfrak a, a\text{ entire}.
\tag{CZ.8}
\]

Indeed \(z\mapsto\sigma_z(a)\Delta^{iz}\Lambda(x)\) extends the real orbit of \(a\Lambda(x)\) to the closed lower half strip. Each vector factor has the required boundedness on that strip; the operator factor is uniformly bounded on its horizontal lines by (CZ.5). The spectral strip criterion MA-09 gives membership in \(D(\Delta^{1/2})\) and the value (CZ.8). This also verifies the half-power domain without treating an unbounded operator product as automatically defined.

## Convert domain tests into strip boundary values

There are two directions to prove: a fixed observation gives cyclicity, and cyclicity forces a fixed observation. The two boundary calculations below are the tests for those directions.

The calculations in this item supply both directions of the centralizer criterion.

First let \(a\) be a two-sided multiplier of \(\mathfrak m\), and let \(x,y\in\mathcal T\). Define

\[
F(z)=\left\langle a\Delta^{-iz}\Lambda(x),
                        \Delta^{-i\bar z+1}\Lambda(y)\right\rangle.
\tag{CZ.9}
\]

This function is entire. On the closed upper unit strip it is bounded: real powers of \(\Delta\) appearing there range over \([0,1]\), while the real-time unitary factors have norm one. On \(\mathcal T\), the spectral norm on any compact real-exponent interval is bounded by the sum of the two endpoint norms. The two boundary values are

\[
F(t)=\varphi(\sigma_t(a)xy^*),\qquad
F(t+i)=\varphi(xy^*\sigma_t(a)).
\tag{CZ.10}
\]

To check domains, \(\sigma_t(a)\) is still a two-sided multiplier, because \(\sigma_t\) preserves \(\mathfrak m\). CZ-01 shows that \(\sigma_t(a)x\) and \(\sigma_t(a^*)y\) belong to \(\mathfrak a\). Moving the real unitary factors in (CZ.9) gives, on the lower edge,

\[
\begin{aligned}
F(t)&=\langle\sigma_t(a)\Lambda(x),\Delta\Lambda(y)\rangle\\
&=\langle\Delta^{1/2}\sigma_t(a)\Lambda(x),\Delta^{1/2}\Lambda(y)\rangle\\
&=\langle\Lambda(y^*),\Lambda(x^*\sigma_t(a^*))\rangle
=\varphi(\sigma_t(a)xy^*).
\end{aligned}
\tag{CZ.11}
\]

At \(t+i\), the analogous expression is
\(\langle\Delta\Lambda(x),\sigma_t(a^*)\Lambda(y)\rangle\). Splitting the half powers and applying \(S\) in reverse order gives the upper edge of (CZ.10). All linear weight values are on \(\mathfrak m\).

Second, let \(a\) be entire and \(z_0\in\mathfrak m\). Then

\[
G(z)=\varphi(\sigma_z(a)z_0)
\tag{CZ.12}
\]

is entire, bounded on the closed upper unit strip, and satisfies

\[
G(t+i)=\varphi(z_0\sigma_t(a)).
\tag{CZ.13}
\]

It suffices to treat \(z_0=xy^*\) with \(x,y\in\mathfrak a\). By (CZ.8),

\[
G(z)=\langle\sigma_{z-i/2}(a)\Delta^{1/2}\Lambda(x),
                                \Delta^{1/2}\Lambda(y)\rangle.
\tag{CZ.14}
\]

This proves holomorphy and the strip bound directly. At \(z=t+i\), move the first operator to the other slot, use
\(\sigma_{t+i/2}(a)^*=\sigma_{t-i/2}(a^*)\), and then (CZ.8). The result is
\(\langle S\sigma_t(a^*)\Lambda(y),S\Lambda(x)\rangle\), which is (CZ.13). Linear combinations prove the general case.

## Recognize exactly the fixed observations

The analytic tests now turn a domain-preserving cyclicity condition into a criterion for fixed observations.

Define the **centralizer** by

\[
N=M_\varphi=\{a\in M:\sigma_t(a)=a\text{ for all }t\in\mathbb R\}.
\tag{CZ.15}
\]

It is a von Neumann subalgebra: each fixed-point condition is sigma-weakly closed, and the automorphisms preserve multiplication, adjoints and the identity.

**Theorem.** An element \(a\in M\) belongs to \(N\) if and only if it is a two-sided multiplier of \(\mathfrak m\) and

\[
\varphi(az)=\varphi(za)\qquad(z\in\mathfrak m).
\tag{CZ.16}
\]

**Proof.** If \(a\in N\), its constant orbit is entire, so CZ-03 gives the multiplier condition. The function (CZ.12) is constant on the real axis. It is therefore constant on the plane, and its upper boundary (CZ.13) proves (CZ.16).

Conversely suppose the two conditions hold. For \(x,y\in\mathcal T\), form (CZ.9). Invariance of \(\varphi\) and the trace identity (CZ.16), applied to \(\sigma_{-t}(xy^*)\in\mathfrak m\), give \(F(t)=F(t+i)\). Thus the entire functions \(F(z+i)\) and \(F(z)\) agree on the real axis and agree everywhere. The strip bound and this period bound \(F\) on the whole plane. Cauchy's estimate makes its derivative zero, so it is constant. Formula (CZ.11) now yields

\[
\langle(\sigma_t(a)-a)\Lambda(x),\Delta\Lambda(y)\rangle=0.
\tag{CZ.17}
\]

The two test spaces are dense: \(\Lambda(\mathcal T)\) is dense and \(\Delta\Lambda(\mathcal T)=\Lambda(\mathcal T)\) by complex-time invariance. The bounded operator \(\sigma_t(a)-a\) vanishes. This holds for every real \(t\), proving the theorem. \(\square\)

For \(a\in N\), (CZ.3) becomes \(\Lambda(xa)=Ja^*J\Lambda(x)\). In particular, if \(u\in\mathcal U(N)\), then

\[
\varphi(u^*xu)=\varphi(x),\qquad x\in M_+.
\tag{CZ.18}
\]

For finite \(\varphi(x)\), this is the norm identity for \(\Lambda(x^{1/2}u)\). If one side is finite, applying the finite identity with \(u\) or \(u^*\) shows the other side is finite and equal. Thus (CZ.18) includes infinite values.

### Test the finite domain

**Problem 1: the wrong finite domain.** On \(L^\infty(0,\infty)\), let \(\varphi\) be Lebesgue integration. Find a bounded analytic finite-star element which has no finite linear weight value. Explain why CZ-01 still supplies every domain needed in (CZ.11).

**Solution.** Take \(f(s)=(1+s)^{-3/4}\). Then \(f\in L^2\cap L^\infty\) but \(f\notin L^1\); hence \(f\in\mathfrak a\setminus\mathfrak m\). The modular flow of a trace is the identity, so its orbit and GNS orbit are entire. Even the multiplier \(a=1\) does not make \(af\) belong to \(\mathfrak m\). In (CZ.11), however, the vector \(\Lambda(af)\) only needs membership in \(D(S)\), which is exactly the finite-star condition. For a general multiplier this follows from (CZ.4). The scalar product \(a x y^*\) does lie in \(\mathfrak m\), because \(xy^*\) does and \(a\) multiplies that domain. Thus no undefined linear weight value occurs.

## Build weights from a cone of bounded densities

The second question is the construction of a weight from a density. Begin with bounded positive densities in the centralizer. Additivity requires no commutation between two such densities; the matrix problem below tests that distinction.

For \(h\in N_+\), define on \(M_+\)

\[
\varphi_h(x)=\varphi(h^{1/2}xh^{1/2}).
\tag{CZ.24}
\]

This is a normal semifinite weight. Normality follows from normality of \(\varphi\). If \(x\in\mathfrak m_+\), then (CZ.3), applied to \(x^{1/2}h^{1/2}\), gives

\[
\varphi_h(x)\leq\|h\|\varphi(x).
\tag{CZ.25}
\]

Thus its finite positive domain contains \(\mathfrak m_+\), which is sigma-weakly dense in \(M_+\); equivalently its finite linear domain is sigma-weakly dense in \(M\). This proves semifiniteness. Inequality (CZ.25) holds on all \(M_+\): if \(h=0\), the constructed weight is zero; if \(h\ne0\) and \(\varphi(x)=\infty\), the right side is infinite. Here scalar multiplication of weights uses \(0\cdot\infty=0\).

The dependence on \(h\) is additive and positively homogeneous, including infinite values:

\[
\varphi_{h+k}=\varphi_h+\varphi_k,\qquad
\varphi_{c h}=c\varphi_h\quad(c\geq0),\qquad
h\leq k\Longrightarrow\varphi_h\leq\varphi_k.
\tag{CZ.26}
\]

We prove additivity carefully because the two densities need not commute. Put \(r=h+k\). The inequality \(h\leq r\) defines a contraction \(u\) by \(u r^{1/2}\xi=h^{1/2}\xi\) on \(\operatorname{ran}r^{1/2}\), with value zero on its orthogonal complement. Extend continuously. It commutes with \(N'\), hence belongs to \(N\). Define \(v\) in the same way for \(k\). Then

\[
h^{1/2}=u r^{1/2}=r^{1/2}u^*,\quad
k^{1/2}=v r^{1/2}=r^{1/2}v^*,\quad
u^*u+v^*v=s(r).
\tag{CZ.27}
\]

The last equality follows by testing on the dense range in the support and using \(h+k=r\); both sides vanish off that support.

For \(x\in M_+\), let \(y=r^{1/2}xr^{1/2}\). If \(\varphi(y)<\infty\), the multiplier property and cyclicity in CZ-05 give

\[
\begin{aligned}
\varphi_h(x)+\varphi_k(x)
&=\varphi(uyu^*)+\varphi(vyv^*)\\
&=\varphi((u^*u+v^*v)y)=\varphi(y).
\end{aligned}
\tag{CZ.28}
\]

Conversely, if both weights on the left are finite, the identity
\(r^{1/2}=h^{1/2}u+k^{1/2}v\) gives

\[
y\leq2u^*h^{1/2}xh^{1/2}u+2v^*k^{1/2}xk^{1/2}v.
\tag{CZ.29}
\]

Both right-hand terms have finite weight by the multiplier property. Hence \(\varphi(y)<\infty\), and (CZ.28) applies. If either term on the left is infinite, the first implication forces \(\varphi(y)=\infty\). This proves additivity in every case. Homogeneity is immediate, with the zero weight at \(c=0\). Apply additivity to \(k=h+(k-h)\) to get monotonicity.

If \(h_i\uparrow h\) is a bounded increasing net in \(N_+\), then \(\varphi_{h_i}(x)\uparrow\varphi_h(x)\). Monotonicity gives one inequality. Strong convergence of the square roots and lower semicontinuity of the normal weight give the other. The supremum is therefore the asserted value even when it is infinite.

### Test additivity with noncommuting densities

**Problem 2: commuting with the reference weight does not mean commuting with another density.** In \(M_2(\mathbb C)\) with the trace, put
\(h=\begin{pmatrix}2&0\\0&1\end{pmatrix}\) and
\(k=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}\).
Verify additivity (CZ.26) even though \(hk\ne kh\), and compute the centralizer of the weight with density \(h\).

**Solution.** The two products have unequal off-diagonal entries, so they do not commute. Every matrix centralizes the reference trace. Cyclicity of the finite-dimensional trace gives, for \(x\geq0\),
\(\operatorname{Tr}(h^{1/2}xh^{1/2})+\operatorname{Tr}(k^{1/2}xk^{1/2})=\operatorname{Tr}((h+k)x)=\operatorname{Tr}((h+k)^{1/2}x(h+k)^{1/2})\).
This checks additivity without incorrectly replacing \((h+k)^{1/2}\) by \(h^{1/2}+k^{1/2}\). The finite-dimensional GNS calculation at the start, with density \(h\), says the new centralizer consists of matrices commuting with all \(h^{it}\), equivalently with its two spectral projections. This computation uses that matrix model directly; the general formula (CZ.38) will recover it later. It is the diagonal algebra.

## Use resolvents to keep an unbounded density and its domain together

For an unbounded density, operator order must also remember a domain inclusion. Resolvents supply bounded tests for precisely that form order, before any supremum of weights is taken.

A positive self-adjoint operator \(h\) is affiliated with \(N\) when all its spectral projections belong to \(N\). It need not be bounded or measurable with respect to any trace. Put

\[
h_\varepsilon=h(1+\varepsilon h)^{-1},\qquad\varepsilon>0.
\tag{CZ.19}
\]

These are bounded positive elements of \(N\), with norm at most \(\varepsilon^{-1}\). They increase as \(\varepsilon\downarrow0\), and

\[
\sup_{\varepsilon>0}\langle h_\varepsilon\xi,\xi\rangle
=\begin{cases}\|h^{1/2}\xi\|^2,&\xi\in D(h^{1/2}),\\+\infty,&\xi\notin D(h^{1/2}).\end{cases}
\tag{CZ.20}
\]

This is scalar monotone convergence for the spectral measure of \(\xi\).

For two positive self-adjoint operators, **form order** \(h\leq k\) means

\[
D(k^{1/2})\subseteq D(h^{1/2}),\qquad
\|h^{1/2}\xi\|\leq\|k^{1/2}\xi\|\quad(\xi\in D(k^{1/2})).
\tag{CZ.21}
\]

It is equivalent to \(h_\varepsilon\leq k_\varepsilon\) for every \(\varepsilon>0\), and also to that inequality for one \(\varepsilon>0\).

This is an exact application of the existing form/resolvent theorem FC-06, which applies to arbitrary noncommuting nonnegative self-adjoint operators. The conversion of parameters and signs is

\[
h_\varepsilon
=\varepsilon^{-1}I-\varepsilon^{-2}(h+\varepsilon^{-1}I)^{-1}.
\tag{CZ.22}
\]

Consequently, for every chosen \(\varepsilon>0\),

\[
h_\varepsilon\leq k_\varepsilon
\quad\Longleftrightarrow\quad
(k+\varepsilon^{-1}I)^{-1}\leq(h+\varepsilon^{-1}I)^{-1}.
\tag{CZ.23}
\]

FC-06 identifies the right side for one positive parameter, for every positive parameter, and with the full domain assertion (CZ.21). Its proof uses the actual ranges of the bounded resolvent square roots, so it establishes the domain inclusion rather than merely a comparison on a previously chosen common subspace. Formula (CZ.20) also directly checks that order of every regularization yields the same domain and form inequality. Thus the regularization convention introduces no new prerequisite theorem.

## Construct affiliated density weights and determine their support

Construct the new weight by the preceding bounded tests. Its support and semifiniteness must be proved before asking for a modular group. The next two models distinguish a kernel from failure of trace measurability.

Let \(h\geq0\) be self-adjoint and affiliated with \(N\). Define

\[
\varphi_h(x)=\sup_{\varepsilon>0}\varphi_{h_\varepsilon}(x)
=\lim_{\varepsilon\downarrow0}\varphi(h_\varepsilon^{1/2}x h_\varepsilon^{1/2}),
\qquad x\in M_+.
\tag{CZ.30}
\]

This is a normal semifinite weight with support \(e=s(h)=1-1_{\{0\}}(h)\). In particular it is faithful exactly when \(\ker h=0\). Form order of affiliated positive operators implies order of their weights.

Indeed the bounded weights in (CZ.30) increase by CZ-06–07. Their supremum is additive and homogeneous: for two elements use the same sufficiently small \(\varepsilon\) to approach both suprema, and treat infinite values by arbitrary finite lower bounds. Suprema commute with increasing positive suprema in \(M\), proving normality. Form monotonicity follows from the regularization order.

For semifiniteness let \(e_n=1_{[0,n]}(h)\). For \(x\in\mathfrak m_+\), multiplication by \(e_n\in N\) gives \(e_nxe_n\in\mathfrak m_+\), and

\[
\varphi_h(e_nxe_n)
=\varphi_{he_n}(x)\leq n\varphi(x).
\tag{CZ.31}
\]

The equality follows by bounded monotone continuity in CZ-07, since \(h_\varepsilon e_n\uparrow he_n\). The positive finite elements in these corners are sigma-weakly dense in the corners; taking \(n\to\infty\), the union of the corners is sigma-strongly dense in \(M\). Thus the finite domain of \(\varphi_h\) is sigma-weakly dense.

Every regularized square root is supported on \(e\), so \(\varphi_h(x)=\varphi_h(exe)\). If this value is zero, faithfulness of \(\varphi\) implies \(x^{1/2}h_\varepsilon^{1/2}=0\) for every \(\varepsilon\). The range of each \(h_\varepsilon^{1/2}\) is dense in \(eH\), so \(x^{1/2}e=0\). Conversely that condition makes the value zero. This proves the support assertion, including \(h=0\). Restriction of \(\varphi_h\) to \(eMe\) is faithful and semifinite.

### Distinguish a zero density from a large density

**A density can have a genuine zero part.** Let \(I\) be any set and \(M=\ell^\infty(I)\), with \(\varphi(x)=\sum_{i\in I}x_i\), where the sum is the supremum of finite subsums. This is a faithful normal semifinite trace, and its centralizer is all of \(M\). For arbitrary finite numbers \(d_i\geq0\), multiplication by \(d\) is a densely defined positive affiliated operator on \(\ell^2(I)\). Its domain consists of \(\xi\) with \(\sum_i d_i^2|\xi_i|^2<\infty\). The constructed weight is

\[
\varphi_h(x)=\sum_{i\in I}d_i x_i,
\qquad s(\varphi_h)=1_{\{i:d_i>0\}}.
\tag{CZ.42}
\]

This follows by monotone convergence of finite subsums and the scalar regularizations. The supported modular group is trivial. The support condition, rather than a convention for \(0^{it}\), determines where its unitaries act.

**An affiliated density need not be trace-measurable.** On \(\ell^2(\mathbb N)\), take \(M=B(\ell^2)\), the usual semifinite trace, and \(he_n=n e_n\). Every finite truncation belongs to the trace's centralizer, but every high spectral tail of \(h\) has infinite trace. Thus the affiliated density is not trace-measurable in the finite-tail sense. Nevertheless (CZ.30) gives the normal semifinite faithful weight
\(\varphi_h(x)=\sum_n n\langle xe_n,e_n\rangle\), and (CZ.40) gives its modular group. Measurability is not an assumption in the theorem.

A general normal weight can have a separate finite-domain obstruction. The normal compression criterion, with its separately credited Matt Daws treatment, distinguishes that obstruction from the support computation here. Its normality hypothesis matters. The reference weight in this lesson is already semifinite, and the new affiliated density weight has just been proved semifinite; neither assertion follows merely by naming a support projection.

## Compute the new clock from a closed GNS graph

The third question is modular time. A bounded invertible density lets us compare closed GNS graphs through an invertible bounded map. This step computes the polar factors independently of the later spectral-corner argument.

Suppose \(h\in N_+\) is bounded and invertible in \(M\), and put \(\psi=\varphi_h\). The two weights have the same finite left ideal and finite linear domain. Indeed
\(\|h^{-1}\|^{-1}\varphi\leq\psi\leq\|h\|\varphi\) by CZ-07. Realize the GNS space of \(\psi\) on \(H_\varphi\) by

\[
\Lambda_\psi(x)=\Lambda(xh^{1/2})=R\Lambda(x),
\qquad R=Jh^{1/2}J.
\tag{CZ.34}
\]

This is an isometric GNS realization by (CZ.24), and has dense range because \(R\) is bounded invertible. It intertwines left multiplication because \(R\in M'\).

The operator \(h\) commutes with every \(\Delta^{it}\), since it is fixed by the modular action. To recover the unbounded domain from this identity, let \(\xi\in D(\Delta)\). The bounded lower-strip function \(z\mapsto h\Delta^{iz}\xi\) extends the real orbit of \(h\xi\). MA-09 therefore gives \(h\xi\in D(\Delta)\) and \(\Delta h\xi=h\Delta\xi\). Applying this to \((1+\Delta)^{-1}\eta\) proves commutation with the bounded resolvent. Polynomial approximation, followed by monotone spectral approximation, gives commutation with every spectral projection of that resolvent and hence of \(\Delta\). The same conclusion holds for every bounded spectral function of \(h\). Conjugating by \(J\) and using \(J\Delta J=\Delta^{-1}\) gives it for \(R\) as well. Also \(h\) and \(R\) commute as elements of \(M\) and \(M'\). On the full finite-star GNS core,

\[
S_\psi=R S R^{-1}
=J\bigl(h^{1/2}R^{-1}\Delta^{1/2}\bigr).
\tag{CZ.35}
\]

This is an equality of closed operators after closure. Conjugating a closed graph by the bounded invertible map \(R\) is closed, and \(R\Lambda(\mathfrak a)\) is its graph core.

Here is the precise commuting-product argument needed in this calculation. Put \(C=h^{1/2}R^{-1}\) and \(D=\Delta^{1/2}\). The bounded commuting positive factors make \(C\) positive and boundedly invertible; it and its inverse preserve \(D(D)\) and commute with \(D\). Thus \(P=CD\), on \(D(D)\), is closed and
\(P^*=DC\), whose domain is \(\{\eta:C\eta\in D(D)\}=D(D)\). Therefore \(P=P^*\). Its positivity follows from
\(\langle P\xi,\xi\rangle=\langle D C^{1/2}\xi,C^{1/2}\xi\rangle\geq0\); the square root also preserves the domain by spectral approximation.

For completeness its powers satisfy \(P^{it}=C^{it}D^{it}\). On a band \(1_{[1/m,m]}(D)H\), both operators are bounded positive and invertible. Approximate their spectral functions uniformly by positive step functions. The spectral projections commute, so the resulting finite orthogonal products reduce the power identity to the scalar identity for two positive numbers. The spectral ranges stay in a fixed compact subset of \((0,\infty)\), so norm-continuous functional calculus passes to the original bounded operators on that band. These bands reduce \(P\) and increase strongly to one. Passing strongly proves the identity on the whole space. The same step argument handles the bounded factors of \(C\). This uses only the single-operator spectral calculus and commuting projections, and identifies the full domain before taking powers. Polar uniqueness now yields

\[
J_\psi=J,\qquad
\Delta_\psi=h\,(JhJ)^{-1}\Delta,
\qquad D(\Delta_\psi^{1/2})=D(\Delta^{1/2}).
\tag{CZ.36}
\]

The product in the middle denotes the positive operator given by the commuting spectral calculus, with its full spectral domain. Its unitary powers are

\[
\Delta_\psi^{it}=h^{it}J h^{it}J\,\Delta^{it}.
\tag{CZ.37}
\]

The same sign on the two written powers is essential: conjugation by the antiunitary \(J\) conjugates the scalar spectral function. The middle factor belongs to \(M'\), so (CZ.37) proves

\[
\sigma_t^\psi(x)=h^{it}\sigma_t^\varphi(x)h^{-it},
\qquad x\in M.
\tag{CZ.38}
\]

There is also a full strip statement for the analytic finite test elements. For \(x\in\mathcal T\), \(y\in\mathfrak a\), put \(\beta_z(x)=h^{iz}\sigma_z(x)h^{-iz}\) and
\(F(z)=\psi(\beta_z(x)y)\). The entire finite GNS formulas in CZ-03 and bounded invertibility of \(h\) make this scalar function entire. It agrees on the real line with the lower boundary of the modular KMS function for \(\psi\); uniqueness of analytic continuation identifies it with that bounded strip function. Thus

\[
F(t)=\varphi(h\beta_t(x)y),\qquad
F(t+i)=\varphi(hy\beta_t(x)),
\tag{CZ.39}
\]

with all values finite. Here \(\psi(z)=\varphi(hz)\) on \(\mathfrak m\), by (CZ.16). For arbitrary finite-star \(x,y\), KM gives the corresponding bounded continuous strip function directly. This proves the analytic boundary assertion as well as the closed-operator computation.

The same entire function has the explicit spectral pairing

\[
F(z)=\left\langle h^{iz+1}\Delta^{iz+1}\Lambda(x),
                         S h^{-iz}\Lambda(y)\right\rangle.
\tag{CZ.39a}
\]

To verify it, first observe that for \(w\in\mathcal T\) and \(y\in\mathfrak a\),
\(\varphi(wy)=\langle\Delta\Lambda(w),\Lambda(y^*)\rangle\). Split the half powers and apply \(S\) to obtain this identity; the entire vector \(\Lambda(w)\) belongs to \(D(\Delta)\). Now \(w=h\beta_z(x)\) lies in \(\mathcal T\), and (CZ.3) gives
\(\Lambda(w)=h^{iz+1}(JhJ)^{-iz}\Delta^{iz}\Lambda(x)\).
Move the bounded commutant factor to the second slot. Since
\((JhJ)^{i\bar z}S\Lambda(y)=S h^{-iz}\Lambda(y)\), the result is (CZ.39a). This last equality follows from \(S=J\Delta^{1/2}\), spectral conjugation by \(J\), and commutation of \(h\) with \(\Delta\). Every term has its stated domain: \(\Lambda(x)\) is an entire vector, whereas \(\Lambda(y)\) is only required to lie in \(D(S)\); the bounded invertible powers of \(h\) preserve that domain. No analyticity of \(y\) has been assumed.

### Check the antiunitary sign on matrix units

**Problem 3: check the antiunitary sign.** Represent \(M_2(\mathbb C)\) on Hilbert–Schmidt matrices by left multiplication. Let the reference density be \(d=\operatorname{diag}(2,5)\) and perturb it by \(h=\operatorname{diag}(3,7)\). Verify (CZ.36–37) on every matrix unit.

**Solution.** The reference GNS vector of \(x\) is \(xd^{1/2}\), \(J\xi=\xi^*\), and \(\Delta\xi=d\xi d^{-1}\). The new density is \(hd=\operatorname{diag}(6,35)\), because \(h\) commutes with \(d\). The map (CZ.34) is right multiplication by \(h^{1/2}\), so \(\Delta_\psi\xi=(hd)\xi(hd)^{-1}\). On \(E_{ij}\) its eigenvalue is \(h_i d_i/(h_j d_j)\), exactly the product of the three factors in (CZ.36). Moreover \(J h^{it}J\) acts by right multiplication by \(h^{-it}\), not by \(h^{it}\). Thus (CZ.37) gives the unitary eigenvalue \((h_i d_i/(h_j d_j))^{it}\), verifying the sign and the commutant factor.

## Justify spectral restriction before using it

To remove the bounds on the density, first justify restriction to its spectral corners. This lemma uses invariance and the fixed-observable criterion; it does not assume the modular formula being proved.

We need to know which projections commute with the new weight before computing its modular group.

**Projection lemma.** Let \(\theta\) be a faithful normal semifinite weight and \(p\in M\) a projection. If \(\theta\) is invariant under conjugation by \(2p-1\), then \(p\in M_\theta\).

**Proof.** Positivity and additivity give, for every \(x\in M_+\),

\[
\theta(x)=\theta(pxp)+\theta((1-p)x(1-p)),
\tag{CZ.32}
\]

because the sum inside the right-hand weight is \((x+(2p-1)x(2p-1))/2\). Hence \(\theta(pxp)\leq\theta(x)\). For \(a\in\mathfrak n_\theta\), this proves \(ap\in\mathfrak n_\theta\). The left-ideal property and adjoints make \(\mathfrak a_\theta\) a \(p\)-bimodule, and products make \(\mathfrak m_\theta\) a \(p\)-bimodule. On this linear domain (CZ.32) extends by linearity, so the off-diagonal terms have zero weight. Consequently \(\theta(pz)=\theta(pzp)=\theta(zp)\) for \(z\in\mathfrak m_\theta\). CZ-05, applied to \(\theta\), gives the result. \(\square\)

Every spectral projection \(p\) of \(h\) commutes with the regularizations of \(h\). The unitary \(2p-1\) belongs to \(N\), so (CZ.18) shows that every weight in (CZ.30), and then their supremum, is invariant under its conjugation. Thus, for nonsingular \(h\), all these projections belong to \(M_{\varphi_h}\). For singular \(h\), the same argument applies to their supported projections in \(eMe\) and to the faithful supported weight there.

If \(p\in M_\theta\), the restriction \(\theta^p=\theta|_{pMp}\) is faithful normal semifinite. Semifiniteness follows from the sigma-weak density of \(p\mathfrak m_\theta p\), whose elements are finite by the multiplier property. Its modular group is

\[
\sigma_t^{\theta^p}(x)=\sigma_t^\theta(x),\qquad x\in pMp.
\tag{CZ.33}
\]

To prove this, restrict the existing modular automorphisms and their KMS strip functions to finite-star elements of the corner. Those elements belong to \(\mathfrak a_\theta\); all products and weight values agree. The restricted group preserves the weight and satisfies the complete KMS condition. KM uniqueness on \(pMp\) gives (CZ.33). No perturbation formula is used in this argument.

## Recover modular time on the support

Both ingredients are now available: the closed-graph computation inside each bounded invertible spectral corner, and a separate theorem identifying the two restricted modular groups. Combining them yields the supported formula at full generality.

**Theorem.** Let \(h\) be a positive self-adjoint operator affiliated with \(M_\varphi\), and let \(e=s(h)\). On \(eMe\), the faithful weight \(\psi=\varphi_h|_{eMe}\) has modular group

\[
\sigma_t^\psi(x)=h^{it}\sigma_t^\varphi(x)h^{-it},
\qquad x\in eMe.
\tag{CZ.40}
\]

The powers here are unitaries on \(eH\), defined by the spectral function \(\lambda^{it}\) on \((0,\infty)\). As elements of \(M\) they have initial and final projection \(e\). In particular if \(h\) is nonsingular, (CZ.40) holds on all of \(M\).

**Proof.** First restrict to \(eMe\). Since \(e\in M_\varphi\), CZ-09 proves that the restricted reference weight is faithful normal semifinite with the restricted modular group. We may therefore assume \(e=1\).

Let \(e_n=1_{[1/n,n]}(h)\). These projections increase strongly to one. They belong to both \(M_\varphi\) and \(M_\psi\) by CZ-09. On \(e_nMe_n\), the operator \(he_n\) is bounded and invertible relative to the identity \(e_n\), and (CZ.30) restricts exactly to the bounded perturbation by \(he_n\). Apply CZ-10 to that corner and then (CZ.33) to both weights. For \(x\in e_nMe_n\), this gives

\[
\sigma_t^\psi(x)=(he_n)^{it}\sigma_t^\varphi(x)(he_n)^{-it}
=h^{it}\sigma_t^\varphi(x)h^{-it}.
\tag{CZ.41}
\]

For an arbitrary \(x\in M\), \(e_nxe_n\to x\) sigma-strongly*, with uniformly bounded norms. Both automorphisms in (CZ.41) are normal and preserve this bounded-set topology. Passing to the limit proves (CZ.40). The sequence is a spectral approximation of one operator; it is not a countable decomposition of the algebra. \(\square\)

The right side forms a pointwise sigma-strongly* continuous group: the spectral unitaries are strongly continuous, \(h\) is fixed by \(\sigma^\varphi\), and the group law follows. Formula (CZ.40) does not define a modular group of a nonfaithful weight on the whole algebra; the supported algebra is the asserted domain.

### Test the corner argument at arbitrarily many coordinates

**Problem 4: unbounded lower and upper scales.** In (CZ.42), take \(I=K\times\mathbb Z\) with arbitrary \(K\) and \(d_{k,m}=e^m\). Prove faithfulness and semifiniteness, and identify a spectral corner approximation which does not assert countability of \(I\).

**Solution.** Every coefficient is positive, so the support is one and the weight is faithful. Finite coordinate supports have finite weight and their projections, directed by finite subsets of \(I\), increase to one; this proves semifiniteness directly. Independently the spectral projections \(e_n=1_{[1/n,n]}(h)\) select all \((k,m)\) with \(|m|\leq\log n\). They increase strongly to one because every fixed coordinate is eventually selected. Each such corner can still have arbitrary cardinality \(|K|\) and need not have finite weight at its identity. Their purpose is to bound the density above and below, not to turn the weight into a state.

## Synthesize the four problem solutions

The four tests can now be read as one construction.

1. The [finite-domain problem](#OA-MOD-CZ-05) gives an entire finite-star element with no finite linear weight value. The criterion tests products in the linear domain; it never replaces that domain by the finite-star algebra.
2. The [noncommuting-density problem](#OA-MOD-CZ-07) distinguishes belonging to the reference centralizer from commuting with a second density. The positive-cone construction covers both without assuming their square roots add.
3. The [matrix-unit sign problem](#OA-MOD-CZ-10) identifies the new modular eigenvalue and checks what antiunitary conjugation does to the written unitary power.
4. The [spectral-scale problem](#OA-MOD-CZ-11) separates bounding one affiliated operator above and below from imposing a countable decomposition or a finite weight on the corner identity.

For a cumulative check, take the product algebra from the real-orbit model and replace each strictly positive density by one with a zero second entry. Determine which part of that model still has modular time. Each block weight is then supported on its first diagonal projection; their product support gives the faithful support corner. That corner is abelian, so the supported modular group is trivial. The original off-diagonal observation lies outside it. Its former noncontinuous norm orbit therefore cannot be used as an orbit of the supported weight. This conclusion uses the support theorem, not a definition of \(0^{it}\).

## Connections beyond a centralizing density

Together these arguments give the full two-sided finite-domain centralizer criterion, bounded additive density changes, normal semifinite weights for arbitrary positive affiliated densities, exact kernel supports, spectral-corner restriction, and the modular formula on the supported algebra. The analytic coefficient lemmas and the bounded invertible GNS polar factors include their graph domains. No trace-measurability or strict-semifiniteness assumption has been added.

Further questions requiring their own arguments include: characterizing all modular-invariant weights as affiliated centralizer perturbations; full closed-strip right-multiplier domains; equivalence of strict semifiniteness with invariant-state separation and weak compactness of predual orbits; the KMS-state simplex and disjointness results, including the correct measure statement for a nonmetrizable state space; general noncommuting perturbations; and the later centralizer and spectral-order callbacks. These statements are not consequences of the centralizing-density construction alone.

### Mathematical sources

Masamichi Takesaki, *Theory of Operator Algebras II*, VIII.2, gives the fixed-element criterion and the centralizer density perturbation theorem. The noncommuting bounded-density argument is already part of that treatment; the closed-graph calculation here supplies its full polar domains and the separate projection lemma supplies the corner restriction. The distinct normal-compression treatment linked above is credited to Matt Daws under its existing component licence. The new matrix entry, explanatory connections, relocated problem commentary and synthesis are OpenAI Codex contributions, Ultra, October 2026, CC0-1.0. Existing proof and component licences remain.

