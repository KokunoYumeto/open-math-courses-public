# Regular level sets and transverse convolution

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

A regular constraint turns a point delta into a weighted surface measure. The weight is the reciprocal normal Jacobian. Differentiating the delta differentiates the inverse-coordinate density as well. For two compact surface measures, independent normals make addition regular and give a smooth convolution density; parallel normals mark the possible singular sums.

Pairings are complex linear. We use completed Lebesgue integration. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12, 13.1–13.5 and 13.7–13.10, supplies Euclidean completeness and compactness, calculus, trigonometric functions and compact smooth cutoffs. The [finite algebra foundation](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, supplies rank, determinants and orthogonal bases. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and 16, supplies Tonelli, Fubini, convergence and measurable sections.

The distribution topology and positive measure representation are proved in [U008](order-positivity-and-limits.md), Proposition 1.2 and Theorem 4.1. Compact partitions, gluing, parameter differentiation and convolution are proved in [U021](convolution-as-addition-of-supports.md), B0–B2 and Theorem 1.1. The exact nonlinear change-of-variables theorem, including completed measures, is [U025](zero-hypersurfaces-as-curvature-measures.md), Lemma 3.0. We prove the needed inverse theorem next.

## Smooth coordinates from a convergent iteration

**Lemma 0.1 (smooth local inverse).** If \(P\) is a smooth map between open subsets of \(\mathbb R^d\) and \(DP(x_0)\) is invertible, there are open neighborhoods on which \(P\) is a smooth bijection with smooth inverse \(h\). Its derivative is \(Dh(y)=DP(h(y))^{-1}\).

**Proof.** Translation and multiplication of the output by \(DP(x_0)^{-1}\) reduce the problem to \(x_0=P(x_0)=0\) and \(DP(0)=I\). Choose \(R>0\) so that the closed ball \(\overline B_R\) is in the domain and
\[
\|DP(x)-I\|\le\tfrac12\qquad(x\in\overline B_R).
\]
For \(|y|<R/4\), put \(T_y(x)=y+x-P(x)\). Coordinatewise integration on a segment gives
\[
|T_y(x)-T_y(x')|\le\tfrac12|x-x'|,
\qquad |T_y(x)|\le |y|+\tfrac12R<\tfrac34R.
\]
Thus \(T_y\) maps \(\overline B_R\) into itself. Starting at \(x_0=0\), set \(x_{j+1}=T_y(x_j)\). The bound
\[
|x_{j+1}-x_j|\le 2^{-j}|x_1-x_0|
\]
and the finite geometric-sum formula show that the sequence is Cauchy. Euclidean completeness gives a limit in the closed ball, and continuity makes it a fixed point. If two fixed points existed, their distance would be at most half itself. This proves uniqueness without assuming a fixed-point theorem. Call the fixed point \(h(y)\); its equation says \(P(h(y))=y\).

For two parameters the same estimate gives
\[
|h(y)-h(y')|\le |y-y'|+\tfrac12|h(y)-h(y')|,
\]
so \(h\) is Lipschitz with constant two, and \(|h(y)|\le2|y|<R/2\). Take \(W=B_{R/4}\) and \(V=B_R\cap P^{-1}(W)\). This is open, contains zero, and uniqueness proves that \(P\) maps it bijectively onto \(W\), with inverse \(h\).

At each \(x\in B_R\), the inequality \(|DP(x)v|\ge |v|/2\) proves injectivity of the square derivative; finite-dimensional rank makes it invertible, with inverse norm at most two. Fix \(y,y+k\in W\), put \(x=h(y)\) and \(s=h(y+k)-h(y)\). Differentiability gives
\[
k=DP(x)s+r(s),\qquad |r(s)|/|s|\longrightarrow0.
\]
As \(|s|\le2|k|\), it follows that
\[
h(y+k)-h(y)-DP(x)^{-1}k
=-DP(x)^{-1}r(s)=o(|k|).
\]
This proves the derivative formula. Matrix inversion is smooth where the determinant is nonzero: the adjugate formula follows by expanding a determinant along a row; off-diagonal entries in the product vanish as determinants with repeated rows, and diagonal entries are the determinant itself. Its entries are therefore polynomial cofactors divided by the nonzero determinant. The derivative formula first shows \(h\in C^1\). Inductively, if \(h\in C^j\), the formula and the chain rule make \(Dh\in C^j\), so \(h\in C^{j+1}\). Hence \(h\) is smooth. Undoing the two affine coordinate changes proves the claim. Dimension zero is the single-point identity. \(\square\)

**Lemma 0.2 (constraint coordinates, with parameters).** If a smooth map \(F:X\subset\mathbb R^n\to\mathbb R^r\) has rank \(r\) at \(x_0\), select \(r\) coordinate columns forming a nonsingular minor and let \(w\) be the remaining coordinates. The map \(x\mapsto(F(x),w)\) has a smooth local inverse \(x=h(t,w)\), with \(F(h(t,w))=t\). If \(F=F_z\) depends smoothly on extra parameters, the inverse can be chosen smoothly in \(z\) near any such point.

**Proof.** After a column permutation, the derivative of the displayed map has block form
\[
\begin{pmatrix}F_v&F_w\\0&I\end{pmatrix},
\]
whose determinant is the chosen nonzero minor. Apply Lemma 0.1. For parameters, apply it instead to \((z,x)\mapsto(z,F_z(x),w)\); the extra diagonal block is the identity. Its inverse retains its first coordinates \(z\), proving the claimed form. Taking \(t=0\) gives the implicit graph. The free coordinates recover \(w\), so its parametrization is injective with injective derivative. \(\square\)

## The normal Jacobian determines the level measure

**Theorem 1.1 (regular constraints and their delta measure).** Let \(X\subset\mathbb R^n\) be open, \(1\le r\le n\), and let \(F:X\to\mathbb R^r\) be smooth with rank \(r\) on \(Z=F^{-1}(0)\). Set \(J_F=\sqrt{\det(DFDF^T)}\) at regular points. Then
\[
\langle\delta_0(F),\psi\rangle
=\int_Z\frac{\psi(x)}{J_F(x)}\,dS_{n-r}(x)
\tag{1.1}
\]
defines a positive locally finite measure and an order-zero distribution. Surface measure uses the Gram density of a parametrization; in dimension zero it is counting measure. Empty determinants equal one. For any compact smooth complex \(\rho\) on \(\mathbb R^r\) with \(\int\rho=1\),
\[
\epsilon^{-r}\rho(F/\epsilon)\longrightarrow\delta_0(F)
\quad\text{in }\mathcal D'(X),\qquad \epsilon\downarrow0.
\tag{1.2}
\]
No positivity, symmetry or reality of \(\rho\) is required.

**Proof: the exact density.** In the coordinates of Lemma 0.2, write
\[
Dh=[A\ B],\qquad A=h_t,\quad B=h_w,\quad L=DF(h).
\]
The chain rule gives \(LA=I_r\), \(LB=0\). Choose orthonormal bases \(Q\) of \(\ker L\) and \(N\) of its orthogonal complement, by the supplied finite Gram procedure. The columns of \(B\) span the kernel, so \(B=QC\) for an invertible square \(C\). As \(LQ=0\),
\[
LL^T=(LN)(LN)^T,\qquad J_F(h)=|\det(LN)|.
\]
Moreover
\[
[N\ Q]^T[A\ B]
=\begin{pmatrix}N^TA&0\\Q^TA&C\end{pmatrix},
\qquad (LN)(N^TA)=I_r.
\]
The orthogonal factor \([N\ Q]^T\) has determinant of absolute value one. Taking determinants, and using \(B^TB=C^TC\), proves
\[
|\det Dh|
=\frac{|\det C|}{|\det(LN)|}
=\frac{\sqrt{\det(B^TB)}}{J_F(h)}.
\tag{1.3}
\]
When \(r=n\), the empty blocks contribute one, and the identity still holds.

Here are the measure details. On a zero-level chart \(\gamma(w)=h(0,w)\), define surface measure by \(\sqrt{\det(D\gamma^TD\gamma)}\,dw\). If \(\widetilde\gamma=\gamma\circ\kappa\) is another chart, its Gram matrix is
\[
D\kappa^T(D\gamma^TD\gamma)D\kappa.
\]
Thus its square-root determinant gains exactly \(|\det D\kappa|\). The transitions are smooth: each is the projection to the free original coordinates composed with the other parametrization, and the reverse transition has the same form. U025 Lemma 3.0 proves equality of the chart measures on every Borel overlap, and also of the measures divided by \(J_F\).

The zero set is relatively closed. The countable Euclidean base gives a countable chart subcover: for each basic neighborhood whose intersection with \(Z\) lies in some chart, choose one such chart. Split their union into disjoint Borel pieces by removing earlier members and add their compatible measures. Compatibility makes this independent of the splitting and gives (1.1). For a fixed compact set in \(X\), finitely many smaller chart neighborhoods cover its intersection with \(Z\). Their densities and inverse Jacobians are bounded on compact subcharts. In particular \(J_F\) has a positive lower bound there. The resulting mass on that compact is finite, and
\[
|\delta_0(F)(\psi)|\le C_K\|\psi\|_\infty
\quad(\operatorname{supp}\psi\subset K).
\]
This proves the asserted distribution order. The locally finite Borel measure is Radon by the measure regularity fact proved immediately after U025 Lemma 3.0.

**Proof: convergence and compact bounds.** First let \(\psi\) have compact support inside a regular coordinate chart. Define
\[
G_\psi(t)=\int\psi(h(t,w))|\det Dh(t,w)|\,dw .
\tag{1.4}
\]
The integrand, extended by zero outside the compact image of that support, is smooth on the full coordinate space. All its \(w\)-supports lie in one compact set. The coordinate FTC and uniform continuity of every derivative permit differentiation under the integral, so \(G_\psi\) is smooth. Exact nonlinear substitution and then \(t=\epsilon s\) give
\[
\int_X\epsilon^{-r}\rho(F(x)/\epsilon)\psi(x)\,dx
=\int_{\mathbb R^r}\rho(s)G_\psi(\epsilon s)\,ds
\longrightarrow G_\psi(0).
\]
Uniform continuity on the compact profile support and \(\int\rho=1\) justify the limit. Equation (1.3) identifies it with (1.1).

For a general compact test support \(K\), U021 B0 gives finitely many smooth chart cutoffs whose sum equals one near \(K\cap Z\). The remaining test piece has compact support disjoint from \(Z\); continuity gives a positive minimum of \(|F|\) there. For small \(\epsilon\) it contributes zero, since \(\rho\) is compactly supported. Sum the chart limits. This proves (1.2) and independence of the profile.

The same proof works for continuous compact tests: the integrated function is then continuous, and uniform continuity still proves the limit. Finally, for a fixed smooth compact weight \(a\), the approximate measures
\[
a(x)\epsilon^{-r}\rho(F(x)/\epsilon)\,dx
\]
have support in \(\operatorname{supp}a\) and uniformly bounded total variation as \(\epsilon\downarrow0\). In each chart their absolute integral is bounded by \(\|\rho\|_1\) times a uniform compact bound for the integrated absolute density; the separated remainder eventually vanishes. These facts apply to complex weights and profiles. \(\square\)

**Corollary 1.2 (two real constraints).** If \(f,g\) have independent differentials at their common zeros in \(\mathbb R^n\), \(n\ge2\), then
\[
\begin{gathered}
\delta_0(f,g)(\psi)=\int_{\{f=g=0\}}\frac{\psi}{\Delta}\,dS_{n-2},\\
\Delta^2=|p|^2|q|^2-(p\cdot q)^2,\quad
p=\nabla f,\quad q=\nabla g,\quad\Delta>0.
\end{gathered}
\tag{1.5}
\]

**Proof.** The matrix \(D(f,g)D(f,g)^T\) has entries \(|p|^2,p\cdot q,|q|^2\); its determinant is the displayed expression. Orthogonal projection of \(q\) onto \(p^\perp\) shows it is positive precisely when the vectors are independent. Apply Theorem 1.1. For \(n=2\), the numerator is counting measure and the denominator is \(|\det D(f,g)|\). For \(n=1\), independence forces the common zero set to be empty; on each compact support \(|(f,g)|\) has positive minimum, so every compact approximate joint delta is eventually zero. Product profiles \(\rho(t)\sigma(s)\) of arbitrary unit integrals are included. \(\square\)

**Example 1.3.** For \(f(x,y)=2(y-\sin x)\), coordinates \(t=f,w=x\) have inverse \((x,\sin x+t/2)\) of absolute determinant \(1/2\). Hence
\[
\delta_0(f)(\psi)=\tfrac12\int\psi(x,\sin x)\,dx.
\]
The graph speed is \(\sqrt{1+\cos^2x}\), and the normal length is twice that; (1.1) gives the same weight.

## A normal derivative also differentiates the density

**Proposition 2.1 (one normal derivative).** For smooth scalar \(f\) with \(df\ne0\) on \(f^{-1}(0)\), define locally, using (1.4),
\[
\langle\delta'_0(f),\psi\rangle=-G_\psi'(0).
\tag{2.1}
\]
The partitioned local expressions give a well-defined distribution of order at most one.

**Proof.** Take a scalar compact smooth unit-integral \(\rho\), and put \(\rho_\epsilon(t)=\epsilon^{-1}\rho(t/\epsilon)\). In a regular chart, substitution and compact integration by parts give
\[
\int\rho_\epsilon'(f(x))\psi(x)\,dx
=\int\rho_\epsilon'(t)G_\psi(t)\,dt
=-\int\rho(s)G_\psi'(\epsilon s)\,ds
\longrightarrow-G_\psi'(0).
\]
For a general test, use the chart partition from Theorem 1.1; its separated remainder contributes zero for sufficiently small \(\epsilon\). Each local sum is consequently the limit of the same globally defined smooth approximants, so all choices give the same pairing. Differentiating (1.4) once differentiates \(\psi\) at most once and differentiates the smooth inverse density. On each fixed compact support the finite chart bounds therefore give \(C_K(\|\psi\|_\infty+\|\nabla\psi\|_\infty)\). This proves continuity and the order bound. \(\square\)

**Proposition 2.2 (crossing axes away from their crossing).** On \(X=\mathbb R^2\setminus\{0\}\), the distribution \(\delta'_0(xy)\) has exact support the two punctured axes and exact order one. On \(x\ne0\),
\[
\delta'_0(xy)=\frac1{x|x|}\delta'_0(y).
\tag{2.2}
\]
Its full pairing is
\[
\begin{aligned}
\langle\delta'_0(xy),\psi\rangle
={}&-\int_{x\ne0}\frac{\psi_y(x,0)}{x|x|}\,dx\\
&-\int_{y\ne0}\frac{\psi_x(0,y)}{y|y|}\,dy.
\end{aligned}
\tag{2.3}
\]

**Proof.** On the first chart, \(t=xy,w=x\) has inverse \((x,t/x)\) and absolute Jacobian \(1/|x|\). Formula (2.1) gives the additional factor \(1/x\) from differentiating the test, proving (2.2). On \(y\ne0\), interchange coordinates. The two formulas both vanish where \(xy\ne0\), so they agree on their overlap. Compact tests in the punctured plane vanish on a neighborhood of the origin; both integrals in (2.3) are ordinary finite integrals. They restrict to the two local formulas, hence gluing in U021 B0 proves the full expression.

Each axis point is in the support: a small product test with prescribed nonzero normal derivative has nonzero pairing there. Elsewhere the formula vanishes. To rule out order zero near a point of the horizontal axis, choose a nonzero nonnegative compact bump \(b\) on an interval avoiding zero and a compact smooth \(\eta\) with \(\eta'(0)\ne0\). For small \(\epsilon\), set
\[
\psi_\epsilon(x,y)=\epsilon b(x)\eta(y/\epsilon).
\]
Their suprema tend to zero on one fixed compact support, but the pairing is the nonzero constant
\(-\eta'(0)\int b(x)/(x|x|)\,dx\); the coefficient has constant sign on the interval. This contradicts an order-zero bound. The vertical-axis proof interchanges variables. Proposition 2.1 proves the upper bound. In particular the negative sign of \(1/(x|x|)\) for \(x<0\) cannot be replaced by \(1/x^2\). \(\square\)

**Example 2.3.** For \(f(x,y)=e^x(y-\sin x)\), the inverse normal coordinate is \(y=\sin x+e^{-x}t\), with density \(e^{-x}\). Thus
\[
\begin{aligned}
\delta_0(f)(\psi)&=\int e^{-x}\psi(x,\sin x)\,dx,\\
\delta'_0(f)(\psi)&=-\int e^{-2x}\psi_y(x,\sin x)\,dx.
\end{aligned}
\]
The second inverse-scale factor comes from differentiating the test.

## Roots and simultaneous constraints

**Proposition 3.1 (periodic point masses).** If \(-1<a<1\) and \(\theta=\arccos a\in(0,\pi)\), then
\[
\delta_a(\cos x)
=\frac1{\sqrt{1-a^2}}\sum_{j\in\mathbb Z}
\bigl(\delta_{\theta+2\pi j}+\delta_{-\theta+2\pi j}\bigr).
\tag{3.1}
\]

**Proof.** The scalar foundation proves the unit-circle parametrization and its period. Cosine decreases strictly from one to minus one on \((0,\pi)\), since its derivative is \(-\sin x<0\); the intermediate value theorem gives the unique \(\theta\). Reflection and the full period give exactly the two root families. At each root the derivative has absolute value \(\sqrt{1-a^2}\). Theorem 1.1 in dimension one gives (3.1). The root set is locally finite, so each compact test meets finitely many masses. Each mass is positive; bumps detect each root, proving exact support and order zero. At \(a=\pm1\) the derivative vanishes and the regular-constraint statement does not apply. \(\square\)

**Proposition 3.2 (two isolated intersections).** For any complex compact smooth \(\phi\) with integral one, and \(\phi_\epsilon(t)=\epsilon^{-1}\phi(t/\epsilon)\),
\[
\phi_\epsilon(x^2-y^2)\phi_\epsilon(y-1)
\longrightarrow\tfrac12\delta_{(1,1)}+\tfrac12\delta_{(-1,1)}
\quad\text{in }\mathcal D'(\mathbb R^2).
\tag{3.2}
\]

**Proof.** The constraint vector \(F=(x^2-y^2,y-1)\) has exactly those two zeros. Its derivative has rows \((2x,-2y)\), \((0,1)\), so its absolute determinant there is two. Apply Theorem 1.1 to the joint profile \(\phi(t)\phi(s)\), whose integral is one by Fubini.

The two branches also check every weight directly. Nonzero approximants force \(y=1+O(\epsilon)\) and \(x^2-y^2=O(\epsilon)\), hence \(x\) lies near \(1\) or \(-1\). In coordinates \(t=x^2-y^2,s=y-1\), their inverses are
\[
y=1+s,\qquad x=\pm\sqrt{(1+s)^2+t},\qquad
|\det Dh|=\frac1{2|x|}.
\]
After \(t=\epsilon u,s=\epsilon v\), the test times density tends uniformly on the fixed profile support to \(\psi(\pm1,1)/2\). Integrating the product profile gives each half mass. No cancellation, symmetry or positivity of \(\phi\) was assumed. \(\square\)

## Independent normals give a smooth convolution density

Let \(f,g\) be smooth real functions on \(\mathbb R^n\), \(n\ge1\), with nonzero gradients on \(M=f^{-1}(0)\), \(N=g^{-1}(0)\). For complex \(a,b\in C_c^\infty(\mathbb R^n)\), define
\[
\mu=a\,\delta_0(f),\qquad \nu=b\,\delta_0(g).
\]
Their total variations are finite by Theorem 1.1. U021 Theorem 1.1 gives the compact convolution, whose explicit measure pairing is
\[
u(\psi)=\int_M\int_N
\frac{a(x)b(y)\psi(x+y)}
{|\nabla f(x)||\nabla g(y)|}\,dS(y)dS(x).
\tag{4.1}
\]
Absolute Fubini is justified by the product of the finite variation bounds and \(\|\psi\|_\infty\).

Put \(K_f=M\cap\operatorname{supp}a\), \(K_g=N\cap\operatorname{supp}b\), and define
\[
B=\{x+y:(x,y)\in K_f\times K_g,\
\nabla f(x),\nabla g(y)\text{ are dependent}\}.
\tag{4.2}
\]
The zero Gram determinant defines a closed subset of this compact product, and addition is continuous. Thus \(B\) is compact.

**Theorem 4.1 (transverse compact convolution).** On \(O=\mathbb R^n\setminus B\), the convolution is smooth. If \(n\ge2\), its value is
\[
\begin{gathered}
U(z)=\int_{\Sigma_z}\frac{a(x)b(z-x)}{\Delta_z(x)}\,dS_{n-2}(x),
\qquad \Sigma_z=\{x:f(x)=g(z-x)=0\},\\
\Delta_z(x)^2=|p|^2|q|^2-(p\cdot q)^2,\qquad
p=\nabla f(x),\quad q=\nabla g(z-x).
\end{gathered}
\tag{4.3}
\]
The integral is taken on a regular neighborhood of the compact weighted intersection, where \(\Delta_z>0\), with weight zero elsewhere. There is no assertion about other, unweighted critical parts of \(\Sigma_z\). For \(n=1\), the function on \(O\) is zero. In every dimension,
\[
\operatorname{sing\,supp}u\subset B.
\tag{4.4}
\]

**Proof: parameter charts.** First suppose \(n\ge2\). Fix \(z_0\in O\) and a small closed ball \(L\) about it contained in \(O\). The set
\[
T=\{(z,x):z\in L,\ x\in\operatorname{supp}a,\
z-x\in\operatorname{supp}b,\ f(x)=g(z-x)=0\}
\]
is compact. At every point of \(T\), the \(x\)-derivative of \(F_z(x)=(f(x),g(z-x))\) has independent rows \(p^T,-q^T\). Choose a nonzero two-column minor there. Lemma 0.2 gives smooth inverse coordinates \(x=h(z,t,s,w)\), with \(n-2\) free coordinates \(w\). On sufficiently small neighborhoods the same minor stays nonzero.

Cover \(T\) by finitely many such charts. U021 B0 supplies compact smooth functions \(\chi_j(z,x)\) supported in the charts, whose sum is one on a neighborhood of \(T\). One obtains them by finitely many smaller bumps, division by their positive sum, and multiplication by a cutoff equal to one near \(T\). On the compact weighted set over \(L\) outside that neighborhood, \(|F_z(x)|\) has a positive lower bound. Consequently this remainder gives zero to all sufficiently narrow compact approximate joint deltas, uniformly for \(z\in L\). If \(T\) is empty, the same compact minimum proves this directly and the eventual density is zero.

In each chart put
\[
\begin{gathered}
H_j(z,t,s)=\int
\chi_j(z,h)a(h)b(z-h)J_h(z,t,s,w)\,dw,\\
J_h=\left|\det\frac{\partial h}{\partial(t,s,w)}\right|.
\end{gathered}
\tag{4.5}
\]
The compact chart support of \(\chi_j\) lets the integrand extend smoothly by zero in all coordinate variables. The determinant has locally constant sign because it never vanishes, so its absolute value is smooth. The \(w\)-support is in a common compact projection. Repeated coordinate FTC under this finite integral, with uniform bounds for each derivative, proves that \(H_j\) is smooth. The candidate density \(U(z)=\sum_jH_j(z,0,0)\) is therefore smooth near \(z_0\).

**Proof: identification with convolution.** Choose arbitrary compact smooth unit-integral scalar profiles \(\rho,\sigma\). Theorem 1.1 gives
\[
\mu_\epsilon=a\,\rho_\epsilon(f)\,dx\longrightarrow\mu,
\qquad
\nu_\epsilon=b\,\sigma_\epsilon(g)\,dy\longrightarrow\nu
\]
on continuous compact tests, with fixed compact supports and uniformly bounded variations.

We justify convergence of their product pairing on \(\psi(x+y)\). On the two fixed compact supports, choose finite nonnegative smooth partitions with each member supported in a ball of radius \(\delta\), and choose a center in the corresponding support piece. Replace \(\psi(x+y)\) by the sum of the center values times the products of partition functions. The partitions sum to one there, so the uniform error is bounded by the modulus of continuity of \(\psi\) at \(4\delta\). This approximant is a finite sum of products of compact continuous functions. Its pairings converge by the two individual measure limits. The error for every \(\epsilon\), and for the limit measures, is bounded by that modulus times their uniform product variation bound. Let \(\delta\downarrow0\). Thus \(\mu_\epsilon*\nu_\epsilon\to u\) on tests.

For each \(\epsilon>0\), the linear substitution \(y=z-x\) has absolute determinant one. Ordinary Fubini gives the density
\[
U_\epsilon(z)=\int a(x)b(z-x)
\rho_\epsilon(f(x))\sigma_\epsilon(g(z-x))\,dx.
\]
For \(z\) near \(z_0\), the compact remainder already vanishes for small \(\epsilon\). U025 Lemma 3.0 in each inverse chart gives exactly
\[
U_\epsilon(z)=\sum_j\iint\rho(v)\sigma(q)
H_j(z,\epsilon v,\epsilon q)\,dv\,dq.
\tag{4.6}
\]
Every \(z\)-derivative satisfies this same identity with the corresponding derivative of \(H_j\). Uniform continuity on the compact parameter and profile supports shows that it converges uniformly to \(\sum_j\partial_z^\alpha H_j(z,0,0)\). Thus \(U_\epsilon\to U\) in all local smooth seminorms. Its distributional limit is already \(u\), so \(u=U\) near \(z_0\).

Apply (1.3) at fixed \(z\) to \(F_z\). Its normal Gram determinant is \(\Delta_z^2\); the minus sign in the second row cancels in that determinant. The numerator is the Gram density of the free \(w\)-coordinates on the intersection. Summing \(\chi_j\) therefore turns \(\sum H_j(z,0,0)\) into (4.3). All relevant charts are regular around the weighted intersection; unrelated critical points contribute nothing. For \(n=2\) the free-coordinate integrals are counting sums, with the same denominator.

For \(n=1\), both nonzero normals are dependent at every weighted pair, so \(B=K_f+K_g\). Formula (4.1) vanishes on its complement. This proves the stated zero function and completes (4.4).

Finally, the tangent criterion agrees with the calculation. The differential of addition on \(M\times N\) takes \((v,w)\in p^\perp\times q^\perp\) to \(v+w\). The orthogonal complement of its image is
\((p^\perp+q^\perp)^\perp=\operatorname{span}(p)\cap\operatorname{span}(q)\),
as follows by testing orthogonality separately against each summand. It is zero exactly when the normals are independent. The result supplies a possible singular set, not equality: complex weights can cancel. \(\square\)

**Example 4.2.** Put compact weights \(\alpha(s)\,ds\) on the horizontal line \((s,0)\) and \(\beta(t)\,dt\) on the vertical line \((0,t)\). Their addition map is the identity \((s,t)\mapsto(s,t)\). Testing gives the entire smooth density \(\alpha(z_1)\beta(z_2)\). In (4.3) the single intersection point is \(x=(z_1,0)\) and \(\Delta_z=1\).

## Exercises

**Exercise 1 (basic).** Determine all point masses and weights in \(\delta_0(3\sin(2x)-1)\) on the full real line.

**Exercise 2 (intermediate).** For \(F(x,y)=e^x(y-x^2)\), give the pairings of \(\delta_0(F)\) and \(\delta'_0(F)\), and prove
\[
\partial_y\delta_0(F)=e^x\delta'_0(F),\qquad
(y-x^2)\delta'_0(F)=-e^{-x}\delta_0(F).
\]

**Exercise 3 (intermediate).** In \(\mathbb R^3\), set \(f=x+2y-z\) and \(g=2x-y+3z\). Compute both \(\delta_0(f,g)\) and \(\delta_0(2f+g,f-3g)\) as line measures, including their normalizations.

**Exercise 4 (advanced).** Let complex compact smooth \(\rho,\sigma\) have integral one and first moments \(m_\rho=\int t\rho(t)\,dt\), \(m_\sigma=\int t\sigma(t)\,dt\). For an arbitrary test \(\psi\), find the limit and the entire first-order correction of the pairing with
\[
\rho_\epsilon(xy-3)\sigma_\epsilon(y-2).
\]
Bound the remainder without assuming vanishing moments, positivity or reality.

**Exercise 5 (basic).** For \(f(x,y)=x^2/4+y^2/9-1\), parametrize \(\delta_0(f)\) and compute its mass and its \(x,y,x^2,y^2\) moments.

**Exercise 6 (intermediate).** Let \(\chi,\eta\in C_c^\infty(\mathbb R)\), with \(\chi(0)=1\). Set
\[
\begin{gathered}
f(x)=x_2,\quad g(y)=y_2-y_1,\\
a(x)=\chi(x_1)\chi(x_2),\quad b(y)=\eta(y_1)\eta(y_2).
\end{gathered}
\]
Find \((a\delta_0(f))*(b\delta_0(g))\) everywhere and its singular support.

**Exercise 7 (intermediate).** Let nonnegative smooth \(\alpha,\beta\) be supported on \([-1,1]\) and positive on \((-1,1)\), and choose \(\kappa\in C_c^\infty(\mathbb R)\) with \(\kappa(0)=1\). In \(\mathbb R^3\), put
\[
\begin{gathered}
f(x)=x_3,\quad g(y)=y_3-2,\\
a(x)=\alpha(x_1)\alpha(x_2)\kappa(x_3),\\
b(y)=\beta(y_1)\beta(y_2)\kappa(y_3-2).
\end{gathered}
\]
Compute the convolution, its exact singular support and its total mass.

**Exercise 8 (advanced).** Let \(\alpha,\beta,\kappa\in C_c^\infty(\mathbb R)\), with \(\kappa(0)=1\), and set
\[
\begin{gathered}
f(x)=x_2-x_1^2,\quad g(y)=y_2-y_1^2,\\
a(x)=\alpha(x_1)\kappa(x_2-x_1^2),\\
b(y)=\beta(y_1)\kappa(y_2-y_1^2).
\end{gathered}
\]
Derive both branches of the convolution density off \(z_2=z_1^2/2\). If \(\alpha,\beta\) are nonnegative and positive at zero, prove that the origin is singular.

**Exercise 9 (advanced).** For \(f=x_3-x_1x_2\), \(g=x_4-x_1^2-x_2^2\) in \(\mathbb R^4\), parametrize the common zero surface. Find its surface density, its normal constraint Jacobian and the pairing of \(\delta_0(f,g)\).

**Exercise 10 (basic).** On \(I=(-1/6,1/6)\), compute \(\delta_0(-2t+3t^2)\) and \(\delta'_0(-2t+3t^2)\), and verify
\[
\partial_t\delta_0(-2t+3t^2)=(-2+6t)\delta'_0(-2t+3t^2).
\]
Account for the point-mass term in the delta derivative.

## Complete solutions

**Solution 1.** There is a unique \(\theta\in(0,\pi/2)\) with \(\sin\theta=1/3\), because sine has positive derivative there and ranges from zero to one. The circle identities give exactly
\[
x=\theta/2+\pi j
\quad\text{or}\quad x=(\pi-\theta)/2+\pi j,\qquad j\in\mathbb Z.
\]
These two families are disjoint and locally finite. The derivative of \(3\sin(2x)-1\) has absolute value \(6|\cos(2x)|=6\sqrt{1-1/9}=4\sqrt2\) at each root. Theorem 1.1 gives
\[
\delta_0(3\sin(2x)-1)
=\frac1{4\sqrt2}\sum_{j\in\mathbb Z}
\left(\delta_{\theta/2+\pi j}
+\delta_{(\pi-\theta)/2+\pi j}\right).
\]
Every compact test meets finitely many terms, proving the global distributional meaning.

**Solution 2.** Take the constraint coordinate \(t=F\), retaining \(x\). Its inverse is \(y=x^2+e^{-x}t\), with absolute Jacobian \(e^{-x}\). Thus
\[
G_\psi(t)=\int e^{-x}\psi(x,x^2+e^{-x}t)\,dx.
\]
The compact projection of the test support bounds the \(x\) range. Evaluation and differentiation under the integral give
\[
\begin{aligned}
\delta_0(F)(\psi)&=\int e^{-x}\psi(x,x^2)\,dx,\\
\delta'_0(F)(\psi)&=-\int e^{-2x}\psi_y(x,x^2)\,dx.
\end{aligned}
\]
The derivative in \(y\) of the first distribution pairs as \(-\int e^{-x}\psi_y(x,x^2)\,dx\). Applying the second distribution to \(e^x\psi\) gives the same integral, proving the first identity.

For the second identity, apply \(\delta'_0(F)\) to \((y-x^2)\psi\). At \(y=x^2\), its \(y\)-derivative is exactly \(\psi(x,x^2)\). The answer is \(-\int e^{-2x}\psi(x,x^2)\,dx\), which equals \((-e^{-x}\delta_0(F))(\psi)\). This proves both statements on every test with the variable coefficients retained.

**Solution 3.** The gradients \(p=(1,2,-1)\), \(q=(2,-1,3)\) satisfy
\[
|p|^2=6,\qquad |q|^2=14,\qquad p\cdot q=-3.
\]
Thus \(\Delta=\sqrt{84-9}=5\sqrt3\). Solving the two equations gives \(\gamma(s)=(s,-s,-s)\), of speed \(\sqrt3\). Therefore
\[
\delta_0(f,g)(\psi)=\frac15\int_{\mathbb R}\psi(s,-s,-s)\,ds.
\]
Replacing the constraints multiplies their column vector by
\[
A=\begin{pmatrix}2&1\\1&-3\end{pmatrix},\qquad \det A=-7.
\]
Its inverse exists, so the zero set is unchanged. The normal Gram matrix becomes \(A(DFDF^T)A^T\), multiplying its determinant by \(49\) and its positive square root by seven. Consequently
\[
\delta_0(2f+g,f-3g)(\psi)
=\frac1{35}\int_{\mathbb R}\psi(s,-s,-s)\,ds.
\]
The negative determinant creates no negative mass.

**Solution 4.** Near the only simultaneous zero \((3/2,2)\), put \(t=xy-3,s=y-2\). Then
\[
h(t,s)=\left(\frac{3+t}{2+s},2+s\right),
\qquad |\det Dh|=\frac1{2+s}.
\]
The compact profile supports force \(y\) close to two and \(xy\) close to three; hence the entire nonzero approximant lies in this chart for all small \(\epsilon\). Define
\[
G(t,s)=\frac1{2+s}\psi\left(\frac{3+t}{2+s},2+s\right).
\]
Substitution makes the pairing \(\iint\rho(u)\sigma(v)G(\epsilon u,\epsilon v)\,du\,dv\). Direct differentiation at \((0,0)\), with all test values below at \((3/2,2)\), gives
\[
\begin{aligned}
G(0,0)&=\tfrac12\psi,\\
G_t(0,0)&=\tfrac14\psi_x,\\
G_s(0,0)&=-\tfrac38\psi_x+\tfrac12\psi_y-\tfrac14\psi.
\end{aligned}
\]
To justify the remainder, apply the scalar FTC twice to \(q(\tau)=G(\tau\epsilon u,\tau\epsilon v)\):
\[
q(1)=q(0)+q'(0)+\int_0^1(1-\tau)q''(\tau)\,d\tau.
\]
This identity follows by integrating \(q'(\tau)=q'(0)+\int_0^\tau q''(s)\,ds\) and interchanging the compact integrals. Compact second-derivative bounds give remainder at most \(C_\psi\epsilon^2(|u|+|v|)^2\). Integration against \(|\rho(u)\sigma(v)|\) is finite. Therefore the full answer is
\[
\begin{aligned}
\langle\rho_\epsilon(xy-3)\sigma_\epsilon(y-2),\psi\rangle
={}&\tfrac12\psi(3/2,2)\\
&+\epsilon\left(m_\rho G_t(0,0)+m_\sigma G_s(0,0)\right)
+O_\psi(\epsilon^2).
\end{aligned}
\]
In particular the limit is \(\delta_{(3/2,2)}/2\). Both possibly complex first moments are retained.

**Solution 5.** The ellipse is parametrized once, apart from the repeated endpoint, by \(\gamma(\theta)=(2\cos\theta,3\sin\theta)\), \(0\le\theta<2\pi\). Its speed and the normal length satisfy
\[
|\gamma'|=\sqrt{4\sin^2\theta+9\cos^2\theta},
\qquad
|\nabla f(\gamma)|=\sqrt{\cos^2\theta+\tfrac49\sin^2\theta},
\]
so their ratio is three. A single point has zero arclength in a regular curve chart, since its parameter singleton has Lebesgue measure zero; the endpoint convention adds no mass. Thus
\[
\delta_0(f)(\psi)=3\int_0^{2\pi}\psi(2\cos\theta,3\sin\theta)\,d\theta.
\]
The mass is \(6\pi\). The first moments vanish by the sine and cosine primitives over a full period. The identities \(\cos^2\theta=(1+\cos2\theta)/2\) and \(\sin^2\theta=(1-\cos2\theta)/2\) give
\[
\int x^2\,d\delta_0(f)=12\pi,\qquad
\int y^2\,d\delta_0(f)=27\pi.
\]
All polynomial pairings mean a compact smooth cutoff times that polynomial, equal to it near the compact ellipse; localization makes the value independent of the cutoff.

**Solution 6.** The first line measure is \(\chi(s)\,ds\) at \((s,0)\), using \(\chi(0)=1\). The second is \(\eta(t)^2\,dt\) at \((t,t)\), because its speed \(\sqrt2\) cancels its normal length \(\sqrt2\). Addition is \((s,t)\mapsto(s+t,t)\), of determinant one and inverse \((z_1-z_2,z_2)\). Direct substitution in the test pairing yields
\[
U(z)=\chi(z_1-z_2)\eta(z_2)^2
\]
on the whole plane. It is compact smooth, so its singular support is empty. The two normals \((0,1)\), \((-1,1)\) are independent, also giving \(B=\varnothing\).

**Solution 7.** Both plane constraints have unit normal length. Their free-coordinate measures are \(\alpha(x_1)\alpha(x_2)\,dx_1dx_2\) on \(x_3=0\) and \(\beta(y_1)\beta(y_2)\,dy_1dy_2\) on \(y_3=2\). Put
\[
c(t)=\int_{\mathbb R}\alpha(s)\beta(t-s)\,ds.
\]
Compact parameter differentiation, as proved in U021 B1, gives \(c\in C_c^\infty\), with support contained in \([-2,2]\). For \(|t|<2\), the intervals \((-1,1)\) and \(t-(-1,1)\) intersect in a nonempty open interval. The integrand is strictly positive there, so \(c(t)>0\); its exact support is \([-2,2]\).

Absolute Fubini in the four free coordinates gives
\[
u=c(z_1)c(z_2)\,\delta_2(z_3).
\]
Every neighborhood of a point of \([-2,2]^2\times\{2\}\) meets an open patch of the plane where both densities are positive. A nonnegative test there has positive pairing. Off that closed set the distribution vanishes, so its support is exactly that set.

Suppose it were smooth near a support point. Its smooth representative vanishes off the plane: on every such open set the distribution is zero, and the continuous-function uniqueness argument in U021 B0 makes the representative pointwise zero. The plane has empty interior, so continuity makes the representative zero on it too. This contradicts the nonzero pairing in every neighborhood. Thus the exact singular support, including its boundary, is
\[
[-2,2]^2\times\{2\}.
\]
Tonelli gives \(\int c=(\int\alpha)(\int\beta)\). The total mass of \(u\) is its square. Here every pair has parallel normals, so \(B\) is that entire closed support.

**Solution 8.** The two weights are compact in the plane: their first coordinates are bounded, and compact support of \(\kappa\) then bounds the second coordinates. The graph speed cancels the normal length, leaving \(\alpha(s)\,ds\) at \((s,s^2)\), and \(\beta(t)\,dt\) at \((t,t^2)\). The addition map has
\[
z_1=s+t,\quad z_2=s^2+t^2,\quad
\det D(s+t,s^2+t^2)=2(t-s).
\]
The normals \((-2s,1)\), \((-2t,1)\) are dependent exactly at \(s=t\); the corresponding sums obey \(z_2=z_1^2/2\).

Write \(D=2z_2-z_1^2\). The identity \(D=(s-t)^2\) shows there is no preimage if \(D<0\). For \(D>0\), put
\[
s_\pm=\frac{z_1\pm\sqrt D}{2}.
\]
There are exactly two preimages \((s_+,s_-)\) and \((s_-,s_+)\). On the two half-planes \(s>t\) and \(s<t\), these are smooth inverses, each of absolute Jacobian \(1/(2\sqrt D)\). Applying U025 Lemma 3.0 separately gives
\[
U(z)=
\frac{\alpha(s_+)\beta(s_-)+\alpha(s_-)\beta(s_+)}{2\sqrt D},
\qquad D>0,
\]
and zero for \(D<0\). The diagonal \(s=t\) has plane measure zero by Fubini, since each one-dimensional section is a singleton. Its pushforward therefore contributes no extra measure on the critical parabola. The displayed density describes the full measure almost everywhere.

It is locally integrable: use the smooth global map \((z_1,z_2)\mapsto(z_1,v)\), where \(v=z_2-z_1^2/2\), with determinant one. Then \(D=2v\), the numerator is bounded, and
\(\int_0^\delta v^{-1/2}\,dv=2\sqrt\delta\)
by the scalar primitive. This proves integrability across the critical curve.

If the two weights are nonnegative and positive at zero, along \(z_1=0,z_2>0\) the numerator tends to \(2\alpha(0)\beta(0)>0\) as \(z_2\downarrow0\). The density diverges like a positive multiple of \(z_2^{-1/2}\). A smooth representative near the origin would equal this smooth density pointwise on the open region above the parabola, by U021 B0's uniqueness argument. It would also be bounded on a smaller compact neighborhood. The divergence contradicts that bound, proving the origin singular. The convolution is still a finite order-zero measure.

**Solution 9.** The parametrization is \(\gamma(s,t)=(s,t,st,s^2+t^2)\). Projection to the first two coordinates is its inverse. The tangent Gram matrix is
\[
D\gamma^TD\gamma=
\begin{pmatrix}
1+t^2+4s^2&5st\\
5st&1+s^2+4t^2
\end{pmatrix}.
\]
Expanding its determinant gives
\[
Q(s,t)=1+5(s^2+t^2)+4(s^2-t^2)^2.
\]
The constraint gradients are \((-t,-s,1,0)\) and \((-2s,-2t,0,1)\), with Gram matrix
\[
\begin{pmatrix}
1+s^2+t^2&4st\\
4st&1+4s^2+4t^2
\end{pmatrix}.
\]
Its determinant is also \(Q\), and \(Q\ge1\). Thus the constraints are regular everywhere on the surface, its area density is \(\sqrt Q\,ds\,dt\), and its normal Jacobian is \(\sqrt Q\). They cancel in (1.1):
\[
\delta_0(f,g)(\psi)=\iint\psi(s,t,st,s^2+t^2)\,ds\,dt.
\]
The first two coordinates of a compact test support bound \(s,t\), proving finiteness. Parameter area \(ds\,dt\) in this delta formula is distinct from the Euclidean surface density \(\sqrt Q\,ds\,dt\).

**Solution 10.** The function \(f(t)=-2t+3t^2\) has its only zero in \(I\) at zero, and \(f'(t)=-2+6t<0\) throughout \(I\). Lemma 0.1 supplies the smooth local inverse \(t=h(s)\). Differentiating \(f(h(s))=s\) once and twice gives
\[
h'(0)=-\tfrac12,\qquad
6(h'(0))^2-2h''(0)=0,\qquad h''(0)=\tfrac34.
\]
Since \(h'<0\), the integrated test is \(G(s)=-h'(s)\psi(h(s))\), and
\[
G(0)=\tfrac12\psi(0),\qquad
G'(0)=-\tfrac14\psi'(0)-\tfrac34\psi(0).
\]
Tests away from the only root give zero, so these local calculations identify the distributions on all of \(I\):
\[
\delta_0(f)=\tfrac12\delta_0,\qquad
\delta'_0(f)=-\tfrac14\delta'_0+\tfrac34\delta_0.
\]
The point mass is the derivative of the inverse density \(|h'|\); differentiating only the test argument would omit it.

For the weak chain rule, direct testing gives \(t\delta'_0=-\delta_0\) and \(t\delta_0=0\), since
\(-\partial_t(t\psi)(0)=-\psi(0)\) and \(t\psi|_{t=0}=0\). Therefore
\[
\begin{aligned}
(-2+6t)(-\tfrac14\delta'_0+\tfrac34\delta_0)
&=\tfrac12\delta'_0-\tfrac32t\delta'_0-\tfrac32\delta_0\\
&=\tfrac12\delta'_0
=\partial_t\delta_0(f).
\end{aligned}
\]
This proves the complete identity, including cancellation of both point-mass terms.

## Free sources and exact proof dependencies

- Jiří Lebl, *Basic Analysis II*, version 2.6, 16 May 2022, §8.5, Theorems 8.5.1 and 8.5.6, pp.47–52. [Free author edition](https://www.jirka.org/ra/realanal2-2.6.pdf). Its inverse-coordinate argument was compared with the actual proof. Lemmas 0.1–0.2 above supply the iteration, convergence, differentiability, smooth bootstrap and parameter version in full.
- Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, 2 October 2026 version, §§10.1.3–10.1.6, pp.109–112. [Free author notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf). The inverse-density and regular-surface calculations were compared with their proofs. The present lesson proves its vector constraint formula and approximation directly, using the supplied nonlinear substitution proof.
- [U008](order-positivity-and-limits.md), Proposition 1.2 and Theorem 4.1; [U021](convolution-as-addition-of-supports.md), B0–B2 and Theorem 1.1; [U025](zero-hypersurfaces-as-curvature-measures.md), Lemma 3.0 and its following measure-regularity proof. These are the exact available proofs used for distributions, compact partitions, parameter integrals, convolution and completed-measure substitution. All further metric identities, smoothness estimates and exercise calculations are proved here.
