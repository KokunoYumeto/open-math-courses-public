# Uniqueness in a slab with bounded support

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Polynomial factors determine whether a homogeneous solution can stay in a bounded part of a slab. Moving leading coefficients, branched roots at infinity and Fourier-sector vanishing give a full distributional uniqueness theorem.

Read [Primitive factors and moving polynomial roots](primitive-factors-and-moving-roots.md), [Choosing polynomial and exponential approximants](choosing-polynomial-and-exponential-approximants.md), [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md), [Fourier windows, sector growth and branched vanishing](fourier-windows-and-sector-vanishing.md), [Continuous functionals, test families and compact limits](continuous-functionals-and-test-families.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz inversion; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the integration estimates. [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies scalar calculus and cutoffs. [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html), Theorems 1.1–2.1, proves proper convolution and compact smoothing. Convex supports and convolution cancellation, Corollary 4.3, proves compact-support injectivity of nonzero polynomial differential operators.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs below use the linked prerequisite lessons and the stated planned results.

## Irreducible covers with a moving leading coefficient

Let \(w\in\mathbb C^\ell\), \(\ell\ge1\), and let
\[
\begin{gathered}
P(w,s)=\sum_{j=0}^{\mu}a_j(w)s^j,\\
\qquad
 \mu\ge1,\\
\qquad a=a_\mu\ne0,
\end{gathered}
\tag{1}
\]
be irreducible in \(\mathbb C[w,s]\). We specify the exceptional set rather than treating every fiber as a fixed-degree polynomial.

**Lemma 1.** There is a nonzero polynomial \(D(w)\) whose complement consists exactly of the parameters with full degree \(\mu\) and simple roots. The regular root cover
\[
 \mathcal V=\{(w,s):D(w)\ne0,\ P(w,s)=0\}
 \tag{2}
\]
is connected. A holomorphic function on this cover which vanishes on a nonempty open subset vanishes everywhere.

**Proof.** Over the field \(K=\mathbb C(w)\), Gauss's lemma makes \(P\) irreducible. Its derivative \(P_s\) has smaller degree, is nonzero in characteristic zero, and is coprime to \(P\). Consider the square linear map
\[
\begin{gathered}
S(w):(A,B)\longmapsto AP+BP_s,\\
\qquad
 \deg_s A<\mu-1,\\
\quad \deg_s B<\mu,
\end{gathered}
\tag{3}
\]
with target the polynomials of degree less than \(2\mu-1\). The first summand is zero when \(\mu=1\). In coefficient bases its entries are polynomials in \(w\). Over \(K\), \(AP+BP_s=0\) implies \(P\mid B\), then \(B=0\) by its degree bound, and finally \(A=0\). Thus \(\det S\) is a nonzero polynomial.

At a parameter with \(a\ne0\), the same reasoning shows that \(S\) is invertible when the scalar polynomials \(P,P_s\) are coprime. If they have a common root, evaluation at that root is a nonzero functional on the target annihilating the image, so \(S\) is singular. The scalar factorization theorem identifies this coprimality with simple roots. When \(a=0\) and \(\mu\ge2\), both terms in (3) have degree at most \(2\mu-3\); the coefficient of \(s^{2\mu-2}\) is missing and \(S\) is singular. For \(\mu=1\), its determinant is \(a\). Consequently
\[
 D=a\det S
 \tag{4}
\]
has exactly the required complement. Multiplying by \(a\) introduces no additional excluded parameter.

We reduce the varying leading coefficient to a monic polynomial without extending the escaping roots through \(a=0\). Set
\[
\begin{gathered}
R(w,y)\\
=a(w)^{\mu-1}P\bigl(w,y/a(w)\bigr)
       \\
=y^\mu+\sum_{j<\mu}a_j(w)a(w)^{\mu-1-j}y^j.
\end{gathered}
\tag{5}
\]
This is a polynomial, is monic, and is irreducible over \(K\): the change \(s=y/a\) and multiplication by a nonzero field element preserve irreducibility. It is primitive in \(\mathbb C[w][y]\), so Gauss's lemma gives irreducibility in \(\mathbb C[w,y]\). Over \(U=\{D\ne0\}\), the change \(y=a(w)s\) is a holomorphic isomorphism of the two root covers, and all roots of \(R\) are simple.

The base \(U\) is path connected. If \(w_0,w_1\in U\), the polynomial \(D(w_0+z(w_1-w_0))\) is not identically zero, since it is nonzero at \(z=0\). Its finitely many zeros in the complex \(z\)-plane can be avoided by a polygonal path from 0 to 1. This supplies a path in \(U\); equal endpoints need no path construction.

Simple-root charts continue each root along every compact base path. Indeed, roots of a monic polynomial \(y^\mu+\sum_{j<\mu}b_jy^j\) satisfy
\[
 |y|\le 1+\max_{j<\mu}|b_j|.
 \tag{6}
\]
For if \(|y|>1+\max|b_j|\), the geometric sum gives
\(\sum_{j<\mu}|b_jy^j|<|y|^\mu\), contradicting the equation. On a compact path these bounds are uniform. At a limit point, compactness gives a limiting root, which remains simple on \(U\) and has a unique local chart. This rules out finite-time failure of continuation. Subdivision into finitely many charts gives uniqueness of path lifting.

Fix one base point. Loops based there permute its finite root fiber. Suppose an orbit \(O\) is proper and nonempty. Continue this subset to every point of \(U\). The subset is independent of the chosen path, because two choices differ by a loop and the orbit is loop invariant. The coefficients of
\[
 R_O(w,y)=\prod_{\rho\in O(w)}(y-\rho)
 \tag{7}
\]
are therefore single-valued and holomorphic on \(U\). Near every excluded parameter, (6) bounds all the roots and hence these symmetric coefficients. The bounded-removal proof in Lemma 3.1 of [Choosing polynomial and exponential approximants](choosing-polynomial-and-exponential-approximants.md) extends them holomorphically across \(D=0\).

The polynomial coefficients of \(R\) and (6) also give global bounds \(C(1+|w|)^L\) for the extended coefficients of \(R_O\), for some finite \(L\). The polydisk Cauchy estimate makes every derivative of order greater than \(L\) at the origin zero: bound the derivative on a polydisk of radius \(r\) by a constant times \(r^{L-|\alpha|}\), then let \(r\) tend to infinity. Its Taylor series is consequently a polynomial. Apply the same argument to the complementary root subset. Their product equals \(R\) on \(U\), and polynomial identity makes it equal everywhere. Both factors have positive \(y\)-degree. This contradicts irreducibility.

The loop action is thus transitive. Path lifting in the connected base, followed by a loop if needed to select its endpoint root, joins any two points of the cover. This proves connectedness. Finally, each simple-root chart identifies the cover locally with an open subset of \(\mathbb C^\ell\). The holomorphic identity principle in these charts propagates vanishing along the finite chart chain of any path, proving the last assertion. \(\square\)

When there is no parameter variable, an irreducible polynomial in \(\mathbb C[s]\) is linear, so its root cover is a single point. This scalar endpoint requires no monodromy argument.

## A finite cover at infinity

Write \(P_m=F\) for the homogeneous part of total degree \(m\). In this section \(P\) need not be irreducible. Its variables are \((\zeta,s)\in\mathbb C^d\times\mathbb C\), \(d\ge1\).

**Lemma 2.** Suppose \(e\in\mathbb R^d\) satisfies \(F(e,0)\ne0\), and \(c_0\) is a root of \(F(c e,1)\). For every \(\eta\in\mathbb C^d\), there are an integer \(1\le p\le m!\), an exterior radius, and a holomorphic function \(t(w)\) on that exterior such that
\[
\begin{gathered}
P\bigl(t(w)e+\eta,w^p\bigr)=0,\\
\qquad
 t(w)=c_0w^p+O(|w|^{p-1})
\end{gathered}
\tag{8}
\]
uniformly for all arguments of \(w\). Repeated roots of the restricted polynomial are permitted.

**Proof.** Introduce the polynomial
\[
\begin{gathered}
G(v,z)\\
=z^mP\bigl(z^{-1}(v e+z\eta),z^{-1}\bigr)
       \\
=\sum_{j=0}^{m}z^{m-j}P_j(v e+z\eta,1).
\end{gathered}
\tag{9}
\]
The second expression defines it also at \(z=0\). Its degree in \(v\) is \(m\), with constant nonzero leading coefficient \(F(e,0)\), and \(G(v,0)=F(v e,1)\). Divide by this leading coefficient for the following monic root bounds.

Over \(\mathbb C(z)\), form the monic squarefree part
\[
 q(v,z)=G(v,z)/\gcd(G,G_v).
 \tag{10}
\]
Here the normalized monic \(G\) is understood; the gcd is monic. Its degree \(r\) is between 1 and \(m\). Its coefficients are rational functions of \(z\), and its discriminant is a nonzero rational function, since it is squarefree in characteristic zero. Choose a sufficiently small punctured disk so that none of their poles or nonzero discriminant zeros occurs there. At every point of this punctured disk the roots of \(q\) are exactly the distinct roots of \(G\). The monic bound (6), applied to \(G\), bounds all of them uniformly. The coefficients of \(q\), being elementary symmetric functions of these roots, are bounded too. The one-variable removable-point argument extends them holomorphically at zero. This does not assert that its discriminant is nonzero at zero.

Choose disjoint small circles around the distinct roots of \(G(v,0)\). On each circle, continuity of coefficients makes \(G(v,z)\) uniformly close to \(G(v,0)\). The persistent-cluster proof in Corollary 2.3 of [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md) shows that the number of \(G\)-roots inside, counted with multiplicity, is unchanged. No root crosses a circle for sufficiently small \(z\). In particular, the cluster around \(c_0\) is nonempty. Continuation of a \(q\)-root in this cluster remains in it.

For completeness, the finite-cover step uses only simple-root charts and a path argument. Put \(z=\exp h\) on the half-plane \(\operatorname{Re}h<\log\delta\). The simple roots of \(q\) lift along every path there: on compact paths the coefficients and roots are bounded, and the nonvanishing discriminant gives the limiting simple-root chart, as in Lemma 1. Endpoints of lifts are unchanged by a homotopy with fixed endpoints. To see this, the lift along a fixed path is covered by finitely many simple-root neighborhoods. Subdivide the path so that each segment lies in one such neighborhood. A sufficiently close path has its lift in the same successive charts, and its endpoint varies continuously. For a continuous homotopy on the compact square, repeat this construction in a neighborhood of each homotopy parameter and use a finite subdivision. Endpoints lie in a finite, discrete root fiber, so they are locally constant and hence constant. The half-plane is convex; straight-line homotopies make all paths with the same endpoints homotopic.

There are therefore \(r\) single-valued holomorphic root branches \(V_j(h)\) on this half-plane. The shift \(h\mapsto h+2\pi i\) permutes them. The permutation is the same throughout: at one point it determines the identification of simple-root germs, and uniqueness of continuation propagates that identification. Let \(p\) be its order. Then \(p\le r!\le m!\), and each branch is invariant under \(h\mapsto h+2\pi ip\).

Take a branch in the \(c_0\) cluster and set
\[
\begin{gathered}
v(u)=V(p\log u),\\
\qquad 0<|u|<\delta^{1/p}.
\end{gathered}
\tag{11}
\]
Changing the logarithm adds \(2\pi ip\), so this is single valued and holomorphic. It is bounded and extends across zero by the removable-point argument. Its value there is \(c_0\): any limiting root lies in the chosen cluster and satisfies \(G(v,0)=0\), and this cluster contains only \(c_0\) among the distinct roots at zero. Thus \(v(u)=c_0+O(|u|)\), uniformly in a small disk, by its convergent Taylor series.

Finally let \(t(w)=w^pv(1/w)\). In (9), take \(z=w^{-p}\) and \(v=v(1/w)\). Equations (10)–(11) give \(G(v,z)=0\), whence (8). The Taylor estimate gives the asserted remainder uniformly on the entire exterior domain. This proves the branch even when \(c_0=0\), when several roots coalesce at zero, or when the original restriction has repeated factors. \(\square\)

## Removing vertical components on a generic line

**Lemma 3.** Let \(P(\zeta,s)\) be irreducible and of positive \(s\)-degree. For each fixed nonzero vector \(e\), there is a nonzero polynomial \(E(\eta)\) such that, when \(E(\eta)\ne0\), the restricted polynomial
\[
 P_\eta(t,s)=P(\eta+t e,s)
 \tag{12}
\]
has no nonconstant factor depending only on \(t\). Equivalently, its coefficients as a polynomial in \(s\) never vanish simultaneously at any \(t\in\mathbb C\).

**Proof.** Adjoining an independent variable \(t\) preserves irreducibility of \(P\): its principal ideal is prime in the polynomial UFD, the quotient is a domain, and a polynomial ring over that quotient remains a domain. The change \(\eta\mapsto\eta+t e\) is a polynomial-ring automorphism, with inverse \(\eta\mapsto\eta-t e\). Thus (12), viewed with \(\eta,t,s\) all independent, is irreducible and has positive \(s\)-degree.

Write its coefficients as \(b_j(\eta,t)=a_j(\eta+t e)\). They have no nonunit common divisor in \(\mathbb C[\eta,t]\), since such a divisor would be a proper factor of the irreducible polynomial. They consequently have gcd 1 in \(K[t]\), \(K=\mathbb C(\eta)\). Indeed, a common nonconstant divisor there has a primitive representative of positive \(t\)-degree in \(\mathbb C[\eta][t]\); Gauss divisibility would make this representative divide every \(b_j\) in that polynomial ring, a contradiction.

The scalar Euclidean algorithm over \(K\), applied successively to the finitely many nonzero coefficients, gives a Bezout identity. Clear its finitely many denominators in \(\eta\) to obtain polynomials \(B_j\) and a nonzero \(E\) with
\[
 \sum_j B_j(\eta,t)a_j(\eta+t e)=E(\eta).
 \tag{13}
\]
If \(E(\eta)\ne0\), evaluation at any \(t\) rules out simultaneous vanishing. A nonconstant polynomial in \(t\) has a complex root; divisibility of every coefficient would force simultaneous vanishing there. Conversely, simultaneous vanishing at \(t_*\) makes \(t-t_*\) divide every coefficient. This proves both formulations. \(\square\)

The restriction can acquire such a factor at exceptional parameters even if \(P\) itself is irreducible. We do not assume that every restricted curve meets the line \(t=0\).

## Choosing coordinates without losing the slab

For a homogeneous nonzero polynomial \(F\), we use the following definition. It is hyperbolic with respect to a real vector \(N\) if \(F(N)\ne0\) and every root in \(\tau\) of \(F(\xi+\tau N)\) is real for every real \(\xi\). Multiplying \(F\) by a nonzero scalar or replacing \(N\) by a nonzero real multiple preserves this property.

**Lemma 4.** Suppose \(N\ne0\), \(n\ge2\), and the degree-\(m\) homogeneous polynomial \(F\), \(m\ge1\), is not hyperbolic with respect to \(N\). There is a real complementary frequency space to \(\mathbb RN\), with coordinates \(\zeta\in\mathbb R^{n-1}\), and an \(e\ne0\) in that space such that
\[
\begin{gathered}
F(e,0)\ne0,\\
\qquad F(c_0 e,1)=0,\\
\qquad
 c_0=0\ \text{or}\ \operatorname{Im}c_0\ne0.
\end{gathered}
\tag{14}
\]
Here the last frequency coordinate represents \(N\), and the spatial coordinate corresponding to it is exactly \(x\cdot N\).

**Proof.** A nonzero complex polynomial cannot vanish on a real open ball: fixing all but one real coordinate and applying the scalar polynomial identity, then successively varying the other coordinates, makes all its coefficients zero. Its real zero set therefore has empty interior. Choose a real \(r\) with \(F(r)\ne0\) and \(r\notin\mathbb RN\). The noncollinearity condition is an open, nonempty condition when \(n\ge2\). Choose a real complement \(H\) of \(\mathbb RN\) containing \(r\); then \(F|_H\) is not identically zero.

If \(F(N)=0\), take \(e=r\) and \(c_0=0\). The equations in (14) follow immediately.

If \(F(N)\ne0\), failure of hyperbolicity provides a real \(\xi\) and a nonreal root \(\sigma\) of \(F(\xi+\sigma N)\). Write \(\xi=\eta+\alpha N\) with \(\eta\in H\) and \(\alpha\in\mathbb R\). The root becomes \(\sigma+\alpha\), still nonreal. A small circle around that root, disjoint from the real axis and from the other distinct roots, retains at least one root when \(\eta\) is perturbed in \(H\): apply the persistent-cluster estimate to \(F(\eta+sN)\), whose leading coefficient \(F(N)\) is fixed and nonzero. This gives a real open neighborhood with a nonreal root. Within it choose \(\eta\) with \(F(\eta)\ne0\), using the empty-interior assertion for \(F|_H\). Set \(e=\eta\) and choose one of its nonreal roots \(\sigma\). It is nonzero. Homogeneity gives
\[
\begin{gathered}
F(\sigma^{-1}e+N)\\
=\sigma^{-m}F(e+\sigma N)=0.
\end{gathered}
\tag{15}
\]
Thus \(c_0=\sigma^{-1}\) is nonreal and satisfies (14).

To check the coordinate assertion, let \(B\) have a real basis of \(H\) as its first \(n-1\) columns and \(N\) as its last column. It is invertible. In physical coordinates \((y,t)=B^Tx\), one has \(t=x\cdot N\), and \(D_x=B D_{(y,t)}\). The transformed symbol is \(P(B(\zeta,s))\), exactly the frequency identification used above. Bounded sets remain bounded under this invertible linear map. Orthogonality of \(H\) is neither needed nor imposed. \(\square\)

An affine change \(t\mapsto4(t-(a+b)/2)/(b-a)\), for finite \(a<b\), puts the slab into \(-2<t<2\). It replaces the last frequency vector by the positive multiple \(4N/(b-a)\). The hyperbolicity condition is invariant under this change. We may apply Lemma 4 after it. Coordinate choices for different irreducible factors may differ; each preserves the same physical slab after its own normalization.

## The smooth uniqueness theorem

**Theorem 5.** Let \(P\ne0\) be a complex polynomial on \(\mathbb R^n\), \(N\in\mathbb R^n\), and \(a<b\). Suppose that the principal part of every nonconstant irreducible factor of \(P\) is not hyperbolic with respect to \(N\). On
\[
 X=\{x\in\mathbb R^n:a<x\cdot N<b\},
 \tag{16}
\]
a distribution \(u\) satisfying \(P(D)u=0\), \(D=-i\partial\), and having bounded relative support is zero. No global growth or finite global order of \(u\) is assumed.

We first prove the smooth irreducible case with \(N\ne0\), \(n\ge2\). The remaining cases are treated below.

**Proof for a smooth function and one irreducible factor.** Use Lemma 4 and the affine slab normalization. Write the transformed symbol again as \(P(\zeta,s)\), with principal part \(F\), total degree \(m\), and the vector \(e\) and root \(c_0\) in (14). Bounded support gives a fixed spatial ball \(\{|y|\le M\}\) containing the support at every \(-2<t<2\). Let \(U\) be its partial Fourier transform and put
\[
\begin{gathered}
Q(\zeta,s,\lambda)=\frac{P(\zeta,s)-P(\zeta,\lambda)}{s-\lambda},
 \\
\qquad W(\zeta,s,t)=Q(\zeta,s,D_t)U(\zeta,t).
\end{gathered}
\tag{17}
\]
The fraction denotes a polynomial difference quotient, including at \(s=\lambda\). Lemmas A and B of [Fourier windows, sector growth and branched vanishing](fourier-windows-and-sector-vanishing.md) give entire dependence on \(\zeta\) and the exact estimate
\[
\begin{gathered}
|W(\zeta,s,0)|\le
 C(1+|s|)^{m-1}
 \\
\exp\bigl(M|\operatorname{Im}\zeta|-|\operatorname{Im}s|\bigr)
 \\
\quad\text{when }P(\zeta,s)=0.
\end{gathered}
\tag{18}
\]
This uses times \(-1\) and \(1\) within the slab and retains the full complex norm, the original spatial radius, and the phase \(W(t)=e^{ist}W(0)\).

If \(P\) has \(s\)-degree zero, \(P(\zeta)U(\zeta,t)=0\). On the nonempty open set where \(P(\zeta)\ne0\) the transform is zero; the entire identity principle gives zero everywhere, and Schwartz inversion gives \(u=0\). Thus assume its \(s\)-degree \(\mu\) is positive.

Let \(D(\eta)\) be the polynomial from Lemma 1 and \(E(\eta)\) that from Lemma 3. Their product is nonzero, so \(\Omega=\{DE\ne0\}\) is nonempty and open. Fix \(\eta\in\Omega\). Lemma 2 supplies \(p\) and \(t(w)\) satisfying (8) with our nonreal or zero slope \(c_0\). Define
\[
 f(w)=W\bigl(\eta+t(w)e,w^p,0\bigr).
 \tag{19}
\]
It is holomorphic on an exterior domain. Estimate (18) is precisely the hypothesis of Proposition 3 of [Fourier windows, sector growth and branched vanishing](fourier-windows-and-sector-vanishing.md), with exponent \(a=m-1\). Hence \(f\) vanishes identically on that exterior domain. This conclusion uses its finite ray cover on all sheets, not just decay along a single ray.

We now propagate this zero to a root over \(\eta\), proving rather than assuming that the chosen branch reaches \(t=0\). Factor \(P_\eta(t,s)=P(\eta+t e,s)\) into irreducible polynomials \(H_i(t,s)\) over \(\mathbb C\). Lemma 3 makes every \(H_i\) have positive \(s\)-degree. Since \(D(\eta)\ne0\), \(P_\eta(0,s)\) has its full degree \(\mu\) and simple roots. Addition of \(s\)-degrees in the product shows that every \(H_i(0,s)\) has its full \(s\)-degree: none of their leading coefficients can vanish at zero. The simple roots of the product also make every factor's roots simple there, and exclude repeated factors.

The product of the finitely many holomorphic functions \(H_i(t(w),w^p)\) is zero on the connected exterior. A finite product of holomorphic functions on a connected domain can vanish identically only if one factor does: for a nonzero factor its zero set has empty interior, and the complement is open dense; finitely many such complements have nonempty intersection. Choose \(H\) with
\[
 H(t(w),w^p)=0\quad\text{identically}.
 \tag{20}
\]
The function \(t(w)\) is nonconstant. Otherwise (8) would make \(P_\eta(t_*,s)\) vanish for all \(s=w^p\) in an exterior open set, hence vanish as a scalar polynomial. All its coefficients at \(t_*\) would be zero, contrary to (13).

Apply Lemma 1 to \(H(t,s)\), with the one-dimensional parameter \(t\). Its regular-base polynomial \(D_H(t)\) satisfies \(D_H(0)\ne0\), by the full degree and simple roots just proved. The nonzero polynomial \(D_H\) cannot vanish identically on the values of the nonconstant holomorphic \(t(w)\): a continuous map from a connected domain into its finite zero set would be constant. Thus choose \(w_*\) with \(D_H(t(w_*))\ne0\). Near that point the root is a simple chart \(s=s(t)\), and differentiation of \(w^p=s(t(w))\) gives
\[
 p w^{p-1}=s'(t(w))t'(w).
 \tag{21}
\]
Since \(w_*\ne0\), \(t'(w_*)\ne0\). The one-variable inverse-function proof, which is the holomorphic implicit-function proof applied to \(t(w)-t_*\), gives an open \(t\)-neighborhood parametrized by \(w\). Therefore (19) says that the holomorphic function \(W(\eta+t e,s,0)\) vanishes on a nonempty open subset of the regular \(H\)-cover. Connectedness and the identity assertion in Lemma 1 extend this vanishing to its entire regular cover. In particular it vanishes at every root of \(H(0,s)\).

For this fixed \(\eta\), at least one root \(s\) of \(P(\eta,s)\) has \(W(\eta,s,0)=0\). We have proved this for every \(\eta\in\Omega\); we have not yet inferred that every root over each parameter vanishes.

Take a small connected ball in \(\Omega\) on which the \(\mu\) roots of \(P(\eta,s)\) have simple holomorphic labels \(s_1(\eta),\ldots,s_\mu(\eta)\). At every point at least one of the functions \(W(\eta,s_j(\eta),0)\) is zero, so
\[
 \prod_{j=1}^{\mu}W(\eta,s_j(\eta),0)=0
 \tag{22}
\]
on the ball. The same finite-product argument makes one factor identically zero on the ball. We thus obtain a nonempty open subset of the global regular \(P\)-cover on which \(W(\zeta,s,0)\) is zero. Lemma 1 now propagates its zero to the whole connected cover.

All roots over every \(\zeta\) with \(D(\zeta)\ne0\) consequently have zero \(W(\zeta,s,0)\). Lemma C of [Fourier windows, sector growth and branched vanishing](fourier-windows-and-sector-vanishing.md), with the full leading coefficient in its interpolation formula, gives \(U(\zeta,t)=0\) for all times. This set of parameters is dense: a nonzero polynomial has no complex open zero set. Continuity, or the entire identity principle, gives \(U=0\) also at all exceptional parameters, including those where the leading coefficient vanishes or the fiber is identically zero. For each real \(t\), \(u(\cdot,t)\) is smooth and compactly supported, hence Schwartz. Exact Schwartz inversion gives \(u=0\). \(\square\)

## Products, distributions and degenerate endpoints

**Completion of Theorem 5.** Unique factorization writes a nonconstant polynomial as
\[
 P=c\prod_{j=1}^{k}q_j^{\,e_j},\qquad
 c\ne0,\quad e_j\ge1,
 \tag{23}
\]
with nonconstant irreducible \(q_j\). For a smooth bounded-support solution, remove one factor at a time. If \(P=qR\), put \(v=R(D)u\). Derivatives do not enlarge relative support, so \(v\) is smooth and has bounded support in the same slab. Since \(q(D)v=0\), the irreducible case gives \(v=0\). Repeat for the remaining factors, including every repeated copy in (23). A final nonzero constant operator is injective. This proves the smooth theorem for \(P\).

Let \(u\) now be a distribution, with \(N\ne0\) and finite \(a<b\). Choose a smooth compactly supported approximate identity
\[
\begin{gathered}
\rho\in C_c^\infty(\mathbb R^n),\\
\quad
 \operatorname{supp}\rho\subset\{|x|\le1\},\\
\quad
 \int\rho=1,\\
\qquad
 \rho_\varepsilon(x)=\varepsilon^{-n}\rho(x/\varepsilon).
\end{gathered}
\tag{24}
\]
Its existence follows from the written cutoff construction and normalization by its positive integral. For
\[
\begin{gathered}
X_\varepsilon=
 \{x:a+\varepsilon|N|\\
<x\cdot N<b-\varepsilon|N|\}
\end{gathered}
\tag{25}
\]
and sufficiently small \(\varepsilon>0\), define
\[
 u_\varepsilon(x)=\langle u(z),\rho_\varepsilon(x-z)\rangle .
 \tag{26}
\]
The test support is compactly contained in \(X\) for each such \(x\). On every relatively compact part of \(X_\varepsilon\), all these tests have a common compact support in \(X\). The proper-convolution/smoothing proof in [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html) applies there after inserting a cutoff equal to one on that compact support. Its result is independent of the cutoff, and its local results agree on overlaps. Thus \(u_\varepsilon\) is smooth. Direct test differentiation also gives \(P(D_x)u_\varepsilon=\langle P(D_z)u,\rho_\varepsilon(x-z)\rangle=0\): distributional transposition and \(\partial_z\rho_\varepsilon(x-z)=-\partial_x\rho_\varepsilon(x-z)\) cancel their signs, with \(D=-i\partial\) unchanged.

If \(K=\operatorname{supp}_X u\) is bounded, \(u_\varepsilon\) is zero wherever its test support is disjoint from \(K\). Its relative support in \(X_\varepsilon\) is therefore contained in the bounded set \(\overline K+\{|x|\le\varepsilon\}\). The already proved smooth theorem on the finite inner slab \(X_\varepsilon\) gives \(u_\varepsilon=0\).

For any fixed \(\phi\in C_c^\infty(X)\), choose \(\varepsilon\) small enough that its support and all the convolution tests below remain inside \(X_\varepsilon\) and \(X\), respectively. Proper convolution, equivalently integration of the smooth compactly supported test family against the distribution, gives
\[
\begin{gathered}
0=\langle u_\varepsilon,\phi\rangle
   \\
=\langle u,\phi*\check\rho_\varepsilon\rangle,
 \\
\qquad \check\rho_\varepsilon(x)=\rho_\varepsilon(-x).
\end{gathered}
\tag{27}
\]
All \(\phi*\check\rho_\varepsilon\) have support in one fixed compact subset of \(X\). For every multi-index \(\alpha\),
\[
\begin{gathered}
\partial^\alpha(\phi*\check\rho_\varepsilon-\phi)(z)
  \\
=\int\rho(y)
       \bigl[\partial^\alpha\phi(z+\varepsilon y)
                         \\
-\partial^\alpha\phi(z)\bigr]\,dy
       \\
\longrightarrow0
\end{gathered}
\tag{28}
\]
uniformly in \(z\), by uniform continuity of the compactly supported smooth derivative and the finite integral of \(|\rho|\). This is convergence in the fixed-support test-function topology. The distribution is continuous on this space; (27) therefore gives \(\langle u,\phi\rangle=0\). All tests \(\phi\) were arbitrary, so \(u=0\). There is no extension of \(u\) across either slab endpoint, and no assumption on its behavior near those endpoints.

If \(P\) is a nonzero constant, \(P(D)u=Pu\) is already injective. If \(n=1\) and \(N\ne0\), every nonconstant irreducible polynomial is linear. Its principal part is a nonzero multiple of the one frequency coordinate, which is hyperbolic with respect to any such \(N\). The theorem's hypothesis therefore allows only the constant case.

If \(N=0\), the slab is empty unless \(a<0<b\). An empty-domain distribution is zero. In the other case \(X=\mathbb R^n\); bounded relative support is closed and bounded in \(\mathbb R^n\), hence compact. The compact-support hull corollary Convex supports and convolution cancellation, Corollary 4.3, with the \(D=-i\partial\) convention, says a nonzero constant-coefficient polynomial is injective on compactly supported distributions. It gives \(u=0\), without using a directional coordinate or the factor hypothesis. In dimension zero a nonzero polynomial is a constant and is handled by that scalar case.

The statement was made for finite real \(a<b\). If an endpoint is allowed to be infinite, restriction to every finite inner slab has bounded relative support and the same equation. The theorem on those slabs proves zero on their union. \(\square\)

## Exercises with complete solutions

**Exercise 1 — basic: a root escaping through a leading coefficient.** For \(P(w,s)=ws-1\), compute the polynomial \(D\), the monic rescaling, and the regular cover in Lemma 1. Explain why connectedness does not mean that its root extends through \(w=0\).

**Solution.** Here \(\mu=1\), \(a=w\), and \(P_s=w\). In (3), \(A=0\) and \(B\) is constant, so \(S\) is multiplication by \(w\) and \(\det S=w\). Thus \(D=w^2\). Formula (5) gives \(R(w,y)=y-1\), since \(y=ws\). The regular cover is
\[
 \{(w,1/w):w\in\mathbb C\setminus\{0\}\}.
 \tag{29}
\]
Its projection is a holomorphic isomorphism to the punctured plane, which is path connected. Its original root \(s=1/w\) has a pole at zero and does not extend there as a finite root. The rescaled root \(y=1\) does extend, exactly as the monic argument needs. An entire transformed solution \(U(w,t)\) which vanishes for all \(w\ne0\) vanishes also at \(w=0\) by continuity; this final parameter continuation concerns \(U\), not extension of the escaping root.

**Exercise 2 — intermediate: a zero leading slope.** For \(P(t,s)=t^2+s+1\), construct the branch in Lemma 2 with \(e=1\), \(\eta=0\), and \(c_0=0\). Check its uniform asymptotic estimate and explain why the twofold cover is natural.

**Solution.** The total degree is 2 and \(F(t,s)=t^2\). Thus \(F(1,0)=1\) and \(F(c,1)=c^2\), with root \(c_0=0\). Equation (9) gives \(G(v,z)=v^2+z+z^2\). For \(z\ne0\) close to zero its two roots are distinct; both approach zero as \(z\to0\). Their continuation once around zero exchanges them. This can be seen by writing a root as \(i\sqrt z\,\sqrt{1+z}\), where the second square root has its single-valued branch near 1 and the first changes sign once around zero. The monodromy permutation has order 2.

Take \(p=2\), \(s=w^2\), and
\[
\begin{gathered}
t(w)=iw\sqrt{1+w^{-2}},
 \\
\qquad
 t(w)^2+w^2+1=0.
\end{gathered}
\tag{30}
\]
The square root in this expression is the holomorphic branch near 1 with value 1, supplied by the simple-root implicit-function proof. Its Taylor series gives
\(t(w)=iw+i/(2w)+O(|w|^{-3})\), uniformly for all sufficiently large \(w\), in every direction. In particular \(t(w)=0\cdot w^2+O(|w|)\), the exact \(p=2,c_0=0\) case of (8), and \(t(w)/w^2\to0\). The vanishing adapter does not require a nonzero slope: its zero-slope case compares an \(O(|w|)\) spatial displacement with the order-\(|w|^2\) time-frequency term and then covers all sheet arguments.

**Exercise 3 — advanced: repeated factors and the hypothesis on each factor.** In two frequency variables \((\zeta,s)\), apply Theorem 5 with normal in the \(s\)-direction to
\[
 P(\zeta,s)=(s+i\zeta)^2(\zeta^2+s^2+1).
 \tag{31}
\]
Then show that adjoining the factor \(s-\zeta\) permits a nonzero smooth solution with bounded relative support on every finite time slab.

**Solution.** The linear factor \(s+i\zeta\) is irreducible, and its principal part has the nonreal root \(s=-i\zeta\) for real \(\zeta\ne0\); hence it is not hyperbolic with respect to the time normal. The quadratic is irreducible. Indeed, it is monic in \(s\); reducibility over \(\mathbb C(\zeta)\) would give a rational square root of \(-(\zeta^2+1)\). The zero at \(\zeta=i\) is simple, whereas every square of a rational function has even zero or pole order: write its numerator and denominator as products of scalar linear factors and double their multiplicities. This is impossible. Gauss's lemma then gives irreducibility in \(\mathbb C[\zeta,s]\). Its principal part \(\zeta^2+s^2\) has roots \(s=\pm i\zeta\), again nonreal for real \(\zeta\ne0\). Theorem 5 applies to all three copies of these factors. Any bounded-relative-support distributional solution of \(P(D)u=0\) on the slab is zero.

For the enlarged polynomial \((s-\zeta)P\), choose a nonzero \(f\in C_c^\infty(\mathbb R)\) and set \(u(y,t)=f(y+t)\). Then \((D_t-D_y)u=-if'(y+t)+if'(y+t)=0\). Constant-coefficient operators commute, so the enlarged product also annihilates \(u\). On a finite slab \(a<t<b\), its support lies where \(y+t\in\operatorname{supp}f\). Both \(t\) and \(y\) are bounded there, so its relative support is bounded. This is a nonzero solution. The new factor's principal part \(s-\zeta\) is hyperbolic with respect to the time normal, with the real root \(s=\zeta\). The example verifies the need to impose the condition on every nonconstant factor, including when other factors already satisfy the condition.

## The equivalent factorwise condition

Excluding every nonconstant factor with hyperbolic principal part is equivalent to the irreducible-factor hypothesis. If a product of principal parts were hyperbolic, its value at \(N\) would be nonzero, so every constituent would be nonzero there. At every real \(\xi\), every root of each constituent \(F_j(\xi+\tau N)\) is also a root of their product. All these roots would therefore be real, making every constituent hyperbolic. Thus a product involving any of our nonhyperbolic constituents cannot acquire a hyperbolic principal part. The reverse implication follows by taking a single irreducible factor. Nonzero constant factors carry no positive-degree hyperbolicity condition.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
