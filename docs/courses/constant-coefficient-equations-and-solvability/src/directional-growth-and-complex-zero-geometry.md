# Directional growth and complex-zero geometry

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Different directions can have different derivative growth for the same smooth solution. For a constant-coefficient equation, the distinction is encoded by how far the complex zeros can extend in each direction while their imaginary parts stay bounded. We show that the optimal growth rates are rational, organize themselves into a finite flag of subspaces, and give sharp lower bounds on any estimate valid for every homogeneous solution.

Read [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md) for escape of complex zeros and the topology of homogeneous solutions. [Uniform interior estimates with distance weights](uniform-interior-estimates-with-distance-weights.md) supplies the matching upper estimates. We use the semialgebraic projection and one-variable growth results developed in [Symbols at infinity](symbols-at-infinity.md); Coste [Coste] gives the real algebraic background.

Throughout the main results, \(n\geq2\) and \(P\) is a nonconstant hypoelliptic polynomial with possibly complex coefficients. Put
\[
\begin{gathered}
\mathcal Z_P=\{\zeta\in\mathbb C^n:P(\zeta)=0\},
\\ d_P(\xi)=\operatorname{dist}(\xi,\mathcal Z_P).
\end{gathered}
\tag{1}
\]
We use \(D=-i\partial\). Zero directions, one-dimensional equations, and nonzero constant symbols are discussed explicitly below.

The complete-metric Baire theorem used in the universal lower estimate is [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html), Section 6; the complete Fréchet metric is its Section 14.1.

## Strip maxima and their optimal powers

For a nonzero real vector \(y\), define
\[
\begin{gathered}
\mathcal Z_P(t)=\{\zeta\in\mathcal Z_P:|\operatorname{Im}\zeta|\leq t\},
\\ M_y(t)=\sup_{\zeta\in\mathcal Z_P(t)}|y\cdot\zeta|,\quad t\geq0,
\end{gathered}
\tag{2}
\]
with supremum zero if the set is empty.

**Theorem 1.1.** There is a rational number \(\rho_P(y)\geq1\) such that
\[
M_y(t)\asymp t^{\rho_P(y)}
\quad\text{as }t\longrightarrow+\infty.
\tag{3}
\]
It is the smallest exponent in either of the equivalent bounds
\[
\begin{aligned}
|y\cdot\zeta|&\leq C(1+|\operatorname{Im}\zeta|)^\rho,
&&\zeta\in\mathcal Z_P,\\
|y\cdot\xi|&\leq C(1+d_P(\xi))^\rho,
&&\xi\in\mathbb R^n.
\end{aligned}
\tag{4}
\]
The optimal power itself satisfies both bounds.

**Proof.** Hypoellipticity says that complex zeros with real parts tending to infinity have imaginary parts tending to infinity. Therefore the closed set
\(\{\zeta\in\mathcal Z_P:|\operatorname{Im}\zeta|\leq t\}\)
is bounded for every fixed \(t\), and hence compact. Its supremum in (2) is a maximum whenever the set is nonempty.

Write the real and imaginary parts of \(P\) as real polynomials in the \(2n\) coordinates of \(\zeta\). The statement that a number is the maximum in (2), including the empty-set convention, is expressed using polynomial equalities, inequalities, and quantifiers. Semialgebraic projection thus makes \(M_y\) a semialgebraic function. Once it is positive and unbounded, one-variable Puiseux growth gives
\[
\begin{gathered}
M_y(t)=b\,t^\rho(1+o(1)),
\\ b>0,\quad\rho\in\mathbb Q.
\end{gathered}
\tag{5}
\]

We must establish this unboundedness and \(\rho\geq1\). Rotate real coordinates so that \(y=|y|e_1\). The polynomial must depend on \(\zeta_1\). Otherwise a zero in the remaining complex coordinates, together with arbitrary real \(\zeta_1\), would violate zero escape.

Let \(a(\eta)\) be the nonzero coefficient of its highest \(\zeta_1\) power, where \(\eta\) denotes the other \(n-1\) coordinates. There are real \(\eta_\ell\to\infty\) with \(a(\eta_\ell)\ne0\): a nonzero polynomial cannot vanish on the exterior of a real ball. Each nonconstant polynomial \(P(z,\eta_\ell)\) has a complex root \(z_\ell\). The zero
\((z_\ell,\eta_\ell)\) has only its first coordinate imaginary, and its real part has norm at least \(|\eta_\ell|\). Zero escape forces
\[
t_\ell=|\operatorname{Im}z_\ell|\longrightarrow\infty.
\]
At these points,
\[
M_y(t_\ell)\geq |y|\,|z_\ell|
\geq |y|\,t_\ell.
\tag{6}
\]
Consequently (5) exists and has \(\rho\geq1\). It implies (3), attains the upper exponent, and excludes every smaller exponent.

To compare the two bounds in (4), first suppose the real-frequency bound holds at \(\rho\geq1\). At a zero \(\zeta=\xi+i\eta\), \(d_P(\xi)\leq|\eta|\), so
\[
|y\cdot\zeta|
\leq C(1+|\eta|)^\rho+|y|\,|\eta|.
\]
The second term is absorbed because \(\rho\geq1\).

Conversely choose a nearest complex zero \(\zeta\) to a real \(\xi\). Such a point exists in the nonempty closed zero set. Then
\[
\begin{aligned}
|\operatorname{Im}\zeta|&\leq d_P(\xi),\\
|y\cdot\xi|
&\leq |y|d_P(\xi)+|y\cdot\zeta|\\
&\leq |y|d_P(\xi)+C(1+d_P(\xi))^\rho.
\end{aligned}
\]
Again the linear term is absorbed. Compact small strip sections enlarge only the constant. This proves all the assertions. \(\square\)

The same comparison proves equivalence in (4) for any prescribed \(\rho\geq1\), even for \(y=0\). We set \(\rho_P(0)=0\) when organizing the directions into subspaces.

## A universal derivative bound must have this growth

**Theorem 2.1.** Let \(x_0\) lie in a nonempty open \(X\), and let \(y\ne0\). Suppose a sequence of finite nonnegative numbers \(M_j\) has this property: for every distributional solution of \(P(D)u=0\) in \(X\), there is a solution-dependent constant \(C_u\) such that
\[
|(y\cdot D)^ju(x_0)|\leq C_u^j M_j,
\qquad j\geq1.
\tag{7}
\]
Then some \(c>0\) satisfies
\[
M_j\geq c^j j^{\rho_P(y)j}
\quad\text{for every }j\geq1.
\tag{8}
\]
In particular every \(M_j\) is positive.

**Proof.** Let \(N\) be the homogeneous solution space with the topology induced by \(L^2_{\mathrm{loc}}(X)\). It is a closed subspace: convergence in that topology implies distributional convergence, and \(P(D)\) is continuous on distributions. Thus \(N\) is Fréchet and complete. Hypoellipticity makes its solutions smooth, and the homogeneous topology equivalence makes every derivative evaluation continuous in this topology.

For each integer \(r\geq1\), let
\[
\begin{aligned}
F_r=\{u\in N:\;& |(y\cdot D)^ju(x_0)|\leq r^jM_j
\\ &\text{for every }j\geq1\}.
\end{aligned}
\tag{9}
\]
These sets are closed, convex, and balanced, and their union is \(N\). Baire's theorem gives one \(F_r\) with interior. Balance and convexity move that interior to zero: take a balanced neighborhood \(U\) with \(u_0+U\subset F_r\), reflect it to \(-u_0+U\subset F_r\), and take midpoints.

A basic zero neighborhood uses finitely many compact \(L^2\) seminorms. Their union can be enlarged to one compact \(K\subset X\), so for some \(\delta>0\),
\(\|u\|_{L^2(K)}<\delta\) implies \(u\in F_r\).
Scaling and passing to the limiting scale give
\[
|(y\cdot D)^ju(x_0)|
\leq \delta^{-1}r^jM_j\|u\|_{L^2(K)}.
\tag{10}
\]
If the seminorm is zero, apply the neighborhood inclusion to every scalar multiple; it gives the same inequality with a zero right side.

For every \(\zeta\in\mathcal Z_P\), use the homogeneous exponential
\[
u_\zeta(x)=e^{i(x-x_0)\cdot\zeta}.
\]
If \(A\) bounds \(|x-x_0|\) on \(K\), (10) yields
\[
|y\cdot\zeta|^j
\leq C r^jM_j e^{A|\operatorname{Im}\zeta|}.
\tag{11}
\]
Choose a maximizing zero in the strip of width \(t\). For all large \(t\), Theorem 1.1 gives
\[
M_j\geq C^{-1}(b/r)^j
t^{\rho_P(y)j}e^{-At}.
\tag{12}
\]
Take \(t=j\). After absorbing the fixed prefactor and the exponential into a smaller \(c\), this proves (8) for all sufficiently large \(j\).

There is a zero with \(y\cdot\zeta\ne0\), by (6). Its exponential has a nonzero derivative of every positive order in that direction, so (7) forces every \(M_j>0\). Shrink \(c\) once more to include the finitely many initial orders. \(\square\)

The hypothesis permits a different \(C_u\) for each solution. Baire's theorem creates the common compact norm estimate (10); uniformity is obtained in the proof rather than assumed.

## The flag of directions

**Theorem 3.1.** The nonzero values of \(\rho_P\) form a finite increasing sequence of rational numbers
\[
1\leq r_1<\cdots<r_k,\qquad k\leq n.
\]
There is a strictly increasing flag
\[
\{0\}=G_0\subsetneq G_1\subsetneq\cdots
\subsetneq G_k=\mathbb R^n
\tag{13}
\]
such that \(\rho_P(y)=r_\ell\) when \(G_\ell\) is the first member containing the nonzero vector \(y\).

**Proof.** The real-frequency bounds in (4) imply
\[
\rho_P(ay+bz)\leq
\max\{\rho_P(y),\rho_P(z)\},
\tag{14}
\]
and \(\rho_P(ay)=\rho_P(y)\) for \(a\ne0\). Thus every sublevel set
\(\{y:\rho_P(y)\leq r\}\), \(r\geq0\), is a linear subspace.

Whenever two increasing values are attained, the corresponding sublevel inclusion is strict: a vector with the later value lies outside the earlier space. Each strict inclusion increases dimension. More than \(n\) nonzero values would therefore give an impossible chain. Finiteness of the coordinate exponents makes some sublevel all of \(\mathbb R^n\). Theorem 1.1 supplies rationality and the lower bound one. Listing the attained values and their subspaces proves (13). \(\square\)

Choose an orthonormal basis adapted to this flag, and write
\(\rho_j=\rho_P(e_j)\) in nondecreasing order. Then
\[
\rho_P(y)=\max_{y_j\ne0}\rho_j
\quad(y\ne0).
\tag{15}
\]
Indeed the span of the basis vectors up to each successive block is exactly the corresponding flag subspace. Formula (15) refers to adapted coordinates; cancellations in an arbitrary basis need not display the flag this way.

**Theorem 3.2.** Equally strong hypoelliptic polynomials have the same function \(\rho_P\) and the same flag.

**Proof.** [Weighted interior estimates and operator strength](weighted-interior-estimates-and-strength.md), Theorem 5.1, proves
\[
1+d_P(\xi)\asymp1+d_Q(\xi)
\quad(\xi\in\mathbb R^n)
\tag{16}
\]
for equally strong hypoelliptic \(P,Q\). Hence their real-frequency bounds in (4) hold at precisely the same exponents in every direction. The smallest exponents and all their sublevels coincide. \(\square\)

## Exact exponents for semielliptic symbols

Let \(P\) be semielliptic with positive integer weights \(m_1,\ldots,m_n\), as in [Algebraic families of hypoelliptic operators](algebraic-families-of-hypoelliptic-operators.md). Its anisotropic principal part \(P^\circ\) is nonzero at every nonzero real point. Put \(m=\max_jm_j\), which is also the ordinary degree.

**Theorem 4.1.** In these coordinates,
\[
\begin{gathered}
\rho_P(e_j)=m/m_j,
\\ \rho_P(y)=\max_{y_j\ne0}m/m_j.
\end{gathered}
\tag{17}
\]
Thus they are already coordinates adapted to the flag, after sorting the weights.

**Proof.** Write \(R(\xi)=1+\sum_j|\xi_j|^{m_j}\). The semielliptic derivative estimates give
\[
\left|\frac{P^{(\alpha)}(\xi)}{P(\xi)}\right|
\leq C_\alpha R(\xi)^{-\sum_j\alpha_j/m_j}
\tag{18}
\]
at large real frequency. Since
\(\sum_j\alpha_j/m_j\geq|\alpha|/m\), the zero-distance comparison implies
\[
d_P(\xi)\geq cR(\xi)^{1/m}
\]
there. Consequently
\[
|\xi_j|\leq C(1+d_P(\xi))^{m/m_j}.
\tag{19}
\]
This proves the coordinate upper bounds.

For the matching lower bound, suppose \(m_j<m\), and choose \(k\) with \(m_k=m\). Consider the one-variable polynomials
\[
q_T(z)=T^{-1}P(T^{1/m_j}e_j+T^{1/m}ze_k).
\tag{20}
\]
As \(T\to\infty\), their coefficients converge to
\(q_\infty(z)=P^\circ(e_j+ze_k)\). Its constant term is \(P^\circ(e_j)\ne0\), and its degree-\(m\) coefficient is \(P^\circ(e_k)\ne0\). It is therefore nonconstant. Choose a disk containing one of its roots whose boundary is zero-free. Rouché's theorem gives a root \(z_T\) in that fixed disk for every large \(T\).

The corresponding zero \(\zeta_T\) of \(P\) has real \(j\)-coordinate \(T^{1/m_j}\), \(k\)-coordinate \(z_TT^{1/m}\), and all other coordinates zero. Thus
\[
|\operatorname{Im}\zeta_T|\leq CT^{1/m}.
\]
Any strip bound for \(e_j\) would imply
\[
T^{1/m_j}\leq C(1+T^{1/m})^\rho,
\]
so \(\rho\geq m/m_j\). If \(m_j=m\), Theorem 1.1 already gives the matching lower bound one.

For a general nonzero \(y\), choose an active index \(j\) with smallest \(m_j\). If \(m_j<m\), the same roots give
\[
y\cdot\zeta_T
=y_jT^{1/m_j}+y_kz_TT^{1/m}.
\]
The first term dominates the second. Hence the lower bound is \(m/m_j\), while (19) and the triangle inequality give the same upper bound. If all active weights equal \(m\), the general lower bound one completes the argument. \(\square\)

For the heat symbol \(P(\tau,\xi)=i\tau+\xi^2\), the weights are \(m_\tau=1\), \(m_\xi=2\). The time exponent is two and the space exponent is one. The complex zeros
\[
(\tau,\xi)=(-2r^2,r(1+i))
\tag{21}
\]
have imaginary norm \(|r|\) and time projection \(2r^2\), displaying the time lower bound directly. The PDE smooths both directions, but its sharp homogeneous derivative rates differ.

## Degenerate directions and one-dimensional equations

For \(y=0\), every positive directional derivative vanishes. There is no positive universal lower bound such as (8); our convention is \(\rho_P(0)=0\).

In one dimension the complex zero set of a nonconstant polynomial is finite. Its strip maximum is eventually constant and can even be identically zero. By contrast, for every nonzero real \(y\), the smallest real-distance exponent in (4) is one: distance to a finite zero set grows linearly at real infinity.

For example \(P(\xi)=\xi\) has only constant homogeneous solutions on an interval. All their positive derivatives vanish, and \(M_j=0\) satisfies (7). Thus the multidimensional positive lower-growth theorem cannot be extended to this example. General constant-coefficient ODE solutions are analytic and have at most exponential derivative growth on a fixed compact set, as proved in [Anisotropic derivative classes and analyticity](anisotropic-derivative-classes-and-analyticity.md).

A nonzero constant \(P\) has only the zero homogeneous solution in any dimension. It needs neither zero-set distance nor a sharp positive derivative-growth invariant.

## Exercises with complete solutions

**Exercise 1. Introductory: why a strip is compact.** Show that an unbounded sequence of complex zeros in a strip \(|\operatorname{Im}\zeta|\leq t\) violates hypoellipticity.

**Solution.** Bounded imaginary parts and unbounded \(|\zeta|\) force the real parts to be unbounded. Pass to a subsequence whose real norms tend to infinity. Zero escape requires its imaginary norms to tend to infinity, contradicting the fixed strip. The zero set and the strip are closed, so boundedness also proves compactness.

**Exercise 2. Introductory: the heat flag.** For \(P(\tau,\xi)=i\tau+\xi^2\), determine \(\rho_P(a,b)\) for all real \((a,b)\), and list the flag.

**Solution.** Theorem 4.1 gives exponents two and one. Thus \(\rho_P(a,b)=2\) if \(a\ne0\), equals one if \(a=0,b\ne0\), and equals zero at the zero vector. The flag is
\(\{0\}\subsetneq\{(0,b):b\in\mathbb R\}\subsetneq\mathbb R^2\),
with successive values one and two.

**Exercise 3. Intermediate: the Baire neighborhood.** Explain why convexity and balance move an interior point of \(F_r\) to zero, and why a vanishing compact seminorm causes no gap in (10).

**Solution.** Choose a balanced zero neighborhood \(U\) with \(u_0+U\subset F_r\). Balance gives \(-u_0+U\subset F_r\); midpoints of \(u_0+v\) and \(-u_0+v\) show \(U\subset F_r\). If \(\|u\|_{L^2(K)}=0\), every scalar multiple of \(u\) belongs to this neighborhood's seminorm ball. Its derivative evaluation is bounded by the same \(r^jM_j\), so scaling by arbitrarily large scalars forces that evaluation to be zero. This is exactly (10) with zero on the right.

**Exercise 4. Intermediate: a bound too small in one direction.** Suppose every local homogeneous heat solution satisfied at one fixed point
\(|D_t^ju|\leq C_u^j(j!)^s\). Prove \(s\geq2\).

**Solution.** The sharp lower theorem gives \((j!)^s\geq c^j j^{2j}\). If \(0\leq s<2\), the bound \(j!\leq j^j\) makes the left side at most \(j^{sj}\). This would require \(j^{2-s}\leq c^{-1}\) for every large \(j\), an impossibility. If \(s<0\), use \((j!)^s\leq1\) instead. Then \(1\geq c^j j^{2j}\), which also fails for all sufficiently large \(j\). Thus every real \(s<2\) is excluded.

**Exercise 5. Advanced: roots in the anisotropic slice.** Prove the nonzero constant and leading coefficients asserted after (20), and explain why Rouché's theorem does not require a simple root.

**Solution.** Setting \(z=0\) gives the pure \(j\)-axis principal value \(P^\circ(e_j)\), which is nonzero. A term of degree \(m\) in \(z\) must have \(k\)-power \(m_k=m\). That already consumes the entire anisotropic degree one, leaving no \(j\)-power. Its coefficient is the pure \(k\)-axis value \(P^\circ(e_k)\ne0\). Choose a boundary circle with no zeros of \(q_\infty\) and containing at least one zero, with multiplicity. Uniform convergence makes \(|q_T-q_\infty|<|q_\infty|\) on that circle. Rouché preserves the positive number of zeros counted with multiplicity, so at least one bounded root exists even when all enclosed roots are multiple.

**Exercise 6. Advanced: coordinates that hide the flag.** Suppose in adapted coordinates \(\rho(e_1)=1\), \(\rho(e_2)=2\). Let \(v_1=e_1+e_2\), \(v_2=e_2\). Show that the maximum of the active basis-vector exponents in this new basis can overestimate a direction.

**Solution.** Both \(v_1\) and \(v_2\) have exponent two. But \(e_1=v_1-v_2\) has exponent one. The new coordinates of \(e_1\) have two nonzero coefficients, so taking their maximum gives two. Their cancellation removes the component transverse to the first flag subspace. Formula (15) therefore requires an adapted basis.

## References

- **[Coste]** Michel Coste, *Real Algebraic Sets*, lecture notes, 2003, §1.1 and §1.5, for semialgebraic projection and one-variable growth. [ICTP notes](https://indico.ictp.it/event/a02455/session/9/contribution/6/material/0/0.pdf).
