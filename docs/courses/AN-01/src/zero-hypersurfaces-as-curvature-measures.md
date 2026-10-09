# Zero hypersurfaces as curvature measures

*Reconstructed and directly checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition by GPT-6.1 Sol (OpenAI). Original exposition: CC0. No independent review.*

For a holomorphic function, the singularities of its logarithmic modulus have a geometric interpretation: their Laplacian is surface area on the zero set, counted with multiplicity. A calculation on a smooth branch establishes only part of this statement. The proof below also accounts for every exceptional zero, proves ambient local finiteness of the surface measure, and determines the whole matrix of second derivatives.

The analytic inputs are the fully proved [logarithm stability and null-zero-set results](compactness-and-complex-line-positivity.md), Lemma 3.1 and Theorem 3.3; the [planar logarithmic source](point-sources-and-complex-gaussian-kernels.md), Corollary 1.2; [positive Riesz representation and convergence on continuous tests](order-positivity-and-limits.md), Theorem 4.1 and Theorem 5.2; and planar flux, Theorem 2.1. The [polydisk Cauchy and identity proofs](holomorphic-boundaries-in-convex-cones.md), Section 3, and [parameter integration and tensor differentiation](convolution-as-addition-of-supports.md), B1–B3, supply the remaining analytic operations. A general change of variables is proved here, rather than presumed among the entry requirements. Exact foundation locations and the freely accessible mathematical sources are listed at the end.

The complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the finite-order remainders used here, including signed increments, complex-valued functions, directional derivatives and uniform bounds for all required derivatives on compact neighborhoods.

## 1. Which zero points form a smooth branch?

Throughout, \(X\subset\mathbb C^n\) is open and \(f\) is holomorphic, with no identically zero connected component. Set \(u=\log|f|\), allowing the value \(-\infty\) at a zero. U024 proves both local integrability and plurisubharmonicity. Our conventions are

\[
\begin{aligned}
\partial_{z_j}&=\tfrac12(\partial_{x_j}-i\partial_{y_j}),&
\partial_{\bar z_j}&=\tfrac12(\partial_{x_j}+i\partial_{y_j}),\\
L_wu&=\sum_{j,k}w_j\overline{w_k}\,
             \partial_{z_j}\partial_{\bar z_k}u,&
\Delta u&=4\sum_jL_{e_j}u .
\end{aligned}
\tag{1.1}
\]

Each \(L_wu\) is a positive Radon measure by U024, Theorem 1.1. Distributional tests are paired linearly, without conjugation.

Let \(Z\) be the set of zeros admitting an ambient neighborhood on which

\[
f=g h^m,\qquad g\ne0,\qquad dh\ne0,\qquad
h(p)=0,\qquad m\in\{1,2,\ldots\}.
\tag{1.2}
\]

The factors \(g,h\) are holomorphic. We call this a *pure branch*. The implicit graph proof below shows that its reduced zero set is smooth. A crossing or a singular reduced branch need not be in \(Z\). We will define Euclidean surface measure \(dS\) on this set and extend it by zero to \(X\); its local finiteness in \(X\) will be a conclusion, not an assumption. Write

\[
|dh|^2=\sum_j|h_{z_j}|^2,\qquad
dh(w)=\sum_jh_{z_j}w_j .
\tag{1.3}
\]

Away from the zeros, shrink a neighborhood until \(f=c(1+v)\), where \(c\ne0\) and \(|v|<q<1\). The convergent series for \(\log(1+v)\) is holomorphic and has real part \(\log|1+v|\); its termwise derivatives converge on smaller neighborhoods. Thus \(\log|f|\) is locally the real part of a holomorphic function plus a constant. All its Levi derivatives vanish there. These series identities were proved in U020, Corollary 1.2, from U015's Cauchy estimates.

## 2. Construct the holomorphic graph we need

**Lemma 2.1 (scalar implicit graph).** Suppose \(F(t,z)\) is holomorphic near \((0,0)\in\mathbb C\times\mathbb C^d\), \(F(0,0)=0\), and \(F_t(0,0)\ne0\). On a sufficiently small product \(D_r\times V\), its zero set is exactly

\[
t=a(z),\qquad a:V\longrightarrow D_r\text{ holomorphic}.
\tag{2.1}
\]

**Proof.** Put \(c=F_t(0,0)\) and \(H(t,z)=t-F(t,z)/c\). Continuity of \(H_t\), which vanishes at the origin, gives a closed product on which

\[
|H_t|\le q<1,\qquad
|H(0,z)|\le (1-q)r/2 .
\tag{2.2}
\]

First choose \(r\) small for the derivative bound, then shrink the base for the second inequality. Integrating \(H_t\) on the straight segment between two points of \(\overline D_r\) gives the contraction bound \(q|t-s|\). In particular, \(H\) sends that disk strictly into itself, since \(qr+(1-q)r/2<r\). Starting with \(a_0=0\), define \(a_{j+1}(z)=H(a_j(z),z)\). Induction gives

\[
|a_{j+1}-a_j|\le q^j(1-q)r/2,\qquad
|a-a_j|\le rq^j/2,\qquad |a|\le r/2.
\tag{2.3}
\]

The sum converges uniformly in \(z\). Its limit is a fixed point by continuity, and two fixed points have distance at most \(q\) times their distance, so coincide. The equation \(H(t,z)=t\) is precisely \(F(t,z)=0\).

Every iterate is holomorphic by the chain rule. For completeness, this rule follows by inserting the differentiability remainder of the inner map into that of the outer map; the product of the two complex-linear differentials is again complex-linear. Holomorphic power series and all their derivatives converge on smaller polydisks by U015. On such a base polydisk the iterates satisfy its iterated Cauchy formula. Uniform convergence permits passage to the limit in the compact contour integral:

\[
a(z)=\frac{1}{(2\pi i)^d}
\int_{\partial D_1}\cdots\int_{\partial D_d}
\frac{a(\zeta)}{\prod_{\ell=1}^d(\zeta_\ell-z_\ell)}
\,d\zeta_d\cdots d\zeta_1 .
\tag{2.4}
\]

The right side has a convergent power series on every smaller polydisk, obtained by the product geometric series with its uniform bound. This proves holomorphy of \(a\). For \(d=0\) the argument is simply a unique scalar root. \(\square\)

**Lemma 2.2 (division along a graph).** Let \(a(z)\) and \(F(t,z)\) be holomorphic near the graph in question. Suppose

\[
\partial_t^\ell F(a(z),z)=0\quad(0\le\ell<m).
\tag{2.5}
\]

Then, near the graph, \(F(t,z)=(t-a(z))^mG(t,z)\) with \(G\) holomorphic. At a graph point where \(\partial_t^mF\ne0\), \(G\) is nonzero nearby.

**Proof.** Use coordinates \(t=a(z)+s\) on a small product. Repeated scalar FTC along the segment from \(0\) to \(s\) gives

\[
\begin{aligned}
F(a(z)+s,z)&=s^mG(a(z)+s,z),\\
G(a(z)+s,z)&=\frac1{(m-1)!}\int_0^1
 (1-\theta)^{m-1}\partial_t^mF(a(z)+\theta s,z)\,d\theta,\\
G(a(z),z)&=\partial_t^mF(a(z),z)/m! .
\end{aligned}
\tag{2.6}
\]

The integral is holomorphic: on compact smaller products its integrand and all first derivatives are uniformly bounded, so difference quotients pass through the integral by U021, B1. The last identity and continuity give the asserted nonvanishing. \(\square\)

## 3. The real area factor and the multiplicity

We first close the change-of-variables input needed for chart independence. All integrals in the next lemma are ordinary real Lebesgue integrals.

**Lemma 3.0 (change of variables).** If \(\chi:V\to W\) is a \(C^1\) diffeomorphism between open subsets of \(\mathbb R^d\), meaning that its inverse is also \(C^1\), then, for every nonnegative Borel function \(b\),

\[
\int_W b(y)\,dy
 =\int_V b(\chi(x))\,|\det D\chi(x)|\,dx .
\tag{3.0a}
\]

The same identity holds for integrable real or complex functions.

**Proof.** For \(d=0\) there is only the one-point counting measure. Suppose \(d\ge1\). Choose a nonnegative continuous function \(\eta\) supported in the unit ball, with integral one, using the proved scalar cutoff construction. Put \(\eta_\epsilon(v)=\epsilon^{-d}\eta(v/\epsilon)\) and \(J(x)=|\det D\chi(x)|>0\). The chain rule applied to both inverse compositions gives \(D\chi^{-1}(\chi(x))=(D\chi(x))^{-1}\).

Fix a compact \(K\subset W\). A closed \(\delta\)-neighborhood of \(K\) lies compactly in \(W\); on it \(\|D\chi^{-1}\|\le C\), enlarging \(C\) to be positive. If \(y\in K\), \(\epsilon<\delta\), and \(\eta_\epsilon(\chi(x)-y)\ne0\), the segment from \(y\) to \(\chi(x)\) remains in that neighborhood. The coordinate FTC therefore gives

\[
|x-\chi^{-1}(y)|\le C|\chi(x)-y|\le C\epsilon.
\tag{3.0b}
\]

Choose \(M>C+1\). Compactness of \(\chi^{-1}(K)\) permits a further uniform bound on \(\epsilon\) so that \(\chi^{-1}(y)+\epsilon\overline B_M\subset V\). The *linear* change of variables, already proved in the measure foundations, now yields, with \(a=\chi^{-1}(y)\),

\[
\begin{aligned}
g_\epsilon(y)
&=\int_V\eta_\epsilon(\chi(x)-y)\,dx\\
&=\int_{B_M}
 \eta\!\left(\frac{\chi(a+\epsilon t)-\chi(a)}{\epsilon}\right)\,dt
 \ \longrightarrow\ \int_{\mathbb R^d}\eta(D\chi(a)t)\,dt
 =J(a)^{-1}.
\end{aligned}
\tag{3.0c}
\]

Indeed, differentiability gives pointwise convergence of the integrand. Its absolute value is at most \(\|\eta\|_\infty 1_{B_M}\). The limiting integrand also vanishes outside \(B_C\), because \(\|(D\chi(a))^{-1}\|\le C\). Dominated convergence proves the limit and the common bound \(g_\epsilon(y)\le \|\eta\|_\infty |B_M|\), uniformly for \(y\in K\). The integration region must contain this entire inverse image of the kernel support; using only the original support of \(\eta\) would be unjustified.

Take \(\phi\in C_c(W)\) and extend \(h(y)=\phi(y)J(\chi^{-1}(y))\) by zero to \(\mathbb R^d\). This extension is continuous with compact support. Fubini gives the two expressions

\[
\begin{aligned}
I_\epsilon
&=\int_W h(y)g_\epsilon(y)\,dy\\
&=\int_V\int_W h(y)\eta_\epsilon(\chi(x)-y)\,dy\,dx .
\end{aligned}
\tag{3.0d}
\]

They are absolutely integrable: for small \(\epsilon\) both \(y\) and \(\chi(x)\) lie in a fixed compact subset \(L\) of \(W\), whose inverse image is compact in \(V\). The first expression tends to \(\int_W\phi\), by (3.0c) and its common bound. In the second, the inner integral is \((h*\eta_\epsilon)(\chi(x))\). Linear substitution gives
\((h*\eta_\epsilon)(v)=\int h(v-\epsilon t)\eta(t)\,dt\);
uniform continuity of \(h\) shows uniform convergence to \(h(v)\). The fixed compact \(\chi^{-1}(L)\) then shows that the second expression tends to \(\int_V\phi(\chi(x))J(x)\,dx\). This proves (3.0a) on \(C_c(W)\).

The image under \(\chi\) of \(J(x)\,dx\) is a locally finite Radon measure: compact inverse images are compact, and the inner and outer approximations for the continuous weighted Lebesgue measure transfer under the homeomorphism. The uniqueness part of the proved positive Riesz theorem in U008 identifies it with Lebesgue measure on \(W\). Indicators, simple functions and monotone convergence give all nonnegative Borel \(b\); positive and negative parts give the integrable versions. This also extends to completed Lebesgue measures. A homeomorphism maps Borel sets to Borel sets, and the indicator identity says that a Borel set and its image are simultaneously null, since \(J>0\); every subset of a null Borel set is therefore carried to a null measurable set. \(\square\)

We will also use the following **measure regularity fact**. Any locally finite Borel measure \(\nu\) on a Euclidean open set is Radon. To prove it using the supplied foundations, apply positive Riesz representation to \(I(\phi)=\int\phi\,d\nu\) on \(C_c\), obtaining a Radon measure \(\rho\). On every open set \(U\), the increasing compactly supported cutoffs from the positive-measure foundations, after (M3), converge to \(1_U\). Monotone convergence gives \(\rho(U)=\nu(U)\). Restrict to a relatively compact open set, where both measures are finite. Relative open sets form an intersection-closed generating class, so the proved generating-class uniqueness argument in the measure foundations, Section 16.2, gives equality on every Borel set there. An increasing exhaustion gives \(\rho=\nu\) on the entire open set, proving the fact.

For an injective \(C^1\) parametrization \(\gamma:O\subset\mathbb R^{2n-2}\to Z\) with injective differential and \(C^1\) chart transitions, define

\[
dS=\sqrt{\det(D\gamma^{\mathsf T}D\gamma)}\,dx .
\tag{3.1}
\]

If another parametrization is \(\gamma\circ\chi\), its Gram matrix is \(D\chi^{\mathsf T}(D\gamma^{\mathsf T}D\gamma)D\chi\). Determinant multiplicativity gives the factor \(|\det D\chi|\) in the square root. Lemma 3.0 proves equality of the resulting measures on every Borel subset of the overlap. In our charts the inverse is an ambient linear projection restricted to the graph, so the transition and its inverse are indeed \(C^1\); no inverse-function theorem is being presumed.

The pure-branch neighborhoods make \(Z\) relatively open in the closed set \(\{f=0\}\), hence Borel. Euclidean space has a countable base of rational balls, and any subspace does as well. Selecting one covering chart for each contained basic neighborhood produces a countable subcover. Partition this cover into disjoint Borel pieces by removing earlier charts and sum their chart measures. Compatibility proves independence of the cover and partition. This defines a measure even before ambient finiteness is known. When \(n=1\), charts have dimension zero and \(dS\) is counting measure.

**Lemma 3.1 (complex graph area).** For a holomorphic graph \(\gamma(z)=(a(z),z)\), with \(z\in\mathbb C^{n-1}\),

\[
dS=(1+|a'(z)|^2)\,d\lambda(z),\qquad
|a'|^2=\sum_{\ell=1}^{n-1}|a_{z_\ell}|^2 .
\tag{3.2}
\]

**Proof.** Write \(a_{z_\ell}=\alpha_\ell+i\beta_\ell\). The two real rows of \(B=Da\) are

\[
(\alpha_1,-\beta_1,\ldots,\alpha_{n-1},-\beta_{n-1}),\quad
(\beta_1,\alpha_1,\ldots,\beta_{n-1},\alpha_{n-1}).
\tag{3.3}
\]

Their dot product is zero and both squared lengths are \(|a'|^2\). If this number is positive, normalize the rows and complete to an orthonormal basis by subtracting projections from a basis and dividing each nonzero residual by its norm. On the two row directions \(I+B^{\mathsf T}B\) acts as multiplication by \(1+|a'|^2\); on their orthogonal complement it acts as the identity. Thus its determinant is \((1+|a'|^2)^2\). If \(|a'|=0\), the Gram matrix is the identity. Taking the positive square root proves the assertion in both cases. For \(n=1\), the empty Gram determinant is one.

For \(h=t-a(z)\) in these coordinates this says

\[
|dh|^2=1+|a'|^2,\qquad dh(e_t)=1,\qquad
\frac{|dh(e_t)|^2}{|dh|^2}\,dS=d\lambda(z).
\tag{3.4}
\]

\(\square\)

The formula does not depend on the chosen reduced equation. If \(\widetilde h\) is another defining function with nonzero differential for this same graph, differentiation of \(\widetilde h(a(z),z)=0\) gives
\(\widetilde h_{z_\ell}=-\widetilde h_t a_{z_\ell}\).
Consequently \(\widetilde h_t\ne0\) on the graph. Lemma 2.2 with \(m=1\) gives \(\widetilde h=b(t-a)\), with \(b\ne0\) nearby. On the graph \(d\widetilde h=b\,d(t-a)\), so every ratio \(|dh(w)|^2/|dh|^2\) is unchanged. Applying the same argument to \(h\) in (1.2), the order of \(t\mapsto f(t,z)\) at \(a(z)\) is exactly \(m\). The first nonzero coefficient of its convergent one-variable Taylor series uniquely determines that order. Thus \(m\) is unambiguous and locally constant on \(Z\), in particular Borel.

## 4. Fibre counts are continuous measures

Fix orthonormal complex coordinates \((t,z)\) near a zero, translated to the origin, for which \(t\mapsto f(t,0)\) has a finite order \(k\). We will later produce enough such directions.

**Lemma 4.1 (constant count and the directional source).** A disk \(D_r\) and connected base polydisk \(V\) can be chosen so that every fibre \(f(\,\cdot\,,z)\) has exactly \(k\) zeros in \(D_r\), counted with order. For every \(\phi\in C_c(D_r\times V)\),

\[
\langle L_{e_t}u,\phi\rangle
 =\frac{\pi}{2}\int_V
       \sum_{p:\,f(p,z)=0}m(p,z)\phi(p,z)\,d\lambda(z).
\tag{4.1}
\]

The sum is a continuous function of \(z\); it does not require a choice of root labels.

**Proof.** The one-variable Taylor factorization at the origin permits a small circle \(|t|=r\) and a closed annular collar on which \(f(t,0)\ne0\). Shrink the base so that \(f\ne0\) on this whole collar for every base point. Each fibre is therefore not identically zero; its zeros are isolated by its first nonzero Taylor term and finite in the remaining compact inner disk.

For each fibre, delete small disjoint disks around its zeros. The logarithmic modulus is harmonic on the punctured region. The planar flux theorem and the local decomposition into \(m\log|t-p|\) plus a harmonic function yield

\[
N(z):=\sum_p m(p,z)
 =\frac1{2\pi}\int_{|t|=r}\partial_\nu\log|f(t,z)|\,ds.
\tag{4.2}
\]

The small-circle flux of \(m\log|t-p|\) is \(2\pi m\), by direct differentiation; the smooth harmonic remainder has limiting flux zero. This proves (4.2) without a root-continuity theorem. The right side is continuous in \(z\), because the outer collar is zero-free. The left side is an integer. A continuous integer-valued function on connected \(V\) is constant: the preimages of each integer are both open and closed. Its value at zero is \(k\).

Suppose \(z_j\to z_0\). On compact subsets of the disk, the fibre functions converge uniformly. U024, Theorem 3.3, and the proved planar source in U020 imply

\[
\log|f(\,\cdot\,,z_j)|\longrightarrow
 \log|f(\,\cdot\,,z_0)|\quad\hbox{in }L^1_{\rm loc}(D_r),\qquad
\Delta_t\log|f(\,\cdot\,,z)|=2\pi\sum_p m(p,z)\delta_p .
\tag{4.3}
\]

Distributional derivatives are continuous under this convergence, directly by their pairing with fixed derivatives of tests. U008, Theorem 5.2, therefore gives convergence of the positive counting measures on every continuous compactly supported disk test. Extend \(\phi\) by zero in the \(t\) variable. Its supports lie in one compact disk, and uniform continuity on that disk times a compact base neighborhood gives

\[
\left|\sum_p m(p,z_j)
       [\phi(p,z_j)-\phi(p,z_0)]\right|
 \le k\sup_t|\phi(t,z_j)-\phi(t,z_0)|\longrightarrow0 .
\tag{4.4}
\]

Together with (4.3), this proves the claimed continuity of the whole sum.

The right side of (4.1) is a positive linear functional on \(C_c(D_r\times V)\). If its support projects into compact \(K\subset V\), its absolute value is bounded by \((\pi/2)k|K|\|\phi\|_\infty\). The proved positive Riesz construction therefore makes it a Radon measure. For a smooth test, ambient local integrability of \(u\) and Fubini allow integration in \(t\) first. The planar identity gives

\[
\begin{aligned}
\langle L_{e_t}u,\phi\rangle
 &=\frac14\int_V\int_{D_r}
            \log|f(t,z)|\,\Delta_t\phi(t,z)\,dA(t)\,d\lambda(z)\\
 &=\frac{\pi}{2}\int_V\sum_p m(p,z)\phi(p,z)\,d\lambda(z).
\end{aligned}
\tag{4.5}
\]

There is no unidentified measure left after this computation: two locally finite measures agreeing on smooth tests agree on continuous tests by compactly supported uniform smoothing, and hence agree by Riesz uniqueness. This proves (4.1). \(\square\)

**Corollary 4.2 (a null projection has no directional mass).** If a Borel subset of this cylinder projects into a null Borel subset of \(V\), its \(L_{e_t}u\) measure is zero.

**Proof.** Given a compact disk \(A\Subset D_r\), choose \(0\le\eta\le1\) supported in \(D_r\), equal to one on \(A\). The positive functional obtained by putting \(\phi(t,z)=\eta(t)\psi(z)\) in (4.1) satisfies

\[
0\le\langle L_{e_t}u,\eta\psi\rangle
\le\frac{\pi k}{2}\int_V\psi\,d\lambda,\qquad
0\le\psi\in C_c(V).
\tag{4.6}
\]

It is the projection of \(\eta L_{e_t}u\); over each compact base subset the support lies in a compact product, so this is a Radon measure on \(V\). Riesz uniqueness applied also to the positive difference in (4.6) proves its domination by \((\pi k/2)\lambda\) on **all Borel sets**, not just tests. In particular \(L_{e_t}u(A\times N)=0\) for every null Borel \(N\). Exhaust \(D_r\) by compact disks to obtain the assertion. \(\square\)

## 5. Account for every exceptional zero

**Proposition 5.1 (complete directional formula).** In a cylinder as above, \(L_{e_t}u\) gives no mass to \(X\setminus Z\), or to the part of \(Z\) tangent to \(e_t\). On the transverse part,

\[
L_{e_t}u=\frac{\pi}{2}\,
       m\,\frac{|dh(e_t)|^2}{|dh|^2}\,dS.
\tag{5.1}
\]

**Proof.** Every zero has fibre order between \(1\) and \(k\). Partition the zeros into the Borel sets

\[
E_m=\{f=f_t=\cdots=f_t^{(m-1)}=0,\quad f_t^{(m)}\ne0\},
\qquad 1\le m\le k .
\tag{5.2}
\]

At a point of \(E_m\), the function \(f_t^{(m-1)}\) has nonzero \(t\) derivative. Lemma 2.1 writes its nearby zero set as \(t=a(z)\) on a connected base neighborhood. Every nearby point of \(E_m\) lies on that graph. Consider the holomorphic functions

\[
b_\ell(z)=f_t^{(\ell)}(a(z),z),\qquad 0\le\ell<m .
\tag{5.3}
\]

If all \(b_\ell\) vanish identically on the base, Lemma 2.2 gives \(f=(t-a(z))^mG\). At the chosen point \(G\ne0\); shrink again until it is nonzero throughout the neighborhood. The whole zero set there is then a pure branch transverse to \(e_t\). Restricting (4.1) to this neighborhood gives \((\pi/2)m\,d\lambda(z)\) on the graph. Formula (3.4) turns this into (5.1).

Otherwise some \(b_\ell\) is not identically zero. Its zero set in the base is a Borel null set by U024, Lemma 3.1. All the nearby points of \(E_m\) project into it, so Corollary 4.2 assigns them zero directional mass.

These neighborhoods cover \(E_m\). Second countability selects a countable subcover, so the union of the latter, null pieces is still null. Doing this for all finitely many \(m\) proves that every zero outside a pure transverse neighborhood has zero directional mass. This includes both non-pure zeros and tangencies on pure branches: such a tangency cannot lie in a pure transverse neighborhood, since the reduced defining differentials are proportional on overlaps. The measure vanishes off all zeros by Section 1. At any pure transverse point, (1.2) and Lemma 2.1 provide a graph chart, and the same calculation from (4.1) gives (5.1) there. Choose a countable cover of this whole transverse part. Formula (5.1) is compatible by Section 3 and determines the measure on its disjoint Borel partition. \(\square\)

## 6. Recover the full Levi matrix and the Laplacian

**Theorem 6.1 (zero-hypersurface measure).** The measures \(dS\) and \(m\,dS\), extended by zero off \(Z\), are locally finite in \(X\). In particular all the following coefficients are Radon measures, and

\[
\partial_{z_j}\partial_{\bar z_k}\log|f|
 =\frac{\pi}{2}\,m\,
       \frac{h_{z_j}\overline{h_{z_k}}}{|dh|^2}\,dS .
\tag{6.1}
\]

Consequently, for every constant \(w\in\mathbb C^n\),

\[
L_w\log|f|=\frac{\pi}{2}\,m\,
                 \frac{|dh(w)|^2}{|dh|^2}\,dS,\qquad
\Delta\log|f|=2\pi\,m\,dS .
\tag{6.2}
\]

Both identities include the assertion that there is no residual measure on excluded zeros.

**Proof.** In one complex dimension this is precisely U020's planar source, including local finiteness of the isolated zeros. Suppose \(n\ge2\). At an arbitrary zero translated to \(0\), the full polydisk power series has a first nonzero homogeneous term \(f_k\). Otherwise every coefficient vanishes, so \(f\) is zero near \(0\), and the proved identity principle would make it zero on its component. A unit vector \(w\) with \(f_k(w)\ne0\) gives \(f(tw)=t^kf_k(w)+O(t^{k+1})\), the finite-order fibre needed above.

There are \(n^2\) such unit vectors whose Hermitian rank-one forms determine every Hermitian matrix. Start with the list

\[
e_j\ (1\le j\le n),\qquad
(e_j+e_\ell)/\sqrt2,\quad
(e_j+i e_\ell)/\sqrt2\quad(j<\ell).
\tag{6.3}
\]

For a Hermitian matrix \(H\), the corresponding quadratic evaluations, with convention \(\sum w_j\overline{w_k}H_{jk}\), give respectively \(H_{jj}\), \((H_{jj}+H_{\ell\ell})/2+\operatorname{Re}H_{j\ell}\), and \((H_{jj}+H_{\ell\ell})/2+\operatorname{Im}H_{j\ell}\). Thus they are linearly independent as real functionals on the \(n^2\)-dimensional space of Hermitian matrices. Their determinant in these explicit real coordinates is nonzero, and stays nonzero under small perturbations.

The set \(f_k(w)\ne0\) is dense on the unit sphere. Indeed, if the homogeneous polynomial vanished on a nonempty relatively open sphere patch, positive radial dilation would make it vanish on an open annular subset of \(\mathbb C^n\). The identity principle would make it the zero polynomial, a contradiction. Its nonzero set is also open, by continuity. Perturb each member of (6.3) within the nonzero-determinant neighborhood to obtain the required \(w_1,\ldots,w_{n^2}\).

Each \(w_i\) can be completed to a unitary basis without a spectral theorem. Extend it to a basis by the proved exchange construction, subtract from each successive vector its projections on the earlier normalized vectors, and divide by the positive norm of the residual. Independence makes each residual nonzero; direct inner-product calculation verifies orthonormality. A unitary matrix, as a real matrix, preserves the Euclidean dot product, so its determinant has absolute value one. Linear substitution and the chain rule therefore identify the directional measure in those coordinates with \(L_{w_i}u\); formula (3.1) is invariant under this orthogonal change as well.

Apply Proposition 5.1 in the resulting finitely many cylinders. Their intersection contains a neighborhood \(Y\) of \(0\) on which all the directional formulas hold. We first extract local finiteness, before forming matrix-valued surface measures. The vectors \(w_i\) span \(\mathbb C^n\): if a nonzero covector annihilated them, its Hermitian rank-one form would have all the determining evaluations zero. Hence the continuous function \(\sum_i|\nu(w_i)|^2\) has a strictly positive minimum on the compact unit sphere of complex covectors. Denote it by \(c>0\). On \(Z\),

\[
\sum_i\frac{|dh(w_i)|^2}{|dh|^2}\ge c .
\tag{6.4}
\]

For each compact \(K\subset Y\), the already defined nonnegative surface integral and Proposition 5.1 give

\[
c\int_{K\cap Z}m\,dS
 \le\frac2\pi\sum_i (L_{w_i}u)(K)<\infty .
\tag{6.5}
\]

Since \(m\ge1\), this also bounds \(dS\). Local finiteness makes these Borel measures Radon by the measure regularity fact proved in Section 3.

Now define the right side of (6.1) as a matrix \(M\) of locally finite complex measures. Its coefficient magnitudes are at most \((\pi/2)m\,dS\); it is Hermitian because \(m,dS\) are real. The actual distribution matrix \(H_{jk}=\partial_{z_j}\partial_{\bar z_k}u\) is also Hermitian: conjugate the derivatives of the real distribution \(u\) and commute their constant real partial derivatives. The quadratic evaluations of \(H-M\) on all \(w_i\) vanish by Proposition 5.1. The invertible real coefficient matrix just constructed implies each real diagonal part and each real and imaginary off-diagonal part is the zero distribution. Thus \(H=M\) on \(Y\).

The same argument applies near every zero. Off the zeros the derivatives vanish. Compatible local measures and the proved locality of distributions (U021, B0) give (6.1) on \(X\). Multiplying by \(w_j\overline{w_k}\) and summing gives the first formula (6.2); taking four times the trace, using \(\sum|h_{z_j}|^2=|dh|^2\), gives the second. \(\square\)

## 7. Quantitative singular and multiple-component examples

In the two-dimensional complex examples, write

\[
\mu=\Delta\log|f|,\qquad
\Theta(R)=\frac{\mu(B_R)}{2\pi^2R^2},\qquad B_R=B_R(0).
\tag{7.1}
\]

The planar radial integrations below follow from the polar formula proved in the angular foundations of U018.

**Example 7.1 (a cusp with no missing mass).** For \(f=z_1^2-z_2^3\), the nonzero zero set has parametrization

\[
\gamma(t)=(t^3,t^2),\quad t\ne0,\qquad
dS=(9|t|^4+4|t|^2)\,dA(t).
\tag{7.2}
\]

Indeed \(t=z_1/z_2\) is its inverse, and the complex derivative of \(\gamma\) is nonzero. The two real derivative columns are orthogonal with the same squared length \(|\gamma'(t)|^2\), so (3.1) gives the displayed area factor. The gradient of \(f\) is nonzero there, giving multiplicity one.

At \(0\) the gradient vanishes. A pure representation with \(m=1\) would make the gradient nonzero; one with \(m>1\) would make it zero at all nearby zeros, contradicting the nonzero points just found. Thus the origin is excluded from \(Z\), and Theorem 6.1 gives no mass there. Let \(T>0\) satisfy \(T^4+T^6=R^2\). Strict increase of the left side ensures uniqueness. Integrating (7.2) over \(|t|<T\) yields

\[
\mu(B_R)=2\pi^2(3T^6+2T^4),\qquad
\Theta(R)=2+\frac{T^2}{1+T^2}.
\tag{7.3}
\]

There is an independent fibre check. In the \(z_1\) direction, the two roots lie in \(B_R\) exactly over \(|z_2|<T^2\); in the \(z_2\) direction, the three roots lie there exactly over \(|z_1|<T^3\). Formula (4.1) therefore gives

\[
(L_{e_1}u)(B_R)=\pi^2T^4,\qquad
(L_{e_2}u)(B_R)=\tfrac32\pi^2T^6 .
\tag{7.4}
\]

The exceptional base point has zero base area. A sufficiently large fibre disk contains all roots for the bounded base range of the ball, so Lemma 4.1 applies, and the resulting measure identity applies to the Borel ball. Four times the sum in (7.4) is (7.3).

**Example 7.2 (two tangent components with different multiplicities).** Consider

\[
f=z_1^3(z_1+z_2^2)^2 .
\tag{7.5}
\]

Except at their intersection, the plane \(z_1=0\) and graph \((-t^2,t)\) have multiplicities three and two. The graph's area factor is \(1+4|t|^2\). If \(s+s^2=R^2\), its ball section is \(|t|<\sqrt s\), of area \(\pi(s+2s^2)\); the plane section has area \(\pi R^2\). The intersection is not a pure branch: if it had a reduced defining function \(h\) with \(dh(0)\ne0\), the identity \(h(0,t)=0\) on the plane would give \(h_{z_2}(0)=0\), hence \(h_{z_1}(0)\ne0\). Lemma 2.1 would give a unique \(z_1\) for each small \(z_2\), contrary to the two zeros \(0\) and \(-z_2^2\) when \(z_2\ne0\). The theorem excludes intersection mass and gives

\[
\mu(B_R)=2\pi^2[3R^2+2s+4s^2],\qquad
\Theta(R)=5+\frac{2s}{1+s}.
\tag{7.6}
\]

For the first directional check the roots of orders three and two occur over base disks of radii \(R\) and \(\sqrt s\), respectively. Hence

\[
(L_{e_1}u)(B_R)=\tfrac{\pi^2}{2}(3R^2+2s).
\tag{7.7}
\]

For the second use the identity of locally integrable functions

\[
u=3\log|z_1|+2\log|z_1+z_2^2|.
\tag{7.8}
\]

The identity holds off the null zero sets, which suffices for distributions. The first summand has zero \(z_2\) derivatives: integrate the corresponding test derivative in \(z_2\) first, using compact support and the scalar FTC, then use Fubini. The other summand has two roots, each weighted by two, over \(|z_1|<s\) in the ball. Thus \((L_{e_2}u)(B_R)=2\pi^2s^2\); four times the sum again equals (7.6). This computation treats the identically zero product fibre through an ambient \(L^1\) factorization. The density increases from five to seven, agreeing with the least and greatest polynomial degrees in U024.

## Exercises

**Exercise 1.** Let \(h=2z_1+iz_2-1\) and \(f=e^{z_3}h^4\) on \(\mathbb C^3\). Find its Laplacian, the area factor over \((z_2,z_3)\), and the directional measures for the unit vectors

\[
w=(1,-i,0)/\sqrt2,\qquad v=(1,2i,0)/\sqrt5 .
\tag{8.1}
\]

**Exercise 2.** In a pure factorization \(f=g h^3\), replace \(h\) by \(\widetilde h=e^{z_1}h\). Determine the new unit and verify both formulas (6.2) using the new equation.

**Exercise 3.** For \(f=(z_1-z_2^2-2z_3)^2\), calculate \(dS\), all three coordinate directional measures in base coordinates \((z_2,z_3)\), and four times their sum. Explain why the graph factor is not \(\sqrt{5+4|z_2|^2}\).

**Exercise 4.** Compute the ball mass and normalized density for \(z_1^3-z_2^4\), including a parametrization, the limits at zero and infinity, and the status of the origin.

**Exercise 5.** Carry out both the surface calculation and the two independent coordinate fibre calculations for

\[
f=z_1^2(z_1+3z_2^2)^4 .
\tag{8.2}
\]

Determine the two endpoint densities.

**Exercise 6.** For \(f(t,z)=t^2-z\), prove that the unordered planar root measures converge to \(2\delta_0\) as \(z\to0\), and prove that a holomorphic square-root label near zero is impossible. Compute the ambient \(e_t\) directional measure, including its behavior at the tangent point.

**Exercise 7.** Deduce from U024's density monotonicity that \(\Delta\log|f|\) has no point atoms in complex dimension at least two. For \(z_1^2-z_2^3\) in \(\mathbb C^3\), give a nonzero atomless positive Radon measure on the excluded singular line. What additional conclusion does Proposition 5.1 supply?

**Exercise 8.** For \(f(t,z_1,z_2)=t^3-z_1^2z_2\) and \(0<s<r\), find the total \(L_{e_t}\log|f|\) measure of \(D_r\times D_s^2\). Account for every zero above \(z_1z_2=0\), and give the geometric density over its complement.

## Complete solutions

**Solution 1.** The logarithmic modulus of the exponential factor is \(\operatorname{Re}z_3\), with zero Levi matrix. For the other factor, \(m=4\), \(|dh|^2=5\), \(dh(w)=3/\sqrt2\), and \(dh(v)=0\). Thus

\[
\Delta\log|f|=8\pi\,dS,\qquad
L_w\log|f|=\frac{9\pi}{5}\,dS,\qquad
L_v\log|f|=0 .
\tag{9.1}
\]

The graph equation \(z_1=(1-iz_2)/2\) has derivative norm squared \(1/4\). Formula (3.2) gives \(dS=(5/4)d\lambda(z_2,z_3)\). The zero directional measure for \(v\) expresses its tangency; the constants for \(w\) use its stated unit normalization.

**Solution 2.** The new nonvanishing factor is \(g e^{-3z_1}\), since \(f=(g e^{-3z_1})\widetilde h^3\). On the zero set the product rule gives \(d\widetilde h=e^{z_1}dh\). The squared numerator and denominator in every directional ratio both acquire the factor \(|e^{z_1}|^2\). The surface and multiplicity stay the same, so the two measures (6.2) agree. Equivalently, the added logarithmic modulus is the smooth pluriharmonic function \(\operatorname{Re}z_1\); its Levi matrix is zero.

**Solution 3.** Here \(a(z_2,z_3)=z_2^2+2z_3\), with \(|a'|^2=4|z_2|^2+4\) and \(m=2\). With \(d\lambda=d\lambda(z_2,z_3)\),

\[
\begin{aligned}
dS&=(5+4|z_2|^2)d\lambda,\\
L_{e_1}\log|f|&=\pi\,d\lambda,\\
L_{e_2}\log|f|&=4\pi|z_2|^2d\lambda,\\
L_{e_3}\log|f|&=4\pi\,d\lambda .
\end{aligned}
\tag{9.2}
\]

The sum is \(\pi\,dS\), giving \(\Delta\log|f|=4\pi\,dS\). There are two nontrivial real Gram eigenvalues, both \(5+4|z_2|^2\), because a complex scalar graph has two real output coordinates. Their product's positive square root is that number itself.

**Solution 4.** The parametrization \(\gamma(t)=(t^4,t^3)\), \(t\ne0\), has inverse \(t=z_1/z_2\) on every nonzero zero. Direct use of \(z_1^3=z_2^4\) checks both inverse identities. Its derivative is nonzero, and the gradient \((3z_1^2,-4z_2^3)\) gives multiplicity one away from the origin. The area factor is \(16|t|^6+9|t|^4\). Let \(T^6+T^8=R^2\). Polar integration gives area \(\pi(4T^8+3T^6)\), so

\[
\mu(B_R)=2\pi^2(4T^8+3T^6),\qquad
\Theta(R)=3+\frac{T^2}{1+T^2}.
\tag{9.3}
\]

The origin has zero gradient whereas nearby zeros are simple, excluding both possible types of pure factorization just as in Example 7.1. The full theorem therefore assigns no atom there. As \(R\) runs from zero to infinity, so does \(T\); the densities tend to three and four.

**Solution 5.** The plane has multiplicity two. The other branch, \((-3t^2,t)\), has multiplicity four and area factor \(1+36|t|^2\). Define \(s>0\) by \(s+9s^2=R^2\); its graph section has area \(\pi(s+18s^2)\). The two distinct tangent graphs exclude a pure branch at the origin by the same unique-graph argument as in Example 7.2. Hence

\[
\begin{aligned}
\mu(B_R)&=2\pi^2[2R^2+4s+72s^2],\\
\Theta(R)&=6+\frac{36s}{1+9s}.
\end{aligned}
\tag{9.4}
\]

In \(z_1\) fibres, the plane root of order two uses base disk radius \(R\), and the graph root of order four uses radius \(\sqrt s\). For \(z_2\) fibres use the ambient identity \(u=2\log|z_1|+4\log|z_1+3z_2^2|\); the first term has zero \(z_2\) derivatives by Fubini and FTC. The latter polynomial has two roots, each of weight four, in the ball over \(|z_1|<3s\). Formula (4.1) therefore gives

\[
(L_{e_1}u)(B_R)=\tfrac{\pi^2}{2}(2R^2+4s),\qquad
(L_{e_2}u)(B_R)=36\pi^2s^2 .
\tag{9.5}
\]

Four times their sum is (9.4). The density tends to six at zero and ten at infinity and is strictly increasing, since \(s\) is strictly increasing and so is \(36s/(1+9s)\). No distribution is assigned to an identically zero product fibre.

**Solution 6.** Both roots, counted with order, have modulus \(|z|^{1/2}\). Thus the sum of any continuous test's values at the roots tends to \(2\psi(0)\), independently of labels. At \(z=0\) the root has order two. If a holomorphic label \(a\) satisfied \(a^2=z\), then \(a(0)=0\) and its first nonzero Taylor coefficient would have some integer degree \(\ell\ge1\). Its square has degree \(2\ell\), contradicting degree one on the right.

In the ambient space the entire graph \(\gamma(t)=(t,t^2)\) is smooth and simple. Taking \(h=t^2-z\), we have

\[
|dh|^2=1+4|t|^2,\qquad dh(e_t)=2t,\qquad
dS=(1+4|t|^2)dA(t),\qquad
L_{e_t}\log|f|=2\pi|t|^2dA(t).
\tag{9.6}
\]

The geometric ratio is \(4|t|^2/(1+4|t|^2)\). It vanishes at the tangent point; there is no atom there. Integrating planar counts over base Lebesgue measure gives no mass to the single exceptional base point, even though that fibre itself has a double atom.

**Solution 7.** U024, Theorem 4.1, gives monotonicity of the normalized open-ball density \(\Theta_p\). If \(\overline B_R(p)\subset X\), its value at \(R\) is finite by the Radon property. Thus

\[
\mu(B_r(p))\le
 2\pi C_{2n-2}\Theta_p(R)\,r^{2n-2},
 \qquad 0<r<R .
\tag{9.7}
\]

Here \(C_{2n-2}\) is the volume of the real unit ball in dimension \(2n-2\), with the same normalization as U024. For \(n\ge2\) the bound tends to zero; continuity from above for a locally finite measure gives \(\mu(\{p\})=0\). For \(n=1\) the exponent is zero and a zero of order \(k\) does have mass \(2\pi k\).

For the three-variable cusp, at each point of \(z_1=z_2=0\) the gradient is zero, while arbitrarily close zeros have nonzero gradient. The pure-factor argument of Example 7.1 excludes the entire line. Nevertheless

\[
\nu=\delta_0(z_1,z_2)\otimes dA(z_3)
\tag{9.8}
\]

is a nonzero positive Radon measure supported on it. Compact sets have bounded \(z_3\) projection, giving local finiteness, and singletons have zero \(dA\) measure, giving no atoms. This example does not claim \(\nu=\Delta\log|f|\); it proves that absence of atoms alone cannot exclude a positive measure on the singular set. Proposition 5.1 excludes the whole exceptional set for the actual logarithmic derivatives.

**Solution 8.** Every base point obeys \(|z_1^2z_2|<s^3<r^3\). Its cubic has three roots counted with order inside \(D_r\); this also follows directly by taking the three polar cube roots when the right side is nonzero, and the triple root when it is zero. The base volume is \(\pi^2s^4\). The Borel measure identity (4.1), extended to the open cylinder by increasing compact cutoffs, gives

\[
(L_{e_t}\log|f|)(D_r\times D_s^2)
 =\frac{3\pi^3}{2}s^4 .
\tag{9.9}
\]

The base set \(z_1z_2=0\) is the union of two product null sets by Fubini. Corollary 4.2 eliminates **all** directional mass above it, including its triple roots. Above its complement, \(t\ne0\), \(f_t=3t^2\ne0\), and the multiplicity is one. The defining differential is \((3t^2,-2z_1z_2,-z_1^2)\), so

\[
\frac{|dh(e_t)|^2}{|dh|^2}
 =\frac{9|t|^4}{9|t|^4+4|z_1z_2|^2+|z_1|^4}.
\tag{9.10}
\]

Multiplication by \((\pi/2)dS\) gives the requested geometric directional measure. Neither the total mass nor the exceptional-set conclusion uses holomorphic root labels.

## Programme proof locations and freely accessible sources

The cited programme lessons contain the proofs used here. The foundation entry is real arithmetic and topology in [Metric foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 12–13, including scalar FTC, polar trigonometry and smooth cutoffs. [Finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), Sections 10.1–10.6, proves bases, determinant identities, Gram constructions and norm comparisons. [Measure foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.4 and 16.1–16.2, supplies Lebesgue measure, linear substitution, dominated convergence and product integration. [Positive-measure foundations](../prerequisites/U011-free-foundations/positive-measure-foundations-U008.md) proves Riesz representation, regularity and measure uniqueness. [Angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4–A5, proves the polar integration and ball constants. Each prerequisite retains its stated licence.

The following freely accessible works were read for the reconstruction. Their mathematical methods are developed in complete programme proofs above; an external citation does not replace a proof.

- [Jiří Lebl, *Tasty Bits of Several Complex Variables*, version 3.4, December 23, 2020](https://www.jirka.org/scv/scv-3.4.pdf), Section 1.3 and Theorem 1.6.2. The derivative-based regular-point construction informs Section 5. Lemmas 2.1–2.2 supply the scalar implicit and division arguments explicitly, and the flux proof in Section 4 supplies the fibre count.
- [Ivan Netuka, *The Change-of-Variables Theorem for the Lebesgue Integral*, 2011, pp. 37–42](https://actamath.savbb.sk/pdf/acta1906.pdf), Theorem 1 and Lemma 2. Lemma 3.0 develops the smoothing argument with an explicit uniform bound for the transformed kernel support and a proved extension from continuous tests to Borel functions.
- [Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, version of June 21, 2012](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), Chapter III, Section 2, formula (2.15) and its proof, pp. 143–144. This provides the comparison for the zero-source normalization. Sections 4–6 here prove the complete formula through scalar fibres, including local finite area and every exceptional zero, without assuming the analytic-set or current-support theorems used in that presentation.
