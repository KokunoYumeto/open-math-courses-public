# Cauchy kernels and distributional boundary limits

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. The earlier edition was written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition and exercises: CC0. The separately credited programme prerequisites retain their own licences.*

A small circle around a pole records a point source. A horizontal line approaching the real axis records a boundary distribution. We compute both effects, keeping the orientation, the factor of pi and the number of test derivatives explicit. Between these calculations we prove that a weak harmonic distribution is a smooth function, and use that result to connect weak Cauchy–Riemann equations with ordinary complex differentiability.

The boundary-flux lesson supplies its proved graph surface measure, divergence theorem, smooth cutoffs and pointwise-to-weak first-order theorem. The [included scalar calculus](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md) and [integration proofs](../prerequisites/U011-free-foundations/banach-foundation-bridges.md) supply the elementary calculus and measure results used below. More precise locations follow the solutions.

## Test functions and local smoothing

We use complex-linear distributions. Concretely, a distribution \(u\) on an open \(X\subset\mathbb R^n\) is a linear functional on \(C_c^\infty(X)\) with this property: for every compact \(K\Subset X\), there are an integer \(m\ge0\) and a constant \(C\) such that

\[
 \begin{gathered}
 |u(\phi)|\le C\max_{|\alpha|\le m}\|\partial^\alpha\phi\|_\infty,\\
 \operatorname{supp}\phi\subset K.
 \end{gathered}
 \tag{D1}
\]

Here a multi-index is a tuple of nonnegative integers, \(|\alpha|\) is their sum, and \(\partial^\alpha\) is the corresponding iterated partial derivative. We define \((\partial_j u)(\phi)=-u(\partial_j\phi)\) and \((a u)(\phi)=u(a\phi)\) for a smooth multiplier \(a\). The finite product rule and (D1) show that these are distributions. Locally integrable functions define distributions by integration against the test, without conjugation. Two continuous functions with the same distribution are equal: if their difference is nonzero at a point, multiplying by a constant complex phase makes its real part positive nearby, and pairing with a nonnegative bump supported there gives a contradiction.

Mixed derivatives commute. For smooth functions this follows by writing the increment around a small coordinate rectangle as the iterated integral of each mixed derivative, using the fundamental theorem twice and Fubini, and then dividing by the rectangle's area and shrinking it. Applied to test functions, this proves commutation also for distributional derivatives. A direct test calculation gives the product rule

\[
 \partial_j(a u)=a\partial_j u+(\partial_j a)u.
 \tag{D2}
\]

Indeed, applying the right side to \(\phi\) gives \(-u(\partial_j(a\phi))+u((\partial_j a)\phi)=-u(a\partial_j\phi)\).

**Local kernel lemma.** Choose an even, nonnegative \(\rho\in C_c^\infty(\mathbb R^n)\), supported in the unit ball and with integral one. One may normalize a nonzero radial bump supplied by the cutoff proof. Set \(\rho_\epsilon(x)=\epsilon^{-n}\rho(x/\epsilon)\). Where \(\overline{B(x,\epsilon)}\subset X\), define

\[
 u_\epsilon(x)=u_y\bigl(\rho_\epsilon(x-y)\bigr).
 \tag{D3}
\]

Then \(u_\epsilon\) is smooth on this interior region and converges to \(u\) distributionally on every compactly contained open subset as \(\epsilon\downarrow0\). Derivatives can be taken on the smooth kernel. In particular, if \(\Delta u=0\), then \(\Delta u_\epsilon=0\).

**Proof.** Fix a compact set of output points for which all the translated kernel supports lie in one compact \(K\Subset X\). Take \(C,m\) from (D1). A kernel difference quotient converges to its indicated output derivative, uniformly together with all input derivatives through order \(m\). This is the fundamental theorem and uniform continuity of one further kernel derivative on a common compact set. Applying (D1) proves differentiability of (D3). Repeating it proves smoothness and all claimed derivative identities. Since \(\Delta_x\rho_\epsilon(x-y)=\Delta_y\rho_\epsilon(x-y)\), the weak equation gives the harmonicity assertion.

We also need an interchange of a distribution with a compact parameter integral. Suppose \(F(x,y)\) is smooth, with \(x\) in a compact integration box and with all its \(y\)-supports in \(K\). Riemann sums for \(\int F(x,\cdot)\,dx\) converge uniformly with all \(y\)-derivatives through order \(m\), because those derivatives are uniformly continuous on the compact product. Applying (D1) to their differences proves

\[
 u_y\left(\int F(x,y)\,dx\right)
       =\int u_y(F(x,y))\,dx.
 \tag{D4}
\]

This argument also applies when a compact smooth factor in \(x\) makes the integrand zero outside such a box. Differentiation under its ordinary integral follows from the same uniform convergence. All integrals here are over bounded boxes with continuous integrands, so the Riemann and Lebesgue integrals agree by their upper and lower step-function bounds.

For \(\phi\in C_c^\infty(X)\) and small \(\epsilon\), (D4) therefore gives

\[
 \begin{aligned}
 \int u_\epsilon(x)\phi(x)\,dx
 &=u_y\left(\int\rho_\epsilon(x-y)\phi(x)\,dx\right)\\
 &=u_y\left(\int\rho(z)\phi(y+\epsilon z)\,dz\right).
 \end{aligned}
 \tag{D5}
\]

For each derivative order, the function inside the last pairing converges uniformly to the corresponding derivative of \(\phi\). This follows by subtracting \(\partial^\alpha\phi(y)\) inside the integral, using \(\int\rho=1\) and uniform continuity. The supports lie in one compact subset of \(X\). Estimate (D1) now proves that (D5) tends to \(u(\phi)\). The same test approximation works in any fixed finite \(C^k\) norm when the test is only \(C_c^k\). \(\square\)

## A small circle detects the Cauchy kernel

Write \(z=x+iy\), \(dA=dx\,dy\), and

\[
 \begin{aligned}
 \partial_{\bar z}&=\tfrac12(\partial_x+i\partial_y),\\
 \partial_z&=\tfrac12(\partial_x-i\partial_y).
 \end{aligned}
 \tag{1.1}
\]

The region lies to the left of its positive boundary orientation. In particular an outer circle is counterclockwise and the inner circle of a punctured region is clockwise. Corollary 2.3 of the boundary-flux lesson proves

\[
 \begin{gathered}
 2\int_Y\partial_{\bar z}v\,dA
      =-i\int_{\partial_XY}v\,dz,\\
 v\in C_c^1(X),
 \end{gathered}
 \tag{1.2}
\]

for open \(Y\subset X\subset\mathbb C\) with relative \(C^1\) boundary.

We first verify the only singular area estimate needed below. Translation invariance and the proved disk-area formula give \(|B(a,t)|=\pi t^2\). Circles have zero area, as follows either from the boundary-flux lesson's graph-null-set argument or by enclosing a circle in annuli of arbitrarily small area. The image of area under \(z\mapsto|z-a|\), restricted to \(0<|z-a|\le r\), thus assigns \((s,t]\) the measure \(\pi(t^2-s^2)\). By the fundamental theorem this is also \(\int_s^t2\pi q\,dq\). The finite-measure uniqueness proof in the integration prerequisite, applied to these generating intervals, identifies the two measures on all Borel sets. Increasing simple approximations then give equality of their integrals for every nonnegative Borel function of the radius. Taking that function to be \(1/q\) proves

\[
 \int_{|z-a|<r}\frac{dA(z)}{|z-a|}=2\pi r.
 \tag{R1}
\]

The single point \(a\) has zero area. This also proves local integrability of the kernel.

**Theorem 1.1 (Cauchy–Pompeiu with a relative boundary).** Let \(Y\subset X\subset\mathbb C\) be open with relative \(C^1\) boundary. If \(\phi\in C_c^1(X)\) and \(\zeta\in Y\), then

\[
 \begin{aligned}
 \phi(\zeta)
 &=\frac1{2\pi i}\int_{\partial_XY}
                 \frac{\phi(z)}{z-\zeta}\,dz\\
 &\quad-\frac1\pi\int_Y
                 \frac{\partial_{\bar z}\phi(z)}{z-\zeta}\,dA(z).
 \end{aligned}
 \tag{1.3}
\]

Both integrals are ordinary integrals; compact support makes the formula meaningful also for unbounded \(Y\).

**Proof.** Choose \(\epsilon>0\) with \(\overline{B(\zeta,\epsilon)}\subset Y\). Away from \(\zeta\), the ordinary quotient rule gives

\[
 \partial_{\bar z}\left(\frac{\phi(z)}{z-\zeta}\right)
       =\frac{\partial_{\bar z}\phi(z)}{z-\zeta}.
 \tag{1.4}
\]

For a literal application of (1.2), multiply the quotient by a smooth cutoff which is zero within radius \(\epsilon/2\) and one beyond radius \(3\epsilon/4\). This is a compact \(C^1\) function on \(X\), agreeing with the quotient and its derivative on the punctured region. Its boundary is the old relative boundary together with the new inner circle. Denote the latter circle with counterclockwise orientation by \(C_\epsilon\). The opposite orientation in the punctured region gives

\[
 \begin{aligned}
 &\frac1{2\pi i}\int_{C_\epsilon}\frac{\phi(z)}{z-\zeta}\,dz\\
 &\quad=\frac1{2\pi i}\int_{\partial_XY}\frac{\phi(z)}{z-\zeta}\,dz\\
 &\qquad-\frac1\pi\int_{Y\setminus\overline{B(\zeta,\epsilon)}}
       \frac{\partial_{\bar z}\phi(z)}{z-\zeta}\,dA.
 \end{aligned}
 \tag{1.5}
\]

The parametrization \(z=\zeta+\epsilon e^{it}\), \(0\le t\le2\pi\), turns the left side into the circle average of \(\phi\). Its difference from \(\phi(\zeta)\) is bounded by the supremum of \(|\phi(z)-\phi(\zeta)|\) on that circle, which tends to zero. By (R1), the omitted area term has magnitude at most \(2\epsilon\|\partial_{\bar z}\phi\|_\infty\). Passing to the limit proves (1.3), with the displayed signs. \(\square\)

**Corollary 1.2 (the point-source normalization).** On the plane,

\[
 E_\zeta(z)=\frac1{\pi(z-\zeta)},
 \qquad \partial_{\bar z}E_\zeta=\delta_\zeta.
 \tag{1.6}
\]

This identity restricts to every open set containing \(\zeta\).

**Proof.** Given a compact smooth test, choose a disk containing both its support and \(\zeta\). The outer integral in (1.3) vanishes, leaving \(-\int E_\zeta\partial_{\bar z}\phi\,dA=\phi(\zeta)\). This is exactly the distributional derivative convention. A compact test on a smaller open set extends by zero smoothly to the plane, so the restricted identity follows too. \(\square\)

## Weak Cauchy–Riemann solutions are holomorphic

### Harmonic means and radial averaging

We prove the regularity needed for both \(\Delta\) on \(\mathbb R^n\), \(n\ge1\), and \(\partial_{\bar z}\) on \(\mathbb R^2\). Let \(B=B(0,1)\), \(S=\partial B\), and let \(dS\) be the graph surface measure proved in the boundary-flux lesson. Set \(b_n=|B|\). It is finite and positive: the ball is contained in a finite cube and contains a cube of positive side length.

For spheres the outward unit normal is their radial unit vector, by differentiating \(|x-a|^2-r^2\). A dilation by \(r>0\) multiplies surface measure by \(r^{n-1}\). To check this directly in a graph chart, the graph \(t=\gamma(x')\) becomes \(t=r\gamma(x'/r)\); its gradient at \(rx'\) is the old gradient, and the base measure gains the factor \(r^{n-1}\) by the affine change-of-variables proof. Sum over a finite chart partition. For \(n=1\), surface measure is counting measure on the two endpoints and this factor is one. Applying the divergence theorem to the field \(x\), with a cutoff equal to one near the closed unit ball, therefore gives

\[
 S(S)=n b_n.
 \tag{R2}
\]

Suppose \(h\) is \(C^2\) and harmonic on a neighborhood of \(\overline{B(a,R)}\). For \(0<r<R\), differentiate its unnormalized spherical mean:

\[
 \begin{aligned}
 M'(r)
 &:=\frac d{dr}\int_S h(a+r\omega)\,dS(\omega)\\
 &=\int_S\nabla h(a+r\omega)\cdot\omega\,dS(\omega)\\
 &=r^{1-n}\int_{\partial B(a,r)}\partial_\nu h\,dS=0.
 \end{aligned}
 \tag{R3}
\]

Differentiation is justified by uniform convergence of the difference quotients on the compact sphere. The last equality is the divergence theorem for \(\nabla h\), again localized by a compact cutoff. Since \(h(a+r\omega)\to h(a)\) uniformly as \(r\downarrow0\), we get \(M(r)=n b_n h(a)\).

For the ball mean put \(H(r)=\int_B h(a+ry)\,dy\). Differentiation under this compact integral and the divergence theorem for \(y\mapsto y h(a+ry)\) give

\[
 nH(r)+rH'(r)=M(r)=n b_n h(a).
\]

Consequently \((r^nH(r))'=n b_n h(a)r^{n-1}\). Integrate from \(\delta\) to \(r\), and let \(\delta\downarrow0\). The term \(\delta^nH(\delta)\) tends to zero because \(H\) is bounded near zero. The affine volume change of variables now proves

\[
 \int_{B(a,r)}h(x)\,dx=|B(a,r)|h(a).
 \tag{R4}
\]

These computations apply to complex \(h\), since the divergence theorem is complex linear. They also apply in dimension one, with the two endpoint normals \(-1,1\); no higher-dimensional polar-coordinate formula has been assumed.

Let \(\kappa\) be any smooth radial kernel supported in \(\overline{B(0,r)}\) with integral one. Write \(\kappa(z)=q(|z|)\), where \(q\) is smooth on \([0,\infty)\) and zero at and beyond \(r\). The fundamental theorem gives

\[
 q(s)=\int_s^r-q'(t)\,dt\quad(0\le s\le r).
\]

Hence \(\kappa(z)=\int_0^r-q'(t)1_{\{|z|<t\}}\,dt\), with endpoint values irrelevant to integration. On the compact ball, \(h\) is bounded and \(q'\) is bounded, so Fubini applies even if the kernel is signed. Using (R4) on each centered ball gives

\[
 \begin{aligned}
 &\int\kappa(z)h(a-z)\,dz\\
 &\quad=\int_0^r-q'(t)\,|B(0,t)|h(a)\,dt\\
 &\quad=h(a)\int\kappa(z)\,dz=h(a).
 \end{aligned}
 \tag{R5}
\]

### Local smoothing for both constant symbols

**Harmonic distribution lemma.** If \(u\in\mathcal D'(X)\) on an arbitrary open \(X\subset\mathbb R^n\), \(n\ge1\), and \(\Delta u=0\), then \(u\) is represented by a smooth harmonic function on \(X\).

**Proof.** Choose a ball \(V\) and \(r>0\) such that its closed \(3r\)-neighborhood lies compactly in \(X\). For \(0<\epsilon<r\), the local kernel lemma gives a smooth harmonic \(u_\epsilon\) on a neighborhood of the closed \(r\)-neighborhood of \(V\). Fix one smooth radial unit-mass kernel \(\kappa\) supported in radius \(r\). By (R5),

\[
 \begin{gathered}
 u_\epsilon(x)=\int\kappa(x-z)u_\epsilon(z)\,dz,\\
 x\in V.
 \end{gathered}
 \tag{R6}
\]

All input supports stay in one compact subset of \(X\). The interchange (D4), followed by an ordinary substitution, writes the right side as

\[
 u_y\bigl((\kappa*\rho_\epsilon)(x-y)\bigr).
\]

Here ordinary convolution means

\[
 \begin{aligned}
 &(\kappa*\rho_\epsilon)(w)\\
 &\quad=\int\kappa(w-t)\rho_\epsilon(t)\,dt.
 \end{aligned}
\]

For every derivative order, \(\kappa*\rho_\epsilon\to\kappa\) uniformly, by the same compact-kernel test approximation proved after (D5). Applying (D1), including any additional output derivatives, shows that (R6) converges uniformly with every derivative on compact subsets of \(V\) to

\[
 h(x)=u_y(\kappa(x-y)).
\]

The local kernel lemma makes this a smooth function. At the same time \(u_\epsilon\to u\) distributionally by (D5). Pairing the locally uniform limit with compact tests identifies \(u\) with \(h\) on \(V\). Since \(\Delta u=0\), the smooth function \(\Delta h\) has zero distribution and is therefore zero pointwise by the bump argument following (D1). Such balls cover \(X\), and their smooth representatives agree on overlaps by that same argument. They define the required smooth harmonic function on all of \(X\). \(\square\)

**Proposition 2.1 (exact regularity specialization).** If \(u\in\mathcal D'(X)\), \(X\subset\mathbb C\) open, and \(\partial_{\bar z}u=0\), then \(u\) is the distribution of a holomorphic function on \(X\).

**Proof.** Commutation of distributional derivatives gives \(\Delta=4\partial_z\partial_{\bar z}\). Thus \(\Delta u=0\), and the harmonic distribution lemma provides a smooth representative \(h\). Its \(\partial_{\bar z}\) derivative is zero pointwise, since its distribution is zero. Equivalently, \(h_y=ih_x\). For a real increment pair \((a,b)\), differentiability yields

\[
 \begin{aligned}
 &h(z+a+ib)-h(z)\\
 &\quad=h_x(z)(a+ib)+o(|a+ib|).
 \end{aligned}
 \tag{2.2}
\]

The complex derivative therefore exists at every point and equals \(h_x\), which is the asserted holomorphy. \(\square\)

For the differential-operator notation \(D_j=-i\partial_j\), the two symbols in the regularity proof are

\[
 \begin{aligned}
 p_{\bar\partial}(\xi)&=(i\xi_x-\xi_y)/2,\\
 |p_{\bar\partial}(\xi)|&=|\xi|/2,\\
 p_\Delta(\xi)&=-|\xi|^2.
 \end{aligned}
 \tag{2.1}
\]

They do not vanish at nonzero real covectors. Their distribution kernels are supported on the diagonal: define the diagonal distribution by \(\delta_{\mathrm{diag}}(\Phi)=\int\Phi(x,x)\,dx\), and apply the relevant differential operator in \(x\). Pairing with \(\Phi(x,y)=\phi(x)\psi(y)\) and integrating by parts gives \(\int\phi(x)P\psi(x)\,dx\), so this is the operator's kernel. The finite derivative estimate on each compact set proves it is a distribution, and every test vanishing near the diagonal pairs to zero. Either diagonal projection over a compact \(K\subset X\) has inverse image \(\{(x,x):x\in K\}\), a compact set; the same is true for the closed kernel support. This verifies the usual ellipticity and proper-support facts directly.

**Corollary 2.2 (complex differentiability is enough).** A function complex differentiable at every point of an open \(X\subset\mathbb C\) is smooth and has a convergent power series in each disk whose closure lies in \(X\).

**Proof.** Complex differentiability gives continuity, real Fréchet differentiability and the pointwise equation \((h_x+ih_y)/2=0\). Theorem 4.1 of the boundary-flux lesson applies with coefficients \(1/2,i/2\), zero zeroth-order coefficient and zero right side. It proves the weak equation without assuming continuity or integrability of the pointwise derivatives. Proposition 2.1 gives a smooth representative. Its difference from the original continuous function has zero distribution, so the two agree everywhere.

Choose \(\overline{B(a,R)}\subset X\) and a smooth compact cutoff equal to one near this closed disk. Apply (1.3) to the disk and to the cutoff times \(h\). Its \(\partial_{\bar z}\) derivative vanishes throughout the disk, hence

\[
 \begin{gathered}
 h(\zeta)=\frac1{2\pi i}\int_{|z-a|=R}
                        \frac{h(z)}{z-\zeta}\,dz,\\
 |\zeta-a|<R.
 \end{gathered}
 \tag{2.3}
\]

For \(|\zeta-a|\le r<R\), the geometric expansion of \(1/(z-\zeta)\) converges uniformly on the contour and has a summable bound with ratio \(r/R\). Integrating its finite partial sums and passing the uniform limit gives

\[
 \begin{aligned}
 h(\zeta)&=\sum_{j=0}^\infty c_j(\zeta-a)^j,\\
 c_j&=\frac1{2\pi i}\int_{|z-a|=R}\frac{h(z)}{(z-a)^{j+1}}\,dz,\\
 |c_j|&\le M R^{-j},\\
 M&=\max_{|z-a|=R}|h(z)|.
 \end{aligned}
 \tag{2.4}
\]

The coefficient bound uses the circle length \(2\pi R\) and \(|dz|=R\,dt\), both proved in the scalar and boundary prerequisites. Each fixed differentiated series also converges uniformly on smaller disks: its bound is a fixed polynomial in \(j\) times \((r/R)^j\). Such a series converges because the ratio of successive bounds is eventually below some number strictly between \(r/R\) and one. The termwise differentiation theorem from scalar calculus applies, giving \(h^{(j)}(a)=j!c_j\) and the estimate \(|h^{(j)}(a)|\le j!M R^{-j}\). \(\square\)

## Test derivatives balance polynomial growth

Let \(I\) be an open interval, \(\gamma>0\), and let \(f\) be holomorphic on the strip \(I+i(0,\gamma)\). Assume for some integer \(N\ge0\) that

\[
 \begin{gathered}
 |f(x+iy)|\le C y^{-N},\\
 x\in I,\quad 0<y<\gamma.
 \end{gathered}
 \tag{3.1}
\]

Corollary 2.2 has already proved all smoothness needed for differentiating \(f\) inside this strip. We allow compact tests with only \(N+1\) continuous derivatives.

**Theorem 3.1 (finite-regularity boundary tests).** For each \(\phi\in C_c^{N+1}(I)\), the limit

\[
 \langle f_+,\phi\rangle
    =\lim_{\epsilon\downarrow0}\int_I f(x+i\epsilon)\phi(x)\,dx
 \tag{3.2}
\]

exists. Restricted to smooth tests, it is a distribution of order at most \(N+1\). On each fixed compact test support, the positive-height pairings have a common \(C^{N+1}\) bound for all sufficiently small heights.

**Proof.** Extend \(\phi\) by zero to the real line. This remains \(C^{N+1}\) because its support lies compactly inside \(I\). For \(s\ge0\), form the finite polynomial

\[
 \Phi_N(x,s)=\sum_{j=0}^N\frac{(is)^j}{j!}\phi^{(j)}(x).
 \tag{3.3}
\]

Its horizontal support is the fixed compact support of the test. It is \(C^1\) in the two real variables. In \((\partial_x+i\partial_s)\Phi_N\), the \(x\)-derivative of term \(j\) cancels the \(i\partial_s\)-derivative of term \(j+1\). The only term left is

\[
 \partial_{\bar z}\Phi_N(x,s)
      =\frac{(is)^N}{2N!}\phi^{(N+1)}(x).
 \tag{3.4}
\]

This computation includes \(N=0\), when there is only the uncancelled term.

Fix \(0<T<\gamma\), take \(0<\epsilon<\gamma-T\), and define
\(A_\epsilon(s)=\int_I f(x+i(\epsilon+s))\Phi_N(x,s)\,dx\) for \(0\le s\le T\). All differentiations and integrations by parts at fixed \(\epsilon>0\) take place on a compact subset of the strip. The equation \(f_y=if_x\) and the absence of horizontal end terms give

\[
 \begin{aligned}
 A_\epsilon'(s)
 &=\int_I f(x+i(\epsilon+s))
                  (\partial_s-i\partial_x)\Phi_N(x,s)\,dx\\
 &=-\frac{i^{N+1}s^N}{N!}
           \int_I f(x+i(\epsilon+s))\phi^{(N+1)}(x)\,dx.
 \end{aligned}
 \tag{3.5}
\]

The fundamental theorem in \(s\) now yields the exact formula

\[
 \begin{aligned}
 &\int_I f(x+i\epsilon)\phi(x)\,dx\\
 &\quad=\int_I f(x+i(\epsilon+T))\Phi_N(x,T)\,dx\\
 &\qquad+\frac{i^{N+1}}{N!}\int_0^T s^N
       \int_I f(x+i(\epsilon+s))\phi^{(N+1)}(x)\,dx\,ds.
 \end{aligned}
 \tag{3.6}
\]

Choose a closed interval \(K\Subset I\) containing the support, and use its length \(|K|\). The integrand in the last term is dominated on \(K\times(0,T)\), because

\[
 s^N|f(x+i(\epsilon+s))|
       \le C\left(\frac{s}{\epsilon+s}\right)^N\le C.
 \tag{3.7}
\]

For \(N=0\), the power in this estimate is one. For every \(s>0\), the integrand converges as \(\epsilon\downarrow0\), and dominated convergence applies. The first term converges by continuity on the compact set at height \(T\). Thus the limit is

\[
 \begin{aligned}
 \langle f_+,\phi\rangle
 &=\int_I f(x+iT)\Phi_N(x,T)\,dx\\
 &\quad+\frac{i^{N+1}}{N!}\int_0^T s^N
            \int_I f(x+is)\phi^{(N+1)}(x)\,dx\,ds.
 \end{aligned}
 \tag{3.8}
\]

Every integral in (3.8) is absolutely convergent. From (3.6), (3.7) and \((\epsilon+T)^{-N}\le T^{-N}\), we obtain

\[
 \begin{aligned}
 \left|\int_I f(x+i\epsilon)\phi(x)\,dx\right|
 &\le C|K|\left(T^{-N}\sum_{j=0}^N\frac{T^j}{j!}
                     +\frac{T}{N!}\right)\\
 &\qquad\cdot\|\phi\|_{C^{N+1}},
 \end{aligned}
 \tag{3.9}
\]

where the norm is the largest supremum norm of the derivatives through order \(N+1\). This bound also holds for the limit. It proves (D1) with order \(N+1\), and hence distributional continuity. The value of (3.8) is independent of \(T\), since it is the limit of the same left side of (3.6). \(\square\)

The theorem proves a sufficient order bound. A holomorphic function extending smoothly through the interval has an order-zero boundary distribution, even if it also satisfies (3.1) with a larger \(N\).

**Corollary 3.2 (moving tests, lower boundaries and local bounds).** If \(\phi_\epsilon\to\phi\) in \(C^{N+1}\) and all tests have a common compact support in \(I\), then

\[
 \int_I f(x+i\epsilon)\phi_\epsilon(x)\,dx
       \longrightarrow\langle f_+,\phi\rangle.
 \tag{3.10}
\]

For a holomorphic function on \(I+i(-\gamma,0)\) with \(|f(x-iy)|\le C y^{-N}\), the lower boundary \(f_-\) exists on the same test class. Formula (3.8) then has height \(-T\), polynomial \(\sum_{j=0}^N(-is)^j\phi^{(j)}(x)/j!\), and coefficient \((-i)^{N+1}/N!\). The same norm bound holds. Bounds of this form on each relatively compact subinterval suffice for local boundary distributions.

**Proof.** Estimate the pairing with \(\phi_\epsilon-\phi\) by (3.9); its norm tends to zero. The fixed-test pairing converges by the theorem. For the lower boundary apply the upper result to \(g(w)=f(-w)\) on the reflected interval and to \(\psi(t)=\phi(-t)\). In the change of variable \(x=-t\), the reversed integration endpoints cancel the Jacobian sign, whereas \(\psi^{(j)}(t)=(-1)^j\phi^{(j)}(-t)\). These are exactly the signs in the asserted polynomial and coefficient. For local bounds, use the theorem on a slightly larger compact interval around any given test support. On overlaps the limits agree because their positive- or negative-height pairings are identical for each test there. \(\square\)

The finite-norm test approximation following (D5), with support in a common slightly larger interval, shows that these formulas give the unique continuous extension of the smooth-test boundary distribution to \(C_c^{N+1}\) tests with fixed compact support.

## A real pole remembers the side of approach

For \(\phi\in C_c^1(\mathbb R)\), symmetric deletion gives

\[
 \begin{aligned}
 \left\langle\operatorname{pv}\frac1x,\phi\right\rangle
 &:=\lim_{r\downarrow0}\int_{|x|>r}\frac{\phi(x)}x\,dx\\
 &=\int_0^\infty\frac{\phi(x)-\phi(-x)}x\,dx.
 \end{aligned}
 \tag{4.1}
\]

Indeed, the fundamental theorem bounds the difference in the numerator by \(2x\|\phi'\|_\infty\). The last integrand is bounded near zero and has bounded support, so dominated convergence justifies the limit. If the support lies in \([-R,R]\), its magnitude is at most \(2R\|\phi'\|_\infty\). Thus (4.1) defines a distribution of order at most one and its continuous action on these \(C^1\) tests.

**Theorem 4.1 (individual pole limits and their jump).** As distributions and on every compact \(C^1\) test,

\[
 \begin{aligned}
 (x+i0)^{-1}&=\operatorname{pv}(1/x)-i\pi\delta_0,\\
 (x-i0)^{-1}&=\operatorname{pv}(1/x)+i\pi\delta_0.
 \end{aligned}
 \tag{4.2}
\]

In particular, the upper value minus the lower value is \(-2\pi i\delta_0\).

**Proof.** For \(y>0\), multiply by the conjugate denominator to write

\[
 (x+iy)^{-1}=\frac{x}{x^2+y^2}-i\frac{y}{x^2+y^2}.
 \tag{4.3}
\]

The odd real kernel pairs with \(\phi\) as

\[
 \int_0^R\frac{x(\phi(x)-\phi(-x))}{x^2+y^2}\,dx.
\]

Its integrand is bounded in magnitude by \(2\|\phi'\|_\infty\), independently of \(y\), and tends to the integrand of (4.1). Dominated convergence identifies its limit with the principal value.

For the even kernel, substitute \(x=yt\):

\[
 \begin{aligned}
 \int_{\mathbb R}\frac{y\phi(x)}{x^2+y^2}\,dx
     &=\int_{\mathbb R}\frac{\phi(yt)}{1+t^2}\,dt\\
     &\longrightarrow\pi\phi(0).
 \end{aligned}
 \tag{4.4}
\]

The dominating function is \(\|\phi\|_\infty/(1+t^2)\). Its integral is finite and equals \(\pi\): the scalar prerequisite constructs \(\arctan t=\int_0^t(1+s^2)^{-1}\,ds\) and proves its endpoint limits \(\pm\pi/2\). The upper sign in (4.2) now follows from (4.3). Replacing \(iy\) by \(-iy\) reverses precisely the even imaginary term and gives the lower sign. These calculations also give the uniform bound \(2R\|\phi'\|_\infty+\pi\|\phi\|_\infty\) for every \(y>0\). \(\square\)

For integers \(m\ge1\), define a normalized finite part by

\[
 \operatorname{pf}(x^{-m})
     =\frac{(-1)^{m-1}}{(m-1)!}
           \partial_x^{m-1}\operatorname{pv}(1/x).
 \tag{4.5}
\]

On tests supported away from zero, repeated ordinary integration by parts identifies it with the function \(x^{-m}\). The derivative definition specifies its value across the singular point.

**Corollary 4.2 (higher poles and their test order).** For every integer \(m\ge1\),

\[
 \begin{aligned}
 (x\pm i0)^{-m}
 &=\operatorname{pf}(x^{-m})\\
 &\quad\mp i\pi\frac{(-1)^{m-1}}{(m-1)!}\delta_0^{(m-1)}.
 \end{aligned}
 \tag{4.6}
\]

The limits exist on \(C_c^m\) tests. Their difference pairs with such a test as
\(-2\pi i\,\phi^{(m-1)}(0)/(m-1)!\).

**Proof.** Ordinary differentiation at positive \(y\) gives

\[
 (x\pm iy)^{-m}
     =\frac{(-1)^{m-1}}{(m-1)!}
                       \partial_x^{m-1}(x\pm iy)^{-1}.
\]

After \(m-1\) integrations by parts, the pairing is \(1/(m-1)!\) times the simple-pole pairing with \(\phi^{(m-1)}\). That derivative is a compact \(C^1\) function when \(\phi\in C_c^m\), so Theorem 4.1 gives its limit. The principal-value term agrees with (4.5) by the definition of a distributional derivative. The concentrated term agrees with (4.6) because \(\delta_0^{(m-1)}(\phi)=(-1)^{m-1}\phi^{(m-1)}(0)\). For support in \([-R,R]\), the same proof bounds every positive-height pairing by

\[
 \frac{2R\|\phi^{(m)}\|_\infty+
               \pi\|\phi^{(m-1)}\|_\infty}{(m-1)!}.
\]

This proves the finite-test continuity as well as distributional convergence. \(\square\)

For \(m=2\), the upper boundary is \(\operatorname{pf}(x^{-2})+i\pi\delta'_0\). Its jump against a test is \(-2\pi i\phi'(0)\); the minus sign comes from the action of \(\delta'_0\).

## Exercises

**Exercise 1 (basic: orientation and a point source).** A compact \(C^1\) function equals one near zero. Compute its quotient by \(z\), integrated over a small circle with each orientation. Relate the two values to the point source of the Cauchy kernel.

**Exercise 2 (intermediate: a translated pole).** For a real \(a\), compute the two boundary values of \((z-a)^{-1}\). Give the jump against a compact test, including the case when its support misses \(a\).

**Exercise 3 (intermediate: assembling a principal part).** Compute both boundary distributions and the jump of \(2(z-a)^{-3}-3(z-a)^{-1}\), with \(a\in\mathbb R\). Express the jump using the values of the test and its second derivative at \(a\).

**Exercise 4 (advanced: a shrinking family of tests).** Under (3.1), let tests have a common compact support and \(\|\phi_\epsilon\|_{C^{N+1}}\le\epsilon^{1/3}\). Prove their positive-height pairings tend to zero. Identify exactly where the last test derivative is used, and explain what would be missing from an attempted \(C^N\) estimate by this proof.

**Exercise 5 (intermediate: regularity before continuous derivatives).** Explain why everywhere complex differentiability gives a smooth function, specifying the pointwise-to-weak and regularity steps. Verify the symbol and proper-support facts in (2.1), and derive \(|h^{(j)}(a)|\le j!M/R^j\). As a dimension-one check on the harmonic distribution lemma, prove that a distribution \(u\) on an open interval satisfying \(u''=0\) has the form \(u(x)=\alpha+\beta x\).

**Exercise 6 (advanced: multiplying a finite part).** Prove the identities \(x\operatorname{pv}(1/x)=1\), \(x\operatorname{pf}(x^{-2})=\operatorname{pv}(1/x)\) and \(x\delta'_0=-\delta_0\). Use them to verify \(x(x\pm i0)^{-2}=(x\pm i0)^{-1}\), including the concentrated terms.

## Complete solutions

**Solution 1.** On a small counterclockwise circle, \(z=re^{it}\) and the cutoff is one. Thus its quotient by \(z\) times \(dz\) is \(i\,dt\), with integral \(2\pi i\). Reversing orientation gives \(-2\pi i\). The latter is the inner-boundary contribution of the punctured region in (1.5). Moving it to the other side and letting the radius shrink leaves evaluation of the test at zero. After division by \(\pi\), the distributional identity is \(\partial_{\bar z}(1/(\pi z))=\delta_0\). Dropping that boundary contribution would lose this nonzero point source.

**Solution 2.** Substitute \(t=x-a\) in the two simple-pole pairings. The results are \(\operatorname{pv}(1/(x-a))\mp i\pi\delta_a\), with the minus sign for the upper side. Subtracting the lower value from the upper gives \(-2\pi i\phi(a)\). This vanishes when the support misses \(a\); there both boundary distributions are the same smooth function \((x-a)^{-1}\).

**Solution 3.** Translation of (4.6) with \(m=3\) gives the upper concentrated term \(-i\pi\delta_a''/2\) for the cubic pole. After multiplying by two and adding the simple-pole contribution with coefficient \(-3\), we obtain

\[
 \begin{aligned}
 f_+={}&2\operatorname{pf}((x-a)^{-3})
                -3\operatorname{pv}(1/(x-a))\\
      &-i\pi\delta_a''+3i\pi\delta_a,\\
 f_-={}&2\operatorname{pf}((x-a)^{-3})
                -3\operatorname{pv}(1/(x-a))\\
      &+i\pi\delta_a''-3i\pi\delta_a.
 \end{aligned}
\]

Their jump is \(-2i\pi\delta_a''+6i\pi\delta_a\). Its value on \(\phi\) is \(-2i\pi\phi''(a)+6i\pi\phi(a)\), because the second distributional derivative has a positive test-pairing sign.

**Solution 4.** Enclose the common support in a closed interval \(K\Subset I\), and fix \(T\) as in the theorem. Bound (3.9) is a fixed constant times \(\epsilon^{1/3}\), so it tends to zero once \(\epsilon<\gamma-T\). In (3.4), cancellation leaves \(s^N\phi_\epsilon^{(N+1)}\). The power \(s^N\) controls the strip growth in (3.7), while the \((N+1)\)-st derivative supplies the remaining test norm. A \(C^N\) bound does not control it, so the displayed argument would not justify that smaller norm. This identifies a limitation of this estimate; it does not rule out sharper estimates for particular functions.

**Solution 5.** Complex differentiability makes \(h\) continuous and real differentiable, with \(h_y=ih_x\) pointwise. The boundary-flux lesson's Theorem 4.1 supplies the weak equation using coefficients \(1/2,i/2\). Proposition 2.1 then applies the harmonic distribution lemma to obtain a smooth representative; continuity identifies it with \(h\). Substituting \(D=-i\partial\) gives the symbol \((i\xi_x-\xi_y)/2\), whose squared magnitude is \((\xi_x^2+\xi_y^2)/4\). Its kernel is the indicated derivative of the diagonal distribution. Either projection over a compact set has compact inverse image in that closed diagonal support, proving properness. Formula (2.4) gives \(|c_j|\le MR^{-j}\) and \(h^{(j)}(a)=j!c_j\), which proves the bound.

In dimension one, the harmonic distribution lemma makes \(u\) a smooth function on the interval. Its second derivative is zero pointwise. The mean value theorem applied to its first derivative, and then the fundamental theorem applied to the function, give \(u'\equiv\beta\) and \(u(x)=\alpha+\beta x\). Both constants may be complex. This argument uses connectedness of the interval, as required for a single pair of constants.

**Solution 6.** In symmetric deletion, multiplication by \(x\) cancels the quotient, so the limit is \(\int\phi\) by dominated convergence. Write \(v=\operatorname{pv}(1/x)\); then \(xv=1\) and \(\operatorname{pf}(x^{-2})=-v'\). The product rule (D2) gives \(0=(xv)'=v+xv'\), hence \(x\operatorname{pf}(x^{-2})=v\). Directly, \((x\delta'_0)(\phi)=-(x\phi)'(0)=-\phi(0)\), so \(x\delta'_0=-\delta_0\). Multiplying the upper second-pole formula by \(x\) now gives \(v-i\pi\delta_0\), and multiplying the lower one gives \(v+i\pi\delta_0\). These are exactly (4.2), with their concentrated terms preserved.

## Programme proof locations and freely accessible sources

The internal proof dependencies are the following included programme texts:

- Boundary flux and weak identities: the graph lemma and cutoff construction in Section 1; Theorem 2.1 and Corollary 2.3 for surface measure, divergence and complex Green; Theorem 4.1 for the pointwise-to-weak equation. Its finite-corner Corollary 2.4 also covers half-disks when such contours are used in later lessons.
- [Scalar calculus and Euclidean topology](../prerequisites/U011-free-foundations/metric-foundation-bridges.md#13-1-limits-with-all-original-scalar-and-coordinate-factors): Sections 12.1–12.9 and 13.1–13.5 supply the field, compactness, mean value theorem, derivatives and integrals; Sections 13.7–13.10 supply termwise differentiation, trigonometric functions, arctangent and smooth cutoffs.
- [Complex scalars and finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md#10-full-finite-linear-algebra-foundations): Sections 10.1–10.6 prove the scalar, finite-coordinate and norm identities used in those calculus proofs.
- [Lebesgue integration and smoothing](../prerequisites/U011-free-foundations/banach-foundation-bridges.md#15-0-constructing-the-measure-without-importing-a-convergence-theorem): Sections 15.0–15.4 and 16.1–16.2 prove measure construction, convergence, Fubini, affine changes and measure uniqueness; Section 15.6 through (PC5) proves the disk-area identity. The distributional smoothing and harmonic regularity required here are proved explicitly above.

These selections retain their CC0 1.0 notices. The following freely accessible human sources informed the mathematical constructions:

- Avi Zeff, [*Lecture 12: Pompeiu's formula*](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_12.html), 6 March 2026, Section 2. The shrinking-circle argument motivates the complete relative-boundary proof above, including its singular area estimate.
- Michael Kunzinger, [*Theory of Distributions*, free author lecture notes](https://www.mat.univie.ac.at/~mike/teaching/ss19/distributions.pdf), 2019, Examples 1.2.7–1.2.8 and Section 4.3, Theorems 4.3.1–4.3.2. These provide the principal-value cancellation, pole-limit computation and regularization methods. We prove the required one-dimensional integral normalization, finite-test bounds and local kernel pairings explicitly.
- Sheldon Axler, Paul Bourdon and Wade Ramey, [*Harmonic Function Theory*, freely readable author-hosted second edition](https://www.axler.net/HFT.pdf), updated 17 July 2020, mean-value section. The proof above derives the spherical and ball averages from the included flux theorem, proves radial reproduction directly, and includes dimension one. The author's PDF retains its copyright.
- Debraj Chakrabarti and Rasul Shafikov, [*Distributional boundary values of holomorphic functions on product domains*, free author-hosted paper](https://math.sci.uwo.ca/~shafikov/papers/MathZ2017.pdf), 2017, Section 2.5, Theorem 2.4, and Section 2.6. Their integration-by-parts construction explains how derivatives of tests compensate for polynomial boundary growth. Formulas (3.3)–(3.9) above give the complete strip calculation, including the explicit order \(N+1\) estimate; no theorem about boundary currents is assumed.
