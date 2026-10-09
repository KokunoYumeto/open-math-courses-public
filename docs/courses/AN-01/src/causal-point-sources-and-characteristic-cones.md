# Causal point sources and characteristic cones

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition by GPT-6.1 Sol (OpenAI). Original exposition: CC0. Self-checked by the writing AI.*

An inverse with prescribed support can turn a point source into an ordinary function, a measure on a cone, or a locally finite train of differentiated pulses. In each case we must check the equation at the corner or cone vertex. Calculations on its complement would leave the source undetermined.

We use the proved tensor construction B0–B3, proper convolution Theorem 1.1 and associativity Theorem 3.1 in [Convolution as addition of supports](convolution-as-addition-of-supports.md). The normalized causal family is in [Causal integration of complex order](causal-integration-of-complex-order.md), (1.3)–(1.6); its Theorems 2.1–2.2 prove the beta integral and convolution law. The [finite-order distribution criterion](order-positivity-and-limits.md), Proposition 1.2, and [scalar identity theorem](gluing-holomorphic-sides.md), Lemma 3.2, justify the continuations below. [Cauchy kernels and boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2, proves the holomorphic power series used for coefficient comparisons. The entire wave family will be constructed here, including its value at parameter zero.

## A quadrant turns integration into an inverse

All distributions act complex linearly. Derivatives satisfy \((\partial_jT)(\phi)=-T(\partial_j\phi)\); multiplication satisfies \((aT)(\phi)=T(a\phi)\). We write \(H=1_{\{x>0\}}\) and

\[
\begin{gathered}
R_a=C_{a-1},\\
R_m(x)=\frac{x^{m-1}H(x)}{(m-1)!},\qquad m\ge1 .
\end{gathered}
\tag{1.1}
\]

Here \(C\) is the entire normalized one-sided family proved in U016 and used in U022. U022 proves, including all boundary terms,

\[
R_0=\delta_0,\qquad R_a'=R_{a-1},\qquad R_a*R_b=R_{a+b}.
\tag{1.2}
\]

Let \(Q_n=[0,\infty)^n\). If a sum of finitely many points of \(Q_n\) belongs to a fixed compact set, every coordinate of every summand is nonnegative and bounded by an upper bound for that sum coordinate. The inverse image of the compact set is also closed, hence compact by the supplied finite-dimensional compactness proof. This is properness of addition. The convolution results therefore give a commutative algebra of \(Q_n\)-supported distributions, with unit \(\delta_0\). Derivatives preserve the support, since they test only derivatives of the same test.

**Theorem 1.1 (all positive integer coordinate orders).** If every entry of the multi-index \(\alpha\) is a positive integer, then

\[
K_\alpha=\bigotimes_{j=1}^nR_{\alpha_j}
\tag{1.3}
\]

has the density and derivative

\[
\begin{gathered}
K_\alpha(x)=\prod_{j=1}^n\frac{x_j^{\alpha_j-1}H(x_j)}{(\alpha_j-1)!},\\
\partial^\alpha K_\alpha=\delta_0 .
\end{gathered}
\tag{1.4}
\]

For every \(Q_n\)-supported distribution \(f\), the unique \(Q_n\)-supported solution of \(\partial^\alpha u=f\) is \(u=K_\alpha*f\).

**Proof.** On a compact box, the product of the absolute values of these one-variable densities is integrable: Tonelli gives the product of their finite integrals. The proved tensor construction thus agrees with this density. Differentiating its iterated test pairing gives

\[
\partial^\alpha K_\alpha
=\bigotimes_{j=1}^n\partial^{\alpha_j}R_{\alpha_j}
=\bigotimes_{j=1}^n\delta_0=\delta_0 .
\tag{1.5}
\]

The final tensor evaluates a test at the origin. Derivative transfer through proper convolution proves the equation for \(K_\alpha*f\). Conversely any supported solution obeys

\[
K_\alpha*f=K_\alpha*(\partial^\alpha u)
=(\partial^\alpha K_\alpha)*u=u .
\tag{1.6}
\]

All supports lie in \(Q_n\); the same properness bound justifies each convolution. \(\square\)

We will repeatedly use this more general consequence. Suppose \(C\) is a closed convex cone, finite addition is proper on it, \(P\) has constant coefficients and \(E\) is \(C\)-supported with \(PE=\delta_0\). For all \(C\)-supported \(f,u\), derivative transfer gives

\[
P(E*f)=f,\qquad E*(Pu)=u .
\tag{1.7}
\]

Since \(C+C\subset C\), the first expression constructs a solution with the prescribed support; the second proves uniqueness. This argument applies to complex coefficients and distributional forcing.

## Repeated signals and the inverse of a finite window

For any complex \(b\), set \(F_b(x)=e^{bx}H(x)\). Its possible growth at positive infinity does not affect local integrability or proper causal convolution.

**Proposition 2.1 (repeated exponentially weighted integration).** For every integer \(m\ge1\),

\[
F_b^{*m}=e^{bx}R_m,\qquad
(\partial_x-b)^mF_b^{*m}=\delta_0 .
\tag{2.1}
\]

**Proof.** On a bounded interval of output variables, convolution of two causal locally integrable functions is controlled by absolute integration on a bounded triangle. Fubini applies, and

\[
e^{bs}e^{b(x-s)}=e^{bx}.
\tag{2.2}
\]

Induction and \(R_1^{*m}=R_m\) therefore give the first identity. Directly from the test definition of a derivative and the ordinary product rule,

\[
(\partial_x-b)(e^{bx}T)=e^{bx}T'
\tag{2.3}
\]

for every distribution \(T\): both sides pair as \(-T(e^{bx}\phi'+be^{bx}\phi)\). Iteration with \(T=R_m\) gives \(e^{bx}\delta_0=\delta_0\). Thus the endpoint is included. In particular \(H^{*m}=R_m\) and \((e^{-x}H)^{*m}=e^{-x}R_m\). \(\square\)

For \(a>0\), write \(f_a=1_{(0,a)}\).

**Theorem 2.2 (the pulse train inverse).** Its unique causal convolution inverse is

\[
U_a=\sum_{j=0}^{\infty}\delta_{ja}' .
\tag{2.4}
\]

This distribution is neither compactly supported nor represented by a locally integrable function.

**Proof.** The sum \(S_a=\sum_{j\ge0}\delta_{ja}\) contains only finitely many nonzero terms on any compact test support. The number of these terms times the test supremum is an order-zero bound; its derivative \(U_a=S_a'\) is also a distribution. Translation and cancellation of finite sums on tests give

\[
(\delta_0-\delta_a)*S_a=\delta_0 .
\tag{2.5}
\]

The identity \(f_a=H*(\delta_0-\delta_a)\) is the ordinary difference of two step functions. Associativity and derivative transfer yield

\[
f_a*U_a
=H*(\delta_0-\delta_a)*S_a'
=H*\delta_0'=\delta_0 .
\tag{2.6}
\]

If \(f_a*V=\delta_0\) with causal \(V\), then \(U_a*(f_a*V)=(U_a*f_a)*V\) gives \(V=U_a\). A test supported near \(ja\) and with nonzero derivative there shows that every \(ja\) is in the support. These points form an unbounded discrete set.

Finally a locally integrable density supported on a discrete set is zero as a distribution. Indeed its restriction to the complementary open set is zero; mollification and local \(L^1\) convergence, proved in U021, make the density zero almost everywhere on that open set. The discrete set has Lebesgue measure zero, by countable additivity and the zero measure of a point. It is therefore zero almost everywhere in total, contradicting (2.6). \(\square\)

No convergence requirement at infinity enters a locally finite distribution sum. Every use of the noncompact step function above is covered by causal properness.

## An entire function supplies a mixed-derivative point source

Consider \(P_c=\partial_x\partial_y-c\), \(c\in\mathbb C\).

**Theorem 3.1 (the entire quadrant kernel).** The series

\[
F(z)=\sum_{k=0}^{\infty}\frac{z^k}{(k!)^2}
\tag{3.1}
\]

defines the unique entire function with \(F(0)=1\) and

\[
zF''(z)+F'(z)=F(z).
\tag{3.2}
\]

The locally integrable kernel

\[
E_c(x,y)=H(x)H(y)F(cxy)
\tag{3.3}
\]

satisfies \(P_cE_c=\delta_{(0,0)}\), depends weakly entirely on \(c\), and gives the unique quadrant-supported solution \(E_c*f\) for every quadrant-supported \(f\).

**Proof.** For \(|z|\le A\), taking \(A\ge1\), the ratio of successive absolute terms is at most \(A/(k+1)^2\). It is eventually at most \(1/2\), so a geometric tail proves uniform convergence. The same argument works with any fixed polynomial in \(k\), proving uniform convergence of each derivative series. The FTC applied to partial sums passes their derivative to the limit, proving holomorphy. Coefficient comparison gives (3.2), since \((k+1)^2/((k+1)!)^2=1/(k!)^2\). Conversely the power series of any entire solution has \((k+1)^2a_{k+1}=a_k\), so \(a_0=1\) determines it uniquely.

Put \(T_k=R_{k+1}\otimes R_{k+1}\). Then

\[
E_c=\sum_{k=0}^{\infty}c^kT_k,\qquad
T_k(x,y)=H(x)H(y)\frac{(xy)^k}{(k!)^2}.
\tag{3.4}
\]

For \(0\le x,y\le M\) and \(|c|\le A\), taking \(M,A\ge1\), the absolute terms are bounded by \((AM^2)^k/(k!)^2\). This proves convergence against compact tests with a common order-zero bound and proves entire dependence, including every fixed parameter derivative. The tensor derivative identities give

\[
\partial_x\partial_yT_0=\delta_{(0,0)},\qquad
\partial_x\partial_yT_k=T_{k-1}\quad(k\ge1).
\tag{3.5}
\]

One may differentiate the convergent distribution series: this just replaces the test by its fixed mixed derivative, with unchanged support. Consequently

\[
\partial_x\partial_yE_c
=\delta_{(0,0)}+\sum_{k=1}^{\infty}c^kT_{k-1}
=\delta_{(0,0)}+cE_c .
\tag{3.6}
\]

Equation (1.7) proves existence and uniqueness for general supported forcing. \(\square\)

For an explicit check of the boundary, two one-dimensional integrations by parts give, for smooth \(f\),

\[
\begin{aligned}
\partial_x\partial_y(H(x)H(y)f)
={}&f(0,0)\delta_x\delta_y\\
&+\delta_xH(y)f_y(0,y)+H(x)\delta_y f_x(x,0)\\
&+H(x)H(y)f_{xy}(x,y),
\end{aligned}
\tag{3.7}
\]

where \(\delta_x=\delta_0(x)\), \(\delta_y=\delta_0(y)\). For \(f=F(cxy)\), the two displayed edge derivatives vanish, the corner value is one, and \(f_{xy}=c(F'+zF'')=cF\). The formula also holds at \(c=0\), when \(E_0=H(x)H(y)\).

## The wave family fixes the global normalization

Let \(n\ge1\) be the spatial dimension, and set

\[
\Box=\partial_t^2-\Delta_x,\qquad
C_+=\{(t,x):t\ge|x|\},\qquad q=t^2-|x|^2 .
\tag{4.1}
\]

Finite addition is proper on \(C_+\). If the sum's time is at most \(M\), every summand has \(0\le t_j\le M\) and \(|x_j|\le t_j\); closedness then gives compactness. Triangle inequality also proves \(C_++C_+=C_+\).

We first prove the general family that fixes all the constants used below.

**Lemma 4.0 (entire causal wave powers).** There is a unique entire family of distributions \(\mathcal R_\lambda\) agreeing with the density (4.3) in its initial range. Its members are tempered, supported in \(C_+\), and satisfy

\[
\Box\mathcal R_{\lambda+1}=\mathcal R_\lambda,\qquad
\mathcal R_0=\delta_{(0,0)},\qquad
\deg\mathcal R_\lambda=2\lambda-n-1 .
\tag{4.2}
\]

For \(\operatorname{Re}\lambda>\max(0,(n-1)/2)\), put \(b_{\lambda,n}=\lambda+(1-n)/2\). The density is

\[
\begin{gathered}
\mathcal R_\lambda
=A_{\lambda,n}H(t-|x|)q^{b_{\lambda,n}-1},\\
A_{\lambda,n}
=2^{1-2\lambda}\pi^{(1-n)/2}G(\lambda)G(b_{\lambda,n}),
\qquad G=1/\Gamma .
\end{gathered}
\tag{4.3}
\]

The power is used only on \(q>0\), with the real logarithm. Degree \(d\) means that, for \(a>0\), \(\mathcal R_\lambda(\phi(a\cdot))=a^{-d-n-1}\mathcal R_\lambda(\phi)\).

**Proof.** The supplied [gamma foundations](../prerequisites/U011-free-foundations/gamma-foundations-U016.md), (G0)–(G2) and (W4a)–(W4e), prove the entire reciprocal, its normalization and recurrence. U022 proves the beta identity by absolutely integrable iterated integrals. We need one additional consequence, which we prove explicitly. For \(\operatorname{Re}z>0\), substitute \(u=(1+v)/2\) in \(B(z,z)\), then use evenness and \(w=v^2\). Substitution first holds on truncated intervals by the scalar FTC and then at the endpoints by absolute convergence. It gives

\[
B(z,z)=2^{1-2z}B(1/2,z),\qquad
\Gamma(2z)=\frac{2^{2z-1}}{\sqrt\pi}
                  \Gamma(z)\Gamma(z+1/2).
\tag{4.0a}
\]

For the second equality insert the beta identity and cancel the nonzero \(\Gamma(z)\); \(\Gamma(1/2)=\sqrt\pi\) follows from the Gaussian integral proved in the supplied angular foundation A5. This proves the duplication constant, rather than leaving it as an external formula.

The [angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4–A5, prove polar integration and \(|S^{n-1}|=2\pi^{n/2}/\Gamma(n/2)\), including the two-point sphere when \(n=1\). For \(\operatorname{Re}b>0\), applying polar coordinates and \(u=r^2\) gives

\[
\begin{aligned}
\int_{|y|<1}(1-|y|^2)^{b-1}\,dy
&=\frac{|S^{n-1}|}{2}B(n/2,b)\\
&=\frac{\pi^{n/2}\Gamma(b)}{\Gamma(b+n/2)}.
\end{aligned}
\tag{4.0b}
\]

At each \(t>0\), use the proved linear change \(x=ty\). The absolute spatial integral of the unnormalized density is a finite constant times \(t^{2\operatorname{Re}\lambda-1}\). This is integrable at the vertex exactly under the stated positive-real-part condition; \(\operatorname{Re}b>0\) controls the cone boundary. Thus (4.3) is locally integrable. On a compact parameter set inside this range, these exponents have positive margins. Derivatives in \(\lambda\) insert powers of
\(\log q=2\log t+\log(1-|y|^2)\).
The logarithmic moment estimates (G1), together with the beta integral near its two endpoints, bound every such power uniformly. Dominated difference quotients, as proved in (G2), give holomorphy and fixed-support order-zero bounds.

For later use this density is also tempered. Choose an integer \(L>\operatorname{Re}\lambda\). Since \(|x|\le t\) on the cone, its absolute integral against \((1+t^2+|x|^2)^{-L}\) is bounded by a constant times
\[
\int_0^\infty t^{2\operatorname{Re}\lambda-1}(1+t^2)^{-L}\,dt<\infty .
\]
Near infinity the exponent is less than \(-1\), and near zero it is greater than \(-1\). A weighted supremum of a Schwartz test therefore bounds its pairing. On compact parameter sets take \(L\) larger once; the same argument with logarithms also bounds every fixed parameter derivative. The definition and derivative continuity of the Schwartz space are supplied in the Fourier companion F1.

We now establish identities before continuing the parameter. For sufficiently large \(\operatorname{Re}\lambda\), the zero extension of \(H(t-|x|)q^{b_{\lambda+1,n}-1}\) is \(C^2\) on all spacetime. To check this assertion, take the real part of its exponent larger than two. Inside the cone its derivatives of order \(j\le2\) are bounded near zero by \(C|(t,x)|^{2\operatorname{Re}(b_{\lambda+1,n}-1)-j}\), and tend to zero at each nonzero cone point as well. Extend these derivatives by zero. They are actual derivatives: restrict to a coordinate line, integrate the interior derivative across its finitely many boundary points, and apply the FTC; a line contained in the boundary gives the zero function. Repeat for the first derivatives. Thus there are no boundary distributions in this initial calculation.

Ordinary differentiation gives
\(\Box q^p=2p(2p+n-1)q^{p-1}\), because \(\Box q=2(n+1)\) and the Lorentzian squared gradient is \(4q\). Gamma recurrence now gives

\[
\begin{gathered}
\Box\mathcal R_{\lambda+1}=\mathcal R_\lambda,\\
t\mathcal R_\lambda=2\lambda\,\partial_t\mathcal R_{\lambda+1},
\qquad
x_j\mathcal R_\lambda=-2\lambda\,\partial_{x_j}\mathcal R_{\lambda+1}.
\end{gathered}
\tag{4.0c}
\]

For example \(A_{\lambda,n}=4\lambda b_{\lambda,n}A_{\lambda+1,n}\), which verifies both the second derivative and coordinate constants. Test pairing and the scalar identity theorem extend these identities throughout the common initial half-plane.

For an arbitrary complex parameter choose \(k\ge0\) with \(\lambda+k\) in the initial range and define

\[
\mathcal R_\lambda=\Box^k\mathcal R_{\lambda+k}.
\tag{4.0d}
\]

The proved recursion makes adjacent choices agree on their entire overlap, hence all choices agree. The half-planes cover \(\mathbb C\); the pairings are entire. On each compact parameter set one \(k\) works, and the earlier estimate applied to \(\Box^k\phi\) gives a finite test order and a Schwartz seminorm bound. Thus every member is a distribution and tempered. Derivatives preserve support, so all members remain supported in \(C_+\). The same scalar identity theorem extends (4.0c) to the whole plane and proves uniqueness of the family. Scaling the initial density gives degree \(2\lambda-n-1\). More explicitly, in (4.0d) the test derivative contributes \(a^{2k}\) and the initial density pairing contributes \(a^{-2(\lambda+k)}\), so the continued pairing scales by \(a^{-2\lambda}\). This proves the degree everywhere.

It remains to identify the vertex at \(\lambda=0\). The coordinate identities imply that every coordinate times \(T=\mathcal R_0\) is zero. This forces \(T=c\delta_0\), as can be seen without importing a point-support theorem. For a test \(\phi\), the FTC on the segment from zero to \(z=(t,x)\) gives

\[
\phi(z)=\phi(0)+\sum_{j=0}^n z_j h_j(z),\qquad
h_j(z)=\int_0^1(\partial_j\phi)(sz)\,ds .
\tag{4.0e}
\]

Choose a compact smooth cutoff equal to one on a neighborhood of the support of \(\phi\) and of zero, and multiply this identity by it. Each coordinate term is killed by \(T\), so \(T(\phi)\) is a constant times \(\phi(0)\). The constant is independent of the chosen large cutoff: their difference vanishes near zero, and any compact test \(\psi\) vanishing near zero is
\(\sum_j z_j(z_j\psi/|z|^2)\), hence is killed by \(T\). A fixed cutoff equal to one near zero therefore fixes a single \(c\).

To determine \(c\), let \(f\in C_c^\infty(\mathbb R)\). Choose \(\chi\in C_c^\infty(\mathbb R^n)\) equal to one on a ball containing all \(|x|\le t\) with \(t\in\operatorname{supp}f\cap[0,\infty)\). For \(\phi(t,x)=f(t)\chi(x)\), (4.0b), followed by (4.0a), gives initially

\[
\begin{aligned}
\mathcal R_\lambda(\phi)
&=\frac1{\Gamma(2\lambda)}
           \int_0^\infty t^{2\lambda-1}f(t)\,dt\\
&=R_{2\lambda}(f).
\end{aligned}
\tag{4.0f}
\]

Indeed the constant after spatial integration is
\(2^{1-2\lambda}\sqrt\pi/[\Gamma(\lambda)\Gamma(\lambda+1/2)]
=1/\Gamma(2\lambda)\).
Both sides are entire pairings, so the equality holds for every \(\lambda\). At zero the proved one-dimensional normalization \(R_0=\delta_0\) makes its value \(f(0)\). Choose \(f(0)=1\); since \(\chi(0)=1\), this gives \(c=1\). All assertions in (4.2) are now established on the whole space, including the vertex. \(\square\)

For coordinate changes used below we record the needed distributional rule. If \(A\) is an invertible real linear map in \(d\) variables, define
\[
(A^*T)(\phi)=|\det A|^{-1}T(\phi\circ A^{-1}).
\tag{4.0g}
\]
The test on the right is smooth with compact support, and its seminorms are bounded by finitely many of those of \(\phi\). This defines a distribution. Linear substitution proves agreement with \(T(Az)\) for a density. Applying the ordinary chain rule to the test in (4.0g) gives
\[
\partial_{z_j}A^*T=\sum_k A_{kj}A^*(\partial_{y_k}T),
\qquad A^*\delta_0=|\det A|^{-1}\delta_0.
\tag{4.0h}
\]
For the derivative identity, expand each derivative of \(\phi\circ A^{-1}\) and use \(\sum_k(A^{-1})_{ik}A_{kj}=\delta_{ij}\). This proves all later operator and delta changes directly on tests.

**Theorem 4.1 (one spatial dimension and any real nonzero speed).** For \(c\in\mathbb R\setminus\{0\}\), put \(s=|c|\). The operator \(P=c^{-2}\partial_t^2-\partial_x^2\) has fundamental solution

\[
E_c(t,x)=\frac{s}{2}H(st-|x|),
\tag{4.4}
\]

with support \(t\ge|x|/s\).

**Proof.** For \(n=1,\lambda=1\), (4.3) gives \(\mathcal R_1=H(t-|x|)/2\); (4.2) proves its source. Under \(A(t,x)=(st,x)\), (4.0h) gives \(P A^*T=A^*(\Box T)\) and

\[
\delta_{(0,0)}(st,x)=s^{-1}\delta_{(0,0)}(t,x).
\tag{4.5}
\]

Thus \(sA^*\mathcal R_1\) has unit point source, which is (4.4). \(\square\)

There is also a direct characteristic-coordinate check. Set \(u=t-x/s\), \(v=t+x/s\). Then

\[
P=\frac4{s^2}\partial_u\partial_v,\qquad
\left|\det\frac{\partial(u,v)}{\partial(t,x)}\right|=\frac2s.
\tag{4.6}
\]

The quadrant kernel is \((s/2)H(u)H(v)\). Its derivative is \((2/s)\delta(u)\delta(v)\), and (4.0h) changes this into \(\delta(t,x)\). Both determinant factors are needed.

## A cone measure produces a point source at its vertex

Now let \(n=3\), \(r=|x|\) and \(u(t,x)=H(t-r)\).

**Theorem 5.1 (two wave derivatives of a cone indicator).** On all of \(\mathbb R^4\),

\[
v=\Box u,\qquad w=\Box v=8\pi\delta_{(0,0)},
\tag{5.1}
\]

where \(v\) is the positive measure

\[
\langle v,\phi\rangle
=2\int_0^\infty r\int_{S^2}\phi(r,r\omega)\,d\omega\,dr.
\tag{5.2}
\]

The sphere measure is Euclidean area, with \(|S^2|=4\pi\).

**Proof.** Formula (4.3) at \(\lambda=2,n=3\) gives

\[
u=8\pi\mathcal R_2,\qquad
\Box u=8\pi\mathcal R_1,\qquad
\Box^2u=8\pi\mathcal R_0=8\pi\delta_{(0,0)} .
\tag{5.3}
\]

We identify the first derivative by direct integration for arbitrary tests, which also provides a separate check of the vertex.

Set \(M(t,r)=\int_{S^2}\phi(t,r\omega)\,d\omega\) for \(r\ge0\). Compact sphere measure permits differentiation under this integral of every order, including right derivatives at zero; \(M(t,0)=4\pi\phi(t,0)\). For \(r>0\), the flux theorem in Boundary flux and weak identities, Theorem 2.1, and polar integration give
\[
\int_{|x|\le r}\Delta_x\phi(t,x)\,dx=r^2M_r(t,r).
\]
Differentiate in \(r\) using the FTC for the polar integral. Thus
\[
\int_{S^2}\Delta_x\phi(t,r\omega)\,d\omega
=M_{rr}(t,r)+\frac2rM_r(t,r).
\tag{5.0a}
\]
The factor \(r^2M_r\) tends to zero at zero because \(M_r\) is bounded.

Polar integration and Fubini now compute \(u(\Box\phi)\). The time part, integrated over \(r\le t<\infty\), is
\(-\int_0^\infty r^2M_t(r,r)\,dr\).
For the spatial part, integrate \(\partial_r(r^2M_r)\) over \(0<r<t\); it gives
\(-\int_0^\infty t^2M_r(t,t)\,dt\).
Every integral is absolutely convergent on bounded ranges determined by the test support. Their sum is
\[
-\int_0^\infty r^2\frac{d}{dr}M(r,r)\,dr
=2\int_0^\infty rM(r,r)\,dr.
\tag{5.0b}
\]
The upper boundary vanishes by compact support and the lower one by the factor \(r^2\). This proves exactly (5.2), with no missing vertex distribution.

One can also compute its next derivative directly. Applying (5.0a),
\[
v(\Box\phi)
=2\int_0^\infty
 \bigl[r(M_{tt}-M_{rr})-2M_r\bigr](r,r)\,dr.
\]
The integrand in brackets is the derivative of
\(J(r)=r(M_t-M_r)(r,r)-M(r,r)\).
Here \(J\) vanishes at infinity and \(J(0)=-4\pi\phi(0,0)\). The integral is therefore \(8\pi\phi(0,0)\), giving (5.1) for every test. \(\square\)

On \(t>0,r>0\), ordinary one-variable substitution at the simple positive root gives

\[
\delta(t^2-r^2)=\frac{\delta(t-r)}{2r}.
\tag{5.4}
\]

For clarity this means the integral of a test against the delta in the \(t\) variable; its substitution Jacobian is \(2r\). Consequently (5.2) can be denoted \(2\delta(t-r)/r\) away from the vertex. Formula (5.2), rather than a critical delta substitution, defines the measure through the vertex. If the test has \(r\le M\) on its support,

\[
|\langle v,\phi\rangle|\le4\pi M^2\|\phi\|_\infty .
\tag{5.5}
\]

Thus it is locally finite and positive. The mass with \(0<r<\varepsilon\) is \(4\pi\varepsilon^2\), so there is no atom at zero. Substitution in (5.2) gives degree \(-2\), agreeing with (4.2). Its second derivatives nevertheless contain the nonzero point source just proved.

**Example 5.2 (a speed changes the source weight).** For \(s>0\), put \(u_s=H(st-r)\), \(P_s=s^{-2}\partial_t^2-\Delta_x\). Apply the proved linear pullback with time factor \(s\):

\[
P_su_s=\frac{2\delta(st-r)}r,\qquad
P_s^2u_s=\frac{8\pi}{s}\delta_{(0,0)}.
\tag{5.6}
\]

The first formula is the measure

\[
\langle P_su_s,\phi\rangle
=\frac2s\int_0^\infty rM_s(r)\,dr,\qquad
M_s(r)=\int_{S^2}\phi(r/s,r\omega)\,d\omega.
\tag{5.7}
\]

The factor \(1/s\) is the time Jacobian. Hence the fundamental measure of \(P_s\) is \((s/(8\pi))P_su_s\), equivalently
\(s\delta(st-r)/(4\pi r)=\delta(t-r/s)/(4\pi r)\).

**Example 5.3 (a radial check of the vertex).** If \(\phi(t,x)=\eta(t)\psi(r)\), with both the time test and the radial spatial function compact and smooth, then

\[
\begin{gathered}
\langle v,\Box\phi\rangle=8\pi\int_0^\infty I(r)\,dr,\\
I(r)=r\eta''(r)\psi(r)-r\eta(r)\psi''(r)-2\eta(r)\psi'(r).
\end{gathered}
\tag{5.8}
\]

The primitive is \(r(\eta'\psi-\eta\psi')-\eta\psi\). It is zero at infinity and equals \(-\eta(0)\psi(0)\) at zero, giving \(8\pi\eta(0)\psi(0)\). The arbitrary-test calculation in Theorem 5.1 proves that this radial check has the same coefficient as the full distributional identity.

## Exercises

**Exercise 1 (basic: a weighted pulse with memory).** For \(h>0\), \(b\in\mathbb C\), put \(p=F_b-F_b(\cdot-h)\), \(q=F_b*p\). Find \(q\), verify \((\partial_x-b)q=p\), and determine whether its tail for \(x>h\) can vanish identically.

**Solution 1.** Translation of a factor translates its convolution, directly by changing the translated test variable in the proper convolution formula. Proposition 2.1 gives

\[
q(x)=xe^{bx}H(x)-(x-h)e^{b(x-h)}H(x-h).
\tag{6.1}
\]

Derivative transfer and \((\partial_x-b)F_b=\delta_0\) prove the equation including both endpoints. For \(x>h\),

\[
q(x)=e^{bx}\bigl[x-e^{-bh}(x-h)\bigr].
\tag{6.2}
\]

The exponential is nonzero. Its affine bracket could be identically zero only if \(1-e^{-bh}=0\) and \(he^{-bh}=0\), which is impossible. For \(b=0\) the tail is the constant \(h\); all other parameters retain the displayed affine exponential tail.

**Exercise 2 (basic: a differentiated point source).** Find the unique quadrant-supported solution of \(\partial_x^2\partial_y^3u=\partial_y\delta_{(0,0)}\), including its density and corner derivative.

**Solution 2.** Theorem 1.1 gives

\[
u=\partial_y(R_2\otimes R_3)=R_2\otimes R_2=x_+y_+.
\tag{6.3}
\]

Its stated derivative is \(\delta_0(x)\otimes\delta_0'(y)\), since the derivative orders are two and three. On a test it is \(-\partial_y\phi(0,0)\), which checks the sign. Formula (1.6) proves uniqueness for this derivative source.

**Exercise 3 (intermediate: a weighted finite window).** Find the causal convolution inverse of \(w(x)=e^{bx}1_{(0,a)}(x)\), for \(a>0\), \(b\in\mathbb C\), with every delta and delta derivative.

**Solution 3.** Since \(w=F_b-e^{ba}F_b(\cdot-a)\), put

\[
S=\sum_{j\ge0}e^{bja}\delta_{ja},\qquad U=(\partial_x-b)S.
\tag{6.4}
\]

These are locally finite sums. On a compact test, cancellation of consecutive coefficients proves \((\delta_0-e^{ba}\delta_a)*S=\delta_0\). Therefore

\[
w*U=F_b*(\partial_x-b)\delta_0=\delta_0 .
\tag{6.5}
\]

In full,

\[
U=\sum_{j\ge0}e^{bja}\bigl(\delta_{ja}'-b\delta_{ja}\bigr).
\tag{6.6}
\]

The weights are never zero. At each support point choose a test supported close to it with value zero and derivative nonzero; its pairing detects the delta derivative and cannot cancel with the delta. The support is exactly this unbounded discrete set. Multiplying any other causal inverse by \(U\) proves uniqueness. Exponential growth of the weights has no effect on local finiteness.

**Exercise 4 (intermediate: an ellipsoidal wave cone).** For any invertible real \(3\times3\) matrix \(B\), put \(G=BB^T\) and

\[
P_B=\partial_t^2-\sum_{i,j=1}^3G_{ij}\partial_{x_i}\partial_{x_j}.
\tag{6.7}
\]

Construct its fundamental measure supported in \(t\ge|B^{-1}x|\). Give an integral pairing including the vertex, and check \(B=\operatorname{diag}(2,1,3)\).

**Solution 4.** With \(E=\mathcal R_1=v/(8\pi)\), define

\[
E_B(t,x)=|\det B|^{-1}E(t,B^{-1}x)
\tag{6.8}
\]

by the linear pullback (4.0g). The chain rule (4.0h) gives the isotropic operator in \(y=B^{-1}x\), because \(B^{-1}GB^{-T}=I\). The spatial delta pullback has coefficient \(|\det B|\), canceled by (6.8). Hence \(P_BE_B=\delta_0\). Its complete pairing is

\[
\langle E_B,\phi\rangle
=\frac1{4\pi}\int_0^\infty rM_B(r)\,dr,\qquad
M_B(r)=\int_{S^2}\phi(r,Br\omega)\,d\omega.
\tag{6.9}
\]

The integral is locally finite and positive; its parameters lie on the claimed cone boundary. For the diagonal example \(G=\operatorname{diag}(4,1,9)\), \(|\det B|=6\) and \(|B^{-1}x|^2=x_1^2/4+x_2^2+x_3^2/9\). The coefficient in the pullback expression is \(1/6\); after the spatial substitution it is already absorbed in (6.9). Cone properness is preserved by this invertible linear map, so (1.7) also gives the corresponding causal uniqueness.

**Exercise 5 (intermediate: a smooth causal forcing).** For \(f\in C_c^\infty(\mathbb R^4)\) supported in \(C_+\), express the unique \(C_+\)-supported solution of \(\Box u=f\) by an ordinary integral and prove smoothness through the cone.

**Solution 5.** Let \(u=E*f\) with \(E=v/(8\pi)\). Inserting the cone pairing and then polar coordinates gives

\[
u(t,x)=\frac1{4\pi}\int_{\mathbb R^3}
                \frac{f(t-|y|,x-y)}{|y|}\,dy .
\tag{6.10}
\]

The integrand vanishes unless \(0\le|y|\le t\), since \(f\) is zero at negative time. On any compact set of \((t,x)\), choose a fixed upper bound \(T\) for positive time. The integrable function \(1_{\{|y|\le T\}}/|y|\) dominates the integral and each fixed derivative after multiplication by a bounded derivative of \(f\). Dominated differentiation proves \(C^\infty\) smoothness on a whole neighborhood, including across the cone and across \(t=0\). Proper convolution gives support in \(C_++C_+=C_+\); (1.7) gives the equation and uniqueness.

**Exercise 6 (advanced: an entire lower-order perturbation).** In three spatial dimensions and for every \(\lambda\in\mathbb C\), prove that

\[
T_\lambda=\mathcal R_1+
                \sum_{k=1}^{\infty}(-\lambda)^k\mathcal R_{k+1}
\tag{6.11}
\]

is a weakly entire causal fundamental solution of \(\Box+\lambda\). Find its added interior density and justify the source at the vertex.

**Solution 6.** The global recursion (4.2) telescopes in each finite sum:

\[
(\Box+\lambda)\sum_{k=0}^N(-\lambda)^k\mathcal R_{k+1}
=\delta_0+(-1)^N\lambda^{N+1}\mathcal R_{N+1}.
\tag{6.12}
\]

For \(k\ge1\), the initial integrable formula applies and the Gamma recurrence gives

\[
\mathcal R_{k+1}
=\frac{H(t-r)q^{k-1}}{2^{2k+1}\pi\,k!(k-1)!}.
\tag{6.13}
\]

Thus the additional density is

\[
H(t-r)\sum_{k=1}^{\infty}a_k(\lambda)q^{k-1},
\qquad
a_k(\lambda)=\frac{(-\lambda)^k}{2^{2k+1}\pi\,k!(k-1)!}.
\tag{6.14}
\]

On a compact spacetime set with \(t\le M\), put \(L=\max(1,M^2)\). In the cone \(0\le q\le M^2\). For \(|\lambda|\le A\), the terms are bounded by \(A^kL^{k-1}/(2^{2k+1}\pi k!(k-1)!)\). The ratio tends to zero; inserting any fixed polynomial in \(k\) still gives convergence. Taking \(\max(1,A)\) also bounds every fixed parameter derivative, including at zero. Thus the interior series converges as a locally bounded density with entire test pairings. The first term \(\mathcal R_1\) is the fixed cone measure.

For \(N\ge1\), the remainder in (6.12) has density bounded on this set by

\[
\frac{A^{N+1}L^{N-1}}{2^{2N+1}\pi\,N!(N-1)!},
\tag{6.15}
\]

which tends to zero. Differentiation of distributions tests fixed derivatives, so it commutes with the convergent series. Passing to the limit in (6.12) proves the complete equation including the vertex. Every term has cone support, and so does the limit. Formula (1.7) proves uniqueness for causal sources and solutions. At \(\lambda=0\) the kernel is \(E\), with no branch choice for a square root.

**Exercise 7 (advanced: a source stopped after a delay).** In one and three spatial dimensions, subtract from the unit-speed causal fundamental kernel its time translate by \(h>0\). Determine the source, spatial support for \(t>h\), total spatial mass, and signs.

**Solution 7.** Write \(V_h=E(t,x)-E(t-h,x)\). Translation of the distribution identity gives

\[
\Box V_h=\delta_{(0,0)}-\delta_{(h,0)}.
\tag{6.16}
\]

In one dimension, for \(t>h\), the density is \(1/2\) on \(t-h<|x|<t\). Its spatial support is the closed pair of intervals with these endpoints and its mass is \(h\). For \(0<t<h\) its support is \([-t,t]\) and its mass is \(t\).

In three dimensions define the spatial measure, for each \(t>0\), by

\[
\langle E(t,\cdot),\psi\rangle
=\frac{t}{4\pi}\int_{S^2}\psi(t\omega)\,d\omega .
\tag{6.17}
\]

Integrating this pairing in \(t\) recovers the full cone measure (5.2) divided by \(8\pi\); thus these are specified spatial slices, not an assumed restriction theorem. For \(t>h\), subtract the formula with \(t-h\). The outer sphere of radius \(t\) has positive measure and the inner sphere of radius \(t-h\) has negative measure. Every open patch on either sphere has positive Euclidean area, so tests localized near one patch show both its nonzero support and the inner negative sign. The support is exactly the union of the two spheres. A cutoff equal to one on both gives mass \(t-(t-h)=h\). For \(0<t<h\) the mass is \(t\); at negative time both measures are zero. Equal total mass therefore does not imply identical geometry or positivity.

**Exercise 8 (advanced: two drifts and a complex potential).** For \(a,b,d\in\mathbb C\), find the quadrant-supported fundamental solution of

\[
P=\partial_x\partial_y-a\partial_x-b\partial_y+d
\tag{6.18}
\]

and verify all edge and corner terms.

**Solution 8.** Set \(c=ab-d\), \(M(x,y)=e^{bx+ay}\), and define

\[
E=M H(x)H(y)F(cxy).
\tag{6.19}
\]

The distribution product rule (proved on tests as in (2.3)) gives

\[
\begin{aligned}
M^{-1}P(MT)
={}&(\partial_x+b)(\partial_y+a)T\\
&-a(\partial_x+b)T-b(\partial_y+a)T+dT\\
={}&(\partial_x\partial_y-c)T.
\end{aligned}
\tag{6.20}
\]

Apply Theorem 3.1: \(PE=M\delta_0=\delta_0\). For the individual boundary terms, (3.7) gives zero pure edge derivatives for \(F(cxy)\). Differentiating \(M\) creates the factors \(a\) on the \(x=0\) edge and \(b\) on the \(y=0\) edge; the terms \(-a\partial_x\) and \(-b\partial_y\) cancel them. The corner is \(M(0,0)F(0)=1\), and the interior remainder is zero by \(c=ab-d\) and (3.2). Formula (1.7) proves uniqueness. If \(ab=d\), then \(c=0\) and \(E=e^{bx+ay}H(x)H(y)\), still with exactly the same unit corner source.

## Programme proof locations and freely accessible sources

The lesson uses the complete supplied tensor, convolution, causal-power, beta and identity proofs named at its beginning. [Scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 13.1–13.5 and 13.7–13.10, supplies FTC, finite differentiation, exponential identities and smooth cutoffs. [Measure foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.4 and 16.1–16.2, proves Tonelli, Fubini, convergence, linear substitution and local approximation. The [finite algebra proofs](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), Section 10, supply inverses and determinants. The [Schwartz foundations](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1, gives the seminorms used for temperedness; its F3 and the angular companion A5 prove the Gaussian constant. Each supplied prerequisite retains its stated licence.

- [Christian Bär, Nicolas Ginoux and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, freely accessible author manuscript, arXiv:0806.1036v1](https://arxiv.org/pdf/0806.1036), Section 1.2, Definition 1.2.1, Lemma 1.2.2 and Proposition 1.2.4, printed pp. 10–17. Their total dimension is \(n+1\) in this lesson and their parameter is \(2\lambda\). Lemma 4.0 supplies the full construction, all scalar normalization proofs and the coordinate-annihilation argument locally.
- [Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, October 2, 2026](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), Proposition 9.11 and its proof, and Section 10.2, Theorem 10.14's three-dimensional construction. The characteristic-coordinate calculation and cone measure motivate the corresponding proofs here; Theorem 5.1 computes both cone derivatives directly for arbitrary compact tests, including the vertex.
