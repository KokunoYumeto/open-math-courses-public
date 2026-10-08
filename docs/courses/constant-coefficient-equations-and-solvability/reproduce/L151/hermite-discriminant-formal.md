# Hermite interpolation and local division with a discriminant

*Original proof exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

Root collisions increase the size of an interpolating polynomial. The full jets at each root determine its remainder, and a discriminant measures the resulting loss. We prove a uniform division theorem on a smaller complex Euclidean ball, including collisions at the central parameter. Its estimate uses the derivative strength of the discriminant, not just its value at the center.

Our complex variables are \(z=(t,y)\in\mathbb C\times\mathbb C^{n-1}\). All polynomial derivatives are ordinary complex derivatives. Use Euclidean complex balls and their real Lebesgue measure \(dV\). Surface measure \(dS\) on a hypersurface is the Euclidean real \(2n-2\) dimensional area; on its smooth graph charts this is the induced area measure. In dimension one it is counting measure on isolated points.

The actual complex-analysis inputs are [L045, Cauchy estimates, parameter contours and root counts](../../AN02-L045.html#cauchy-estimates-and-parameter-contours). The scalar logarithm, its submean inequality and local integrability are proved in [L147 GD4](../../AN02-L147.html#gd4-scalar-holomorphic-logarithms-are-proper-psh-and-locally-integrable); its calculation applies on any connected local holomorphic domain as well as to entire functions. We give the finite Hermite formula, uniform root circle, holomorphic local factors, contour remainder, weighted mean estimate and surface projection inequality in full. Only finite polynomial factorization, finite-dimensional compactness and ordinary determinant algebra are additional entries.

## H1. Root-distance conventions and the full Hermite estimate

Let \(t_1,\ldots,t_\nu\) be distinct points of the unit disk. Let their positive multiplicities be \(\mu_j\), with
\[
\mu=\sum_{j=1}^{\nu}\mu_j,\qquad
\bar\mu=\max_j\mu_j,\qquad
D=\prod_{i<j}|t_i-t_j|,\qquad
\Delta=\prod_{i\ne j}|t_i-t_j|=D^2.
\tag{H1}
\]
Empty products are one. For every polynomial \(q\) of degree at most \(\mu-1\),
\[
\begin{aligned}
D^{\,2\bar\mu-1}\sup_{|t|<1}|q(t)|
&\le C_\mu\sum_j\sum_{a<\mu_j}|q^{(a)}(t_j)|,\\
\Delta^{\,2\bar\mu-1}\sup_{|t|<1}|q(t)|
&\le C'_\mu\sum_j\sum_{a<\mu_j}|q^{(a)}(t_j)|.
\end{aligned}
\tag{H2}
\]
The second is the ordered-product version. We prove the stronger first version because the usual monic discriminant has modulus \(D^2\), so this version gives the correct half-integer discriminant exponent.

Put
\[
p_j(t)=\prod_{i\ne j}(t-t_i)^{\mu_i},\qquad
q_j(t)=\sum_{b<\mu_j}\frac{(q/p_j)^{(b)}(t_j)}{b!}(t-t_j)^b.
\tag{H3}
\]
The quotient is analytic near \(t_j\), since \(p_j(t_j)\ne0\). The difference
\(q-\sum_jq_jp_j\) has a zero of order at least \(\mu_j\) at each \(t_j\): its \(j\)-term agrees with \(q\) to that order, while every other \(p_i\) contains \((t-t_j)^{\mu_j}\). Successive one-variable factor division makes the difference divisible by the degree-\(\mu\) product
\(\prod_j(t-t_j)^{\mu_j}\). Its degree is at most \(\mu-1\), so it vanishes identically. Thus
\[
q(t)=\sum_jq_j(t)p_j(t).
\tag{H4}
\]
This also proves uniqueness of the Hermite interpolant: a polynomial of degree below \(\mu\) with all the specified jets zero is zero.

For \(|w|<\min_{i\ne j}|t_j-t_i|\), the reciprocal factors have the convergent expansion
\[
(t_j+w-t_i)^{-\mu_i}
=\sum_{l\ge0}(-1)^l
 \binom{\mu_i+l-1}{l}
 (t_j-t_i)^{-\mu_i-l}w^l.
\tag{H5}
\]
This is the binomial series, obtained by differentiating the geometric series \(\mu_i-1\) times and dividing by its factorial. Multiplication gives the coefficient of \(w^l\) in \(1/p_j(t_j+w)\) as a sum over \(l_i\ge0\), \(\sum_{i\ne j}l_i=l\), of products of the factors in H5. Only \(l<\mu_j\) is needed. Each denominator exponent obeys
\[
\mu_i+l_i\le\mu_i+\mu_j-1\le2\bar\mu-1=:S.
\tag{H6}
\]
There are finitely many such coefficients, and all their binomial and factorial constants are bounded in terms of \(\mu\).

For any one denominator product, multiplication by \(D^S\) cancels every required pair distance at least once with exponent \(S\). The distances of pairs incident with \(j\) occur with residual exponent \(S-\mu_i-l_i\ge0\); all other pair distances have exponent \(S\). Each distance is at most two. Hence the product after multiplication is bounded by \(2^{S\nu(\nu-1)/2}\), which depends only on \(\mu\). The Taylor product with \(q(t_j+w)\) therefore gives
\[
D^S\sum_{b<\mu_j}
\left|\frac{(q/p_j)^{(b)}(t_j)}{b!}\right|
\le C_\mu\sum_{a<\mu_j}|q^{(a)}(t_j)|.
\tag{H7}
\]
For \(|t|<1\), \(|t-t_j|\le2\) and
\(|p_j(t)|\le2^{\mu-\mu_j}\). Substitute these estimates and H7 in H4 to prove the first part of H2. Also
\(D\le2^{\nu(\nu-1)/2}\), so multiplication by the additional factor \(D^S\) proves its ordered-product version. Neither proof assumes that \(D\) is at most one.

For a larger chosen exponent \(S'\ge S\), boundedness of \(D\) gives the same estimate with a changed constant whenever \(S'\) has a fixed bound in terms of the total multiplicity. We will use \(S'=2\bar m-1\) below even if the roots in a particular local cluster have smaller maximal multiplicity.

![Exact double-node collision and root-product scales](figures/hermite-collision-and-root-products.png)

**Figure H-A.** For the exact double nodes \(0,\varepsilon\), the cubic with data \(0,0,-1,0\) has disk supremum \(3\varepsilon^{-2}+2\varepsilon^{-3}\), attained at the boundary point \(-1\). Its unordered normalization is \(2+3\varepsilon\); its ordered normalization is \(2\varepsilon^3+3\varepsilon^4\). The left curves are explicitly real slices of the normalized polynomial. Learner Example 1 proves every value; H1–H7 prove the uniform estimate with all complex nodes and multiplicities.

## H2. The exact local division theorem

For any polynomial \(A\) in \(d\) complex variables, define its derivative strength at zero by
\[
\widetilde A(0)=
\left(\sum_\alpha|\partial^\alpha A(0)|^2\right)^{1/2}.
\tag{H8}
\]
Only derivatives up to its degree contribute. For zero variables this is the absolute value of the constant. The strength is positive if and only if the polynomial is nonzero.

Let \(Q_1,\ldots,Q_s\) have positive degrees \(d_j\), with highest homogeneous part equal to one at \((1,0,\ldots,0)\). Equivalently each \(Q_j(t,y)\) is monic of degree \(d_j\) in \(t\); its coefficient of \(t^{d_j}\) is the constant one. Let \(m_j\ge1\), and write
\[
Q=\prod_j Q_j^{m_j},\qquad
m=\sum_jm_jd_j,\qquad
\bar m=\max_jm_j,\qquad
A_0=\widetilde Q(0).
\tag{H9}
\]
A constant monic factor is one and is omitted when listing the factors and their multiplicities. In particular \(\bar m\le m\).
Assume that for a fixed \(M>0\),
\[
A_0\le M\sup_{|t|<1}|Q(t,0)|.
\tag{H10}
\]
Let \(R(y)\) be the usual monic discriminant of
\(Q_*(t,y)=\prod_jQ_j(t,y)\), and assume it is not identically zero. With the roots of \(Q_*(\cdot,y)\), counted with multiplicity, it has
\[
|R(y)|=\prod_{\alpha<\beta}
                  |a_\alpha(y)-a_\beta(y)|^2.
\tag{H11}
\]
The harmless sign in the algebraic product does not affect any estimate. It is a polynomial in \(y\): the monic resultant determinant of \(Q_*\) and its \(t\)-derivative supplies it, up to that sign. If \(d_*=\sum_jd_j\le m\), its degree in \(y\) is at most \(d_*(2d_*-1)\), since the determinant has \(2d_*-1\) rows and each polynomial coefficient has degree at most \(d_*\). This loose bound is sufficient.

**Theorem H2.** There are \(c,C>0\), depending only on \(n,m,M\), such that every holomorphic \(f\) on the unit Euclidean ball has
\[
f(z)=Q(z)g(z)+h(z)\quad(|z|<c),
\tag{H12}
\]
where \(g,h\) are holomorphic there and \(h(t,y)\) is a polynomial in \(t\) of degree less than \(m\). Moreover
\[
\widetilde R(0)^{\,\bar m-1/2}
\sup_{|z|<c}|h(z)|
\le C A_0^{\,K}
\sum_{j=1}^{s}\sum_{a<m_j}
\int_{\{Q_j=0\}\cap\{|z|<1\}}
               |\partial_t^a f(z)|\,dS_j(z).
\tag{H13}
\]
One admissible loose exponent is \(K=m^3\). The integral is an \(L^1\) surface integral. If its right side is infinite, the inequality has its ordinary extended meaning; the analytic decomposition is still constructed. The discriminant may vanish at \(y=0\). Replacing \(\widetilde R(0)\) by \(|R(0)|\) would weaken the claim and make it vacuous at such a collision.

## H3. A root circle chosen uniformly from the normalized coefficients

The coefficient of \(t^m\) in \(Q\) is one, so
\(A_0\ge|\partial_t^mQ(0)|=m!\ge1\).
The univariate polynomial \(p(t)=Q(t,0)/A_0\) belongs to the compact family
\[
\mathcal F=
\left\{\sum_{l=0}^{m}b_lt^l:
 |b_l|\le1/l!,\
 \sup_{|t|\le1}|p(t)|\ge1/M\right\}.
\tag{H14}
\]
The coefficient bounds come directly from H8; H10 gives the lower supremum. The supremum on the closed disk equals that on the open disk by continuity. The family is closed and bounded in a finite-dimensional space, and contains no zero polynomial. It allows a leading coefficient to approach zero; a degree-drop limit is harmless.

For each member choose a radius \(\rho\in(1/3,2/3)\) whose circle contains no zero. Such a radius exists because a nonzero polynomial has finitely many roots. Its positive boundary minimum persists for all polynomials in a coefficient neighborhood of that member. A finite cover of \(\mathcal F\) gives a common \(b>0\), depending only on \(m,M\), such that for every \(Q\) one of those circles satisfies
\[
|Q(t,0)|\ge b A_0\quad(|t|=\rho).
\tag{H15}
\]
This is a uniform bound although the selected circle may depend on \(Q\).

The finite Taylor expansion of \(Q/A_0\) at zero bounds all its first derivatives on \(|z|\le1\) by a constant depending only on \(n,m\). Choose \(0<\rho'<1/12\), depending only on \(n,m,M\), small enough that the following band remains in \(|z|<1\), and the Taylor difference from the nearest point of the central circle is at most \(bA_0/2\):
\[
|Q(t,y)|\ge(b/2)A_0
\quad\left(\bigl||t|-\rho\bigr|\le\rho',\ |y|<\rho'\right).
\tag{H16}
\]
For example the segment length is at most \(\sqrt2\,\rho'\), so the uniform derivative bound supplies this choice. Because \(\rho<2/3\), all these segments lie in a fixed smaller ball once \(\rho'<1/12\). Thus every \(Q_j\) is zero-free on that band. The roots inside the selected circle have modulus below \(\rho-\rho'\), and all roots outside have modulus above \(\rho+\rho'\).

## H4. Holomorphic local factors and the contour remainder

For \(|y|<\rho'\), each \(Q_j(\cdot,y)\) has a fixed number \(\nu_j\) of roots inside \(|t|<\rho\), counted with multiplicity. Indeed its nonvanishing contour values vary continuously; the root count of L045 is an integer-valued continuous function on the connected parameter ball. Its power sums are
\[
s_{j,l}(y)=\frac1{2\pi i}
\int_{|w|=\rho}w^l
\frac{\partial_wQ_j(w,y)}{Q_j(w,y)}\,dw
\quad(l\ge1).
\tag{H17}
\]
They are holomorphic in \(y\) by fixed-contour differentiation. The logarithmic derivative of the factored univariate polynomial is a sum of reciprocal root factors, including their multiplicities; the Cauchy formula evaluates H17 as the indicated sum of root powers.

Newton's identities express the elementary symmetric functions of these \(\nu_j\) roots polynomially in the first \(\nu_j\) power sums, with fixed scalar denominators. One direct verification is to expand
\(\prod_\ell(1-a_\ell u)\), differentiate it logarithmically as a formal polynomial series, and compare coefficients in
\(-\sum_{l\ge1}s_{j,l}u^{l-1}\).
Thus the monic root polynomial \(q_j(t,y)\) of the inside cluster has holomorphic coefficients even through root collisions and permutations. Since the roots have modulus below \(2/3\), its coefficient of order \(l\) is bounded by
\(\binom{\nu_j}{l}(2/3)^l\), uniformly.

Monic polynomial long division of \(Q_j\) by \(q_j\) has holomorphic quotient coefficients. For every fixed \(y\) the remainder is zero, by the root factorization, so the quotient \(b_j\) is an exact holomorphic polynomial. It is zero-free for \(|t|<\rho\), since it contains only outside roots. Put
\[
q=\prod_jq_j^{m_j},\qquad
\mu=\deg_tq\le m,\qquad
B=\prod_jb_j^{m_j},\qquad Q=qB.
\tag{H18}
\]
The function \(B\) is holomorphic and zero-free on the cylinder
\(|t|<\rho,\ |y|<\rho'\). The empty cluster has \(q=1\).

The entire contour \((w,y)\), \(|w|=\rho,\ |y|<\rho'\), lies inside the unit **Euclidean ball**, because
\(\rho^2+\rho'^2< (2/3)^2+(1/3)^2<1\).
Thus its values of \(f\) are available without extending \(f\) to a unit polydisk. Define
\[
h(t,y)=\frac1{2\pi i}
\int_{|w|=\rho}
f(w,y)\,
\frac{q(w,y)-q(t,y)}{(w-t)q(w,y)}\,dw .
\tag{H19}
\]
The divided difference in its numerator is a polynomial in \(t\) of degree below \(\mu\), with holomorphic parameter coefficients. No inside root is on the circle. Thus \(h\) is holomorphic on this cylinder and polynomial of degree below \(\mu\) in \(t\). For \(\mu=0\) its numerator is zero, so \(h=0\).
The disk Cauchy formula also gives
\[
f(t,y)-h(t,y)
=q(t,y)\frac1{2\pi i}
\int_{|w|=\rho}
\frac{f(w,y)}{(w-t)q(w,y)}\,dw
=Q(t,y)g(t,y),
\tag{H20}
\]
where the last integral is divided by the zero-free \(B(t,y)\). Hence \(g\) is holomorphic there. Take eventually
\(c\le\min(\rho'/4,1/12)\); the required smaller Euclidean ball lies in this cylinder.

## H5. A discriminant-weighted estimate on each generic fiber

At a parameter with \(R(y)\ne0\), all roots of all \(Q_j(\cdot,y)\) are simple and mutually distinct. If \(t_i\) is an inside root of \(Q_j\), then \(f-h=Qg\) has a zero of order at least \(m_j\) there. Thus
\[
\partial_t^a h(t_i,y)=\partial_t^a f(t_i,y)
\quad(0\le a<m_j).
\tag{H21}
\]
Apply H2 to the inside roots with those multiplicities. Its stronger unordered-product bound, and the final observation of H1 if fewer multiplicities occur, show
\[
D_{\mathrm{in}}^{\,2\bar m-1}
\sup_{|t|<\rho}|h(t,y)|
\le C_m
\sum_j\sum_{a<m_j}
\sum_{\substack{Q_j(t_i,y)=0\\|t_i|<\rho}}
|\partial_t^a f(t_i,y)|.
\tag{H22}
\]
The degree of \(h\) is below the total inside multiplicity, which is exactly the hypothesis needed here.

For \(|y|<\rho'<1\), every coefficient of \(Q(\cdot,y)\) is bounded by \(C_{n,m}A_0\), by its Taylor expansion at zero. The elementary monic root bound gives
\[
|a_\alpha(y)|\le1+\max_{l<m}|[t^l]Q(t,y)|
\le C_{n,m}'A_0.
\tag{H23}
\]
To verify the first bound, if \(|t|>1+\max|c_l|\), then
\(\sum_{l<m}|c_l||t|^l<|t|^m\), so the monic term cannot be cancelled. Every root of \(Q_*\) is also a root of \(Q\), making H23 applicable to all of them.

Split H11 into inside-inside pairs and all other pairs. Each remaining distance is bounded by twice the root bound in H23. Hence, with \(a_*=\bar m-1/2\),
\[
|R(y)|^{a_*}
\le C_{n,m}A_0^{m^3}D_{\mathrm{in}}^{\,2\bar m-1}.
\tag{H24}
\]
There are at most \(m(m-1)/2\) pairs. Their total exponent after raising the squared product to \(a_*\) is at most
\(m(m-1)(m-1/2)<m^3\), and \(A_0\ge1\) permits the written looser exponent. This is the usual discriminant relation with the **unordered** distance product. The ordered product in H1 is its square; replacing one by the other inside this step would change the exponent.

Combining H22 and H24 gives the uniform fiber estimate
\[
|R(y)|^{a_*}\sup_{|t|<\rho}|h(t,y)|
\le C A_0^{m^3}
\sum_j\sum_{a<m_j}
\sum_{\substack{Q_j(t_i,y)=0\\|t_i|<\rho}}
|\partial_t^a f(t_i,y)|.
\tag{H25}
\]
It holds on the complement of the discriminant zeros, which has full parameter measure. The logarithm argument in the next section proves that a nonzero polynomial has a null zero set as well as proving the needed weighted estimate.

## H6. Replace the discriminant value by its derivative strength

Here is the complete polynomial-weighted holomorphic mean estimate needed to pass H25 to H13.

**Lemma H6.** Fix a degree bound \(L\), a radius \(\rho'>0\), a dimension \(d\ge1\), and \(a_*>0\). There is a constant \(C\), depending only on these data, such that for every nonzero polynomial \(R\) of degree at most \(L\) and every holomorphic \(H\) on \(B_d(0,\rho')\),
\[
\widetilde R(0)^{a_*}
\sup_{|b|<\rho'/4}|H(b)|
\le C\int_{|y|<\rho'}|R(y)|^{a_*}|H(y)|\,dV(y).
\tag{H26}
\]

Normalize \(S=R/\widetilde R(0)\). Its coefficient vector belongs to the compact unit sphere of the derivative norm in the finite-dimensional polynomial space of degree at most \(L\). The translates \(S(b+\cdot)\), \(|b|\le\rho'/4\), form a compact family of nonzero polynomials: the translation depends continuously on coefficients and \(b\), and cannot make a nonzero polynomial identically zero.

For this family there is a uniform lower bound on the mean of its logarithm on the fixed ball \(B_d(0,\rho'/2)\):
\[
\frac1{|B_d(0,\rho'/2)|}
\int_{|v|<\rho'/2}\log|S(b+v)|\,dV(v)\ge-C_0.
\tag{H27}
\]
We prove the bound rather than assuming continuity of logarithms through zeros. If it failed, a sequence from this compact coefficient family would converge to a nonzero polynomial \(S_\infty\) while its log integrals tended to minus infinity. Choose a point \(v_0\) where \(S_\infty(v_0)\ne0\). Such a point exists in any open ball, by the polynomial identity principle. Values of the sequence at \(v_0\) then have a positive lower bound.

Choose one larger ball centered at \(v_0\) containing \(B_d(0,\rho'/2)\). The bounded coefficient family gives a common upper bound \(C_1\) for all its logarithms on that larger ball. Each logarithm is proper PSH, is locally integrable, and satisfies the real ball submean inequality: apply the explicit regularization
\(\frac12\log(|S|^2+\varepsilon^2)\), whose Levi matrix is positive, and the local-integrability argument of L147 GD4. Hence the nonnegative function
\(C_1-\log|S|\) satisfies the supermean inequality at \(v_0\), and
\[
\int_{|v|<\rho'/2}(C_1-\log|S(v)|)\,dV(v)
\le |B(v_0,R_0)|\bigl(C_1-\log|S(v_0)|\bigr).
\tag{H28}
\]
The right side is uniformly bounded along the proposed sequence. This contradicts its diverging negative log integrals, proving H27. Proper logarithmic local integrability also shows that a nonzero polynomial's zero set has Lebesgue measure zero.

If \(H(b)=0\), the pointwise assertion in H26 is immediate. Otherwise its logarithm is locally integrable and subharmonic on the parameter ball; the same regularization calculation just used works for a local holomorphic function. The radius-\(\rho'/2\) ball centered at \(b\) lies in \(B_d(0,\rho')\). Submeans for \(\log|H|\) and H27 give
\[
\begin{aligned}
a_*\log\widetilde R(0)+\log|H(b)|
&\le
\frac1{|B_d(0,\rho'/2)|}
\int_{B_d(b,\rho'/2)}\log\bigl(|R|^{a_*}|H|\bigr)\,dV
+a_*C_0\\
&\le
\log\left(\frac1{|B_d(0,\rho'/2)|}
\int_{B_d(b,\rho'/2)}|R|^{a_*}|H|\,dV\right)+a_*C_0.
\end{aligned}
\tag{H29}
\]
The second inequality is the arithmetic-geometric mean inequality, or Jensen's inequality for the logarithm on a probability space. If \(H\) is identically zero, the conclusion is again immediate; otherwise its zeros are null by the same local-integrability proof. All logarithms in this computation are therefore legitimate local integrals. Exponentiation and enlargement of the integration ball prove H26, uniformly in \(b\).

Apply H26 to \(H(y)=h(t,y)\) for each fixed \(|t|<c\), with \(L\le m(2m-1)\). Its constants are independent of \(t\). Increasing the right side to
\(\int|R|^{a_*}\sup_{|t|<\rho}|h(t,y)|\,dV(y)\)
and taking the supremum over \(|t|<c\) yields
\[
\widetilde R(0)^{a_*}
\sup_{\substack{|t|<c\\|y|<c}}|h(t,y)|
\le C\int_{|y|<\rho'}
          |R(y)|^{a_*}\sup_{|t|<\rho}|h(t,y)|\,dV(y).
\tag{H30}
\]
If an integral is infinite the bound remains valid; the local estimates themselves use strictly interior balls, where the holomorphic functions are bounded. Since \(\bar m\) is one of the finitely many integers \(1,\ldots,m\), constants in this use of H26 can be chosen uniformly over all its allowed half-integer exponents.

## H7. Integrate fibers using the actual surface measure

Outside \(\{R=0\}\), an individual root is locally a holomorphic function \(t_i(y)\). A direct construction avoids any choice of a global root branch: choose a small circle separating that simple root from the others at a given parameter. Its boundary stays zero-free on a parameter neighborhood and its root count stays one. The integral in H17 with \(l=1\), over this smaller circle, gives its single root as a holomorphic function.

For such a graph, the real derivative of
\(y\mapsto(t_i(y),y)\) has Gram matrix
\[
I+(Dt_i)^T Dt_i,\qquad
\sqrt{\det\bigl(I+(Dt_i)^TDt_i\bigr)}\ge1.
\tag{H31}
\]
The matrix \((Dt_i)^TDt_i\) is positive semidefinite because its quadratic form is \(|Dt_i\,v|^2\). Every eigenvalue of its addition to \(I\) is at least one, so its determinant has the stated lower bound. The ordinary induced graph-area formula therefore implies that integrating a nonnegative function over this root graph dominates its integral over the parameter base.

Take a countable cover by these root-separating parameter neighborhoods and a disjoint measurable partition subordinate to the cover. On each piece label the finitely many roots, integrate by H31, and sum. This does not count a graph twice: the parameter pieces are disjoint, and a simple root is counted once in its factor. Every inside root has
\(|t_i|<\rho,\ |y|<\rho'\), hence
\(|(t_i,y)|<1\). Additional parts of the hypersurface have nonnegative measure and can only enlarge the right side. Consequently
\[
\int_{|y|<\rho'}
\sum_{\substack{Q_j(t_i,y)=0\\|t_i|<\rho}}
|\partial_t^a f(t_i,y)|\,dV(y)
\le
\int_{\{Q_j=0\}\cap\{|z|<1\}}
|\partial_t^a f(z)|\,dS_j(z).
\tag{H32}
\]
The excluded discriminant parameter set is null by H6; its absence in the parameter integral requires no assertion that every point above it is a regular graph. At generic roots the nonzero \(t\)-derivative makes the graph a regular hypersurface chart, so the surface measure used there is precisely the given one.

![Exact branched projection and surface metric](figures/branched-projection-and-surface-area.png)

**Figure H-B.** The complex curve \((t,t^2)\) lies in four real ambient dimensions. The first two panels are its plane projections; opposite nonzero roots give the same projected parameter. The metric panel gives its full area density \(1+4|t|^2\) and projected Jacobian \(4|t|^2\). The unit Euclidean ball cuts its parameter disk at \(|t|<\sqrt{(\sqrt5-1)/2}\). The complete real derivative and exact fiber/surface integrals are in learner Example 3. H31–H32 establish the general projection inequality.

Integrate H25, use H32, and then H30. The Euclidean ball \(|z|<c\) is contained in the product \(|t|<c,\ |y|<c\), so the resulting bound is exactly H13. Together with H19–H20 this proves the local division theorem for \(n\ge2\).

## H8. One complex variable and the empty cluster

For \(n=1\) there are no transverse parameters. The nonzero discriminant is a constant and
\(\widetilde R(0)=|R|\). Its roots are distinct; H19–H20 give the same local decomposition. H25 itself is H13, since the surface integrals are the finite sums of derivative values over the roots in the unit disk. The weighted parameter mean lemma is unnecessary in this dimension. If the chosen inside cluster has no roots, H19 gives \(h=0\) and \(g=f/Q\) is holomorphic on the smaller disk; the estimate is then immediate.

The same empty-cluster statement applies in any dimension. Contour root counts make that cluster empty throughout the selected parameter ball, so \(Q\) is zero-free on the inner cylinder and the division is ordinary analytic division with remainder zero.

## Source credit and the two conventions

The classical targets are Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, §15.3, Lemmas 15.3.4–15.3.5, printed pp. 292–293; 1983 edition, second revised printing 1990, reprint 2005. Its polynomial-strength notation is given in §10.4, formula 10.4.2, printed p. 32.

The ordered root product is \(\Delta=D^2\). We prove both its Hermite estimate and the stronger unordered-product estimate, and use the latter with the usual discriminant in H24. The discriminant factor in the full local theorem is \(\widetilde R(0)^{\bar m-1/2}\), including all polynomial derivatives at zero. H6 proves why its derivative strength controls the weighted local mean even when its point value is zero.

This proof supplies the quantitative local interpolation and division bounds. The subsequent global surface representation additionally requires the full hypersurface area bound, anisotropic cover, global Cauchy–Riemann repair, multiplicity action and weighted representation limit; those are separate arguments.
