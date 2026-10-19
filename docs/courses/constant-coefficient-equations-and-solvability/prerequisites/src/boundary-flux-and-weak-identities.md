# Boundary flux and weak identities

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. The earlier edition was written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition and exercises: CC0. The separately credited programme prerequisites retain their own licences.*

An outward flux can be recovered from what a function does on the inside of a region. We first calculate that flux on a graph, use the calculation to construct a surface measure, and then pass to continuous fields with an integrable weak divergence. A separate finite-partition argument explains why an everywhere differentiable solution of a first-order equation also solves the weak equation even when its gradient is not integrable.

Our integration convention is complex linear: a distribution acts on a test without conjugating it, and \(\langle\partial_jT,\phi\rangle=-\langle T,\partial_j\phi\rangle\). The elementary programme prerequisites are the mean value and fundamental theorems of calculus, finite-dimensional compactness, smooth compact cutoffs, Fubini–Tonelli, dominated convergence, and translation continuity in \(L^1\). Their exact proof locations are listed after the solutions. The graph lemma, the required partition of unity, the surface-measure compatibility, the flux identities and the finite tagged-partition lemma are proved here.

## A boundary separates two local sides

Let \(Y\subset X\subset\mathbb R^n\) be open, with \(n\ge1\). All closures and boundaries below are relative to \(X\). By a \(C^1\) boundary we mean that every \(p\in\partial_XY\) has a neighbourhood \(U\) and a real \(r\in C^1(U)\) satisfying

\[
 \begin{gathered}
 Y\cap U=\{r<0\},\\
 \partial_XY\cap U=\{r=0\},\\
 \nabla r\ne0\text{ on }\{r=0\}.
 \end{gathered}
 \tag{1.1}
\]

**Graph lemma.** Near each such point, after permuting and possibly reversing one coordinate, there are a base box \(V\subset\mathbb R^{n-1}\), an interval \((a,b)\), and a function \(\gamma\in C^1(V)\) for which

\[
 \begin{gathered}
 Y\cap(V\times(a,b))\\
   =\{(x',t):a<t<\gamma(x')\},\\
 r(x',\gamma(x'))=0.
 \end{gathered}
 \tag{1.2}
\]

**Proof.** Choose the last coordinate so that \(\partial_t r(p)>0\). On a smaller closed box it is at least some \(c>0\). Choose \(a<p_n<b\) so close to \(p_n\) that the vertical segment stays in that box. The mean value theorem gives \(r(p',a)<0<r(p',b)\); continuity preserves these strict inequalities for \(x'\) in a sufficiently small base box. The intermediate value theorem gives a zero on each vertical segment, and \(\partial_t r\ge c\) makes it unique. The same monotonicity gives the asserted negative side.

On a still smaller box, bound \(|\nabla_{x'}r|\) by \(M\). Applying the mean value bound first on a horizontal segment and then on the vertical segment between the two zeros gives

\[
 |\gamma(x'+h)-\gamma(x')|\le (M/c)|h|.
\]

For \(k=\gamma(x'+h)-\gamma(x')=O(|h|)\), differentiability of \(r\) at \((x',\gamma(x'))\) gives

\[
 0=\nabla_{x'}r\cdot h+\partial_t r\,k+o(|h|).
\]

Thus \(D\gamma=-\nabla_{x'}r/\partial_t r\) evaluated on the graph. This expression is continuous, so \(\gamma\) is \(C^1\). In dimension one the base is a point and the same proof gives a locally isolated boundary point. \(\square\)

The outward unit normal in these coordinates is

\[
 \nu=\frac{(-\nabla\gamma,1)}{\sqrt{1+|\nabla\gamma|^2}}
     =\frac{\nabla r}{|\nabla r|}.
 \tag{1.3}
\]

This is independent of the defining function. Indeed, its tangent vectors are \((v,D\gamma v)\), whose orthogonal complement is the line spanned by \((-\nabla\gamma,1)\). The sign is the one pointing to the side outside \(Y\). Any other defining function has that same zero tangent space and positive side, and therefore gives the same unit normal.

We will need a partition with supports actually inside its charts, including when \(X\) is unbounded.

**Partition lemma.** Every open cover of an open subset \(X\) of Euclidean space has a countable smooth partition of unity whose supports are compact subsets of members of the cover and form a locally finite family in \(X\).

**Proof.** Put

\[
 \begin{gathered}
 K_m=\{x\in X:|x|\le m,\ d(x)\ge1/m\},\\
 d(x)=\operatorname{dist}(x,\mathbb R^n\setminus X),\qquad m\ge1,
 \end{gathered}
\]

using infinite distance when \(X=\mathbb R^n\), and set \(K_m=\varnothing\) for \(m\le0\). Each \(K_m\) is compact, \(K_m\subset\operatorname{int}K_{m+1}\), and their interiors exhaust \(X\). Distance to a nonempty closed set is continuous because the triangle inequality gives \(|d(x)-d(y)|\le|x-y|\); this also justifies closedness in this formula.

The compact layer \(L_m=K_m\setminus\operatorname{int}K_{m-1}\) lies in the open set \(\operatorname{int}K_{m+1}\setminus K_{m-2}\). Around each of its points choose concentric balls \(B\subset2B\) with \(\overline{2B}\) inside that open set and inside one member of the given cover. Finitely many of the smaller balls cover \(L_m\). Take a smooth nonnegative bump equal to one on each smaller ball and supported in its corresponding larger ball; the exact radial bump construction is in the stated cutoff prerequisite.

The resulting countable family of supports is locally finite. In fact a point has a neighbourhood inside some \(\operatorname{int}K_N\), and every layer with \(m\ge N+2\) has its selected supports outside \(K_{m-2}\supset K_N\); the finitely many earlier layers contribute only finitely many balls. At least one bump is positive at each point: choose the smallest \(m\) for which the point belongs to \(K_m\), and use its layer. The locally finite sum \(s\) of all bumps is therefore positive and smooth. Dividing each bump by \(s\) gives the required partition, with its original support unchanged. \(\square\)

**Proposition 1.1 (a global defining function).** There is a real \(\rho\in C^1(X)\) such that

\[
 \begin{gathered}
 Y=\{\rho<0\},\qquad \partial_XY=\{\rho=0\},\\
 \nabla\rho\ne0\text{ on }\partial_XY.
 \end{gathered}
 \tag{1.4}
\]

**Proof.** Apply the partition lemma to the boundary charts together with \(Y\) and \(X\setminus\overline Y\). To a boundary chart assign its defining function, and to the last two open sets assign respectively \(-1\) and \(1\). Let \(\rho\) be the sum of these functions times their partition factors, each product extended by zero. Every product is \(C^1\) across the edge of its chart because its factor has compact support inside the chart; local finiteness proves that the sum is \(C^1\).

All active summands have the same strict sign at an interior or exterior point. At a boundary point their defining functions vanish. Differentiating there consequently gives

\[
 \begin{aligned}
 \nabla\rho(p)&=\sum_i\theta_i(p)\nabla r_i(p)\\
       &=\left(\sum_i\theta_i(p)|\nabla r_i(p)|\right)\nu(p).
 \end{aligned}
\]

Only boundary charts can have nonzero factors at \(p\); those factors sum to one. The scalar in parentheses is strictly positive. This proves every assertion. \(\square\)

## The derivative of a region is its oriented surface measure

In a graph chart define the local positive measure

\[
 \begin{aligned}
 &J_\gamma(x')=\sqrt{1+|\nabla\gamma(x')|^2},\\
 &\int h\,d\mu_\gamma\\
 &\qquad=\int_V h(x',\gamma(x'))J_\gamma(x')\,dx'.
 \end{aligned}
 \tag{2.1}
\]

The graph map sends the measure with this continuous density to a measure on the graph. It is finite on compact subcharts. The density is the Euclidean one: the Gram matrix of its tangent vectors is \(I+vv^{\mathsf T}\), where \(v=\nabla\gamma\), and its determinant is \(1+|v|^2\). To see the last identity directly, the map is the identity on \(v^\perp\) and multiplication by \(1+|v|^2\) on the span of \(v\), with the case \(v=0\) immediate.

Here is a construction of compatibility that does not assume a nonlinear change-of-variables theorem for surfaces.

**Theorem 2.1 (surface measure and the boundary derivative).** The graph measures (2.1) agree on overlaps and define a locally finite measure \(dS\) on \(\partial_XY\). With the normal (1.3),

\[
 \partial_j\chi_Y=-\nu_j\,dS\quad\text{in }\mathcal D'(X).
 \tag{2.2}
\]

Consequently, for every \(A\in C_c^1(X;\mathbb C^n)\),

\[
 \int_Y\operatorname{div}A\,dx
      =\int_{\partial_XY}A\cdot\nu\,dS.
 \tag{2.3}
\]

The total variation of the vector measure \(\nabla\chi_Y\) is \(dS\), and its support and singular support are both \(\partial_XY\).

**Proof.** Take a \(C_c^1\) scalar test \(h\) supported in one graph cylinder. For the vertical derivative, Fubini and the one-dimensional fundamental theorem give

\[
 \int_Y\partial_t h\,dx=\int_V h(x',\gamma(x'))\,dx'.
\]

For \(j<n\), differentiation of \(H(x')=\int_a^{\gamma(x')}h(x',t)\,dt\) gives

\[
 \partial_jH=\int_a^{\gamma(x')}\partial_jh(x',t)\,dt
              +h(x',\gamma(x'))\partial_j\gamma.
\]

This differentiation follows by splitting the increment into an integral over the fixed interval and an integral between the two upper endpoints: the first quotient converges uniformly on compact subcharts by continuity of \(\partial_jh\), while the second converges to \(h(x',\gamma)\partial_j\gamma\). The function \(H\) has compact support in the base. Integrating its derivative gives zero by the fundamental theorem, so

\[
 \int_Y\partial_jh\,dx=-\int_V h(x',\gamma(x'))\partial_j\gamma(x')\,dx'.
\]

These identities are precisely \(\int_Y\nabla h=\int h\nu\,d\mu_\gamma\). Coordinate permutations and reflections preserve volume with absolute Jacobian one and transform the gradient and normal by the same orthogonal matrix; thus the identity also holds in the original coordinates.

For two charts, apply that identity to tests supported in their overlap. Their vector measures \(\nu\mu_\gamma\) give the same values on all smooth compact tests. They then give the same values on continuous compact tests: convolution with a nonnegative smooth unit-mass bump uniformly approximates each such test, with supports in one fixed compact neighbourhood. Uniform continuity proves this approximation, and local finiteness bounds its integral error. Extend the normal continuously off the graph using its formula in the first chart. Test the \(j\)-th component equality with \(h\nu_j\), where \(h\) is continuous with compact support in the overlap, and sum over \(j\). Since \(\sum_j\nu_j^2=1\) on the graph, this gives \(\int h\,d\mu_{\gamma_1}=\int h\,d\mu_{\gamma_2}\).

Here is the needed measure-uniqueness step. For an open set \(O\) in the overlap, the continuous functions

\[
 \begin{aligned}
 h_k(x)&=\min\{1,(k\operatorname{dist}(x,O^c)-1)_+\}\\
       &\qquad\cdot\min\{1,(k-|x|)_+\}
 \end{aligned}
\]

have compact support inside \(O\), increase, and tend to \(1_O\). For empty \(O\) take zero. Thus monotone convergence makes the two measures agree on every open set. On each relatively compact open neighbourhood \(W\) in the overlap they are finite. The subsets of \(W\) on which they agree form a Dynkin class: complements subtract from their common finite measure of \(W\), and disjoint countable unions use countable additivity. Relatively open sets form an intersection-closed generating family. The Dynkin-class argument proved in the product-measure prerequisite therefore gives equality on all Borel subsets of \(W\). A countable exhaustion of the overlap by such \(W\)'s proves \(\mu_{\gamma_1}=\mu_{\gamma_2}\) everywhere on the overlap.

One may glue the measures by a countable chart partition: set \(\int h\,dS=\sum_i\int\theta_i h\,d\mu_i\). On any chart the agreement just proved reduces this sum to its graph integral, so the construction is independent of the partition. Compact subsets meet only finitely many partition supports, proving local finiteness. For \(n=1\) the graph formula assigns mass one to each locally isolated boundary point.

Split a compact test by the partition from Section 1. The graph identities hold on boundary charts; on interior charts the integral of a compact derivative is zero; exterior charts contribute zero. In summing, the derivatives of the partition factors cancel because their sum is one near the support of the test. This proves (2.2), and the same argument applied to the components of a \(C_c^1\) field proves (2.3).

For the variation assertion, on a compact portion of the boundary every Borel partition \(E=\bigsqcup E_k\) satisfies

\[
 \sum_k\left|\int_{E_k}\nu\,dS\right|\le S(E).
\]

Conversely, partition the unit sphere into finitely many Borel sets of diameter at most \(\varepsilon\), and split \(E\) according to the values of \(\nu\). In each nonempty piece choose a unit vector \(v_k\) within \(\varepsilon\) of its normals. Then

\[
 \left|\int_{E_k}\nu\,dS\right|
 \ge v_k\cdot\int_{E_k}\nu\,dS\ge(1-\varepsilon)S(E_k).
\]

Take the supremum over partitions and then let \(\varepsilon\) tend to zero. Exhaustion by compact neighbourhoods gives the locally finite statement.

Every boundary neighbourhood has positive graph measure, since its projection contains a nonempty base ball and the density is at least one. Thus the support is exactly the boundary. Each graph has zero \(n\)-dimensional volume by Fubini, and a countable chart cover makes the whole boundary null. If the vector distribution were smooth near a boundary point, its smooth density would vanish off that null set and hence, by continuity, everywhere in that neighbourhood. This contradicts its positive variation there. Its singular support is therefore also exactly the boundary. The indicator itself has the same singular support: it is constant off the boundary, while a continuous representative near a boundary point would have to take both the inside value one and the outside value zero at that point. Both sides approach the point by the graph description, so that is impossible. \(\square\)

**Corollary 2.2 (cutting off a differentiable amplitude).** For \(u\in C^1(X)\),

\[
 \partial_j(u\chi_Y)=(\partial_ju)\chi_Y-u\nu_j\,dS.
 \tag{2.4}
\]

**Proof.** Use (2.3) on the field having \(u\phi\) in its \(j\)-th component and zero in the others. Expand \(\partial_j(u\phi)\), then rearrange. Every term is integrable on the compact support of \(\phi\), and the resulting identity is exactly the distributional pairing in (2.4). \(\square\)

**Corollary 2.3 (the planar complex sign).** For \(n=2\), write \(z=x+iy\) and \(\partial_{\bar z}=(\partial_x+i\partial_y)/2\). Orient the boundary by the tangent \(\tau=(-\nu_y,\nu_x)\), so that the region is on the left. For \(\phi\in C_c^1(X)\),

\[
 \begin{aligned}
 2\int_Y\partial_{\bar z}\phi\,dx\,dy&=-i\int_{\partial_XY}\phi\,dz,\\
 \langle\partial_{\bar z}\chi_Y,\phi\rangle
          &=\frac i2\int_{\partial_XY}\phi\,dz.
 \end{aligned}
 \tag{2.5}
\]

**Proof.** Formula (2.3), applied to \((\phi,i\phi)\), gives the boundary factor \(\nu_x+i\nu_y\). But \(dz=(\tau_x+i\tau_y)dS=i(\nu_x+i\nu_y)dS\). Substitution proves both identities, including their signs. \(\square\)

### Corollary 2.4 (finitely many planar corners)

Let \(Y\Subset X\subset\mathbb R^2\) be open. Suppose its boundary is the union of finitely many regular \(C^1\) arcs, each parametrized injectively on a compact interval, with intersections only at endpoints. Let \(E\) be the finite set of those endpoints. Assume the boundary is \(C^1\) and locally one-sided at every point outside \(E\). Then (2.3) and (2.5) remain valid, with the outward normal on the open arcs and with line integrals oriented so that \(Y\) lies to the left. No normal or point mass is assigned to a corner. In particular the formulas apply to a half-disk and to a rectangle. For any \(a\in Y\), they also give

\[
 \int_{\partial Y}\frac{dz}{z-a}=2\pi i.
\]

**Proof.** On a regular arc \(\alpha:[a,b]\to\mathbb R^2\), a coordinate direction \(e\) with \(e\cdot\alpha'(t_0)\ne0\) has the same strict derivative sign on a small parameter interval. The mean value theorem makes its coordinate strictly monotone there, and the graph lemma identifies that part of the arc with a graph. The one-variable substitution formula and the chain rule give

\[
 \sqrt{1+|\gamma'(x)|^2}\,|dx|
       =|\alpha'(t)|\,dt.
\]

Compactness gives finitely many such parameter intervals. Additivity of their integrals, or a partition in the parameter, proves that the graph surface integral on the arc is its ordinary arclength integral. In particular its total length is finite.

There is also a uniform \(O(r)\) length bound near any endpoint \(p=\alpha(a)\). Choose a unit vector \(e\) with \(e\cdot\alpha'(a)>0\). On a small right interval, \(e\cdot\alpha'(t)\ge c>0\) and \(|\alpha'(t)|\le M\). Hence

\[
 |\alpha(t)-p|\ge e\cdot(\alpha(t)-p)\ge c(t-a).
\]

The part of that interval inside \(B(p,r)\) has length at most \(Mr/c\). The remaining compact part of the injective arc stays a positive distance from \(p\). At the other endpoint the same argument runs with the parameter reversed. Other arcs not incident to \(p\) stay a positive distance away. A simple closed regular curve can be split into arcs with distinct endpoints. Thus, for small \(r\), the length of \(\partial Y\cap B(p,r)\) is at most \(C_pr\).

For each \(p\in E\), take a smooth radial function \(\zeta_{p,\epsilon}\) which is zero on \(B(p,\epsilon)\), one outside \(B(p,2\epsilon)\), lies between zero and one, and has \(|\nabla\zeta_{p,\epsilon}|\le C/\epsilon\). It is obtained by scaling the fixed bump from the cutoff prerequisite. Put \(\zeta_\epsilon=\prod_{p\in E}\zeta_{p,\epsilon}\); if \(E\) is empty put \(\zeta_\epsilon=1\). Its gradient is supported in the union of these finitely many radius-\(2\epsilon\) balls and has bound \(C|E|/\epsilon\).

For \(A\in C_c^1(X;\mathbb C^2)\), the field \(\zeta_\epsilon A\) vanishes near every corner. The graph proof of Theorem 2.1 can therefore be localized on its support and gives

\[
 \int_Y\bigl(\zeta_\epsilon\operatorname{div}A
                   +A\cdot\nabla\zeta_\epsilon\bigr)\,dx
       =\int_{\partial Y}\zeta_\epsilon A\cdot\nu\,dS.
\]

The second volume term tends to zero: a radius-\(2\epsilon\) ball lies in a square of area \(16\epsilon^2\), so its absolute value is bounded by a fixed constant times \(\|A\|_\infty\epsilon\). The first volume term tends to \(\int_Y\operatorname{div}A\) by dominated convergence. The boundary term tends to \(\int_{\partial Y}A\cdot\nu\,dS\); the omitted portions have total length \(O(\epsilon)\) by the endpoint estimate. This proves (2.3). Substitution of \(A=(\phi,i\phi)\) and the same tangent computation as in Corollary 2.3 proves (2.5), including the distributional indicator identity. A half-disk has one regular semicircular arc and one segment, and a rectangle has four segments; their only exceptional points are their finitely many vertices.

For the last identity choose \(\rho>0\) with \(\overline{B(a,\rho)}\subset Y\). Apply the established complex Green formula to \(Y\setminus\overline{B(a,\rho)}\) and to \(1/(z-a)\), multiplied by a smooth compact cutoff equal to one near this closed punctured region and supported away from \(a\). Its \(\partial_{\bar z}\) derivative is zero on the punctured region, by the ordinary quotient rule. The inner boundary circle is clockwise, so the integral over \(\partial Y\) equals the counterclockwise integral over that circle. Parametrizing it by \(z=a+\rho(\cos t+i\sin t)\), \(0\le t\le2\pi\), makes \(dz/(z-a)=i\,dt\), with integral \(2\pi i\). \(\square\)

## Integration by parts with an integrable weak divergence

**Theorem 3.1 (continuous boundary values and weak divergence).** Suppose \(F\in C_c(X;\mathbb C^n)\), and its distributional divergence on \(Y\) is a function \(g\in L^1(Y)\). No divergence assumption is made outside \(Y\). Then, for every \(\phi\in C_c^1(X)\),

\[
 \begin{aligned}
 &\int_Y(g\phi+F\cdot\nabla\phi)\,dx\\
 &\qquad=\int_{\partial_XY}\phi F\cdot\nu\,dS.
 \end{aligned}
 \tag{3.1}
\]

In particular,

\[
 \int_Yg\,dx=\int_{\partial_XY}F\cdot\nu\,dS.
 \tag{3.2}
\]

**Proof.** The weak divergence identity extends to \(C_c^1(Y)\) tests. Extend such a test by zero, mollify it with a smooth compact unit-mass kernel, and use uniform convergence of the test and all its first derivatives. Their supports lie in a common compact subset of \(Y\) for sufficiently small scales. The integrals against \(g\) and the continuous \(F\) therefore converge. Expanding the product derivative then shows

\[
 \operatorname{div}(\psi F)=\psi g+F\cdot\nabla\psi
 \quad\text{on }Y
 \tag{3.3}
\]

for every compact \(C^1\) multiplier \(\psi\).

Use the partition lemma to split \(\phi\) into finitely many \(C_c^1\) functions supported in boundary, interior or exterior charts. It suffices to prove (3.1) for each part. An exterior part is zero on both sides. For an interior part, its left side is zero by the definition of divergence extended to \(C_c^1\) tests, and it has zero boundary values.

For a boundary part, put \(B=\phi F\) and \(G=\phi g+F\cdot\nabla\phi\) inside \(Y\). Their supports are contained in one fixed compact subset of the graph cylinder. Extend \(B\) by zero to \(\mathbb R^n\); it remains continuous and compactly supported. Extend \(G\) by zero outside \(Y\), writing the resulting \(L^1(\mathbb R^n)\) function as \(G_0\). Let \(\eta\ge0\) be a smooth kernel supported in the unit ball with integral one, and let \(\eta_\varepsilon(z)=\varepsilon^{-n}\eta(z/\varepsilon)\). Such a kernel is obtained by normalizing a nonzero bump from the cutoff prerequisite.

Bound \(|\nabla\gamma|\) by \(L\) on a compact base neighbourhood of the supports. For small \(h>0\), choose \(0<\varepsilon<h/[2(1+L)]\) and define

\[
 \begin{aligned}
 &B_{h,\varepsilon}(x)\\
 &\qquad=\int\eta_\varepsilon(z)B(x-he_n-z)\,dz.
 \end{aligned}
 \tag{3.4}
\]

These fields are smooth and have supports in one fixed compact subset of the original cylinder. If \(x=(x',t)\in Y\) in that cylinder and \(|z|\le\varepsilon\), then

\[
 t-h-z_n<\gamma(x')-h+\varepsilon
       <\gamma(x'-z')
\]

because \(|\gamma(x'-z')-\gamma(x')|\le L\varepsilon\). At every point where the convolution can be nonzero, its kernel thus tests only the interior of \(Y\). All kernel points also stay in the chart by the fixed support margin and smallness of \(h+\varepsilon\). The distributional identity (3.3), tested against the translated kernel, now gives

\[
 \begin{gathered}
 \operatorname{div}B_{h,\varepsilon}(x)
       =(\eta_\varepsilon*G_0)(x-he_n),\\
 x\in Y.
 \end{gathered}
 \tag{3.5}
\]

Outside the same compact chart neighbourhood both sides vanish. One can check the sign directly: the negative derivative in the input variable of \(\eta_\varepsilon(x-he_n-y)\) is its positive derivative in \(x\).

Apply (2.3) to the smooth field (3.4). Its boundary values converge uniformly to those of \(B\): the integration points are within \(h+\varepsilon\) of \(x\), and a continuous compactly supported function is uniformly continuous. Their boundary integrals converge, since the common compact support meets a finite amount of surface measure. On the other hand, translation continuity and the approximate-identity theorem in \(L^1\) give

\[
 \begin{aligned}
 &\|\tau_{he_n}(\eta_\varepsilon*G_0)-G_0\|_1\\
 &\quad\le\|\eta_\varepsilon*G_0-G_0\|_1
        +\|\tau_{he_n}G_0-G_0\|_1\\
 &\quad\longrightarrow0.
 \end{aligned}
\]

Hence the volume integral in (2.3) tends to \(\int_YG\), and the surface integral tends to \(\int_{\partial_XY}B\cdot\nu\). This proves (3.1) in the chart. Summing the partition pieces proves it globally; the derivatives of their factors sum to zero.

Finally choose \(\phi=1\) on a neighbourhood of \(\operatorname{supp}F\), with compact support in \(X\). The term \(F\cdot\nabla\phi\) vanishes. Also \(g=0\) almost everywhere in \(Y\setminus\operatorname{supp}F\): its distribution is zero there, and uniqueness of a locally integrable distribution gives this conclusion. That uniqueness follows by convolution with the same kernels and their \(L^1_{\rm loc}\) convergence. Thus \(g\phi=g\) almost everywhere, proving (3.2). \(\square\)

## Cubes and a pointwise equation with a rough gradient

A cube has corners, so we establish the formula needed here directly. For a closed coordinate cube \(Q\) and a continuous field \(A\) on its faces, write

\[
 \begin{aligned}
 \Phi_Q(A)&=\sum_{j=1}^n\int_{x_j=b_j}A_j\,dx_{\widehat j}\\
          &\qquad-\sum_{j=1}^n\int_{x_j=a_j}A_j\,dx_{\widehat j}.
 \end{aligned}
 \tag{4.1}
\]

For an affine field \(A(y)=v+M(y-x)\), integration of each opposing pair gives \(\Phi_Q(A)=\operatorname{tr}(M)|Q|\). The constant terms and all off-diagonal terms cancel; the diagonal term is \(M_{jj}(b_j-a_j)\) times the area of that face. The same formula for a \(C^1\) field follows by Fubini and the one-dimensional fundamental theorem. These statements include \(n=1\), where a face integral is its endpoint value.

**Finite tagged-partition lemma.** If \(Q\) is a closed cube and \(\delta:Q\to(0,\infty)\) is any function, there is a finite subdivision of \(Q\) into closed dyadic cubes with disjoint interiors, with one tag \(x_R\in R\) per cube, such that \(R\subset B(x_R,\delta(x_R))\).

**Proof.** Call a dyadic cube good if it admits such a finite partition. If all its \(2^n\) children are good, their finitely many partitions combine to make it good. If \(Q\) were bad, choose a bad child, then a bad child of that child, indefinitely. The resulting nested closed cubes have side lengths tending to zero. For each coordinate their nested intervals have a unique common point, obtained as the supremum of the left endpoints; it is no larger than every right endpoint, and their lengths tending to zero give uniqueness. Thus the cubes have a common point \(x\). A sufficiently small member has diameter less than \(\delta(x)\) and contains \(x\), so its one-cube partition with tag \(x\) is good. This contradiction proves the assertion. \(\square\)

This is the finite-partition principle used in Kudryashov's freely accessible proof of the divergence theorem. For the continuous-divergence case needed below, no theory of generalized integration is required.

**Cube flux lemma.** Let \(A\) be real Fréchet differentiable at every point of a neighbourhood of \(Q\), with values in \(\mathbb C^n\). Suppose \(q=\sum_j\partial_jA_j\) is continuous there. Individual entries of \(DA\) need not be continuous or integrable. Then

\[
 \Phi_Q(A)=\int_Qq(x)\,dx.
 \tag{4.2}
\]

**Proof.** Fix \(\epsilon>0\). At every \(x\in Q\) choose \(\delta(x)>0\) small enough that, for \(y\in Q\) with \(|y-x|<\delta(x)\),

\[
 \begin{gathered}
 |A(y)-A(x)-DA(x)(y-x)|\le\epsilon|y-x|,\\
 |q(y)-q(x)|\le\epsilon.
 \end{gathered}
\]

Apply the finite tagged-partition lemma. For a cube \(R\) of side \(s\) with tag \(x_R\), its affine approximation has flux \(q(x_R)|R|\). On each of its \(2n\) faces the error is at most \(\epsilon\sqrt n\,s\); the face area is \(s^{n-1}\). Consequently

\[
 \begin{aligned}
 |\Phi_R(A)-q(x_R)|R||&\le2n\sqrt n\,\epsilon|R|,\\
 \left|\int_Rq-q(x_R)|R|\right|&\le\epsilon|R|.
 \end{aligned}
\]

Sum over the finite partition. Interior face contributions cancel with their opposite normals. When faces have different sizes, subdivide all faces to the finest dyadic level occurring in this finite partition; their coordinate integrals are additive on that common refinement. Face edges have zero face measure, and in dimension one each shared endpoint cancels once with each sign. Volume integrals also add, since cube boundaries are null. We obtain

\[
 \left|\Phi_Q(A)-\int_Qq\right|
      \le(2n\sqrt n+1)\epsilon|Q|.
\]

Let \(\epsilon\) tend to zero. All integrals used in this proof are of continuous functions on cubes or their faces. \(\square\)

**Theorem 4.1 (pointwise first-order equations imply weak equations).** Let

\[
 \begin{gathered}
 P=\sum_{j=1}^na_j(x)\partial_j+b(x),\\
 a_j\in C^1(X;\mathbb C),\quad b\in C(X;\mathbb C).
 \end{gathered}
\]

Suppose \(u:X\to\mathbb C\) is real Fréchet differentiable at every point and its pointwise value \(Pu=f\) is continuous. Then

\[
 \begin{gathered}
 -\int_Xu\sum_j\partial_j(a_j\phi)\,dx
          +\int_Xbu\phi\,dx\\
 \qquad=\int_Xf\phi\,dx,
 \qquad\phi\in C_c^\infty(X).
 \end{gathered}
 \tag{4.3}
\]

This is the distributional equation with the given \(C^1\) coefficients; it does not assert that the pointwise derivatives of \(u\) define locally integrable functions.

**Proof.** First suppose \(\phi\) is supported in the interior of a closed cube \(Q\Subset X\). Define the everywhere differentiable field \(A=\phi u(a_1,\ldots,a_n)\). The finite-dimensional product rule gives the pointwise identity

\[
 \operatorname{div}A
   =\phi(f-bu)+u\sum_j\partial_j(a_j\phi).
 \tag{4.4}
\]

Its right side is continuous: differentiability makes \(u\) continuous, and all the other displayed factors are continuous by hypothesis. The cube flux lemma therefore applies. Since \(A=0\) near the boundary of \(Q\), its flux is zero. Integrating (4.4) and rearranging proves (4.3).

For a general compact test, use the partition lemma with cube interiors compactly contained in \(X\). Only finitely many partition factors meet its support. Apply the proved identity to those finitely many tests and sum; their sum and the sums of their derivatives are exactly the original test and its derivatives. Finally, the left side of (4.3) is a continuous distributional functional: on any fixed compact test support it is bounded by a constant times \(\sup|\phi|+\sup|\nabla\phi|\). Thus (4.3) has the asserted distributional meaning even though the coefficients need be only \(C^1\). \(\square\)

## Exercises

1. **An affine interface and its density — foundation.** Let \(v\in\mathbb R^{n-1}\), \(c\in\mathbb R\), and \(Y=\{(x',t):t<v\cdot x'+c\}\). Define \(M(h)=\int h(x',v\cdot x'+c)\,dx'\). Compute \(\nabla\chi_Y\), \(dS\), and \(\nabla(w\chi_Y)\) for any \(w\in C^1(\mathbb R^n)\). Specialize to \(n=2,v=2,c=0,w=1+x^2\).
2. **The two sides of a shell — intermediate.** For \(0<a<b\) and \(n\ge2\), use \(\rho=(|x|^2-a^2)(|x|^2-b^2)\) to determine the two outward normals of \(Y=\{a<|x|<b\}\). Find \(\nabla\chi_Y\). Prove that the two fluxes of \(x/|x|^n\) have equal magnitudes and opposite signs, including the surface-scaling calculation.
3. **A rough tangential dependence — intermediate.** Let \(Y=\{(x,y):y<x^2\}\), let \(h:\mathbb R\to\mathbb C\) be any continuous function, and let \(\eta\in C_c^\infty(\mathbb R^2)\). For \(F=(0,h(x)\eta(x,y))\), calculate the weak divergence and the two sides of (3.2). Take \(h(x)=|x|^{1/2}\) to exhibit failure of an ordinary partial derivative that is not needed by the formula.
4. **An exceptional point cannot simply be discarded — advanced.** Choose \(p\in(0,1)^n\) with no dyadic-rational coordinate. On dyadic subcubes put \(D(R)=1\) if \(p\in R\), and \(D(R)=0\) otherwise. Prove finite dyadic additivity, and prove that \(D(R)/|R|\) tends to zero along shrinking cubes containing any fixed \(x\ne p\). Explain why almost-everywhere local error control cannot replace the everywhere control used when choosing the gauge in the cube flux lemma.
5. **A continuous equation with a nonintegrable derivative — advanced.** Set \(u(0)=0\) and \(u(x)=x^3\sin(x^{-4})\) for \(x\ne0\). Prove that \(u\) is everywhere differentiable but \(u'\notin L^1_{\rm loc}\). Compute the continuous function \(f=x^3u'\) and write the exact weak equation on a test. Also give the corresponding calculation for \(v(0)=0,v(x)=x^2\sin(x^{-2})\) and the coefficient \(x^2\).
6. **Orientation in the complex plane — foundation.** Let \(Y=\{|z|<R\}\). Choose \(\phi\in C_c^\infty(\mathbb C)\) equal to \(\bar z\) near \(\overline Y\). Evaluate \(\langle\partial_{\bar z}\chi_Y,\phi\rangle\) from the volume definition and from the counterclockwise boundary integral. Then perform the same comparison for the annulus \(a<|z|<b\), recording the orientation on both circles.

## Complete solutions

**Solution 1.** The normal is \((-v,1)/\sqrt{1+|v|^2}\) and \(dS=\sqrt{1+|v|^2}\,M\). Equations (2.2) and (2.4) give

\[
 \begin{aligned}
 \nabla\chi_Y&=(v,-1)M,\\
 \nabla(w\chi_Y)&=\chi_Y\nabla w+w(v,-1)M.
 \end{aligned}
\]

Values multiplying \(M\) are restricted to the graph. In the stated planar case this reads

\[
 \begin{gathered}
 \partial_x\chi_Y=2M,\qquad\partial_y\chi_Y=-M,\\
 \partial_x[(1+x^2)\chi_Y]=2x\chi_Y+2(1+x^2)M,\\
 \partial_y[(1+x^2)\chi_Y]=-(1+x^2)M.
 \end{gathered}
\]

Thus the parameter measure \(M\) is not Euclidean arclength; the latter is \(\sqrt5 M\).

**Solution 2.** The function \(\rho\) has the required signs, and

\[
 \nabla\rho=2x(2|x|^2-a^2-b^2).
\]

At radius \(a\) this points as \(-x\), and at radius \(b\) it points as \(x\); neither value is zero. Hence the normals are \(-x/a\) and \(x/b\), and

\[
 \nabla\chi_Y=(x/a)dS_a-(x/b)dS_b.
\]

For a sphere graph \(t=\gamma(x')\), dilation by \(r>0\) produces \(t=r\gamma(x'/r)\). Its graph density is \(\sqrt{1+|\nabla\gamma(x'/r)|^2}\), while the base substitution has Jacobian \(r^{n-1}\). A finite partition on the compact unit sphere proves \(S(S_r^{n-1})=r^{n-1}\omega_n\), where \(\omega_n=S(S^{n-1})\). The field \(V=x/|x|^n\) has normal components \(-a^{1-n}\) and \(b^{1-n}\) on the two boundaries. Its fluxes are therefore \(-\omega_n\) and \(\omega_n\).

Direct differentiation gives \(\operatorname{div}V=n|x|^{-n}-n|x|^{-n-2}|x|^2=0\) away from zero. Multiplying by a smooth cutoff supported away from zero and equal to one near the closed shell puts the field within (2.3) without changing either flux or its divergence on \(Y\). The flux cancellation agrees with that formula.

**Solution 3.** Fubini and integration by parts in \(y\) give

\[
 \operatorname{div}F=h(x)\partial_y\eta(x,y).
\]

It is continuous and compactly supported. Integrating from \(y=-\infty\) to \(y=x^2\) yields

\[
 \int_Y\operatorname{div}F\,dx\,dy
       =\int_{\mathbb R}h(x)\eta(x,x^2)\,dx.
\]

The boundary normal times its graph measure is \((-2x,1)\,dx\), so the surface flux is the same integral. For \(h(x)=|x|^{1/2}\), wherever \(\eta(0,y)\ne0\) the \(x\)-difference quotient of the second component has unbounded magnitude as \(x\to0\). This derivative is not part of divergence, and the continuous boundary values already specify the flux.

**Solution 4.** A parent containing \(p\) has exactly one child containing \(p\), since \(p\) lies on no dyadic face. A parent not containing \(p\) has none. Thus the child values sum to the parent value; repeating proves finite dyadic additivity. For fixed \(x\ne p\), every cube containing \(x\) with diameter less than \(|x-p|\) misses \(p\), so its density is zero. The nested cubes containing \(p\), however, have density \(1/|R|\), tending to infinity, and the original cube has value one.

The flux proof must choose a positive gauge at every possible tag, including this point. The exceptional set consisting of \(p\) is null, but it can carry the entire additive defect. Discarding it would leave the gauge estimate unjustified on cubes tagged there. This example concerns the proof's needed hypothesis; it does not assert that \(D\) comes from an everywhere differentiable field.

**Solution 5.** The quotient \(u(x)/x=x^2\sin(x^{-4})\) tends to zero, so \(u'(0)=0\). For \(x\ne0\),

\[
 \begin{aligned}
 u'(x)&=3x^2\sin(x^{-4})-4x^{-2}\cos(x^{-4}),\\
 f(x)&=3x^5\sin(x^{-4})-4x\cos(x^{-4}).
 \end{aligned}
\]

The first term of \(u'\) is absolutely integrable near zero. In the other term, the substitution \(s=x^{-4}\) on positive compact intervals, followed by monotone convergence, gives

\[
 \begin{aligned}
 &\int_0^\epsilon4x^{-2}|\cos(x^{-4})|\,dx\\
 &\qquad=\int_{\epsilon^{-4}}^\infty s^{-3/4}|\cos s|\,ds=\infty.
 \end{aligned}
\]

Indeed, in each sufficiently large period choose a fixed-length interval where \(|\cos s|\ge1/2\). Its contribution is bounded below by a positive constant times \(k^{-3/4}\). These terms diverge: the terms with \(2^m\le k<2^{m+1}\) have sum at least \(2^m(2^{m+1})^{-3/4}\). The integrable first term cannot cancel this failure of absolute integrability, by the triangle inequality. Both terms of \(f\) tend to zero, agreeing with \(x^3u'(x)\) at zero. Theorem 4.1 gives

\[
 -\int u(x)[x^3\phi(x)]'\,dx=\int f(x)\phi(x)\,dx.
\]

For the second function, \(v'(0)=0\) because \(v(x)/x=x\sin(x^{-2})\to0\), while

\[
 \begin{aligned}
 v'&=2x\sin(x^{-2})-2x^{-1}\cos(x^{-2}),\\
 x^2v'&=2x^3\sin(x^{-2})-2x\cos(x^{-2})=:g(x).
 \end{aligned}
\]

Now the absolute integral of the second derivative term is \(\int_{\epsilon^{-2}}^\infty |\cos s|s^{-1}\,ds\), which diverges by the same fixed subinterval argument and dyadic grouping of \(\sum k^{-1}\). The continuous extension has \(g(0)=0\), and the weak identity is \(-\int v(x)[x^2\phi(x)]'\,dx=\int g(x)\phi(x)\,dx\). These are integrals of continuous compactly tested functions, never integrals of the nonintegrable pointwise derivatives.

**Solution 6.** Since \(\partial_{\bar z}\bar z=1\), the volume pairing on the disk is \(-\pi R^2\). On its counterclockwise boundary, \(z=Re^{it}\) gives \(\bar z\,dz=iR^2dt\). The boundary expression is

\[
 \frac i2\int_0^{2\pi}iR^2\,dt=-\pi R^2.
\]

For the annulus the outer circle is counterclockwise and the inner circle clockwise. The two contributions to \((i/2)\int\bar z\,dz\) are respectively \(-\pi b^2\) and \(+\pi a^2\). Their sum is \(-\pi(b^2-a^2)\), the negative area of the annulus, as required by the volume pairing.

## Programme proof locations and freely accessible sources

The exact programme entries needed for this lesson are:

- **Scalar calculus and Euclidean topology**, selected from programme lesson AN03-P003: [Sections 12.1–12.3, the real field](../prerequisites/U011-free-foundations/metric-foundation-bridges.md#12-real-numbers-and-finite-dimensional-topology); [12.4–12.9, Euclidean topology and finite norms](../prerequisites/U011-free-foundations/metric-foundation-bridges.md#12-4-square-roots-and-the-full-euclidean-distance); [13.1–13.5, limits, mean values and calculus](../prerequisites/U011-free-foundations/metric-foundation-bridges.md#13-1-limits-with-all-original-scalar-and-coordinate-factors); [13.7–13.9, series, exponential and trigonometric functions](../prerequisites/U011-free-foundations/metric-foundation-bridges.md#13-7-uniform-limits-and-differentiation-of-the-actual-series); and [13.10, smooth cutoffs](../prerequisites/U011-free-foundations/metric-foundation-bridges.md#13-10-the-actual-smooth-cutoff-with-all-endpoint-constants).
- **Complex scalars and finite algebra**, selected from programme lesson AN03-P002: [Sections 10.1–10.6](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md#10-full-finite-linear-algebra-foundations) supply the complex arithmetic, finite bases and norm comparisons used in the scalar and measure prerequisites.
- **Lebesgue integration and smoothing**, selected from programme lesson AN03-P004: [Sections 15.0–15.2, measure, convergence, Fubini and integral estimates](../prerequisites/U011-free-foundations/banach-foundation-bridges.md#15-0-constructing-the-measure-without-importing-a-convergence-theorem); [15.3–15.4, translation continuity and mollification](../prerequisites/U011-free-foundations/banach-foundation-bridges.md#15-3-completeness-and-compact-smooth-density); [15.6 through the sector-area calculation, disk area](../prerequisites/U011-free-foundations/banach-foundation-bridges.md#15-6-the-full-polar-formula-on-the-original-plane); and [16.1–16.2, measurable functions and measure uniqueness](../prerequisites/U011-free-foundations/banach-foundation-bridges.md#16-1-measures-completions-measurable-limits-and-the-full-nonnegative-integral). Only scalar \(L^1\) and finite-dimensional cases are needed here.

The linked selections include the proof text and retain their GFDL 1.2 licence notices. The real-field construction starts from natural-number arithmetic with induction, ordinary set theory and countable choice; the selected algebra, topology, calculus and integration sections build on it. The following freely accessible publications informed the proofs written in this lesson:

- Michael Kunzinger, *Theory of Distributions*, University of Vienna, 2019, Section 3.3, Theorem 3.3.1 and Corollary 3.3.2. [Author's free lecture notes](https://www.mat.univie.ac.at/~mike/teaching/ss19/distributions.pdf). Those notes give the multidimensional jump formula; the proof above constructs the \(C^1\) graph measure and flux identity directly.
- Yury Kudryashov, *Formalizing the Divergence Theorem and the Cauchy Integral Formula in Lean*, ITP 2022, Sections 4.4 and 4.9. [Free paper and source metadata](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITP.2022.23), [author's source](https://github.com/urkud/divthm-paper). The paper is distributed under CC BY 4.0. Its finite tagged partitions and affine face estimates inform the complete continuous-divergence specialization proved here; the broader generalized-integral theorem is not assumed.
- Gui-Qiang G. Chen and Monica Torres, *Divergence-Measure Fields: Gauss-Green Formulas and Normal Traces*, 2021 author version. [Free arXiv text](https://arxiv.org/html/2005.10949v3). It explains one-sided normal-trace approximation. Theorem 3.1 above supplies a direct proof in the continuous-field, \(C^1\)-boundary case, with integrable divergence required only on the inside.
