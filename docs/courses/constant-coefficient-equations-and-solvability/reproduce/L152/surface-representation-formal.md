# Exponential-polynomial representations on the characteristic hypersurfaces

*Original proof exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

We represent a solution of a constant-coefficient equation by integrals over its actual characteristic hypersurfaces. Repeated factors require polynomial amplitudes. We prove the area bound, the anisotropic cover, the local division estimates, the global holomorphic repair and the compact-support argument needed for this conclusion.

Use \(D=-i\partial_x\), complex-linear distribution pairings and
\[
F_v(z)=v(e^{-ix\cdot z}),\qquad
\check k(\xi)=k(-\xi),\qquad W(z)=1+|z|^2 .
\tag{SR1}
\]
The dot product in an exponential or in \(x\cdot\tau\) is bilinear. A shift weight \(k\) is positive and satisfies \(k(\xi+h)\le(1+C|h|)^N k(\xi)\). In particular both \(k\) and its reciprocal have polynomial bounds, and \(\log k\) is Lipschitz. The compact test space \(E_k(X)=B_{2,k}\cap\mathcal E'(X)\) has its compact-support-stage inductive topology. Its canonical bilinear dual is \(B_{2,1/\check k}^{\mathrm{loc}}(X)\).

Our complete lower inputs are [L151 H2–H6, local Hermite division](../../AN02-L151.html#h2-the-exact-local-division-theorem), [L147 GD4, locally integrable holomorphic logarithms](../../AN02-L147.html#gd4-scalar-holomorphic-logarithms-are-proper-psh-and-locally-integrable), [L131 NP2–NP3 and NP5, positive Laplacian measures and harmonic regularity](../../AN02-L131.html#np5-a-direct-harmonic-smoothing-argument), [L149 PW1–PW11, weights with their actual finite stages](../../AN02-L149.html#complete-proof), [L150 NV2, NV4 and NV7, smooth polynomial strength, nonsmooth weighted existence and compact annihilation](../../AN02-L150.html#nv4-a-strict-estimate-for-a-nonsmooth-weight), [L122 CF2.1–CF4.1, compact Fourier support and entire division](../../AN02-L122.html#complete-formal-proof-compact-fourier-division-and-multiplicity-sensitive-annihilators), and [L043, complex Hilbert representation](../../AN02-L043.html#a-representing-vector-in-hilbert-space). Each extra geometric and covering estimate used below is proved here.

## SR1. The exact surface theorem

**Theorem SR1.** Let \(X\subset\mathbb R^n\) be open and convex, \(n\ge1\), and let \(u\in B_{2,1/\check k}^{\mathrm{loc}}(X)\) satisfy \(P(D)u=0\). For nonconstant \(P\), factor it as
\[
P=c_P\prod_{j=1}^s P_j^{m_j},\qquad
d_j=\deg P_j,\quad m=\deg P=\sum_jm_jd_j,\quad
P_m(\tau)\ne0,\quad \tau\in\mathbb C^n.
\tag{SR2}
\]
The \(P_j\) are distinct irreducible nonconstant polynomials. Let \(N_j=\{P_j=0\}\). On a hypersurface, \(dS_j\) is its Euclidean real \(2n-2\) dimensional area on its smooth local reduced graph charts, extended by zero to the remaining points. Equivalently use the regular-power locus: near such a point a defining polynomial is a nonvanishing factor times a power of a holomorphic defining function with nonzero differential. This is the surface measure in the source theorem. In dimension one it is counting measure at distinct points.

There is a finite real locally Lipschitz PSH function \(\phi\) satisfying
\[
\begin{aligned}
e^{-\phi(\xi+i\eta)}&\le C_L e^{-H_L(\eta)}k(\xi)
&& (L\Subset X\text{ compact convex}),\\
k(\xi)&\le C_Ae^{-\phi(\xi+i\eta)}
&& (|\eta|<A),\\
|\nabla\phi(\xi+i\eta)|&\le C_0+\log(1+|\eta|)
&&\text{almost everywhere},\\
\mathcal L_\phi(w)&\ge c(1+|\eta|^2)^{-3/4}|w|^2
&&\text{distributionally},
\end{aligned}
\tag{SR3}
\]
and measurable \(U_j^a\) on \(N_j\), \(0\le a<m_j\), for which
\[
\sum_j\sum_{a<m_j}
\int_{N_j}|U_j^a(z)|^2 e^{2\phi(-z)}W(z)^{-K}\,dS_j(z)<\infty ,
\tag{SR4}
\]
and
\[
u(x)=\sum_j\sum_{a<m_j}(x\cdot\tau)^a
           \int_{N_j}U_j^a(z)e^{ix\cdot z}\,dS_j(z).
\tag{SR5}
\]
Here SR5 means distributional testing with every \(v\in C_c^\infty(X)\); the corresponding integrals of the tested kernels converge absolutely. It need not give an absolutely convergent pointwise integral.

One admissible, deliberately nonoptimal, integer depending only on \(n,m\) is
\[
E=m^4+m^2(2m-1)(m-1)+(m-1)(2n-2),\qquad
K=E+2m+2.
\tag{SR6}
\]
Constants in the proof may depend on the polynomial, the direction, the weight and the solution; the exponent \(K\) does not. Every exponential-polynomial kernel in SR5 itself solves \(P(D)h=0\).

We first prove the geometric estimates, then construct the representation. No tube density is substituted for a surface density.

## SR2. An exact algebraic area bound

Write \(b_{2n-2}=\pi^{n-1}/(n-1)!\), with \(b_0=1\). For any nonzero polynomial \(A\) of degree \(d\) and its regular-power zero locus \(Z_A\),
\[
\int_{Z_A\cap B(z,r)}dS\le b_{2n-2}\,d\,r^{2n-2}.
\tag{SR7}
\]
In particular, for \(A=P_j\), this gives the exact degree bound required for each \(N_j\).

Put \(q_\epsilon=\frac12\log(|A|^2+\epsilon^2)\). Its complex Hessian is positive: differentiation gives
\(\partial_l\bar\partial_h q_\epsilon=\epsilon^2 A_l\overline{A_h}/[2(|A|^2+\epsilon^2)^2]\).
It decreases locally in \(L^1\) to \(\log|A|\), as proved in L147 GD4. Thus \(\Delta q_\epsilon\) tends distributionally to the positive locally finite measure \(\mu=\Delta\log|A|\). We will bound that measure and compare its mass with area on regular charts.

Translate the center to zero and let \(M_\epsilon(r)\) be the spherical average of \(q_\epsilon(r\theta)\) over the unit sphere in \(\mathbb C^n\). Its function of logarithmic radius,
\[
s\longmapsto M_\epsilon(e^s),
\tag{SR8}
\]
is convex. Indeed, for each unit \(\theta\), the restriction \(w\mapsto q_\epsilon(w\theta)\) is smooth subharmonic in the complex plane. Its circle mean \(a_\theta(r)\) satisfies
\[
\frac{d^2}{ds^2}a_\theta(e^s)
=\frac{r^2}{2\pi}\int_0^{2\pi}
       \Delta_{\mathbb R^2}[q_\epsilon(w\theta)]_{w=re^{it}}\,dt\ge0.
\tag{SR9}
\]
This follows by differentiating the circle mean twice and integrating the angular second derivative to zero. Averaging \(a_\theta(r)\) over \(\theta\) is exactly \(M_\epsilon(r)\), since multiplication of \(\theta\) by any unit complex number preserves spherical measure. This proves SR8 without a unitary-group averaging theorem.

For \(r\ge1\), polynomial growth gives \(M_\epsilon(r)\le d\log r+C_\epsilon\). The derivative of a differentiable convex function bounded above by \(ds+C_\epsilon\) on a right half-line is at most \(d\): a derivative greater than \(d\) at one point supplies a tangent line contradicting that upper bound at large \(s\). The divergence theorem therefore yields
\[
\begin{aligned}
\int_{B(0,r)}\Delta q_\epsilon\,dV
&=|S^{2n-1}|\,r^{2n-1}M_\epsilon'(r)\\
&\le |S^{2n-1}|\,d\,r^{2n-2}
 =2\pi b_{2n-2}\,d\,r^{2n-2}.
\end{aligned}
\tag{SR10}
\]
The sphere constant follows from polar integration of the Gaussian:
\(\int_{\mathbb R^{2n}}e^{-|x|^2}dx=\pi^n\) and
\(\int_0^\infty e^{-r^2}r^{2n-1}dr=(n-1)!/2\).
The latter is obtained by substitution \(s=r^2\) and \(n-1\) integrations by parts.

For any \(0\le\psi\le1\) smooth and compactly supported inside \(B(0,r)\), distributional convergence passes SR10 to \(\int\psi\,d\mu\). Exhaust the open ball by such cutoffs and apply monotone convergence, or the inner regularity of the positive Radon measure, to get
\[
\mu(B(0,r))\le2\pi b_{2n-2}\,d\,r^{2n-2}.
\tag{SR11}
\]
This step does not assume that ball boundaries have zero mass.

Here is the precise area comparison. At a regular-power point choose unitary coordinates \((t,y)\) in which the zero set is \(t=a(y)\), and write \(A=g(t,y)(t-a(y))^\ell\), \(g\ne0\). The graph exists, for example, by an isolating circle and the first root power sum: the unique small reduced root equals its contour power sum and is holomorphic in \(y\); uniqueness and division give the nonvanishing factor. This is the local contour construction in L045 and L151 H4, and also proves the local implicit graph claim. A local holomorphic logarithm of \(g\), obtained by its convergent logarithm series after shrinking the neighborhood, has harmonic real part. Hence
\(\Delta\log|A|=\ell\,\Delta\log|t-a(y)|\) there.

For \(h=t-a(y)\), direct differentiation gives
\[
\Delta\left(\tfrac12\log(|h|^2+\delta^2)\right)
=\frac{2\delta^2(1+\sum_l|a_{y_l}|^2)}
              {( |t-a(y)|^2+\delta^2)^2}.
\tag{SR12}
\]
The real change \((t,y)\mapsto(t-a(y),y)\) has determinant one. In the normal complex variable the kernel \(2\delta^2/(|w|^2+\delta^2)^2\) has total mass \(2\pi\), by polar integration, and its mass outside any fixed disk tends to zero. Testing SR12 and using this approximate identity proves
\[
\Delta\log|h|=2\pi(1+|a'(y)|^2)\,dV_y
                 \quad\hbox{on the graph}.
\tag{SR13}
\]
For completeness, the real graph derivative has Gram matrix \(I+Da^{\mathsf T}Da\). Holomorphicity makes the two nonzero singular values of \(Da\) equal to \(|a'|\): the real matrix of a complex row has two orthogonal rows of squared norm \(|a'|^2\). Thus the square root of that Gram determinant is \(1+|a'|^2\). Consequently SR13 is exactly \(2\pi\,dS\), and \(\mu=2\pi\ell\,dS\) on this chart.

There are countably many such charts because Euclidean space has a countable base. A disjoint measurable partition subordinate to them makes their local identities additive. Since \(\ell\ge1\) and \(\mu\) is positive also on the complement, \(\mu\ge2\pi\,dS\) on \(Z_A\). Combine this with SR11 to prove SR7. No unproved assertion about the Hausdorff measure of the singular locus is needed: the surface measure being used was defined on the regular-power charts. For \(n=1\), the same computation is the usual \(2\pi\ell\) atom at an isolated zero, and SR7 counts at most \(d\) distinct zeros.

## SR3. Normalize the direction and obtain uniform local remainders

Let \(e=\tau/|\tau|\) and choose unitary complex coordinates \(z=T(t,y)\) whose first column is \(e\). The weight and its imaginary part remain in the original variables \(z\); we do not assume that a complex unitary change preserves the real physical space or \(\operatorname{Im}z\). All distances, volumes and surface areas are preserved by this frequency-coordinate change.

Because \(P_m(e)\ne0\), every highest-degree part \((P_j)_{d_j}(e)\) is nonzero. Normalize the factors of \(P(-T(t,y))\) by their nonzero leading \(t\)-coefficients to write a monic polynomial
\[
Q(t,y)=\prod_j Q_j(t,y)^{m_j},\qquad
Q_j\text{ monic of degree }d_j\text{ in }t,\qquad
Q=c\,P(-T(t,y)).
\tag{SR14}
\]
Every coefficient of \(t^\ell\) has \(y\)-degree at most \(m-\ell\). In characteristic zero the monic reduced product \(Q_*=\prod_jQ_j\) is squarefree over the fraction field \(\mathbb C(y)\): an irreducible factor cannot divide its nonzero \(t\)-derivative of smaller \(t\)-degree, and distinct factors remain relatively prime there by clearing denominators and polynomial unique factorization. Thus its usual monic discriminant \(R(y)\) is not identically zero. The Sylvester determinant gives
\[
d:=\deg R\le m(2m-1).
\tag{SR15}
\]

For a center \(\theta\) in these coordinates set
\[
\sigma_\theta=(1+|\theta|)^{1-m},\qquad
A_\theta=\operatorname{diag}(1,\sigma_\theta,\ldots,\sigma_\theta),
\qquad B_r(\theta)=\theta+A_\theta B(0,r).
\tag{SR16}
\]
The ball on the right is a complex Euclidean ball. Put
\(Q_\theta(w)=Q(\theta_1+w_1,\theta'+\sigma_\theta w')\).
Its leading \(w_1^m\)-coefficient is one. For \(|\alpha'|\ge1\), polynomial differentiation and the factor \(\sigma_\theta^{|\alpha'|}\) bound \(|\partial^\alpha Q_\theta(0)|\) uniformly in \(\theta\): its possible power of \(1+|\theta|\) is
\(m-|\alpha_1|-m|\alpha'|\le0\).
The pure \(w_1\)-derivatives are at most their factorials times
\(\sup_{|w_1|<1}|Q_\theta(w_1,0)|\), by Cauchy's estimate. This supremum is at least one by the monic leading coefficient. Hence the hypothesis H10 of L151 holds with one fixed constant depending on \(Q,n,m\).

Also \(\widetilde Q_\theta(0)\le C_Q(1+|\theta|)^m\). The discriminant of the reduced transformed product is \(R(\theta'+\sigma_\theta w')\), because translating all \(t\)-roots does not change their differences. A nonzero derivative of top total order \(d\) is a constant \(c_R\ne0\). Therefore its full derivative strength obeys
\[
\widetilde R_\theta(0)\ge |c_R|\sigma_\theta^d
=|c_R|(1+|\theta|)^{-d(m-1)}.
\tag{SR17}
\]
This remains valid for constant \(R\), including \(n=1\).

Apply the complete division theorem L151 H2 to
\(F(T(\theta+A_\theta w))\). With one uniform \(0<c<1/4\), it gives
\[
F(Tz)=Q(z)g_\theta(z)+h_\theta(z)\quad(z\in B_c(\theta)),
\tag{SR18}
\]
where \(g_\theta,h_\theta\) are holomorphic there. The surface scaling of \(A_\theta\) has every singular value at least \(\sigma_\theta\); thus its \(2n-2\) dimensional area factor is at least \(\sigma_\theta^{2n-2}\). Combining this with L151 H13, its admissible exponent \(m^3\), SR15–SR17, and \(\max m_j-\frac12\le m\), proves
\[
H_\theta:=\sup_{B_c(\theta)}|h_\theta|
\le C(1+|\theta|)^E
   \sum_j\sum_{a<m_j}
   \int_{\widetilde N_j\cap B_1(\theta)}
          |\partial_t^a[F(Tz)]|\,dS_j(z),
\tag{SR19}
\]
where \(\widetilde N_j=T^{-1}(-N_j)\) and \(E\) is SR6. The estimate remains true if its actual local degree or multiplicity is smaller. In particular the remainder is zero when all these surface pieces are empty.

Because \(B_1(\theta)\) is contained in the ordinary unit Euclidean ball, SR7 and Cauchy–Schwarz give
\[
H_\theta^2\le C W(\theta)^E J_\theta(F),\qquad
J_\theta(F)=\sum_j\sum_{a<m_j}
 \int_{\widetilde N_j\cap B_1(\theta)}
       |\partial_t^a[F(Tz)]|^2\,dS_j(z).
\tag{SR20}
\]
Indeed the total area counted with these multiplicities is at most
\(b_{2n-2}\sum_jm_jd_j=b_{2n-2}m\). This proves the square estimate without a uniform bound on the coefficients of \(F\).

## SR4. A full anisotropic cover and partition

Here is a concrete covering argument. Let \(L_0=3^{m-1}\) and choose
\(a=c/[16(1+L_0)]\).
Enumerate the rational points of \(\mathbb R^{2n}\). At each point include its open ball \(B_a(\theta)\) if it is disjoint from all previously included balls; otherwise omit it. The resulting balls are disjoint. If two such radius-\(a\) balls intersect, their centers have ordinary distance below \(2a\), so their \(1+|\theta|\) ratios lie between \(1/(1+2a)\) and \(1+2a\); their \(\sigma\)-ratios are between \(L_0^{-1}\) and \(L_0\). The triangle inequality after applying \(A_\theta^{-1}\) then shows that the center of one lies in \(B_{a(1+L_0)}(\theta)\) about the other.

Every enumerated rational point therefore lies in one of these enlarged balls. On any fixed ordinary compact set, the centers under consideration lie in a bounded set; their disjoint small balls have a common positive lower volume there. Only finitely many of them can occur, by packing in an ordinary larger bounded set. Approximating any point by rational points and taking a recurring one of those finitely many centers gives membership in a closed enlarged ball. The strictly larger \(B_{c/4}(\theta_\nu)\) therefore cover all of \(\mathbb C^n\), and the family is locally finite.

There is a uniform bound on the overlap of the \(B_1(\theta_\nu)\). If \(z\) belongs to such a ball, \(|z-\theta_\nu|<1\), so with \(L_1=2^{m-1}\) the \(\sigma\)-ratio lies between \(L_1^{-1}\) and \(L_1\). Every disjoint inner \(B_a(\theta_\nu)\) for these centers lies in
\(z+A_z B(0,L_1(1+a))\), and has volume at least
\(b_{2n}a^{2n}L_1^{-(2n-2)}\sigma_z^{2n-2}\).
Comparing volumes bounds the number by the finite integer
\[
N_*=\left\lceil
 \left(\frac{L_1(1+a)}a\right)^{2n}L_1^{2n-2}
\right\rceil.
\tag{SR21}
\]

Choose a nonnegative smooth function \(\beta\) equal to one on the closed ball of radius \(c/4\), and supported in the open ball of radius \(c/2\). Such a function is obtained from the usual \(e^{-1/s}\) smooth step, with all derivatives zero at its endpoints. Set
\[
\beta_\nu(z)=\beta(A_{\theta_\nu}^{-1}(z-\theta_\nu)),
\quad S(z)=\sum_\nu\beta_\nu(z),\quad
\chi_\nu=\beta_\nu/S .
\tag{SR22}
\]
The sums are locally finite, \(S\ge1\), and at most \(N_*\) terms are active. Differentiating the quotient and using the local \(\sigma\)-comparisons just proved yields
\[
\sum_\nu\chi_\nu=1,\quad
\operatorname{supp}\chi_\nu\subset B_{c/2}(\theta_\nu),\quad
|\partial_t\chi_\nu|
 +\sigma_{\theta_\nu}|\partial_{y_l}\chi_\nu|\le C.
\tag{SR23}
\]
The same estimate holds for real derivatives and conjugate derivatives. Thus
\(|\bar\partial\chi_\nu(z)|\le C(1+|z|)^{m-1}\) on its support.

## SR5. Uniform division on every overlap

If \(z\) belongs to both inner balls, the \(t\)-disk centered at \(z\), with the \(y\)-coordinate fixed and radius \(c/4\), lies in both outer \(B_c\)-balls. On their intersection,
\[
h_{\theta_\nu}-h_{\theta_\mu}
       =Q(g_{\theta_\mu}-g_{\theta_\nu}).
\tag{SR24}
\]
The quotient on the right is already holomorphic, including at the zeros of \(Q\).

For any monic degree-\(m\) polynomial \(q(t)\) and any center \(t_0\), one can choose \(r\in[c/8,c/4]\) such that its circle stays a fixed distance \(\delta>0\) from all its roots, where \(\delta\) depends only on \(c,m\). In fact remove from this radius interval the intervals of length \(2\delta\) about the at most \(m\) numbers \(|\alpha-t_0|\), with \(\delta=c/[64(m+1)]\). Their total length is less than the interval length. Choose a radius outside them. The reverse triangle inequality gives \(|t-\alpha|\ge\delta\) on that circle, so \(|q(t)|\ge\delta^m\). The circle can be chosen strictly inside the allowed interval if necessary.

The Cauchy formula for the holomorphic quotient in SR24 therefore proves, at every such overlap point,
\[
|g_{\theta_\mu}(z)-g_{\theta_\nu}(z)|
\le\delta^{-m}(H_{\theta_\nu}+H_{\theta_\mu}).
\tag{SR25}
\]
This supplies the needed division estimate directly. It does not use a pointwise lower bound on \(Q(z)\) at the overlap point.

## SR6. Repair the local remainders with one strict weight

Return all functions to the original frequency coordinates; unitary changes do not alter the estimates above. Let \(q(v)=|u(v)|\) on \(E_k(X)\), using its canonical continuous action. Apply the full L149 construction to this seminorm. Retain its specific stages \(\phi_j\uparrow\phi\), exhaustion \(K_j\Subset\operatorname{int}K_{j+1}\), and strip parameters \(A_j\), with \(\alpha_j\ge1/2\). They have the common gradient and curvature bounds SR3, the upper estimate
\[
\phi_j(\xi+i\eta)\le H_{K_{j+1}}(\eta)-\log k(\xi)+D_j,
\tag{SR26}
\]
the lower seed estimate
\(\phi_j\ge H_{K_j}(\eta)-\log k(\xi)-D'_j\),
and the actual domination
\[
\alpha_j q(w)\le
\left(\int_{|\eta|<A_j}|F_w(z)|^2e^{-2\phi_j(z)}\,dV(z)\right)^{1/2}
\quad(\operatorname{supp}w\subset K_{j+3}).
\tag{SR27}
\]
Using arbitrary stage weights without this support and seminorm information would not justify the next argument.

Let \(\mathcal Q(z)=Q(T^{-1}z)=cP(-z)\). For a fixed large parameter \(T_0\), define the smooth polynomial strength
\[
\mathcal J(z)^2=\sum_{|\gamma|\le m}
    |\partial_z^\gamma\mathcal Q(z)|^2
           (T_0^2+|\operatorname{Im}z|^2)^{|\gamma|}.
\tag{SR28}
\]
L150 NV2 proves positivity, \(|\mathcal Q|\le\mathcal J\), and the complex Hessian bound
\(\|\mathcal L_{\log\mathcal J}\|\le B(T_0^2+|\eta|^2)^{-1}\).
The same proof applies to these original coordinates. Choose \(T_0\) once so that this is at most half the common SR3 lower curvature; existence follows from the bound
\((1+|\eta|^2)^{3/4}/(T_0^2+|\eta|^2)\le 2^{3/4}T_0^{-1/2}\).
Then \(2(\phi_j-\log\mathcal J)\) is finite continuous PSH with Levi matrix at least \(c(1+|\eta|^2)^{-3/4}I\), uniformly in \(j\). Ordinary polynomial growth, keeping the decrease of degree after each derivative, also gives
\[
\mathcal J(z)^2\le C_{\mathcal Q,T_0}W(z)^m.
\tag{SR29}
\]
The scale factor in a jet of order \(|\gamma|\) contributes at most that same power \(|\gamma|\); its polynomial degree is at most \(m-|\gamma|\).

For \(v\in C_c^\infty(X)\), put \(F=F_v\), and use its local decompositions SR18. Define smooth locally finite sums
\[
H=\sum_\nu\chi_\nu h_\nu,\quad
G=\sum_\nu\chi_\nu g_\nu,\quad
F=H+\mathcal QG,\quad
f=-\bar\partial G
=\sum_{\mu,\nu}\chi_\mu(g_\mu-g_\nu)\bar\partial\chi_\nu .
\tag{SR30}
\]
The identity for \(f\) uses \(\sum\bar\partial\chi_\nu=0\); signs follow by expanding the double sum. In particular \(f\) is smooth and closed, with all apparent quotients removable. By SR20, SR23 and SR25,
\[
|H(z)|^2\le C\sum_{\nu:z\in B_{c/2}(\theta_\nu)}H_\nu^2,\qquad
|f(z)|^2\le C W(z)^{m-1}
             \sum_{\nu:z\in B_{c/2}(\theta_\nu)}H_\nu^2 .
\tag{SR31}
\]
The overlap bound absorbs both finite sums.

We record the complete weighted summation. If \(z\in B_{c/2}(\theta_\nu)\) and \(s\in B_1(\theta_\nu)\), then \(|z-s|<2\), and \(W(z),W(s),W(\theta_\nu)\) are comparable by fixed constants. The common gradient bound in SR3 gives
\[
e^{-2\phi_j(z)}\le C W(s)^2 e^{-2\phi_j(s)}.
\tag{SR32}
\]
To see this, integrate the local Lipschitz bound along the segment: its length is below two, and \(1+|\operatorname{Im}\zeta|\le3(1+|\operatorname{Im}s|)\) along it. Thus
\(|\phi_j(z)-\phi_j(s)|\le C+2\log(1+|\operatorname{Im}s|)\);
exponentiation gives SR32. The estimate holds for every segment by local Lipschitz continuity, including exceptional differentiability points.

The volume of each inner ellipsoid is at most that of a fixed ordinary unit ball. SR20, SR29–SR32 and the \(N_*\) overlap of the outer balls imply
\[
\begin{aligned}
\int |H|^2e^{-2\phi_j}\,dV&\le C\mathcal A_j(F),\\
\int |f|^2\mathcal J^2e^{-2\phi_j}
                       (1+|\eta|^2)^{3/4}\,dV
&\le C\mathcal A_j(F),\\
\mathcal A_j(F)&=
\sum_{\ell=1}^s\sum_{a<m_\ell}
 \int_{-N_\ell}
       |\partial_e^aF(s)|^2e^{-2\phi_j(s)}W(s)^K\,dS_\ell(s).
\end{aligned}
\tag{SR33}
\]
Here \(\ell\) labels factors and \(j\) labels stages; \(\partial_e=\sum_l e_l\partial_{z_l}\) is in the original coordinates. More explicitly, the squared cutoff bound contributes \(W^{m-1}\), strength contributes \(W^m\), and inverse curvature contributes at most \(W\). These give \(W^{2m}\); the squared local remainder contributes \(W^E\), and SR32 contributes \(W^2\). Hence \(K=E+2m+2\) suffices. Sum the local surface integrals last: each surface point is counted at most \(N_*\) times. This explains every exponent and all uses of overlap.

For any sufficiently large stage containing the support of \(v\) strictly inside \(K_j\), \(\mathcal A_j(F)\) is finite. Here are details of that assertion. Choose a compact convex carrier \(S\) and \(\rho>0\) with \(S+\rho\overline B\subset K_j\). Integration by parts in the real variables of each compact smooth function \((x\cdot e)^a v(x)\) gives, for every integer \(L\),
\[
|\partial_e^aF(\xi+i\eta)|
\le C_L(1+|\xi|)^{-2L}(1+|\eta|)^{2L} e^{H_S(\eta)} .
\tag{SR34}
\]
Apply \((1-\Delta_x)^L\) to the compact amplitude \(e^{x\cdot\eta}(x\cdot e)^av(x)\), getting denominator \((1+|\xi|^2)^L\). Its derivatives have order at most \(2L\) and give the displayed imaginary-frequency polynomial. The lower seed estimate, polynomial growth of \(k\), and \(H_{K_j}\ge H_S+\rho|\eta|\) now give arbitrary real-frequency decay, polynomial imaginary-frequency growth and \(e^{-2\rho|\eta|}\) in the integrand of SR33. Cover complex space by unit lattice cubes; SR7 bounds their surface mass by a uniform constant, using an enclosing ball of fixed radius. The suprema of these integrands are summable when \(L\) is chosen large enough. This proves finiteness, not just a formal trace restriction.

Apply the nonsmooth strict estimate proved in L150 NV4 to the weight \(2(\phi_j-\log\mathcal J)\) and the closed data \(f\). It gives a locally square-integrable \(w_j\) with \(\bar\partial w_j=f\) and
\[
\int |w_j|^2\mathcal J^2 e^{-2\phi_j}\,dV
\le C\mathcal A_j(F).
\tag{SR35}
\]
Set
\[
V_{1,j}=H-\mathcal Qw_j,\qquad
V_{2,j}=\mathcal Q(G+w_j),\qquad F=V_{1,j}+V_{2,j}.
\tag{SR36}
\]
Since \(\bar\partial H=\mathcal Q f\), both transforms are distributionally holomorphic. The quotient \(G+w_j\) is locally \(L^2\) and distributionally holomorphic as well. Its real Laplacian is zero; L131 NP5 gives smoothness, and its Cauchy–Riemann equations give holomorphicity. The same argument applies to \(V_{1,j}\). Thus all are actual entire functions. From \(|\mathcal Q|\le\mathcal J\), SR33 and SR35,
\[
\int |V_{1,j}|^2e^{-2\phi_j}\,dV\le C\mathcal A_j(F).
\tag{SR37}
\]

## SR7. Verify compact carriers and annihilation

The unit-ball holomorphic submean estimate, the common gradient bound and SR26 turn SR37 into
\[
|V_{1,j}(z)|\le C_j(1+|z|)^{N+1}
                           e^{H_{K_{j+1}}(\operatorname{Im}z)} .
\tag{SR38}
\]
Indeed on a unit ball the exponential weight changes by at most \(C(1+|\eta|)^2\); taking a square root gives \(1+|\eta|\), and \(1/k(\xi)\) has polynomial order \(N\). L122 CF2.1 therefore identifies \(V_{1,j}\) as the transform of a compact distribution \(v_{1,j}\) supported in \(K_{j+1}\Subset X\).

It also belongs to \(B_{2,k}\). On \(|\eta|<1\), the upper estimate SR26 gives \(e^{-\phi_j}\ge c_j k(\xi)\). Its weighted strip \(L^2\) norm is consequently finite by SR37. The full real-plane control by a unit imaginary strip in L148 CF22 gives its real \(B_{2,k}\) norm. Thus the canonical action of \(u\) on \(v_{1,j}\) is legitimate. The difference \(v_{2,j}=v-v_{1,j}\) is compact with the same carrier stage and belongs to \(B_{2,k}\).

By SR36 its entire transform is divisible by \(\mathcal Q=cP(-z)\). The full entire division and support theorem L122 CF3.2–CF4.1 gives a compact distribution \(a_j\) with carrier in \(K_{j+1}\) and \(v_{2,j}=cP(-D)a_j\). To justify annihilation without testing a rough distribution against another one, mollify \(a_j\) in the physical variables. For a compact smooth normalized mollifier \(\rho_\epsilon\), \(a_j*\rho_\epsilon\) is a compact smooth test in one fixed subset of \(X\), and
\[
cP(-D)(a_j*\rho_\epsilon)
       =v_{2,j}*\rho_\epsilon\longrightarrow v_{2,j}
                    \quad\hbox{in }B_{2,k}.
\tag{SR39}
\]
The convergence follows by dominated convergence for the bounded multipliers
\(\widehat\rho(\epsilon\xi)\to1\) acting on its existing weighted \(L^2\) Fourier transform. The supports stay in that fixed compact stage. The equation \(P(D)u=0\) annihilates each smooth left side, and continuity of the canonical stage action therefore gives \(u(v_{2,j})=0\).

Since \(v_{1,j}\) is supported in \(K_{j+1}\subset K_{j+3}\), SR27 and SR37 imply
\[
|u(v)|^2=|u(v_{1,j})|^2
   \le C\mathcal A_j(F_v).
\tag{SR40}
\]
All constants here are uniform in sufficiently large stage indices. In particular we did not infer compact support from holomorphicity alone.

## SR8. Pass to one weight and obtain the densities

The stage weights increase to \(\phi\); the integrands of \(\mathcal A_j(F)\) decrease. Their value at one sufficiently large initial stage is integrable by SR34. Dominated convergence, with that fixed majorant, passes SR40 to
\[
|u(v)|^2\le C\mathcal A(F_v),\qquad
\mathcal A(F)=
\sum_j\sum_{a<m_j}
 \int_{-N_j}|\partial_e^aF(s)|^2e^{-2\phi(s)}W(s)^K\,dS_j(s).
\tag{SR41}
\]
We have retained all four conditions SR3, since the final weight is the actual L149 weight; polynomial strength was subtracted only for the auxiliary \(\bar\partial\) estimate.

In the finite Hilbert direct sum
\[
\mathcal H=\bigoplus_{j,a<m_j}
 L^2(-N_j,e^{-2\phi(s)}W(s)^K\,dS_j(s)),
\tag{SR42}
\]
map a compact smooth \(v\) to its restricted jets \(Jv=(\partial_e^aF_v)\). SR41 makes \(L(Jv)=u(v)\) well defined and bounded: a zero jet vector forces \(u(v)=0\). Extend \(L\) continuously to the closure of this range. By the full complex Hilbert representation, with inner product linear in its first variable, there is \(g\) in that closure such that
\[
u(v)=\sum_{j,a}\int_{-N_j}\partial_e^aF_v(s)
                  \overline{g_j^a(s)}e^{-2\phi(s)}W(s)^K\,dS_j(s).
\tag{SR43}
\]
Put \(B_j^a(s)=\overline{g_j^a(s)}e^{-2\phi(s)}W(s)^K\).
Then \(\sum\int|B_j^a|^2e^{2\phi}W^{-K}=\|g\|_{\mathcal H}^2<\infty\).
Reflection \(s=-z\) preserves Euclidean area and \(W\), while
\[
\partial_e^aF_v(-z)
 =v\bigl((-i\,x\cdot e)^ae^{ix\cdot z}\bigr).
\tag{SR44}
\]
Define \(U_j^a(z)=(-i)^a|\tau|^{-a}B_j^a(-z)\). Equations SR43–SR44 are exactly SR4–SR5. Cauchy–Schwarz with SR41 proves absolute convergence for every compact smooth test. It also proves the same identity for any compact weighted test whose restricted jet vector is defined by a compatible limit in this Hilbert space; we do not assert finite trace energy for all of \(E_k(X)\).

Finally, for \(z\in N_j\),
\[
P(D)\bigl[(x\cdot\tau)^ae^{ix\cdot z}\bigr]
=e^{ix\cdot z}\sum_{b=0}^a
   \binom ab(-i)^b(x\cdot\tau)^{a-b}
                   (\tau\cdot\partial_z)^bP(z)=0
       \quad(a<m_j).
\tag{SR45}
\]
The formula is the finite polynomial product rule. The derivative in the sum is the \(b\)-th derivative of \(P(z+s\tau)\) at zero. Since \(P_j(z)=0\), that one-variable polynomial is divisible by \(s^{m_j}\), or is identically zero; thus all these derivatives vanish. This includes singular characteristic points.

If \(X\) is empty the conclusion is vacuous. A nonzero constant polynomial forces \(u=0\), giving an empty representation. The zero polynomial has no noncharacteristic direction and no factorization SR2; its unconstrained whole-complex-space representation is the separately proved L150 NV9, rather than an assertion of this surface theorem. This completes SR1 with the exact hypotheses and endpoint scope. \(\square\)

## Source scope and remaining work

This original proof gives the full surface representation in Hörmander, *The Analysis of Linear Partial Differential Operators II*, second edition, Theorem 15.3.3, printed pages 291–296, with its polynomial loss, all multiplicity jets and the reflected test-weight convention. Its area prerequisite matches the regular-power surface convention of Hörmander, *The Analysis of Linear Partial Differential Operators I*, second edition, Theorem 4.1.12, printed page 98. SR8–SR13 give a direct complete proof of the needed sharp polynomial area upper bound; they avoid requiring the full general Lelong-number limit theorem 4.1.15 as an unproved dependency. The prescribed highest-degree/noncharacteristic hypothesis and Euclidean metric are retained.

The source was read in approved local copies, including the statement and final Fourier sign on actual page pixels. No book text or source-page image is part of this original lesson. Illustrations and checks accompanying it are independently reproducible. This one theorem does not complete Chapter 15, its embedded exercise targets, the Chapter 16 inventory or the assigned residual work in Chapters 10–13.
