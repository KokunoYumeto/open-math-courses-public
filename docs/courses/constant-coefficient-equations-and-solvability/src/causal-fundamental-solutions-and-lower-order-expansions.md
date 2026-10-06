# Causal fundamental solutions and lower order expansions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A hyperbolic root barrier yields an actual causal inverse. We construct it by moving Fourier integration lines, prove its support and weighted regularity, and determine its smallest closed convex supporting cone. Lower order terms then give a convergent expansion in principal-power kernels, with a quantitative tail in the local Fourier norm.

Read [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md), [Causal solvability forces hyperbolicity](causal-solvability-forces-hyperbolicity.md), [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md), and [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md). We use their full cone transport, homogeneous-component ratios, causal-necessity theorem, shifted derivative estimate, cutoff theorem and compact weighted-convolution bound.

We also use Fourier inversion on Schwartz functions and tempered distributions, polynomial factorization, Cauchy's theorem, integration by parts and finite-dimensional convex separation. For distributions on independent variables, their tensor product is the iterated test pairing, has the product of their supports, and commutes with differentiation in either variable. This is Theorem 2.1 and Corollary 2.2 of *Tensor products and parameter-dependent distributions*. Theorem 1.1 of *Convolution as addition of supports* gives convolution when addition is proper on the supports; Theorem 2.1 gives smoothing by a compact smooth factor. We prove the required cone geometry below. The characteristic-halfspace entry is stated in *Causal solvability forces hyperbolicity*. The finite Taylor-jet proof for point-supported distributions is in [The wave Cauchy problem and Kirchhoff's formula](flat-wave-cauchy-and-kirchhoff.md), Lemma 2.

We use \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\), inverse factor \((2\pi)^{-n}\), and \(D=-i\partial\). The positive moderate weight \(S_P\) is the derivative-vector norm of the polynomial. All lower order coefficients may be complex.

Assume first that \(P\ne0\) has degree \(m\ge1\), is hyperbolic in the real direction \(N\ne0\), and write \(F=P_m\). Put
\[
\begin{gathered}
\Gamma=\Gamma(F,N),\\
C=\Gamma^*=
\{a:a\cdot\theta\ge0\text{ for every }\theta\in\Gamma\},\\
H_N=\{x:N\cdot x\ge0\}.
\end{gathered}
\]
The scalar case is dealt with explicitly at the end of the full lower order expansion and the flat Cauchy problem. Complex lower order coefficients are allowed throughout.

## Cone geometry and proper convolution

Since \(N\) is interior to the open convex cone \(\Gamma\), there is \(b>0\) with \(B(N,2b)\subset\Gamma\). For \(a\in C\), choose \(\theta=N-b a/|a|\) when \(a\ne0\). Then
\[
N\cdot a\ge b|a|\qquad(a\in C).
\tag{1}
\]
Thus \(C\) is closed, convex, pointed and contained in \(H_N\), with no nonzero point on its boundary plane.

Addition is proper on \(C\times H_N\). Indeed, if \(a\in C\), \(z\in H_N\), and \(a+z\) lies in a fixed compact set \(K\), then
\[
\begin{gathered}
0\le b|a|\le N\cdot a\le N\cdot(a+z)\le T,\\
T=\max_{w\in K}N\cdot w.
\end{gathered}
\]
If \(T<0\), there is no such pair. Otherwise both \(|a|\le T/b\) and \(|z|\le\max_K|w|+T/b\) are bounded. The set of pairs is closed, hence compact. The same argument applies to any closed cone \(K_0\) satisfying \(N\cdot a>0\) for all \(a\in K_0\setminus\{0\}\): compactness of \(K_0\cap S^{n-1}\) gives (1) for that cone. If \(K_0=\{0\}\), properness is immediate.

For distributions \(A,B\) supported respectively in such a cone and \(H_N\), apply the convolution theorem in *Convolution as addition of supports*, Theorem1.1, to the proper pair just proved. Its canonical formula is
\[
\langle A*B,\phi\rangle
=\langle A\otimes B,\chi(a,z)\phi(a+z)\rangle.
\tag{2}
\]
Here \(\chi\in C_c^\infty\) equals one near the compact part of \(\operatorname{supp}A\times\operatorname{supp}B\) over \(\operatorname{supp}\phi\). The imported theorem gives cutoff independence, distributional continuity and
\[
\begin{aligned}
Q(D)(A*B)&=(Q(D)A)*B\\
&=A*(Q(D)B).
\end{aligned}
\tag{3}
\]
It also gives support contained in the closed sum \(\operatorname{supp}A+\operatorname{supp}B\). No temperedness or bound at infinity on \(B\) is required. The cone bound (1) identifies the compact input regions needed for every output compact; it is the geometry we will use throughout the causal construction.

## Construct the regular causal kernel

Choose a barrier \(\tau_0\) with \(P(\xi+i\tau N)\ne0\) for every real \(\xi\), \(\tau<\tau_0\). For fixed \(\xi\), the degree-\(m\) polynomial in \(z\)
\[
P(\xi+izN)=i^mF(N)\prod_{\nu=1}^m(z-z_\nu)
\]
has \(\operatorname{Re}z_\nu\ge\tau_0\). This follows by absorbing the real vector \(-\operatorname{Im}z_\nu N\) into \(\xi\). Therefore
\[
\begin{gathered}
|P(\xi+i\tau N)|\ge |F(N)|(\tau_0-\tau)^m,\\
\tau<\tau_0.
\end{gathered}
\tag{4}
\]
For such a fixed \(\tau\), define
\[
\begin{gathered}
\langle E_\tau,\phi\rangle\\
=(2\pi)^{-n}\int_{\mathbb R^n}
\frac{\widehat\phi(-\xi-i\tau N)}{P(\xi+i\tau N)}\,d\xi,\\
\phi\in C_c^\infty.
\end{gathered}
\tag{5}
\]
The signs in both numerator and denominator are part of the formula.

For a test supported in a fixed compact \(K\), integrations by parts against the real Fourier variable give, for every integer \(L\),
\[
\begin{aligned}
&|\widehat\phi(-\xi-i\eta)|\\
&\quad\le C_{K,L}(1+|\eta|)^{2L}(1+|\xi|^2)^{-L}\\
&\qquad{}\cdot e^{\sup_{x\in K}(-x\cdot\eta)}
\sum_{|\alpha|\le2L}\sup_K|\partial^\alpha\phi|.
\end{aligned}
\tag{6}
\]
To see this, apply \(1-\Delta_x\) repeatedly to \(e^{-x\cdot\eta}\phi(x)\), whose derivatives have the displayed polynomial factors, and use its fixed compact support. Taking \(2L>n\), (4) proves absolute convergence and a continuous test-function bound for (5). Thus \(E_\tau\in\mathcal D'\).

Let \(G_\tau=\mathcal F^{-1}(1/P(\xi+i\tau N))\), a tempered distribution because the multiplier is bounded. Formula (5) says exactly
\[
E_\tau=e^{-\tau N\cdot x}G_\tau.
\tag{7}
\]
Indeed the Fourier transform of \(e^{-\tau N\cdot x}\phi(x)\), evaluated at \(-\xi\), is \(\widehat\phi(-\xi-i\tau N)\). Hence
\[
\begin{aligned}
P(D)E_\tau
&=e^{-\tau N\cdot x}P(D+i\tau N)G_\tau\\
&=e^{-\tau N\cdot x}\delta=\delta.
\end{aligned}
\tag{8}
\]
This also follows by applying (5) to \(P(-D)\phi\): the numerator acquires \(P(\xi+i\tau N)\) and Fourier inversion gives \(\phi(0)\).

The distributions \(E_\tau\) do not depend on the choice of \(\tau<\tau_0\). Align one real Fourier coordinate with \(N\). For two fixed permitted \(\tau\)'s, Cauchy's theorem moves that coordinate between the two parallel lines. On the whole finite strip, (4) has a uniform positive lower bound. The numerator has arbitrarily rapid real-frequency decay by (6), uniformly on that finite strip. After integrating the other \(n-1\) real coordinates, a vertical side at real coordinate \(\pm R\) is bounded by a constant times \(R^{n-1-2L}\), hence tends to zero for sufficiently large \(L\). Fubini is justified by the same integrable bound. The horizontal limits give equality of (5). Denote the common distribution by \(E\).

If \(\operatorname{supp}\phi\subset\{N\cdot x<0\}\), compactness gives \(N\cdot x\le-a<0\) there. Formula (6), with \(\eta=\tau N\) and \(\tau\to-\infty\), bounds (5) by
\[
C(1+|\tau|)^{2L}(\tau_0-\tau)^{-m}e^{-a|\tau|},
\]
which tends to zero. Thus \(\operatorname{supp}E\subset H_N\).

To obtain the full cone, fix \(\theta\in\Gamma\). The two-parameter exclusion in *Hyperbolicity and lower order terms* gives
\[
\begin{gathered}
P(\xi+i\tau N+i\sigma\theta)\ne0,\\
\operatorname{Re}\tau<\tau_0,\quad
\operatorname{Re}\sigma\le0.
\end{gathered}
\tag{9}
\]
For fixed real \(\sigma\le0\), factor this polynomial in \(\tau\). Its leading coefficient is still \(i^mF(N)\), and every root has real part at least \(\tau_0\), by (9). Consequently (4) holds with the same lower bound after inserting \(i\sigma\theta\). Moving the line along \(\theta\), with \(\tau\) fixed and \(\sigma\) in a finite negative interval, is legitimate by the rectangle argument just proved. We obtain
\[
\begin{gathered}
\langle E,\phi\rangle\\
=(2\pi)^{-n}\int
\frac{\widehat\phi(-\xi-i\tau N-i\sigma\theta)}
{P(\xi+i\tau N+i\sigma\theta)}\,d\xi,\\
\sigma\le0.
\end{gathered}
\tag{10}
\]
For a test supported in \(\{\theta\cdot x<0\}\), let \(\sigma\to-\infty\). Its compact support makes the numerator exponentially small, up to a polynomial in \(|\sigma|\), while the denominator retains the fixed positive lower bound. Hence \(E\) annihilates this test. This proves
\[
\operatorname{supp}E\subset C.
\tag{11}
\]

We also prove the claimed regularity. Fix \(\tau<\tau_0\) and choose \(a>0\) with \(\tau+a<\tau_0\). For sufficiently small real \(\eta\), \(aN-\eta\in\Gamma\). In (9) use the parameters \(\tau+a\), \(\sigma=-1\), and direction \(aN-\eta\). It follows that
\[
P(\xi+i\tau N+i\eta)\ne0
\]
uniformly in real \(\xi\), for \(|\eta|\) in a fixed ball. The real part of an additional complex shift is absorbed into \(\xi\), so \(B(w)=P(w+i\tau N)\) has a uniformly positive complex-zero distance at every real \(w=\xi\). *Hypoellipticity and complex zeros* Lemma1.1 therefore bounds all its derivative ratios. Fixed complex translation is an invertible finite Taylor matrix on the derivative vector, giving
\[
S_P(\xi)\le C_\tau |P(\xi+i\tau N)|.
\tag{12}
\]
Thus \(G_\tau\in B_{\infty,S_P}\). For any compact smooth \(\chi\), the function \(\chi e^{-\tau N\cdot x}\) is a compact smooth multiplier; *Measuring regularity with weighted Fourier spaces* Theorem4.1 and (7) imply
\[
E\in B_{\infty,S_P}^{\mathrm{loc}}.
\tag{13}
\]
This is the regular fundamental solution assertion. Formula (5) is an actual distributional construction, not a purely formal inverse.

## Uniqueness, the cone converse and minimality

If \(V\in\mathcal D'\) is supported in \(H_N\), (1)–(3) make \(E*V\) legitimate. In particular,
\[
\begin{aligned}
E*(P(D)V)&=(P(D)E)*V\\
&=\delta*V=V.
\end{aligned}
\tag{14}
\]
Hence there is at most one fundamental solution supported in \(H_N\), since the difference of two such solutions has zero image and (14) makes it zero. This proof imposes no growth condition.

Conversely, suppose an arbitrary fundamental solution \(A\) is supported in a closed cone \(K_0\) with \(M\cdot a>0\) for every \(a\in K_0\setminus\{0\}\), where \(M\ne0\). Properness was proved in the cone geometry. If \(P_m(M)=0\), the characteristic-halfspace entry in *Causal solvability forces hyperbolicity* supplies a nonzero smooth homogeneous solution \(V\) supported in \(H_M\); but
\[
V=A*(P(D)V)=0,
\]
a contradiction. Thus \(P_m(M)\ne0\). For every compact smooth \(f\) supported in \(H_M\), \(A*f\) is a smooth causal solution. Compact convolution with a distribution is smooth by differentiation of translated tests; its support lies in \(K_0+\operatorname{supp}f\subset H_M\). The causal-necessity theorem proved in *Causal solvability forces hyperbolicity* now gives hyperbolicity in direction \(M\). This proves the full closed-cone converse, including cones that are not convex.

For minimality, first note that \(E\) cannot be point supported when \(m\ge1\). The finite Taylor-jet proof in *The wave Cauchy problem and Kirchhoff's formula* makes such an \(E\) a finite sum of delta derivatives, with a polynomial Fourier transform \(R\). The identity \(P(D)E=\delta\) would imply \(P R=1\); degrees make this impossible for positive-degree \(P\).

Let \(L\) be any closed convex cone containing \(\operatorname{supp}E\). Put \(K=L\cap C\), which still contains that support, is nonzero, and satisfies (1). Its strict polar is
\[
\Omega=\{\theta:\theta\cdot a>0\text{ for all }a\in K\setminus\{0\}\}.
\]
It is nonempty, open and convex, contains \(N\), and does not contain zero. Openness follows from the positive minimum on \(K\cap S^{n-1}\). For every \(\theta\in\Omega\), the cone converse makes \(P\) hyperbolic in direction \(\theta\), in particular \(F(\theta)\ne0\). Connectedness therefore implies \(\Omega\subset\Gamma\).

The closed positive polar \(K^*\) is the closure of \(\Omega\): if \(\theta\in K^*\), then \(\theta+\varepsilon N\in\Omega\) for \(\varepsilon>0\), by (1). Finite-dimensional separation gives \(K=(K^*)^*=\Omega^*\). Since \(\Omega\subset\Gamma\),
\[
C=\Gamma^*\subset\Omega^*=K\subset L.
\tag{15}
\]
Together with (11), this proves that the smallest closed convex cone containing the support of \(E\) is exactly \(C\). It does not assert that the support fills every point of that cone.

## The full lower order expansion

Put \(Q=F-P\). For \(k\ge0\), let \(E_k\) be the unique causal fundamental solution for \(F(D)^{k+1}\). Its hyperbolicity cone is the same \(\Gamma\), because \(\{F^{k+1}\ne0\}=\{F\ne0\}\); the kernel construction therefore constructs it with support in \(C\). Properness gives the optional identity
\[
E_k=E_0^{*(k+1)}.
\]
Indeed the convolution power is supported in \(C\) and its image under \(F(D)^{k+1}\) is \(\delta\), so uniqueness applies.

Apply the homogeneous-component ratio bounds of *Hyperbolicity and lower order terms* in direction \(-N\). For \(s=|\tau|\ge1\), \(\tau=-s\), homogeneity gives
\[
\begin{aligned}
\frac{|P_j(\xi+i\tau N)|}{|F(\xi+i\tau N)|}
&=s^{j-m}\frac{|P_j(\xi/s-iN)|}{|F(\xi/s-iN)|}\\
&\le C_j s^{j-m}.
\end{aligned}
\]
Thus
\[
\rho_\tau:=\sup_{\xi\in\mathbb R^n}
\left|\frac{Q(\xi+i\tau N)}{F(\xi+i\tau N)}\right|
\le\frac{C}{|\tau|}.
\tag{16}
\]
Choose one negative \(\tau\) below the barrier for \(P\) and so large in absolute value that \(\rho_\tau<1\). For this single fixed \(\tau\),
\[
\begin{aligned}
&\frac1{P(\xi+i\tau N)}\\
&\qquad=\sum_{k=0}^\infty
\frac{Q(\xi+i\tau N)^k}{F(\xi+i\tau N)^{k+1}}.
\end{aligned}
\tag{17}
\]
The shifted derivative estimate for \(F\), proved in the kernel construction, is
\(S_F(\xi)\le A_\tau |F(\xi+i\tau N)|\). Therefore the tail after term \(K\), multiplied by \(S_F(\xi)\), has absolute value at most
\[
A_\tau\frac{\rho_\tau^{K+1}}{1-\rho_\tau}
\tag{18}
\]
uniformly in \(\xi\).

For every \(k\), the tempered transform of \(e^{\tau N\cdot x}E_k\) is \(F(\xi+i\tau N)^{-k-1}\), by the kernel construction. Conjugating the differential operator gives
\[
\mathcal F\!\left(e^{\tau N\cdot x}Q(D)^kE_k\right)
=\frac{Q(\xi+i\tau N)^k}{F(\xi+i\tau N)^{k+1}}.
\]
Equations (17)–(18) prove convergence in the global \(B_{\infty,S_F}\) norm after this exponential conjugation. Multiplication by \(\chi e^{-\tau N\cdot x}\), for any compact smooth \(\chi\), is bounded in that norm. Consequently
\[
\begin{gathered}
E=\sum_{k=0}^\infty(F(D)-P(D))^kE_k,\\
\text{convergence in }B_{\infty,S_F}^{\mathrm{loc}}.
\end{gathered}
\tag{19}
\]
Its limit is exactly the kernel of the kernel construction by its conjugated Fourier transform. Each term is supported in \(C\), as is the limit. The quantitative norm tail proves the full expansion in the stated topology.

There is also a useful homogeneous interpretation. Write \(r=(k+1)m\). For \(\lambda>0\), the distribution \(\lambda^{n-r}E_k(\lambda\cdot)\) is another fundamental solution of \(F(D)^{k+1}\) supported in \(C\): scaling produces \(\lambda^r\delta(\lambda\cdot)=\lambda^{r-n}\delta\). Uniqueness gives
\[
E_k(\lambda\cdot)=\lambda^{-n+(k+1)m}E_k.
\tag{20}
\]
These homogeneous distributions are tempered. On an annulus, finite distribution order bounds their pairing by finitely many test derivatives. A dyadic partition outside the unit ball and (20) bound the annulus at radius \(2^\ell\) by \(C2^{\ell(r+q)}\) times finitely many Schwartz derivatives there, for some finite \(q\). Arbitrarily rapid Schwartz decay makes the sum converge. The part near zero is bounded by finite distribution order on a compact set.

In this convention
\[
\begin{gathered}
\widehat E_k=\lim_{s\downarrow0}F(\xi-isN)^{-k-1}\\
=F(\xi-i0N)^{-k-1},\\
\text{convergence in }\mathcal S'.
\end{gathered}
\tag{21}
\]
To justify the limit, use (1) to choose a smooth cutoff equal to one near \(C\), supported, outside a bounded ball, in \(N\cdot x\ge (b/2)|x|\). On this larger cone, derivatives of \(e^{-sN\cdot x}\), \(0<s\le1\), satisfy uniform polynomial multiplier bounds, since \(s^j e^{-s b|x|/2}\le C_j(1+|x|)^{-j}\) outside the ball. Multiplying a Schwartz test by that cutoff and the exponential converges in the Schwartz topology to the cutoff times the test. Temperedness and support of \(E_k\) give \(e^{-sN\cdot x}E_k\to E_k\) in \(\mathcal S'\). The kernel construction identifies the transforms, proving (21).

A homogeneous component of degree \(d\) in \(Q^k\) gives a term in (19) of degree
\[
-n+(k+1)m-d,\qquad 0\le d\le k(m-1).
\]
Every nonzero such term has degree between \(-n+m+k\) and \(-n+(k+1)m\). Hence only finitely many terms can have any one fixed homogeneity degree. These are the homogeneity degrees and the distributional boundary value.

If \(m=0\), \(P=F\ne0\), \(Q=0\), \(\Gamma=\mathbb R^n\), \(C=\{0\}\), and \(E=P^{-1}\delta\). The cone converse and minimality are immediate. All positive-\(k\) terms in (19) vanish; \(E_k=P^{-k-1}\delta\) if those constant-power kernels are desired. No strict-root or positive-degree cone assertion is assigned to this case.

## Arbitrary causal distributions and the local weight gain

For every \(f\in\mathcal D'(\mathbb R^n)\) with \(\operatorname{supp}f\subset H_N\), the cone geometry makes
\[
u=E*f
\tag{22}
\]
a distribution, supported in \(H_N\), with \(P(D)u=f\). Conversely, every distributional solution supported in \(H_N\) satisfies (14), hence equals (22). This proves existence and uniqueness in the full distribution class.

Let \(1\le p\le\infty\), let \(k\) be a moderate weight as in *Measuring regularity with weighted Fourier spaces*, and suppose \(f\in B_{p,k}^{\mathrm{loc}}\). Fix a compact output neighborhood. Properness gives a compact set of relevant pairs \((a,z)\in\operatorname{supp}E\times\operatorname{supp}f\). Choose independent smooth compact cutoffs \(\chi(a)\), \(\psi(z)\), each equal to one near the respective projections of those pairs. On that neighborhood,
\[
u=(\chi E)*(\psi f).
\]
The first factor is in \(B_{\infty,S_P}\) by (13); the second is in \(B_{p,k}\). Their compact convolution satisfies
\[
\begin{aligned}
&\|(\chi E)*(\psi f)\|_{p,S_Pk}\\
&\qquad\le\|\chi E\|_{\infty,S_P}\|\psi f\|_{p,k}.
\end{aligned}
\tag{23}
\]
by *Measuring regularity with weighted Fourier spaces* Theorem4.2, with its normalization \((2\pi)^{-n/p}\). Multiplying by a further output cutoff is bounded by *Measuring regularity with weighted Fourier spaces* Theorem4.1. Consequently
\[
\begin{gathered}
f\in B_{p,k}^{\mathrm{loc}},\quad
\operatorname{supp}f\subset H_N\\
\Longrightarrow\quad
u\in B_{p,S_Pk}^{\mathrm{loc}}.
\end{gathered}
\tag{24}
\]
The proof includes \(p=1,\infty\), nonradial weights, noncompact forcing and arbitrary distributional growth. The same argument applies to forcing supported in any translate of \(H_N\), or in another closed set with proper addition by \(C\). The compact pairing regions give the stated local gain.

## Exercises with complete solutions

**Exercise 1 (introductory: the signs of a first-order kernel).** For \(P(D)=D_t-ia\), \(a\in\mathbb C\), construct the positive-time kernel, identify a permitted root barrier, and compute its series in principal-power kernels. Explain why a global temperedness assumption would discard legitimate kernels.

**Solution.** Since \(D_t=-i\partial_t\),
\[
E(t)=i1_{\{t\ge0\}}e^{-at}
\]
satisfies \((D_t-ia)E=-i(\partial_t+a)(i1_{\{t\ge0\}}e^{-at})=\delta\). The polynomial root is \(ia\), with imaginary part \(\operatorname{Re}a\), so any \(\tau_0\le\operatorname{Re}a\) is a barrier. For \(\tau<\operatorname{Re}a\),
\[
\mathcal F(e^{\tau t}E)(\xi)
=\frac{i}{a-\tau+i\xi}
=\frac1{\xi+i\tau-ia}.
\]
The principal polynomial is \(F(\xi)=\xi\), and \(Q=ia\). The kernel of \(D_t^{k+1}\) is \(E_k=i^{k+1}1_{\{t\ge0\}}t^k/k!\). Therefore
\[
Q^kE_k=i\,1_{\{t\ge0\}}\frac{(-at)^k}{k!},
\]
and the sum is the displayed \(E\). The full lower order expansion proves convergence in the local weighted norm as well as distributionally. For \(a=-1\), the kernel grows like \(e^t\); pairing it with a fixed nonnegative bump translated to \(R\) grows like \(e^R\), whereas the finite Schwartz seminorms of that translated bump grow at most polynomially in \(R\). Thus \(E\notin\mathcal S'\), although its sufficiently negative exponential conjugate is tempered and it is a valid regular causal kernel.

**Exercise 2 (introductory: powers and homogeneity).** Find the positive-time kernel for \(D_t^m\), \(m\ge1\), and the kernel for its \((k+1)\)-st power. Check the exact homogeneous degree and the sign in its Fourier boundary value.

**Solution.** The identity \(\partial_t^r(1_{\{t\ge0\}}t^{r-1}/(r-1)!)=\delta\), \(r\ge1\), follows by \(r\) integrations by parts. Thus
\[
\begin{gathered}
E_0=i^m1_{\{t\ge0\}}\frac{t^{m-1}}{(m-1)!},\\
E_k=i^{m(k+1)}1_{\{t\ge0\}}
\frac{t^{m(k+1)-1}}{(m(k+1)-1)!}.
\end{gathered}
\]
For positive dilation these have degree \(m(k+1)-1\), the value \(-n+(k+1)m\) for \(n=1\). Their tempered exponentially damped transforms are \((\xi-is)^{-m(k+1)}\), \(s>0\), so their boundary values are \((\xi-i0)^{-m(k+1)}\). The opposite sign would give the negative-time support and would not satisfy the positive-time support condition.

**Exercise 3 (intermediate: a minimal cone can contain holes in the support).** Determine the dual cone for \(F(\tau,\eta)=\tau^2-|\eta|^2\) and its future time direction. In spacetime dimension four, compare the minimal convex support cone with the actual support of the principal kernel.

**Solution.** The principal cone is \(\Gamma=\{(\theta_t,\theta_y):\theta_t>|\theta_y|\}\). If \(x=(t,y)\) has \(t\ge|y|\), then \(x\cdot\theta\ge t\theta_t-|y||\theta_y|\ge0\) for every \(\theta\in\Gamma\). If \(t<0\), take \(\theta_y=0\). If \(0\le t<|y|\), choose \(\theta_y\) opposite to \(y\), with \(|\theta_y|/\theta_t\) sufficiently close to one, to make the pairing negative. Hence
\[
C=\{(t,y):t\ge|y|\}.
\]
In dimension four, \(P(D)=-\partial_t^2+\Delta_y\) is the negative of the unit-speed wave operator. *The wave Cauchy problem and Kirchhoff's formula*'s Kirchhoff kernel therefore gives its kernel as
\[
E(t,y)=-\frac{\delta(t-|y|)}{4\pi|y|}.
\]
Its support is the future null cone, including its vertex, and contains no point in \(t>|y|\). Every point of the solid future cone is a nonnegative combination of future null vectors: for \(y\ne0\), combine \((|y|,y)\) with equal opposite null vectors to supply the excess time; for \(y=0\), use two opposite null vectors. Thus the closed convex cone generated by the actual support is exactly \(C\). Minimal convex support does not mean that the kernel is nonzero throughout the interior.

**Exercise 4 (intermediate: local cutoffs for noncompact forcing).** Assume \(|N|=1\) and \(N\cdot a\ge b|a|\) on \(C\). For outputs in \(B(0,R)\), give explicit bounds on the convolution variables for \(E*f\), when \(f\) is supported in \(H_N\). Derive the local \(B_{p,k}\)-gain for both endpoints.

**Solution.** If \(x=a+z\), \(|x|\le R\), \(a\in C\), \(z\in H_N\), then \(b|a|\le N\cdot a\le N\cdot x\le R\), so
\[
|a|\le R/b,\qquad |z|\le R+R/b.
\]
Take \(\chi=1\) near the first closed ball and \(\psi=1\) near the second, with slightly larger compact supports. Then \(E*f=(\chi E)*(\psi f)\) on \(B(0,R)\). If \(\eta\) is an output cutoff supported in that ball, *Measuring regularity with weighted Fourier spaces* gives
\[
\|\eta(E*f)\|_{p,S_Pk}
\le A_{S_Pk}(\eta)\|\chi E\|_{\infty,S_P}\|\psi f\|_{p,k}.
\]
The compact Fourier transforms multiply, so the bound is the ordinary multiplication bound \(L^\infty\cdot L^p\to L^p\). It is valid for \(p=1,\infty\); no density of compact tests in a global \(B_{\infty,k}\) norm is needed.

## References

The full complex cone exclusion and homogeneous strength ratios are proved in [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md). The converse uses [Causal solvability forces hyperbolicity](causal-solvability-forces-hyperbolicity.md), including its stated characteristic-halfspace entry. The derivative-ratio estimate is Lemma 1.1 of [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md). The cutoff and weighted-convolution estimates are Theorems 4.1–4.2 of [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md). Point-support jets and the Kirchhoff example are proved in [The wave Cauchy problem and Kirchhoff's formula](flat-wave-cauchy-and-kirchhoff.md).

Tensor and parameter pairing are Lemma 1.1, Theorem 2.1 and Corollary 2.2 of [Tensor products and parameter-dependent distributions](../prerequisites/tensor-products-and-parameters.html). Proper-support convolution and smoothing are Theorems 1.1 and 2.1 of [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html). Both lessons use CC0-1.0.
