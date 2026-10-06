# Small Gevrey solutions of the full Cauchy problem

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The sublinear imaginary-root growth is absorbed by small-Gevrey Fourier decay. We construct solutions with arbitrary data and forcing, including the endpoint, and then prove finite-speed uniqueness and local stabilization.

Read [Principal roots and uniform time kernels](principal-roots-and-time-kernels.md), [Small Gevrey classes and compact Fourier decay](small-gevrey-and-compact-fourier-decay.md), [Compact Cauchy data and local coherence](compact-cauchy-data-and-local-coherence.md).

One prerequisite remains planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html): a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface vanishes near that surface. The uses of this Holmgren theorem below are conditional on that planned proof.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs below use the linked prerequisite lessons and the stated planned results.

## The full statement and normal convention

**Theorem.** Let \(P\) be of order \(m\ge1\) and let its principal part be hyperbolic with respect to a nonzero real \(N\). If
\[
 1<\delta\le\frac{m}{m-1},
 \tag{1}
\]
then, for every \(f\in\gamma^{(\delta)}(\mathbb R^n)\) and every \(\phi_k\in\gamma^{(\delta)}(\Sigma)\), \(0\le k<m\), there is a solution \(u\in\gamma^{(\delta)}(\mathbb R^n)\) of
\[
\begin{gathered}
P(D)u=f,\\
\qquad
 \langle D,N\rangle^k u|_\Sigma=\phi_k,\\
\qquad
 \Sigma=\{x:x\cdot N=0\}.
\end{gathered}
\tag{2}
\]
For \(m=1\), the upper endpoint means infinity. The solution is unique among global \(C^m\) solutions, relative to the declared Holmgren input, and no growth condition is imposed.

Choose orthogonal coordinates \((y,t)\) with \(t=x\cdot N/|N|\). Then \(\langle D,N\rangle=|N|D_t\), so the prescribed \(D_t\)-data are \(g_k=|N|^{-k}\phi_k\). Hyperbolicity is invariant under this positive normal rescaling. Affine closure of the small class preserves the prescribed order. Write
\[
\begin{gathered}
P(\xi,\tau)=c\,p(\xi,\tau),\\
\qquad
 c=P_m(N/|N|)\ne0,
\end{gathered}
\tag{3}
\]
where \(p\) is monic of degree \(m\) in \(\tau\). Thus its equation has forcing \(f/c\). We prove the construction in these coordinates and then transform back, retaining the original \(N\) and its trace factors.

Put \(d=n-1\), \(a=1/\delta\), and \(\beta=1-1/m\). The range (1) is exactly the inequality \(a\ge\beta\), together with \(\delta>1\) for the cutoff construction. Let \(F_k(\xi,t)\) be the monic time kernels from Lemma 2 of [Principal roots and uniform time kernels](principal-roots-and-time-kernels.md). Its root bounds give constants independent of \(j,\xi,t\) such that
\[
\begin{gathered}
|D_t^jF_k(\xi,t)|
 \\
\le C K^{j}(1+|\xi|)^{j+m-k}
                  e^{C|t|(1+|\xi|)^\beta},
 \\
\qquad j\ge0,\quad \xi\in\mathbb R^d.
\end{gathered}
\tag{4}
\]
This includes repeated roots and \(m=1,\beta=0\). The \(F_k\) depend smoothly on \(\xi\): their companion matrix has polynomial entries, and its exponential series has all derivatives uniformly convergent on compact parameter sets, as proved in Proposition 4 of [Compact Cauchy data and local coherence](compact-cauchy-data-and-local-coherence.md).

## A moment estimate with every derivative scale

We record how (4) leads to the total derivative factorial, rather than a factorial only in the spatial variables. For every \(L\ge1\) and \(\eta>0\), a sufficiently large \(B\) gives
\[
\begin{gathered}
L^\ell\int_{\mathbb R^d}(1+|\xi|)^\ell e^{-B|\xi|^a}\,d\xi
       \\
\le C_{B,L,\eta}\eta^\ell(\ell!)^\delta,
 \\
\qquad \ell\ge0.
\end{gathered}
\tag{5}
\]
Indeed, \((1+r)^\ell\le2^\ell(1+r^\ell)\). The moment argument ([equation 17 in Small Gevrey classes and compact Fourier decay](small-gevrey-and-compact-fourier-decay.md))–([equation 18 in Small Gevrey classes and compact Fourier decay](small-gevrey-and-compact-fourier-decay.md)) bounds the \(r^\ell\) term by
\(J_{B/2}(2\delta/B)^{\delta\ell}(\ell!)^\delta\). Choose \(B\) with \(2L(2\delta/B)^\delta\le\eta\). The remaining constant term contributes \((2L)^\ell J_B\), which is at most another constant times \(\eta^\ell(\ell!)^\delta\), because a positive factorial power absorbs every fixed exponential, as in ([equation 7 in Small Gevrey classes and compact Fourier decay](small-gevrey-and-compact-fourier-decay.md)). Order zero is covered by enlarging the constant.

In \(d=0\), integration over the one-point frequency space means evaluation at \(\xi=0\) and \(J_B=1\). The same constant-term factorial argument proves (5); no nonexistent coordinate is selected. A fixed additional power \((1+r)^q\) can be absorbed into \(e^{Br^a/2}\) with a finite constant, so (5) also applies with any fixed nonnegative integer weight \(q\), after replacing \(B\) by a larger decay constant.

## Homogeneous solutions for compact initial data

**Proposition 1.** If all \(g_k\) have compact support and belong to \(\gamma^{(\delta)}\), the homogeneous problem has a global solution in that small class.

**Proof.** Let \(\widehat g_k\) be their entire transforms. The preceding Fourier characterization gives, for every \(B_0>0\), a uniform bound
\(|\widehat g_k(\xi)|\le C_{B_0}e^{-B_0|\xi|^a}\) on real frequencies, for all finitely many \(k\). Define
\[
\begin{gathered}
U(\xi,t)=\sum_{k=0}^{m-1}\widehat g_k(\xi)F_k(\xi,t),
 \\
\qquad
 u(y,t)=(2\pi)^{-d}\int_{\mathbb R^d}e^{iy\cdot\xi}U(\xi,t)\,d\xi.
\end{gathered}
\tag{6}
\]
For every fixed compact time interval \(|t|\le T\), one has
\((1+r)^\beta\le C_\beta(1+r^a)\), since \(a\ge\beta\). For \(\beta=0\) the left side is 1. Given any desired \(B>0\), choose the data decay constant \(B_0\) larger than \(B+C C_\beta T\). Then (4) bounds each differentiated integrand by a constant times a polynomial in \(r\) times \(e^{-Br^a}\). This is integrable for every finite derivative order. Differentiation under the integral proves smoothness, the homogeneous equation and the exact initial jets by the time kernels and Schwartz inversion.

For a mixed derivative \(D_y^\alpha D_t^j\), set \(\ell=|\alpha|+j\). Bound (4) gives at most \(C_{T,B}K^\ell(1+r)^{\ell+m}e^{-Br^a}\) under the integral. The fixed power \(m\) is absorbed as stated after (5). Apply (5) with any requested scale \(\eta\). Its factorial is the full \((\ell!)^\delta\), with a constant independent of \(\alpha,j\). This proves the small-class bound on every compact time interval, uniformly for all real \(y\), and hence on every compact subset of the full space. At the endpoint \(a=\beta\), the choice of the arbitrarily large \(B_0\) absorbs the time-growth constant exactly; no strict inequality is required. \(\square\)

## Compact forcing with zero initial traces

**Proposition 2.** For compactly supported \(f\in\gamma^{(\delta)}(\mathbb R^{d+1})\), the inhomogeneous problem has a global small-class solution with all \(m\) initial \(D_t\)-traces zero.

**Proof.** Partial spatial transformation of the forcing satisfies, for every \(B_0>0\) and every \(\eta>0\),
\[
\begin{gathered}
|D_s^b\widehat f(\xi,s)|
       \\
\le C_{B_0,\eta}\eta^b(b!)^\delta e^{-B_0|\xi|^a},
 \\
\qquad b\ge0,\\
\quad s\in\mathbb R,\\
\quad \xi\in\mathbb R^d.
\end{gathered}
\tag{7}
\]
To prove the simultaneous bound, all forcing derivatives have one compact spatial support, and integration by parts \(k\) times in a coordinate with \(|\xi_j|\ge|\xi|/\sqrt d\) gives a bound by
\(C_\varepsilon\varepsilon^{k+b}((k+b)!)^\delta\) times that ball's volume. The factorial inequality
\((k+b)!\le2^{k+b}k!b!\) splits it into
\(C_\varepsilon(2^\delta\varepsilon)^k(k!)^\delta
(2^\delta\varepsilon)^b(b!)^\delta\).
Choose \(\varepsilon\) small enough both to make \(2^\delta\varepsilon\le\eta\) and to obtain the requested \(B_0\) by the forward Fourier optimization ([equation 9 in Small Gevrey classes and compact Fourier decay](small-gevrey-and-compact-fourier-decay.md))–([equation 11 in Small Gevrey classes and compact Fourier decay](small-gevrey-and-compact-fourier-decay.md)). Its small-frequency constant is independent of \(b\), so (7) follows. In \(d=0\), no integration by parts is needed: the time derivative estimate itself gives (7) at the sole frequency zero.

Put \(G=F_{m-1}\) and define
\[
\begin{gathered}
V(\xi,t)=\frac{i}{c}\int_0^tG(\xi,t-s)\widehat f(\xi,s)\,ds,
 \\
\qquad
 v(y,t)=(2\pi)^{-d}\int e^{iy\cdot\xi}V(\xi,t)\,d\xi.
\end{gathered}
\tag{8}
\]
The time integral is oriented when \(t<0\). For any smooth scalar function \(h\), repeated differentiation gives
\[
\begin{gathered}
D_t^j\int_0^tG(t-s)h(s)\,ds
 \\
=\int_0^tD_t^jG(t-s)h(s)\,ds
       \\
-i\sum_{r=0}^{j-1}(D_t^{j-1-r}G)(0)(D_t^rh)(t).
\end{gathered}
\tag{9}
\]
The empty sum corresponds to \(j=0\). For \(j=1\), the boundary term is \(-iG(0)h(t)\). Applying \(D_t\) to the integral creates the next \(r=0\) term, and applying it to each previous boundary term increases its derivative of \(h\); this proves the formula inductively, with exactly one copy of every term and its fixed \(-i\).

The initial jets of \(G\) are zero through order \(m-2\) and one at order \(m-1\). Thus all first \(m\) initial jets of the integral in (8) are zero. When \(p(D_t)\) is applied, the interior terms cancel by its kernel equation, and among the boundary terms only the order-\(m\) term \(-ih(t)\) survives. Multiplication by \(i/c\) gives \(P(\xi,D_t)V=\widehat f\) with the original nonzero leading coefficient \(c\). This verifies both the Duhamel coefficient and its phase.

We spell out the small-class control of all boundary terms in (9). On \(|t|\le T\), (4) and (7) make its integral term, after a mixed derivative of total order \(\ell=|\alpha|+j\), at most
\[
\begin{gathered}
C_{T,B_0}K^\ell(1+|\xi|)^{\ell+1}
\\
\exp[-B_0|\xi|^a+CT(1+|\xi|)^\beta]
\end{gathered}
\].
As in Proposition 1, choose \(B_0\) large enough and use (5), absorbing the fixed additional power 1. This gives every scale \(\eta^\ell(\ell!)^\delta\).

For its boundary summand with time derivative \(r\), the kernel derivative order is \(j-1-r\). Since \(G=F_{m-1}\), its polynomial exponent in (4) is \(j-r\). After spatial differentiation the total exponent is \(\ell-r\). Thus integration in \(\xi\), (5) at an arbitrarily small scale \(\eta_1\), and (7) at an arbitrarily small \(\eta_2\) bound this term by
\[
\begin{gathered}
C\,\eta_1^{\ell-r}\eta_2^r
             ((\ell-r)!)^\delta(r!)^\delta
 \\
\le C\,\eta_1^{\ell-r}\eta_2^r(\ell!)^\delta.
\end{gathered}
\tag{10}
\]
The kernel coefficient \(K^{j-1-r}\) is included in the \(L^{\ell-r}\) choice in (5); constants are independent of the derivative indices. Choose both scales at most the requested \(\eta/2\). There are at most \(j\le\ell\) boundary terms, and \(\ell2^{-\ell}\le1\) for \(\ell\ge1\). Their sum has the requested \(\eta^\ell(\ell!)^\delta\) bound. Order zero has only the integral term. Absolute domination also justifies every differentiation, including the variable-time endpoint. Hence \(v\in\gamma^{(\delta)}\), solves the full equation and has zero initial traces. \(\square\)

## A sufficient finite-speed cone

**Lemma 3, relative to Holmgren.** There is \(L>0\), depending only on the principal part, with the following property. Let \(T>0\) and let \(w\in C^m\) solve \(P(D)w=0\) on a neighborhood of the closed backward cone
\[
\begin{gathered}
\mathcal K=\{(y,t):0\le t\le T,\\
\ |y-y_0|\le L(T-t)\}.
\end{gathered}
\tag{11}
\]
If all \(m\) initial traces are zero on a neighborhood of its closed base ball, then \(w=0\) near the apex \((y_0,T)\). The same assertion holds when \(w\) is defined only \(C^m\) up to the plane from \(t\ge0\), on a relative neighborhood of that cone in the closed halfspace. The reversed-time assertion holds as well. This is a sufficient cone for the construction; no smallest-cone claim is made.

**Proof.** Homogeneity and the nonzero leading coefficient give a constant \(C_*\) such that every root of \(F(\xi,\tau)\) has \(|\tau|\le C_*|\xi|\). To see this, its coefficient of \(\tau^{m-j}\) is homogeneous of degree \(j\) in \(\xi\), so the same finite geometric-sum proof as ([equation 3 in Principal roots and uniform time kernels](principal-roots-and-time-kernels.md))–([equation 4 in Principal roots and uniform time kernels](principal-roots-and-time-kernels.md)) has \(|\xi|\) in place of \(1+|\xi|\). At \(\xi=0\), all roots are zero. Choose \(L>C_*\). Therefore
\[
 F(\xi,1)\ne0\quad\text{whenever }|\xi|\le1/L.
 \tag{12}
\]

The equation is homogeneous on a neighborhood of the compact cone, and its base traces are zero on a neighborhood of the compact base ball. These neighborhoods may be relative to the closed halfspace in the one-sided version. Consequently one may enlarge \(T\) slightly to \(T'>T\), retaining both properties on the enlarged closed cone and base ball. Indeed the cones with \(T'\downarrow T\) approach the original cone in Hausdorff distance, as is seen by scaling their coordinates about \((y_0,0)\); compactness supplies a positive distance to the relative complement of the given neighborhood. The base enlargement has the same property.

Choose \(e>0\) with \(e/L<T'-T\), and use the smooth function
\[
 h_e(y,t)=t+\frac{\sqrt{|y-y_0|^2+e^2}}{L}.
 \tag{13}
\]
It has time derivative 1 and \(|\nabla_yh_e|<1/L\), so every level surface is noncharacteristic by (12). Its level below \(T'\), in \(t\ge0\), lies inside the enlarged cone.

Extend \(w\) by zero to \(t<0\) locally along the entire enlarged base ball. The zero-trace calculation ([equation 3 in Compact Cauchy data and local coherence](compact-cauchy-data-and-local-coherence.md)) makes this distribution solve the homogeneous equation across the plane wherever that extension is used. Consider the open region with \(|y-y_0|<LT'\), \(t>-\rho\), \(t<T'\), and \(h_e<T'\), for a sufficiently small fixed \(\rho>0\). For positive times it lies in the enlarged cone; for negative times the extension is zero. The equation holds there, including along its plane section.

Suppose the apex belongs to the support of this distribution. Its value of \(h_e\) is \(T+e/L<T'\). The support intersected with the sublevel \(h_e\le T+e/L\) is nonempty and compact inside this open region: support is absent at negative times, and the sublevel bounds \(t\) and the spatial radius strictly below the region's upper and lateral boundaries. Thus \(h_e\) has a minimum at a support point \(p\). In a neighborhood of \(p\), the distribution is zero on the side \(h_e<h_e(p)\). The level surface through \(p\) is \(C^\infty\) and noncharacteristic. The exact planned distributional Holmgren theorem makes the distribution zero near \(p\), contradicting its membership in the support. The apex is not in the support, proving local vanishing.

For the reversed-time problem replace \(t\) by \(-t\). Its principal roots have the same modulus bound, its leading coefficient remains nonzero, and the initial zero jets acquire only signs. The same proof applies with the same \(L\). \(\square\)

The smooth level surfaces in this proof require the general noncharacteristic-surface Holmgren theorem stated in the prerequisites.

## Removing the support restrictions

**Completion of the theorem.** For unrestricted initial data \(g_k\in\gamma^{(\delta)}(\mathbb R^d)\), choose small-class spatial cutoffs \(\psi_\nu\) equal to one on \(|y|\le\nu\), supported in a larger compact set. Proposition 1 supplies global homogeneous solutions \(u_\nu\) for the compact data \(\psi_\nu g_k\). Fix a compact set with \(|y|\le R\), \(|t|\le T\). For all sufficiently large \(\nu,\mu\), their initial differences vanish on a ball containing the bases of all forward and backward cones in Lemma 3 with apex in this compact set. The difference solves the homogeneous equation globally. Lemma 3 therefore makes \(u_\nu=u_\mu\) near every point of the compact set.

For an explicit uniform margin, take \(\nu,\mu>R+L(T+1)+1\). The base balls for times up to \(T+1\) lie inside both initial equality balls. The slightly enlarged cones used in Lemma 3 are thus allowed. A finite cover of the compact set supplies local equality on its neighborhood. These solutions stabilize locally; define \(u_0\) by their common local value. The definitions agree on overlaps. On every compact set \(u_0\) agrees with one of the small-class solutions, so it belongs to \(\gamma^{(\delta)}\), solves the equation and has all the original initial traces. Exact local stabilization, rather than an unproved limit in a Gevrey topology, is used.

For arbitrary forcing \(f\in\gamma^{(\delta)}(\mathbb R^{d+1})\), choose small-class spacetime cutoffs \(\chi_\nu=1\) on the full Euclidean ball of radius \(\nu\). Let \(v_\nu\) be the zero-data solution from Proposition 2 for the compact forcing \(f_\nu=\chi_\nu f\), and put \(u_\nu=u_0+v_\nu\). These have the original initial data and forcing \(f_\nu\).

For a fixed compact set \(|y|\le R,\ |t|\le T\), sufficiently large \(\nu,\mu\) make \(f_\nu=f_\mu=f\) on a neighborhood of every relevant closed cone. For example \(\nu,\mu>R+L(T+1)+T+2\) contains the enlarged cones in the initial equality region. Their solution difference has zero initial traces everywhere and is homogeneous on those neighborhoods. Apply Lemma 3 again. Thus \(u_\nu\) stabilizes near that compact set, giving a global \(u\). Each local representative is in the small class; the equation, forcing and initial traces pass by local equality. This proves existence for all prescribed data and forcing without a growth assumption.

If two global \(C^m\) solutions have the same forcing and initial data, their difference is homogeneous with all zero initial jets. Lemma 3 at any positive or negative time proves it zero there; the order-zero initial trace gives zero on the plane as well. This proves uniqueness. Finally undo the orthogonal change of coordinates and the factors \(g_k=|N|^{-k}\phi_k\). The solution is in the original small class by affine closure and has precisely the original traces in (2). \(\square\)

## Exercises with complete solutions

**Exercise 1 — basic: the Duhamel coefficient.** For \(P=c(D_t-\lambda)\), \(c\ne0\), check the zero-data forcing formula in (8) and its sign.

**Solution.** Here \(m=1\), \(G(t)=e^{i\lambda t}\), and
\[
 V(t)=\frac{i}{c}\int_0^te^{i\lambda(t-s)}h(s)\,ds.
 \tag{14}
\]
Differentiation gives
\(\partial_tV=ih(t)/c+i\lambda V\). Thus
\((D_t-\lambda)V=-i(ih/c+i\lambda V)-\lambda V=h/c\), and multiplication by \(c\) gives \(h\). The initial value is zero. The same calculation holds at negative times with the oriented integral. A coefficient \(-i/c\) would produce \(-h\).

**Exercise 2 — intermediate: why the endpoint is included.** Explain, for \(m=2,3,4\), how the maximal small-Gevrey order matches the root-growth exponent, and why a fixed single decay constant would not suffice for the argument on arbitrary time intervals.

**Solution.** The pairs \((\beta,\delta_{\max})\) are \((1/2,2)\), \((2/3,3/2)\), and \((3/4,4/3)\). In each case \(1/\delta_{\max}=\beta\). On \(|t|\le T\), the root/time estimate contributes \(e^{CT(1+r)^\beta}\). At the endpoint the data estimate contributes \(e^{-B_0r^\beta}\), with \(B_0\) available arbitrarily large. Choose it larger than the time-growth coefficient and all requested moment-decay constants; the proof then works on this time interval. Repeat for every \(T\), allowing its constant to change. A single fixed \(B_0\) does not allow this choice uniformly over all \(T\); that is a limitation of this estimate, not an asserted nonexistence theorem for every fixed-scale datum. The small class's every-scale condition supplies the exact freedom used in the proof.

**Exercise 3 — advanced: the sideways heat series.** Given \(g_0,g_1\in\gamma^{(2)}(\mathbb R)\), construct the solution of \(u_{xx}=u_t\) with ordinary traces \(u(0,t)=g_0(t)\), \(u_x(0,t)=g_1(t)\) by a series. Show its convergence with all fixed mixed derivatives and identify its small-class regularity.

**Solution.** Define
\[
\begin{gathered}
u(x,t)=\sum_{k=0}^\infty\frac{x^{2k}}{(2k)!}g_0^{(k)}(t)
       \\
+\sum_{k=0}^\infty\frac{x^{2k+1}}{(2k+1)!}g_1^{(k)}(t).
\end{gathered}
\tag{15}
\]
On a compact \(t\)-interval, each datum has
\(|g_\ell^{(k)}|\le C_\varepsilon\varepsilon^k(k!)^2\) at every scale. Since \((k!)^2\le(2k)!\), the two series converge uniformly on \(|x|\le R\) by choosing \(\varepsilon R^2<1\).

For a fixed time derivative order \(q\), the factorial inequality
\((k+q)!\le2^{k+q}k!q!\) gives a bound by
\(C_\varepsilon(4\varepsilon)^{k+q}(k!)^2(q!)^2\).
For a fixed spatial derivative order \(p\), differentiating the normalized monomial introduces, relative to its original factorial, a factor at most \((2k+1)^p\), and the remaining power on \(|x|\le R\) is bounded using \(\max(1,R)^{2k+1}\). Choose \(4\varepsilon\max(1,R)^2<1\). The resulting polynomial-in-\(k\) geometric majorant is summable. Finitely many terms of degree less than \(p\) either vanish or are handled individually. Hence every fixed mixed derivative series converges uniformly on compact sets.

Twice differentiating in \(x\) shifts \(k\) to \(k+1\), exactly as one differentiation in \(t\). Thus the smooth sum solves the heat equation and has the stated traces. The full theorem also constructs a global \(\gamma^{(2)}\) solution: its symbol in spatial-normal coordinates is \(\tau^2+i\xi\), whose principal part is hyperbolic; the \(D_x\)-trace is \(-ig_1\), while the order-zero trace is \(g_0\). The uniqueness just proved identifies that solution with this series, so the series belongs to the small order-two class jointly in \((x,t)\). This establishes the joint order-two small-class estimate.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Springer, 1983.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
