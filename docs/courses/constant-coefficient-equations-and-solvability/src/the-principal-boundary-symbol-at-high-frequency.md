# The principal boundary symbol at high frequency

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Separated groups of polynomial roots have analytic factor coefficients even when roots within a group repeat. This lets us scale a mixed boundary determinant to high frequency. Its first nonzero coefficient defines the principal boundary symbol. Cancellations can lower its degree below the degrees suggested by the boundary operators, even to a negative integer.

Read [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md), [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md), [Boundary determinants annihilate causal solutions](boundary-determinants-annihilate-causal-solutions.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Schwartz Fourier transform; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies compact extrema and cutoffs; [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html) supplies proper convolution.

The hyperbolic-cone and analytic zero-order prerequisites remain planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html); their precise statements are given in [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md). Local Holmgren uniqueness also remains planned: a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic surface vanishes near that surface. The uses of these prerequisites are conditional on their planned proofs.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The written prerequisite lessons supply the auxiliary proofs used below.

## Coprime factors, including repeated and empty factors

Let \(g_+\) and \(g_-\) be monic polynomials of degrees \(h\) and \(\ell\), with no common root. A degree-zero monic factor is one. Put \(d=h+\ell\), and let \(E_a\) be the vector space of polynomials of degree strictly below \(a\), with \(E_0=\{0\}\). The linear map
\[
\begin{gathered}
A:E_h\oplus E_\ell\longrightarrow E_d,\\
\qquad
 A(v_+,v_-)=g_-v_++g_+v_-
\end{gathered}
\tag{1}
\]
is invertible. Indeed \(A(v)=0\) implies that \(g_+\) divides \(g_-v_+\). Coprimality and polynomial division imply that \(g_+\) divides \(v_+\); its degree bound then gives \(v_+=0\), followed by \(v_-=0\). Domain and codomain both have dimension \(d\), so injectivity implies bijectivity. This includes one empty factor. If both are empty, every space is zero and every assertion below is trivial.

For \(d>0\), use the coefficient \(\ell^1\) norm and the sum norm on the pair. Polynomial multiplication satisfies \(\|fg\|\le\|f\|\|g\|\). Write \(K=\|A^{-1}\|>0\). The desired perturbation equation is
\[
\begin{gathered}
g_+g_-+r=(g_++v_+)(g_-+v_-),\\
\qquad
 v=A^{-1}r-A^{-1}(v_+v_-).
\end{gathered}
\tag{2}
\]
The nonlinear product still belongs to \(E_d\). Choose \(R>0\) with \(4KR\le1\), and restrict \(\|r\|<R/(2K)\). The right side defines a map \(\Phi_r\) of the closed pair ball of radius \(R\) into itself. More precisely,
\[
\begin{gathered}
\|\Phi_r(v)\|\le R/2+KR^2\le3R/4,\\
\qquad
 \|\Phi_r(v)-\Phi_r(z)\|\\
\le2KR\|v-z\|\le\tfrac12\|v-z\|.
\end{gathered}
\tag{3}
\]
For the difference estimate, expand \(v_+v_--z_+z_-\) into two products. Starting at \(v^{(0)}=0\), iterate \(\Phi_r\). Successive differences decrease by a factor at most one half, so their sum converges in each of the finitely many complete scalar coordinates. The limit stays in the ball and satisfies equation 2. The same estimate applied to two solutions in that ball proves uniqueness there. Thus the factors are uniquely determined among small coefficient perturbations; no claim of uniqueness among all globally relabeled factorizations is needed.

Every finite iterate is a polynomial in the complex coefficients of \(r\). Its geometric convergence is uniform on the stated coefficient ball. Uniform convergence on smaller complex polydiscs and the one-variable Cauchy formula in each coordinate show that its limit is holomorphic: apply the iterated Cauchy formula to the polynomial iterates, pass through the uniformly convergent boundary integrals, and expand each Cauchy kernel on a smaller polydisc to obtain a convergent joint power series. Consequently the coefficients of \(v_+\) and \(v_-\) are analytic functions of those of \(r\).

The same proof works with additional analytic parameters in \(g_\pm\). Near any one coprime pair, the finite matrix \(A\) remains invertible, its inverse is analytic by adjugate divided by its nonzero determinant, and its norm has a common bound on a small parameter neighborhood. One common \(R\) and the same iteration give joint analyticity. Repeated roots inside either factor cause no problem: only common roots between the two factors would destroy equation 1. This completes the full perturbation lemma.

## Scaling at a characteristic boundary

Use [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s normalized time barrier and its full negative cone tube
\[
\begin{gathered}
\Omega=\mathbb R^n-i\Gamma,\\
\qquad
 \pi:\mathbb C^n\longrightarrow\mathbb C^n/\mathbb C\theta,\\
\qquad
 \Omega'=\pi(\Omega).
\end{gathered}
\tag{4}
\]
The real independent normals are \(N,\theta\). Here \(\Gamma=\Gamma(P_m,N)\), the total degree is \(m\ge1\), and [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) gives
\[
\begin{gathered}
d=m-m_0=h+\ell,\\
\qquad
 P(\zeta+w\theta)\\
=q(\zeta)P_+(w,\zeta)P_-(w,\zeta).
\end{gathered}
\tag{5}
\]
The factors are monic of degrees \(h=m_+\) and \(\ell=m_-\). The normal leading coefficient \(q\) has degree \(m_0\), is constant in the \(\theta\) direction, and has principal homogeneous part \(G\). Apply the same [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) result to \(P_m\), whose time barrier is zero. It gives, throughout \(\Omega\),
\[
\begin{gathered}
P_m(\zeta+w\theta)=G(\zeta)g_+(w,\zeta)g_-(w,\zeta),
 \\
\qquad G(\zeta)\ne0.
\end{gathered}
\tag{6}
\]
The monic principal factors have the same degrees \(h,\ell\), are holomorphic, and have all roots in their respective strict upper and lower halfplanes. In particular they are coprime at every such parameter. This includes repeated roots and \(d<m\); replacing \(q\) by a constant would lose the characteristic-boundary case.

For a complex scale parameter \(\epsilon\), form the polynomial-in-\(\epsilon\) expressions
\[
\begin{gathered}
F(\zeta,w,\epsilon)\\
=\epsilon^mP((\zeta+w\theta)/\epsilon)
       \\
=\sum_{j=0}^m\epsilon^{m-j}P_j(\zeta+w\theta),
 \\
\qquad
 Q(\zeta,\epsilon)=\epsilon^{m_0}q(\zeta/\epsilon).
\end{gathered}
\tag{7}
\]
Their definitions at \(\epsilon=0\) are the finite sums, rather than the displayed quotients. \(F\) has degree at most \(d\) in \(w\), its \(w^d\) coefficient is \(Q\), and \(Q(\zeta,0)=G(\zeta)\ne0\). Hence \(F/Q\) is a monic degree-\(d\) polynomial jointly analytic near every \((\zeta,0)\), and reduces there to \(g_+g_-\). Its difference from \(g_+g_-\) has degree below \(d\) and small coefficients.

Equations 1–3 with analytic parameters give unique local monic factors \(A_+,A_-\), jointly analytic in \((\zeta,\epsilon)\), with
\[
\begin{gathered}
F/Q=A_+A_-,\\
\qquad
 A_\pm(\zeta,w,0)=g_\pm(w,\zeta).
\end{gathered}
\tag{8}
\]
For small positive real \(\epsilon\), these factors retain their upper/lower root signs by [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)/[Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md)'s root persistence. The original scaled factors have exactly those signs too, so grouping roots and monicity identify them:
\[
\begin{gathered}
A_+(\zeta,w,\epsilon)=\epsilon^hP_+(w/\epsilon,\zeta/\epsilon),
 \\
\qquad
 A_-(\zeta,w,\epsilon)=\epsilon^\ell P_-(w/\epsilon,\zeta/\epsilon).
\end{gathered}
\tag{9}
\]
The right sides need initially be defined only for positive \(\epsilon\); equation 8 supplies their complex analytic continuation across zero. Locally constructed continuations agree on overlaps: their equality for positive \(\epsilon\), followed by the one-variable analytic identity in \(\epsilon\), proves equality near zero. No labels for individual roots or fractional expansions are needed.

## The determinant's exact scaling power

Assume there are exactly \(h\) boundary symbols \(B_1,\ldots,B_h\), and that their descended determinant \(L^\partial\) is not identically zero on \(\Omega'\). At \(h=0\), the determinant equals one; all the following conclusions hold with principal degree zero and principal symbol one. For \(h>0\), every \(B_j\) is nonzero; let \(b_j\) be its total degree. Its scaled symbol
\[
\begin{gathered}
\widetilde B_{j,\epsilon}(w,\zeta)
     \\
=\epsilon^{b_j}B_j((\zeta+w\theta)/\epsilon)
     \\
=\sum_{k=0}^{b_j}\epsilon^{b_j-k}B_{j,k}(\zeta+w\theta)
\end{gathered}
\tag{10}
\]
is jointly polynomial and reduces to its top homogeneous part at zero.

For a monic degree-\(h\) polynomial \(p\), [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s pairing is
\(\beta_p(f,g)=[w^{-1}]\,fg/p\).
This coefficient is a polynomial in the finite coefficients of \(f,g,p\), as follows from monic division or the finite Laurent recurrence. The rescaled matrix
\[
\begin{gathered}
\widetilde M_{jk}(\zeta,\epsilon)
    =\beta_{A_+}(\widetilde B_{j,\epsilon},w^k),
       \\
\qquad 1\le j\le h,\\
\quad0\le k<h
\end{gathered}
\tag{11}
\]
is therefore jointly analytic near every \((\zeta,0)\).

Changing the old normal variable \(v\) to \(w=\epsilon v\) in the residue integral for positive \(\epsilon\) gives the matrix-entry factor
\(\epsilon^{h-k-1-b_j}\).
The \(h-1\) comes from the monic denominator scaling and the integration differential; the test monomial contributes \(\epsilon^{-k}\). Multiplying row and column factors yields
\[
\begin{gathered}
M_*=\sum_{j=1}^h b_j-\frac{h(h-1)}2,\\
\qquad
 \det\widetilde M(\zeta,\epsilon)
       =\epsilon^{M_*}L^\partial(\pi\zeta/\epsilon).
\end{gathered}
\tag{12}
\]
In particular \(M_*\) is an integer. The exact column contribution cannot be replaced by \(h\), \(m\), or the sum of boundary orders.

Let the left side of equation 12 be \(D(\zeta,\epsilon)\). Because the right side is independent of the normal representative for positive \(\epsilon\), analytic identity shows that all its Taylor coefficients at zero are independent of that representative. [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md) gives connected convex normal fibers. Fixed local normal sections thus glue the analytic germs to a neighborhood of \(\Omega'\times\{0\}\), with a scale radius that may vary from point to point. Write this descended analytic function as
\[
 D(\zeta',\epsilon)=\sum_{j\ge0}d_j(\zeta')\epsilon^j .
 \tag{13}
\]
Each coefficient is holomorphic on the connected projected tube.

Some \(d_j\) is not identically zero. Otherwise every local germ would vanish, and equation 12 would make \(L^\partial(\zeta'/\epsilon)=0\) on an open set for a small positive fixed \(\epsilon\). Analytic identity on the connected projected tube would give \(L^\partial\equiv0\), contrary to the hypothesis. Let \(j_0\) be the least index whose coefficient is not identically zero, and define
\[
\begin{gathered}
\kappa=M_*-j_0,\\
\qquad
 \Lambda(\zeta',\epsilon)=\epsilon^{-j_0}D(\zeta',\epsilon),
 \\
\qquad \Lambda_0(\zeta')=d_{j_0}(\zeta').
\end{gathered}
\tag{14}
\]
The lower coefficients vanish identically, so the middle quotient extends holomorphically at zero. For positive \(\epsilon\) it equals
\(\epsilon^\kappa L^\partial(\zeta'/\epsilon)\).
Its zero-scale value \(\Lambda_0\) is not identically zero. Thus the complete proposition holds with the integer \(\kappa\), even if negative. At any point where \(\Lambda_0\ne0\), a smaller exponent leaves a pole and a larger exponent gives zero; this characterizes the principal scaling degree uniquely.

## Homogeneous extension without a ray ambiguity

For \(t>0\), compare equation 12 at \(t\zeta'\) and at the scale \(\epsilon/t\). Analytic identity extends that comparison to the zero-scale germs:
\[
\begin{gathered}
D(t\zeta',\epsilon)=t^{M_*}D(\zeta',\epsilon/t),\\
\qquad
 \Lambda_0(t\zeta')=t^\kappa\Lambda_0(\zeta').
\end{gathered}
\tag{15}
\]
Let
\[
 \mathscr D=\bigcup_{c\in\mathbb C,\ c\ne0}c\Omega'.
 \tag{16}
\]
For \(z\in\mathscr D\), put \(S_z=\{c\in\mathbb C:cz\in\Omega'\}\). The imaginary part of \(cz\) is real-linear in \((\operatorname{Re}c,\operatorname{Im}c)\), so \(S_z\) is an open convex cone, the inverse image of the projected cone. If \(0\notin\Omega'\), it excludes zero and is connected. If \(0\in\Omega'\), that open projected cone is the entire real quotient space, so \(\Omega'\) is the entire complex quotient space and \(S_z=\mathbb C\); its nonzero part is still connected.

On \(S_z\setminus\{0\}\), the holomorphic function
\[
                        c^{-\kappa}\Lambda_0(cz)
 \tag{17}
\]
is constant. To see this, differentiate equation 15 in the positive real multiplier at one. The complex derivative at \(c\) then satisfies the same Euler identity as the derivative of \(c^\kappa\), so the derivative of equation 17 is zero. Connectedness makes the value independent of \(c\). The integer exponent is essential: it gives a single-valued holomorphic power on every nonzero ray parameter.

Define the extension by that constant:
\[
\begin{gathered}
\widehat\Lambda_0(z)=c^{-\kappa}\Lambda_0(cz)
       \\
\quad(cz\in\Omega',\ c\ne0).
\end{gathered}
\tag{18}
\]
One fixed admissible \(c\) remains admissible in a neighborhood of \(z\), which proves local holomorphy. The formula agrees with \(\Lambda_0\) on \(\Omega'\), and comparison with an admissible \(c\) for \(\lambda z\) gives
\(\widehat\Lambda_0(\lambda z)=\lambda^\kappa\widehat\Lambda_0(z)\)
whenever \(\lambda\ne0\). Every point can be brought into \(\Omega'\), so this also proves uniqueness of a homogeneous extension. When the tube is the entire quotient space, analyticity at zero and positive homogeneity show by its Taylor series that a nonzero \(\Lambda_0\) is a homogeneous polynomial of nonnegative degree; equation 18 is valid there too.

Since \(\pi\) is complex-linear, \(\mathscr D\) is also the projection of the full complex saturation \(\bigcup_{c\ne0}c(\mathbb R^n-i\Gamma)\). Thus the construction is invariantly defined on the quotient by \(\mathbb C\theta\), rather than tied to a chosen zero normal representative. We call \(\widehat\Lambda_0\) the principal boundary symbol. This use of \(\Lambda_0\) keeps it distinct from the causal inverse distribution \(L_0\) of [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md) and [Boundary determinants annihilate causal solutions](boundary-determinants-annihilate-causal-solutions.md).

## Exercises with complete solutions

**Exercise 1 (entry: repeated roots without analytic root labels).** Let \(g_+=(w-i)^2\), \(g_-=w+2i\), and perturb their product by the constant \(\tau\). Find the first derivatives at \(\tau=0\) of the two monic factors. Explain why a repeated upper root does not obstruct the lemma.

**Solution.** Write \(v_+=\tau(aw+b)+O(\tau^2)\) and \(v_-=\tau c+O(\tau^2)\). The first-order equation is
\[
\begin{gathered}
1=(w+2i)(aw+b)+(w-i)^2c,\\
\qquad
 a=-c=\frac19,\\
\quad b=-\frac{4i}{9},\\
\quad c=-\frac19 .
\end{gathered}
\tag{19}
\]
Indeed its quadratic coefficient is \(a+c\), its linear coefficient is \(b+2ia-2ic\), and its constant is \(2ib-c\); these become \(0,0,1\). Therefore the upper factor is \((w-i)^2+\tau(w-4i)/9+O(\tau^2)\), and the lower factor is \(w+2i-\tau/9+O(\tau^2)\). Their coefficients are analytic although the two upper individual roots can split with a square-root dependence on \(\tau\). No upper root coincides with the lower root \(-2i\), so equation 1 remains invertible.

**Exercise 2 (intermediate: the first scaled boundary matrix can vanish).** For the normalized wave polynomial \(P(\xi,s)=(s-i)^2-\xi^2\), compute the principal degree and symbol for the scalar boundary symbols \(1\), \(\xi\), \(\xi+s\) and \(\xi+s-i\). Compare the nominal exponent \(M_*\) with the true exponent.

**Solution.** There is one upper mode with root \(i-s\). The scalar determinant evaluates the boundary symbol at that root. For the four choices this gives
\[
\begin{gathered}
L^\partial=1,\\
\quad i-s,\\
\quad i,\\
\quad0,\\
\qquad
 (\kappa,\Lambda_0)=(0,1),\\
\quad(1,-s),\\
\quad(0,i).
\end{gathered}
\tag{20}
\]
The fourth choice is identically zero and does not satisfy the proposition's hypothesis. For \(\xi\), the nominal exponent is one and
\(\epsilon L^\partial(s/\epsilon)=i\epsilon-s\).
For \(\xi+s\), the same nominal exponent is one but
\(\epsilon L^\partial(s/\epsilon)=i\epsilon\);
its first nonzero coefficient is at \(j_0=1\), so \(\kappa=0\). The top homogeneous boundary operator \(\xi+s\) evaluates to zero on the principal upper mode, yet the full determinant has nonzero constant principal symbol. The first nonzero coefficient is necessary.

**Exercise 3 (advanced: negative principal degree at a characteristic boundary).** Let
\[
\begin{gathered}
P(\xi,s)=(s-i)(\xi+s-i)-1,\\
\qquad B_1(\xi,s)=\xi+s-i,
 \\
\qquad N=e_s,\\
\quad\theta=e_\xi.
\end{gathered}
\tag{21}
\]
Verify hyperbolicity and the normal count, then determine the full determinant, its nominal scaling exponent, its first nonzero coefficient and its principal symbol.

**Solution.** Put \(z=s-i\). For real \(\xi\), the two time roots of \(z^2+\xi z-1\) are \((-\xi\pm\sqrt{\xi^2+4})/2\), which are real. The roots in \(s\) therefore have imaginary part one. The principal polynomial \(P_m=s(\xi+s)\) has \(P_m(N)=1\) and cone \(\Gamma=\{\eta_s>0,\eta_\xi+\eta_s>0\}\). Its principal line \(P_m(\theta-tN)=(-t)(1-t)\) has roots \(0,1\), so \(m_0=h=1\), \(\ell=0\), and the normal degree is one although the total degree is two.

The leading normal coefficient is \(q=s-i\), and the transported monic upper factor and scalar determinant are
\[
\begin{gathered}
R_+(w,s)=w+s-i-\frac1{s-i},\\
\qquad
 L^\partial(s)=\frac1{s-i},\\
\qquad
 \epsilon L^\partial(s/\epsilon)
       =\frac{\epsilon^2}{s-i\epsilon}.
\end{gathered}
\tag{22}
\]
For \(\operatorname{Im}s<0\), the upper root \(-s+i+1/(s-i)\) has strictly positive imaginary part, confirming the factor on the intersection tube. The full cone is zero-free as well: the two quantities \(s-i\) and \(\xi+s-i\) have strictly negative imaginary parts there, and their product cannot be the positive real number one. The nominal exponent is \(M_*=1\), but the first nonzero Taylor coefficient occurs at \(j_0=2\). Hence
\[
\begin{gathered}
\kappa=-1,\\
\qquad
 \epsilon^{-1}L^\partial(s/\epsilon)=\frac1{s-i\epsilon},
 \\
\qquad \Lambda_0(s)=\frac1s .
\end{gathered}
\tag{23}
\]
It is homogeneous of degree minus one and holomorphic on the complex saturation of the negative time halfplane, namely \(\mathbb C\setminus\{0\}\). Both the principal factor and the first cancellation must be retained to obtain this answer. A blanket nonnegative-degree assumption would exclude this valid hyperbolic mixed problem.

## Extra boundary data and the necessary balanced count

Let \(T=L_0\) be [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s causal inverse of a determinant \(L^\partial\not\equiv0\). If a smooth compactly supported boundary function \(\phi\) satisfies \(T*\phi=0\), then \(\phi=0\). Indeed compact support makes \(\widehat\phi\) entire. [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s weighted Fourier identity and proper convolution give, on the projected tube,
\[
                    L^\partial(\zeta')\widehat\phi(\zeta')=0 .
 \tag{24}
\]
For completeness, choose any fixed imaginary vector in that tube. Its exponential weight makes the transform of \(T\) the stated polynomially bounded analytic function. Multiplying the same weight into the compact input changes its transform to the entire value \(\widehat\phi(\xi+i\eta)\). The usual compact-convolution Fourier product follows by tensor pairing; it is valid in tempered distributions on that line. Thus the product vanishes there for every real \(\xi\). Varying the fixed imaginary vector gives equation 24 throughout the open complex tube. On the nonempty open set where \(L^\partial\ne0\), the entire function \(\widehat\phi\) vanishes. Analytic identity makes it zero everywhere, and the Schwartz Fourier injectivity implies \(\phi=0\). This uses neither a Titchmarsh support theorem nor a first-support-time argument.

Now prescribe zero interior forcing, zero initial data and zero data for a selected \(h\) boundary rows with determinant not identically zero. Any smooth causal solution is annihilated by \(T\), by [Boundary determinants annihilate causal solutions](boundary-determinants-annihilate-causal-solutions.md). Since proper tangential convolution commutes with every polynomial normal/tangent derivative and right trace, an additional boundary equation \(B_*(D)u|_{a=0}=\phi\) would give
\[
\begin{gathered}
T*\phi=0,\\
\qquad
                \phi\in C_c^\infty(\partial H')\ \Longrightarrow\ \phi=0 .
\end{gathered}
\tag{25}
\]
Every nonzero compact extra datum is therefore incompatible with those other zero data. This includes \(h=0\), when \(T\) is the identity.

For an arbitrary number \(\mu\) of boundary rows, [Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md) shows that everywhere rank below \(h\) prevents uniqueness. In particular \(\mu<h\) cannot give uniqueness. If \(\mu\ge h\) and generic rank is \(h\), some fixed \(h\)-row minor is nonzero at one point and hence is not identically zero. For \(\mu>h\), choose those rows, prescribe their data zero, and choose any one extra row's nonzero compact datum supported at positive time; equation 25 prevents a solution. If \(\mu=h\) but its determinant is identically zero, [Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md) again prevents uniqueness. Therefore existence for arbitrary smooth causal data flat at initial time, together with uniqueness, requires exactly \(\mu=h\) and a determinant not identically zero. This is a necessary condition only; the principal-symbol and hyperbolicity conditions for sufficiency remain to be proved.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Springer, 1983.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
