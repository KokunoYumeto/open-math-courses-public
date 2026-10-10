# Analytic root barriers and supported solvability

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The negative-time test estimate restricts roots that remain far below the real axis on a large complex ball. A compact frequency window converts such a root into a homogeneous solution with value one at the origin. At the fixed observation set, it is small either by spatial cancellation or by time decay. Polynomial geometry prevents the radius and the negative root height from growing more slowly than every power at distant real centers. We supply the finite root-transport description needed to make that last statement precise.

Read [Supported fundamental solutions and test estimates](supported-fundamental-solutions-and-test-estimates.md), [Regular balls, moving roots and complex gauges](regular-balls-moving-roots-and-complex-gauges.md), [Symbols at infinity](symbols-at-infinity.md), [Global supported solvability on countably many scales](global-supported-solvability-on-countably-many-scales.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

The local distributional Holmgren theorem is proved in [Analytic coefficients and one-sided uniqueness](../AN02-L191.html#3-a-continuously-differentiable-surface-needs-no-analytic-flattening), Theorem 3.2: a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface vanishes near that surface. The uses of the Holmgren theorem draw on that complete proof.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## Five equivalent conditions

Let \(P\ne0\), \(D=-i\partial\), \(N\in\mathbb R^n\setminus\{0\}\), and \(H=\{y:y\cdot N\ge0\}\). The following conditions are equivalent, with the available Holmgren prerequisite used in the sufficient direction.

1. **(i)** There is a distribution \(E\) with \(P(D)E=\delta_0\) and \(\operatorname{supp}E\subset H\).
2. **(ii)** Some compact neighborhood \(K\) of zero, integer \(J\ge0\) and constant \(C\) satisfy \(|u(0)|\le C\sum_{|\alpha|\le J}\sup_{\mathbb R^n\setminus\operatorname{int}H}|D^\alpha P(D)u|\) for every smooth \(u\) supported in \(K\).
3. **(iii)** There are \(A_1>0,A_2\in\mathbb R\) such that every analytic \(\sigma\) on a complex \(n\)-dimensional ball \(B\) of radius \(A_1\) with real center, satisfying \(P(\zeta+\sigma(\zeta)N)=0\), obeys \(\sup_B\operatorname{Im}\sigma\ge A_2\).
4. **(iv)** For every \(1\le p<\infty\), positive moderate weight \(k\), and \(f\in B^{\mathrm{loc}}_{p,k}\) supported in \(H\), there is \(u\in B^{\mathrm{loc}}_{p,kS_P}\) supported in \(H\) with \(P(D)u=f\).
5. **(v)** Every finite-order distribution \(f\) supported in \(H\) has a finite-order distributional solution \(u\) supported in \(H\).

Here finite order means one derivative order valid on every compact set, with constants allowed to depend on that compact set. The full-frequency root in(iii) is a displacement along \(N\). Its conversion to the tangential normal-root formulation is proved in [Supported fundamental solutions and test estimates](supported-fundamental-solutions-and-test-estimates.md). The local supported estimate also covers \(p=\infty\); condition(iv) above retains its stated finite-exponent scope.

The elementary chain(iv) to(v) to(i) to(ii) is proved in that lesson. [Global supported solvability on countably many scales](global-supported-solvability-on-countably-many-scales.md) proves(iii) to(iv). The proof below supplies(ii) to(iii).

## The observation estimate and the irreducible reduction

Let \(P\ne0\). Use \(y=(x,t)\), \(x\in\mathbb R^d\), \(d\ge1\), \(D=-i\partial\), and \(H=\{t\ge0\}\). Assume clause(ii) of [the five-way theorem](analytic-root-barriers-and-supported-solvability.md). The written cutoff adapter gives a compact \(K'\subset\{t\le0\}\setminus\{0\}\), an integer \(J\ge0\) and \(C\) such that
\[
\begin{gathered}
|u(0)|\le C\sum_{|\alpha|\le J}\sup_{K'}|D^\alpha u|,
             \\
\qquad P(D)u=0,\\
\quad u\in C^\infty(\mathbb R^{d+1}).
\end{gathered}
\tag{1}
\]
The observation set is nonempty: a compact cutoff equal to one near zero must change value along the negative-time axis, so some first derivative is nonzero there. Put \(\delta=\operatorname{dist}(0,K')/2>0\). Every point of \(K'\) has either \(|x|\ge\delta\) or \(t\le-\delta\). Indeed if both inequalities failed then \(|y|<\sqrt2\delta<\operatorname{dist}(0,K')\).

Fix an irreducible factor \(Q\) of \(P\) having positive normal degree \(q\). Every global homogeneous solution for \(Q\) is one for \(P\), so(1) applies without a different observation set. Write
\[
\begin{gathered}
Q(z,s)=\sum_{\nu=0}^q a_\nu(z)s^\nu,\\
\quad a=a_q\not\equiv0,
       \\
\quad M=\deg Q,\\
\quad\kappa=M-q+1\ge1,\\
\quad K=\kappa J.
\end{gathered}
\tag{2}
\]
The written Gauss and Sylvester calculation gives a nonzero discriminant polynomial \(\Delta(z)\) for full-degree simple normal fibers. Set \(B(z)=a(z)\Delta(z)\), replacing a nonzero constant discriminant by that constant in the degree-one case.

For a real center \(c\in\mathbb R^d\) and \(\rho>0\), let
\[
\begin{gathered}
\Phi(c,\rho):\\
\quad B(z)\ne0\\
\quad
                       \text{for all }|z-c|<\rho+1.
\end{gathered}
\tag{3}
\]
On this ball all \(q\) roots have distinct analytic labels by [Regular balls, moving roots and complex gauges](regular-balls-moving-roots-and-complex-gauges.md)'s full-ball labeling proof. Define the bad-branch set
\[
\begin{gathered}
\mathcal U_Q=\{(c,\rho,A):c\in\mathbb R^d,\ \\
\rho,A>0,\ \Phi(c,\rho),
       \\
\ \exists\tau\text{ analytic on }B(c,\rho):
       \\
Q(z,\tau(z))=0,\ \operatorname{Im}\tau(z)\le-A\}.
\end{gathered}
\tag{4}
\]
Such a \(\tau\) is the restriction of one of the labels on the larger regular ball: it agrees with that label at the center, local simple-root uniqueness gives agreement nearby, and the holomorphic identity theorem gives agreement throughout the connected smaller ball.

## A normalized homogeneous solution from a bad branch

Choose a fixed \(\varphi\in C_c^\infty(B_{\mathbb R^d}(0,1/2))\), with integral one. For a member of(4), define
\[
\begin{gathered}
u(x,t)=\rho^{-d}\int_{\mathbb R^d}
       e^{i(x\cdot\xi+t\tau(\xi))}
                        \\
\varphi((\xi-c)/\rho)\,d\xi\\
 =\int e^{i(x\cdot(c+\rho\eta)+t\tau(c+\rho\eta))}
                                      \\
\varphi(\eta)\,d\eta.
\end{gathered}
\tag{5}
\]
Compact real frequency support makes this a global smooth function: on each compact time interval every finite derivative of its integrand has a finite uniform bound. Differentiation by \(D\) multiplies it by \((\xi,\tau(\xi))\). Consequently
\[
\begin{gathered}
Q(D)u=P(D)u=0,\\
\qquad u(0,0)=1.
\end{gathered}
\tag{6}
\]
The normalization \(\rho^{-d}\) is essential.

Let \(\Lambda=1+|c|+\rho\). The actual inset estimate([equation 12 in Regular balls, moving roots and complex gauges](regular-balls-moving-roots-and-complex-gauges.md)) gives
\[
                       |\tau(z)|\le C_Q\Lambda^\kappa
                                      \quad(|z-c|<\rho).
 \tag{7}
\]
The leading coefficient is zero-free on the larger radius-\(\rho+1\) ball, so its modulus has the fixed positive inset lower bound used by that estimate. Neither \(C_Q\) nor \(\kappa\) depends on the center, radius or branch.

For \(|\alpha|\le J\), put
\(F_\alpha(z,t)=z^{\alpha_x}\tau(z)^{\alpha_t}e^{it\tau(z)}\).
For real \(t\le0\), the branch hypothesis and(7) give
\[
\begin{gathered}
|F_\alpha(z,t)|\le C_\alpha\Lambda^K e^{-A|t|}
       \\(|z-c|<\rho),\\|\partial_{z_j}^{\,h}F_\alpha(\xi,t)|
   \\
\le C_\alpha h!(4/\rho)^h\Lambda^K e^{-A|t|}
                           \\(|\xi-c|\le\rho/2).
\end{gathered}
\tag{8}
\]
The exponent \(K\) works because
\(|\alpha_x|+\kappa\alpha_t\le\kappa|\alpha|\le\kappa J\).
The second inequality is one-variable Cauchy on the coordinate circle of radius \(\rho/4\), which stays inside the complex radius-\(\rho\) ball. Crucially that entire complex ball has \(\operatorname{Im}\tau\le-A\). Thus its exponential remains bounded by the same time-decay factor when arbitrarily many frequency derivatives are taken.

Leibniz differentiates the product of \(F_\alpha\) and the compact window \(N\) times in a chosen coordinate. Each window derivative supplies the corresponding power of \(\rho^{-1}\), and(8) supplies the remaining power. The \(L^1\) bound of those derivatives has a factor \(\rho^d\) from its support volume, canceled by(5). For \(|x|\ge\delta\), choose \(j\) with \(|x_j|\ge\delta/\sqrt d\), and integrate by parts \(N\) times in \(\xi_j\). There is no boundary term. For every integer \(N\ge0\),
\[
\begin{gathered}
|D^\alpha u(x,t)|\le C_{N,\delta}\Lambda^K\rho^{-N}e^{-A|t|}
           \\
\quad(|\alpha|\le J,\ |x|\ge\delta,\ t\le0).
\end{gathered}
\tag{9}
\]
The constants may depend on \(N\), but the power \(K\) does not. Without integration by parts, direct absolute integration also gives
\[
\begin{gathered}
|D^\alpha u(x,t)|\le C_0\Lambda^K e^{-A\delta}
                        \\
\quad(|\alpha|\le J,\ t\le-\delta).
\end{gathered}
\tag{10}
\]
Apply(1), using the two parts of the observation set. Equations(6),(9),(10) give
\[
\begin{gathered}
1\le C_N(1+|c|+\rho)^K
                   \bigl(\rho^{-N}+e^{-\delta A}\bigr),
                             \\
\qquad(c,\rho,A)\in\mathcal U_Q,
\end{gathered}
\tag{11}
\]
for every fixed \(N\). This estimate alone does not yet give a uniform bound at centers tending to infinity.

## Finite semialgebraic transport of a selected root

We now prove that(4) is a semialgebraic set using only the projection theorem. A complex variable is always represented by its two real coordinates. In particular \(\Phi\) is already a real quantified polynomial condition, hence semialgebraic: replace \(B\ne0\) by \(|B|^2>0\) and use the real squared ball norm.

Fix parameters satisfying \(\Phi(c,\rho)\), a complex endpoint \(|z-c|<\rho\), and a root \(w_0\) at \(c\). The segment \(z_\lambda=c+\lambda(z-c)\), \(0\le\lambda\le1\), lies in the regular ball. The \(q\) full-ball labels restrict to analytic functions along this segment and a complex neighborhood of its closed parameter interval.

Use one of the finitely many real projections
\[
\begin{gathered}
\ell_b(w)=\operatorname{Re}w+b\operatorname{Im}w,
                   \\
\qquad b=0,1,\ldots,q(q-1)/2.
\end{gathered}
\tag{12}
\]
At least one separates all roots at \(\lambda=0\). Each pair of distinct roots forbids at most one value of \(b\): if its imaginary difference is zero, its nonzero real difference forbids none. There are at most \(q(q-1)/2\) pairs. Initial separation is itself a quantified polynomial predicate on the roots of \(Q(c,\cdot)\).

For a separating \(b\), define the projection-collision predicate
\[
\begin{gathered}
E_b(c,z,\lambda):\quad
   \exists v\ne v'\ 
      \\
[Q(z_\lambda,v)=Q(z_\lambda,v')=0,\
                              \\
\ell_b(v)=\ell_b(v')].
\end{gathered}
\tag{13}
\]
On the selected regular parameters it holds at finitely many points of \([0,1]\). For each pair of analytic labels, their projected difference is a real analytic function of real \(\lambda\), nonzero at zero. Its zeros cannot accumulate on the closed interval, because the labels extend to a neighborhood of that interval; an accumulation would make this difference identically zero. There are finitely many pairs.

There is a uniform finite bound \(L\), depending only on \(Q\), on the number of collision points for all these parameters and projections. By the projection theorem, \(E_b\) has a formula using a fixed finite collection of real polynomials in \(c,\operatorname{Re}z,\operatorname{Im}z,\lambda\). At fixed parameters, discard members identically zero as polynomials in \(\lambda\). At every isolated collision point at least one remaining polynomial must vanish; otherwise all signs would be constant on a parameter interval about that point, contradicting isolation. This also applies at endpoint one by its one-sided neighborhood. Thus the number is bounded by the sum of the \(\lambda\)-degrees in that finite formula. Take the maximum of these finite sums over the finite list of \(b\)'s. No formula for a root path has been assumed in this bound.

On an open interval containing no collision, define \(R^b_r(\lambda,v)\), \(0\le r<q\), to mean that \(v\) is the root of projected rank \(r\). A polynomial formula is obtained by introducing \(q\) pairwise distinct roots, requiring
\[
\begin{gathered}
Q(z_\lambda,v_i)=0\ (i=1,\ldots,q),\\
\quad
 \ell_b(v_1)<\cdots<\ell_b(v_q),\\
\quad v=v_{r+1}.
\end{gathered}
\tag{14}
\]
The degree and regularity imply these are all roots. Projection makes this a semialgebraic predicate. On that interval it selects one unique analytic label; its projected rank cannot change without a collision.

Limits at interval boundaries are also finite quantified polynomial conditions. For example a right limit of rank \(r\) on \((a_0,a_1)\) at \(a_0\) equal to \(w\) says
\[
\begin{gathered}
\forall\epsilon>0\ \exists h>0\ \forall\lambda,v:\\
 [\,a_0<\lambda<a_1,\ \lambda-a_0<h,\
                           R^b_r(\lambda,v)\,]
                  \ \\
\Longrightarrow\ |v-w|^2<\epsilon^2.
\end{gathered}
\tag{15}
\]
The left-limit formula replaces \(\lambda-a_0\) by \(a_1-\lambda\). There is always one ranked root at each interior parameter, so these tests are not vacuous. On the regular segment the limits exist by the analytic labels.

Define \(\operatorname{Reach}(c,\rho,w_0,z,w)\), only on the regular parameters under consideration, by the following finite union of polynomial-quantifier descriptions. Choose a separating projection from(12), a number \(0\le h\le L\), and a list of ranks from the finite set \(\{0,\ldots,q-1\}\). Introduce
\[
\begin{gathered}
0=\lambda_0<\lambda_1<\cdots<\lambda_h<\lambda_{h+1}=1,
                      \\
\quad w_0,w_1,\ldots,w_h,w_{h+1}=w.
\end{gathered}
\tag{16}
\]
Require that \(\lambda_1,\ldots,\lambda_h\) are exactly the collision points in \((0,1)\), using a universal instance of(13), and require every \(w_i\) to be a root at its boundary parameter. On each intervening interval, require the right and left limits of its selected rank, via(15), to be \(w_i,w_{i+1}\). Endpoint collisions at one are permitted by the left-limit condition; zero is not a collision by initial separation.

This is a finite real quantified polynomial formula: there are boundedly many parameters, finitely many rank lists and projections, and all the displayed tests use polynomial equalities and inequalities. The projection theorem makes Reach semialgebraic on \(\Phi(c,\rho),|z-c|<\rho,Q(c,w_0)=0\).

It describes exactly the selected root's transport. Starting at \(w_0\), the first right limit identifies one full-ball analytic label. At each collision parameter, the roots still have distinct full complex values. Matching \(w_i\) therefore forces the same analytic label on the next interval, even if its projected rank changes. Induction identifies its endpoint \(w\). Conversely the label determines the required ranks, boundary values and collision list, so satisfies the formula. This proves existence and uniqueness in the description, not merely that some root at the endpoint can be selected.

The bad-branch condition is now exactly
\[
\begin{gathered}
\rho,A>0,\ \Phi(c,\rho),\ \\
\exists w_0\ [Q(c,w_0)=0,\ 
      \\
\forall z,w:\ \\
(|z-c|^2<\rho^2,\
               \\
\operatorname{Reach}(c,\rho,w_0,z,w))\\
                                      \Longrightarrow\operatorname{Im}w\le-A].
\end{gathered}
\tag{17}
\]
The unique analytic label selected by \(w_0\) proves its equivalence to(4). All quantifiers are over finitely many real coordinates. Thus \(\mathcal U_Q\) is semialgebraic by the projection theorem, with the root-transport step supplied in full here.

## A finite supremum and its polynomial power gap

For \(T\ge1\), define
\[
\begin{gathered}
f(T)\\
=\sup\bigl(\{0\}\cup
       \{s>0:\exists c,\ |c|\\
\le T,\ (c,s,s)\in\mathcal U_Q\}\bigr).
\end{gathered}
\tag{18}
\]
This is finite and at most linearly growing. Choose a fixed \(N_0>K\) in(11). If \(s>T+1\), then \(1+|c|+s<2s\), and its right side is bounded by
\(C_{N_0}2^K(s^{K-N_0}+s^Ke^{-\delta s})\), which tends to zero. Hence a fixed \(S_0\) excludes every sufficiently large such \(s\), and
\[
                       0\le f(T)\le\max(T+1,S_0).
 \tag{19}
\]
It is nondecreasing. Its graph is semialgebraic even when the supremum is not attained: \(y=f(T)\) means that \(y\ge0\) is an upper bound of the set in(18) and that for every \(\epsilon>0\) this set, including zero, has a member greater than \(y-\epsilon\). These are finite real polynomial quantifiers using(17).

Suppose \(f\) were unbounded. Its monotonicity gives \(f(T)\to\infty\). A graph defined by finitely many nonzero polynomial sign tests cannot contain an open two-dimensional ball. At each graph point at least one of those polynomials is zero; otherwise all signs would be constant nearby and the defining formula would include a ball. Their product is a nonzero polynomial \(F\) with
\[
\begin{gathered}
F(T,f(T))=0,\\
\qquad
             F(T,y)=\sum_{j=0}^{J_0}T^j b_j(y),\\
\quad b_{J_0}\ne0.
\end{gathered}
\tag{20}
\]
Identically zero defining polynomials are discarded beforehand. If \(J_0=0\), the nonzero polynomial \(b_0\) has finitely many roots, contradicting \(f(T)\to\infty\).

For \(J_0>0\), let \(l=\deg b_{J_0}\) and \(D_0=\max_j\deg b_j\). For large positive \(y\), \(|b_{J_0}(y)|\ge c y^l\), while all other coefficients have modulus at most \(C y^{D_0}\). Divide(20) by \(T^{J_0}\), and use \(T^{j-J_0}\le T^{-1}\) when \(j<J_0\). For all large \(T\),
\[
                c f(T)^l\le C'T^{-1} f(T)^{D_0}.
 \tag{21}
\]
If \(D_0=l\), this is impossible for large \(T\). If \(D_0>l\), it gives \(f(T)\ge c_1T^\alpha\), \(\alpha=1/(D_0-l)>0\). This direct polynomial power gap uses no Puiseux expansion.

Select, for each sufficiently large \(T\), an admissible \(s_T>f(T)/2\) in(18), with center \(c_T\) of norm at most \(T\). The supremum definition supplies it; attainment is unnecessary. By(19) it is at most \(C_1T\), and by(21) it is at least \(c_2T^\alpha\). Choose a fixed integer \(N\) with \(\alpha N>K\). Applying(11) to \((c_T,s_T,s_T)\) now gives
\[
\begin{gathered}
1\\
\le C_N'(T^{K-\alpha N}
                         +T^Ke^{-\delta c_2T^\alpha})\\
\longrightarrow0.
\end{gathered}
\tag{22}
\]
The first exponent is negative. For the second term, \(\log T/T^\alpha\to0\), for example by differentiating this elementary scalar quotient; its logarithm tends to minus infinity. This contradiction proves that \(f\) is uniformly bounded, say \(f(T)\le S\) with \(S\ge1\).

If \((c,\rho,A)\in\mathcal U_Q\), every \(0<s\le\min(\rho,A)\) is also admissible as \((c,s,s)\), by restricting the regular ball and the same label. Thus the same \(S\) bounds \(\min(\rho,A)\) for every member of \(\mathcal U_Q\).

## The uniform root barrier and the full equivalence

Apply [Regular balls, moving roots and complex gauges](regular-balls-moving-roots-and-complex-gauges.md)'s real-centered zero-free subball lemma to the fixed nonzero exceptional polynomial \(B\), and let \(\gamma>0\) be its constant. Choose
\[
                       A_1=(S+3)/\gamma,\qquad A_2=-S-2.
 \tag{23}
\]
If an analytic root on any real-centered radius-\(A_1\) ball had imaginary supremum below \(A_2\), the subball lemma would supply a real center \(c'\) and a zero-free radius-\((S+3)\) ball inside it. Its restriction to radius \(\rho=S+2\) then gives \((c',S+2,S+2)\in\mathcal U_Q\), contradicting the bound \(S\). Consequently every such branch has imaginary supremum at least \(A_2\). This is the tangential root condition for the factor \(Q\).

Factors of normal degree zero have no analytic normal root on an open tangential ball, since a nonzero tangential polynomial cannot vanish there. There are finitely many irreducible factors, with repetitions allowed. Choose the maximum of the radii just obtained and the minimum of their heights. A root of their product on the larger connected ball is a root of some fixed factor throughout that ball. To justify this, compose each factor with the analytic root. Their product is identically zero. If all were nonzero holomorphic functions, their closed zero sets would have empty interior; successively shrinking a nonempty open subset to avoid each one would produce a point where their product is nonzero. Hence one factor vanishes identically. Restrict to its smaller concentric ball to obtain the common height bound. If all factors have normal degree zero, the product has no such root and the condition is vacuous.

In \(d=0\), the normal polynomial has finitely many scalar roots; their imaginary parts have a fixed minimum. The root condition therefore holds directly, including constants with no roots. The higher-dimensional transport argument is unnecessary in this case. [equation 11 in Supported fundamental solutions and test estimates](supported-fundamental-solutions-and-test-estimates.md)–[equation 12 in Supported fundamental solutions and test estimates](supported-fundamental-solutions-and-test-estimates.md) convert the tangential condition to the exact full-frequency displacement condition of [the five-way theorem](analytic-root-barriers-and-supported-solvability.md)(iii).

We have proved(ii) to(iii) relative to exact written bases. Together with [Supported fundamental solutions and test estimates](supported-fundamental-solutions-and-test-estimates.md)'s(iv) to(v) to(i) to(ii) and [Global supported solvability on countably many scales](global-supported-solvability-on-countably-many-scales.md)'s(iii) to(iv), this yields the full five-way equivalence. The [Global supported solvability on countably many scales](global-supported-solvability-on-countably-many-scales.md) sufficient direction uses the available general Holmgren theorem; no part of this necessary argument assumes that theorem.

For completeness, arbitrary half-space normals reduce to these coordinates. If \(N\ne0\), choose an orthogonal matrix \(O\) with last column \(N/|N|\), and write \(y=Ox\), \(\widetilde P(\xi)=P(O\xi)\). The support condition becomes \(x_n\ge0\). Fourier substitution has absolute determinant one. The finite derivative-chain matrices for \(O,O^{-1}\) give
\[
 S_{\widetilde P}(\xi)\asymp S_P(O\xi),\qquad
                            \widetilde k(\xi)=k(O\xi).
 \tag{24}
\]
Indeed each derivative of \(P(O\xi)\) of order at most \(\deg P\) is a fixed linear combination of derivatives of \(P\) at \(O\xi\); the inverse change gives the reverse inequality. The weight remains moderate because \(O\) preserves real distances. Thus the weighted local memberships with their precise derivative-norm gain transform to equivalent norms. Test seminorms and compact neighborhoods likewise transform by finite derivative combinations. For the full root condition, replacing \(N\) by \(N/|N|\) multiplies its displacement root by \(|N|\), hence multiplies its height constant by the same positive number; orthogonal changes preserve balls and their real centers. This verifies every clause's coordinate reduction rather than presuming literal invariance of the unweighted multi-index derivative norm.

## Exercises with complete solutions

**Exercise 1 (entry).** For a constant bad root \(\tau(\xi)=-iA\), compute(5) using the Fourier transform of \(\varphi\). Verify both smallness mechanisms and the normalization.

**Solution.** The formula is \(u(x,t)=e^{ix\cdot c+At}\widehat\varphi(-\rho x)\). Since \(\widehat\varphi(0)=\int\varphi=1\), its value at the origin is one. It solves \((D_t+iA)u=0\), because \(D_tu=-iA u\). At \(t\le-\delta\) its modulus is bounded by \(e^{-A\delta}\|\widehat\varphi\|_\infty\). At \(|x|\ge\delta,t\le0\), the compact smooth window gives \(|\widehat\varphi(-\rho x)|\le C_{N,\delta}\rho^{-N}\) for every \(N\), by integration by parts. Both estimates have the correct negative-time sign. Omitting \(\rho^{-d}\) from the real-frequency integral would instead give value \(\rho^d\) at the origin and would invalidate the fixed normalized test of(1).

**Exercise 2 (intermediate).** On \(0\le\lambda\le1\), consider the two supplied analytic roots \(v_1(\lambda)=\lambda+i\), \(v_2(\lambda)=1-\lambda-i\). With projection \(\ell_0=\operatorname{Re}\), follow the first root from \(\lambda=0\) to one. Explain why keeping its initial projected rank fails. This is a segment transport model; no larger regular-ball hypothesis is claimed for its polynomial.

**Solution.** At zero the projections are \(0,1\), so \(v_1\) has rank zero. They coincide only at \(\lambda=1/2\), where the full roots are \(1/2+i\) and \(1/2-i\), still distinct. On the right interval \(v_1\) has rank one. Matching the boundary value \(1/2+i\) therefore changes the rank from zero to one while retaining the same complex root path. It ends at \(v_1(1)=1+i\). Keeping rank zero instead selects \(v_2\) after the crossing and ends at \(-i\); the path jumps at the crossing. The polynomial \((s-\lambda-i)(s-1+\lambda+i)\) has exactly the displayed distinct roots along this segment. Their explicit analytic labels justify the limit tests of the finite-chain mechanism in this example.

**Exercise 3 (advanced).** Use \(F(T,y)=y^3-T\) to illustrate the power-gap argument. Explain why a hypothetical nondecreasing semialgebraic bad-branch supremum growing as \(\log T\) cannot survive this argument, and why its supremum need not be attained.

**Solution.** Here the highest \(T\)-coefficient is \(b_1=-1\), with degree \(l=0\), and the other coefficient is \(b_0=y^3\), giving \(D_0=3\). Equation(21) gives \(1\le T^{-1}f(T)^3\), hence \(f(T)\ge T^{1/3}\), exactly the positive root of this equation. More generally an unbounded nondecreasing semialgebraic \(f\) has a nonzero annihilating polynomial and the same argument supplies some positive power lower bound. Since \(\log T/T^\alpha\to0\) for every \(\alpha>0\), logarithmic growth is impossible in that class. For the illustrative power \(1/3\), choose \(N>3K\) in(22); the oscillatory and exponential terms both tend to zero. A supremum can fail to belong to its set: \(\sup(0,T)=T\) although \(T\) is excluded. The upper-bound and arbitrary-accuracy quantifiers still define that supremum, and selecting an admissible value above half of it requires no attainment. The proof uses precisely those two properties.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
