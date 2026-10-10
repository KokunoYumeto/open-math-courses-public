# Small Gevrey fundamental solutions in the principal polar cone

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A retarded Cauchy solution defines a continuous fundamental functional. Comparing nearby time directions sharpens its support to the principal polar cone; local analytic carrier estimates give a hyperfunction realization.

Read [Small Gevrey solutions of the full Cauchy problem](small-gevrey-cauchy-solutions.md), [Small Gevrey classes and compact Fourier decay](small-gevrey-and-compact-fourier-decay.md), [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md).

The local distributional Holmgren theorem is proved in [Analytic coefficients and one-sided uniqueness](../AN02-L191.html#3-a-continuously-differentiable-surface-needs-no-analytic-flattening), Theorem 3.2: a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface vanishes near that surface. The uses of the Holmgren theorem draw on that complete proof.

Every direction in the component of a homogeneous hyperbolic polynomial is a hyperbolic direction, as proved in [Real roots and their convex component](../AN02-L192.html#4-pass-to-multiple-roots-and-obtain-convexity), Theorem 4.1. The following real-carrier realization remains planned in the prerequisite course. Compact real-carrier analytic functionals define hyperfunctions with the same support bound; their restrictions preserve equality off a carrier, compatible local hyperfunctions glue, and constant-coefficient derivatives and the Dirac functional have their usual meanings. The analytic carrier estimates and their application to the equation are proved below.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs below use the linked prerequisite lessons and the stated planned results.

## The test-space topology and the statement

Fix \(1<\delta\le m/(m-1)\), where the upper endpoint is infinity for \(m=1\). Let \(P\) be any polynomial of degree \(m\ge1\), with complex coefficients and principal part \(F\) hyperbolic in \(N\ne0\). Irreducibility is not required. Let \(\Gamma\) be the component of \(N\) in \(\{F\ne0\}\subset\mathbb R^n\), and put \(C=\Gamma^*\), meaning \(C=\{c:c\cdot\theta\ge0\text{ for all }\theta\in\Gamma\}\).

For a compact real set \(K\), let \(\mathcal D_K^{(\delta)}\) be the small-class functions supported in \(K\), with seminorms
\[
\begin{gathered}
q_{K,\varepsilon}(\phi)=
 \sup_{\alpha,\ x\in\mathbb R^n}
 \frac{|\partial^\alpha\phi(x)|}
      {\varepsilon^{|\alpha|}(|\alpha|!)^\delta},
 \\
\qquad \varepsilon>0.
\end{gathered}
\tag{1}
\]
Order zero is included. The supremum outside \(K\) is zero, and the estimates on \(K\) are the defining small-class estimates. Scales \(\varepsilon=1/j\), \(j\ge1\), suffice, since the seminorm decreases as its scale increases. Give
\[
 \mathcal D^{(\delta)}=\gamma_0^{(\delta)}
       =\bigcup_{j\ge1}\mathcal D_{K_j}^{(\delta)}
 \tag{2}
\]
the final locally convex topology for an increasing compact exhaustion whose interiors cover the space. Thus a linear functional is continuous precisely when its restriction to each of these stages is continuous. We use this defining universal property; no unproved regularity assertion about the inductive limit is needed. All fixed-compact estimates below hold for every compact \(K\), so the choice of exhaustion does not change the functional's continuity.

Products with fixed small-class cutoffs and constant-coefficient derivatives preserve these test spaces continuously, with a possibly smaller input scale. For products, apply the proof of ([equation 2 in Small Gevrey classes and compact Fourier decay](small-gevrey-and-compact-fourier-decay.md)) to \(\chi\) at scale \(\varepsilon/2\) and to \(\phi\) using \(q_{K,\varepsilon/2}\). For a derivative of fixed order \(r\), use \((k+r)!\le2^{k+r}k!r!\) and an input scale at most \(\varepsilon/2^\delta\). The fixed remaining factors depend on \(r,\varepsilon\), not on \(k\). Reflection preserves each derivative modulus and replaces \(K\) by \(-K\).

**Theorem.** Relative to the stated planned prerequisites, there is a continuous complex linear functional \(E\in(\mathcal D^{(\delta)})'\) such that
\[
 P(D)E=\delta_0,\qquad \operatorname{supp}E\subset C.
 \tag{3}
\]
The functional has a compatible local analytic-functional realization defining a hyperfunction \(E_{\mathcal B}\), with \(P(D)E_{\mathcal B}=\delta_0\) and support contained in \(C\).

The support of a test-space functional is the complement of the union of open sets on whose supported tests it is zero. Derivatives are defined by the bilinear transpose: \((P(D)E)(\phi)=E(P(-D)\phi)\). Coefficients are not conjugated.

## Retarded solutions and their sufficient cone

For a unit vector \(e\in\Gamma\), the planned hyperbolic-direction theorem makes \(F\) hyperbolic in \(e\). For a compact forcing \(f\in\mathcal D^{(\delta)}\), choose
\[
 a<\min_{x\in\operatorname{supp}f}x\cdot e
 \tag{4}
\]
when \(f\ne0\). Construct the global Cauchy solution with all \(m\) data zero on \(x\cdot e=a\). This is the already written full small-Gevrey theorem after translation and orthogonal coordinates. For \(f=0\), use the zero solution.

Call this solution \(S_e f\). It is zero below the forcing. Indeed, backward cone uniqueness below the plane \(a\) makes it zero there, and forward cone uniqueness makes it zero at any intermediate point before the minimum in (4), because the entire cone there misses the forcing. In particular it vanishes on a neighborhood of the initial plane. A different earlier plane gives the same solution: both solutions have zero data on a still earlier plane, and global \(C^m\) Cauchy uniqueness applies. This also proves linearity by choosing one earlier plane for finitely many forcings.

The principal-root estimate and cone Lemma 3 give a number \(L_e>0\) and the closed sufficient cone
\[
\begin{gathered}
C_e^{\,L}=\{t e+z:t\ge0,\\
\ z\cdot e=0,\ |z|\le L_e t\}.
\end{gathered}
\tag{5}
\]
Then
\[
 \operatorname{supp}(S_e f)
          \subset\operatorname{supp}f+C_e^{\,L}.
 \tag{6}
\]
Here the sum is closed: in a convergent sequence of sums, pass to a convergent subsequence of the summands in the compact forcing support, and then the remaining cone summands converge in the closed cone.

To prove (6), take an apex outside this closed sum with time above \(a\). Its entire closed backward cone down to \(a\) misses the forcing: any intersection point would express the apex as a forcing point plus an element of (5). This compact cone has a neighborhood disjoint from the compact forcing support. The equation is homogeneous there and all initial jets on its base are zero, so the one-sided cone lemma makes the solution zero near the apex. Points below \(a\) are already zero. At time \(a\), the solution is zero on a neighborhood because of the strict gap in (4). This proves the support assertion, including its boundary.

## Independence of direction

If \(e'\) is a unit vector sufficiently close to \(e\), then
\[
\begin{gathered}
e\cdot e'>L_e\,|\operatorname{proj}_{e^\perp}e'|,
 \\
\qquad C_e^{\,L}\subset\{v:v\cdot e'\ge0\}.
\end{gathered}
\tag{7}
\]
For \(v=t e+z\) in (5), its pairing with \(e'\) is at least
\(t(e\cdot e'-L_e|\operatorname{proj}_{e^\perp}e'|)\), proving the inclusion. The strict inequality holds at \(e'=e\) and persists on a neighborhood.

Take \(e'\) in that neighborhood and in \(\Gamma\). By (6)–(7), \(S_e f\) is zero on the open halfspace
\(x\cdot e'<\min_{\operatorname{supp}f}x\cdot e'\).
The same is true for \(S_{e'}f\) by its own causality. Both solve \(P(D)u=f\), and both have zero data on a common earlier \(e'\)-plane. Global \(C^m\) uniqueness for the \(e'\)-problem gives \(S_e f=S_{e'}f\).

For nonunit \(\theta\in\Gamma\), set \(S_\theta=S_{\theta/|\theta|}\). Positive dilation preserves the component: for \(z\in\Gamma\), the path \(r z\), \(r>0\), stays in \(\{F\ne0\}\) because \(F(rz)=r^mF(z)\ne0\). The preceding comparison makes \(\theta\mapsto S_\theta f\) locally constant on \(\Gamma\). A connected set cannot split into two nonempty disjoint open level sets: the level set of any one value is open, and its complement is the union of the other open level sets. Hence
\[
 S_\theta f=S_N f=:Sf,\qquad \theta\in\Gamma.
 \tag{8}
\]
 The compared objects are smooth solutions, and every uniqueness application is the declared \(C^m\) Cauchy result.

## A continuous fundamental functional

Write \(\check\phi(x)=\phi(-x)\), and define
\[
 E(\phi)=(S\check\phi)(0).
 \tag{9}
\]
Linearity follows from the retarded construction. We prove a fixed-stage bound, rather than treating existence of \(S\) as a continuity theorem.

Fix \(K\), take \(e=N/|N|\), and use orthogonal coordinates \((y,t)\) for it. All reflected forcings supported in \(-K\) fit in one fixed spatial box and one time interval \([-T,T]\). Choose a common \(a<-T-1<0\). With \(c=F(e)\ne0\), the existing Duhamel formula, translated to this initial time, gives
\[
\begin{gathered}
E(\phi)=\frac{i}{c}(2\pi)^{-(n-1)}
 \\
\int_{\mathbb R^{n-1}}\int_a^0
       G(\xi,-s)\,\widehat{\check\phi}(\xi,s)\,ds\,d\xi,
 \\
\qquad G=F_{m-1}.
\end{gathered}
\tag{10}
\]
The original lower-order coefficients are all retained in \(G\). For \(d=n-1>0\), the compact Fourier integration-by-parts proof, with its constants kept linear in the derivative bound, gives
\[
\begin{gathered}
|\widehat{\check\phi}(\xi,s)|
 \\
\le A_{K,\varepsilon}q_{K,\varepsilon}(\phi)
                  e^{-B_\varepsilon|\xi|^{1/\delta}},
 \\
\qquad B_\varepsilon\longrightarrow\infty
                 \text{ as }\varepsilon\downarrow0.
\end{gathered}
\tag{11}
\]
Explicitly, an orthogonal change of variables replaces the derivative scale by \(A_n\varepsilon\), for a fixed coefficient-sum bound \(A_n\). Spatial integration is over a fixed box of finite volume. Selecting \(|\xi_j|\ge|\xi|/\sqrt d\), integrating by parts \(k\) times and optimizing the integer \(k\) as in the forward part of ([equation 9 in Small Gevrey classes and compact Fourier decay](small-gevrey-and-compact-fourier-decay.md)) gives \(B_\varepsilon=b_\delta(A_n\sqrt d\,\varepsilon)^{-1/\delta}\), with some fixed \(b_\delta>0\). For bounded frequencies, the order-zero bound supplies \(A_{K,\varepsilon}\); it is independent of \(\phi,s\). This is a bound by a single seminorm, not merely an existential Fourier-decay constant for each individual forcing.

The kernel estimate ([equation 4 in Small Gevrey solutions of the full Cauchy problem](small-gevrey-cauchy-solutions.md)) with \(j=0,k=m-1\) bounds \(G\), for \(|s|\le|a|\), by a constant times
\((1+|\xi|)e^{A|a|(1+|\xi|)^{1-1/m}}\).
Since \(1/\delta\ge1-1/m\), choose \(\varepsilon\) so small that (11) absorbs this exponential with a positive decay remainder. The weighted integrability already proved in ([equation 5 in Small Gevrey solutions of the full Cauchy problem](small-gevrey-cauchy-solutions.md)) makes (10) absolutely convergent and gives
\[
 |E(\phi)|\le C_K q_{K,\varepsilon_K}(\phi),
              \qquad \phi\in\mathcal D_K^{(\delta)}.
 \tag{12}
\]
This includes equality at the endpoint. In \(d=0\), the spatial transform and integral mean evaluation on the one-point frequency space; the bounded-time kernel and order-zero forcing bound give (12) directly. The stage bounds and the defining final topology in (2) prove continuity of \(E\).

For any compact \(h\) in the small class, \(h\) itself solves the forcing problem with right side \(P(D)h\), and is zero near a plane earlier than both supports. Global Cauchy uniqueness therefore gives \(S(P(D)h)=h\). Reflection satisfies
\(\check{P(-D)\phi}=P(D)\check\phi\). Hence
\[
\begin{gathered}
(P(D)E)(\phi)\\
=E(P(-D)\phi)
        \\
=(S(P(D)\check\phi))(0)\\
=\phi(0).
\end{gathered}
\tag{13}
\]
This proves the fundamental equation with its exact transpose and \(D=-i\partial\) phases.

## Support in the principal polar

Suppose a compact test \(\phi\) has support in a strict halfspace \(x\cdot\theta<0\) for one \(\theta\in\Gamma\). The reflected forcing then has positive minimum \(\theta\)-time. By (8), \(S\check\phi=S_\theta\check\phi\), whose causality makes its value at zero vanish. Thus \(E(\phi)=0\).

For an arbitrary compactly supported \(\phi\) whose support misses \(C\), every support point \(x\) has \(x\cdot\theta_x<0\) for some \(\theta_x\in\Gamma\), by the definition of the polar. Finitely many strict negative halfspaces cover the compact support. Choose small-class compact cutoffs \(0\le\chi_j\le1\), supported in these halfspaces, so that their sets where \(\chi_j=1\) cover a neighborhood of the support. This follows by applying the already written cutoff lemma to sufficiently small closed balls inside each halfspace. Put
\[
\begin{gathered}
\psi_j=\chi_j\prod_{\ell<j}(1-\chi_\ell),
 \\
\qquad
 \sum_j\psi_j=1-\prod_j(1-\chi_j)=1
        \\
\quad\hbox{near }\operatorname{supp}\phi.
\end{gathered}
\tag{14}
\]
The products are in the small class, each \(\psi_j\phi\) is compactly supported in its negative halfspace, and \(\phi=\sum_j\psi_j\phi\). Every summand has zero \(E\)-value, proving \(\operatorname{supp}E\subset C\). In particular \(C\subset H\). Also \(C\cap\Sigma=\{0\}\): if \(c\in C\), \(c\cdot N=0\), and \(c\ne0\), a small perturbation \(N-r c\in\Gamma\) would give \(c\cdot(N-r c)=-r|c|^2<0\), a contradiction.

The cone in this support assertion is exactly \(\Gamma^*\), rather than the sufficient circular cone (5). We assert containment; no assertion of equality of convex support or of a smallest possible cone is needed for the source remark.

## From the functional to a hyperfunction

We write the localization argument explicitly. Choose \(\chi\in\mathcal D^{(\delta)}\), and for an entire holomorphic \(g\) define the analytic functional
\[
\begin{gathered}
T_\chi(g)=E(\chi g|_{\mathbb R^n}),\\
\qquad
 J_\chi=\operatorname{supp}\chi\cap\operatorname{supp}E.
\end{gathered}
\tag{15}
\]
The product is a compact small-class test: on a fixed real compact set, Cauchy's inequalities bound analytic derivatives by \(A k!\rho^{-k}\), and the positive factorial gap \(\delta-1\) absorbs every fixed exponential at every small-class scale. Product estimates then apply.

We prove that \(T_\chi\) is carried by the compact real set \(J_\chi\), in the precise analytic-functional sense. If \(J_\chi\) is empty it is zero by the support assertion. Otherwise take any complex neighborhood \(W\) of \(J_\chi\), and choose a small-class cutoff \(\lambda=1\) near \(J_\chi\), with real compact support so close to that set that a fixed complex polydisk of radius \(\rho>0\) about every support point lies inside \(W\). Since \(\chi(1-\lambda)g\) has support disjoint from \(\operatorname{supp}E\),
\(T_\chi(g)=E(\chi\lambda g)\).
The real compact support \(K'\) of \(\chi\lambda\) lies in that polydisk neighborhood. Apply (12) on \(K'\). Cauchy's inequalities give
\(|\partial^\alpha g|\le |\alpha|!\rho^{-|\alpha|}\sup_W|g|\)
there, using \(\alpha!\le|\alpha|!\). The factorial-gap argument bounds the analytic factor at scale \(\varepsilon_{K'}/2\) by a constant times \(\sup_W|g|\); bound \(\chi\lambda\) at the same scale and apply ([equation 2 in Small Gevrey classes and compact Fourier decay](small-gevrey-and-compact-fourier-decay.md)). Consequently
\[
 |T_\chi(g)|\le C_{\chi,W}\sup_W|g|.
 \tag{16}
\]
If that supremum is infinite the inequality is vacuous; a smaller relatively compact neighborhood supplies the finite bound needed for each local germ. This proves the every-neighborhood carrier estimate. It is the original adapter from (12), a direct analytic carrier estimate.

For a relatively compact open \(X\), choose \(\chi=1\) on a neighborhood of \(\overline X\). The planned real-carrier localization theorem turns \(T_\chi\) into a compactly supported hyperfunction on a bounded larger open set, and then restricts it to \(X\). Different such cutoffs give the same restriction: their difference in (15) is carried by the compact set
\(\operatorname{supp}(\chi-\chi')\cap\operatorname{supp}E\),
which misses \(X\), so its restriction is zero. The same argument on overlaps gives compatible local hyperfunctions. The planned hyperfunction localization theorem glues them to \(E_{\mathcal B}\) on the full real space. The carrier bound implies \(\operatorname{supp}E_{\mathcal B}\subset\operatorname{supp}E\subset C\).

The equation survives this realization. Write \(P(D)=\sum_\alpha a_\alpha D^\alpha\). Apply (13) to the compact small test \(\chi g\) and expand \(P(-D)(\chi g)\). The term with no derivative on \(\chi\) is \(T_\chi(P(-D)g)\). Every other term has a factor \((-D)^\beta\chi\), \(\beta\ne0\), and is an analytic functional carried outside \(X\), because \(\chi=1\) near \(\overline X\). Derivatives of analytic functionals preserve their carriers, by Cauchy's inequalities on a slightly smaller neighborhood, so these remaining terms restrict to zero on \(X\). The right side is \(\chi(0)g(0)\), whose restriction is the Dirac hyperfunction on \(X\). The planned derivative/restriction compatibility therefore gives \(P(D)E_{\mathcal B}=\delta_0\) locally, and hence globally. This finishes both conclusions of the theorem. \(\square\)

The uniqueness comparisons concern smooth retarded solutions. The hyperfunction conclusion uses the planned analytic-functional localization theorem stated in the prerequisites.

## Exercises with complete solutions

**Exercise 1 — basic: the retarded first-order phase.** For \(P=c(D_t-\lambda)\) on the real line, \(c\ne0\), compute \(E\) from (9).

**Solution.** The retarded solution is
\(Sf(t)=\frac{i}{c}\int_{-\infty}^t e^{i\lambda(t-s)}f(s)\,ds\),
where the integral begins effectively before the compact forcing support. Reflection and \(r=-s\) give
\[
\begin{gathered}
E(\phi)=\frac{i}{c}\int_0^\infty e^{i\lambda r}\phi(r)\,dr,
 \\
\qquad E=\frac{i}{c}1_{\{t\ge0\}}e^{i\lambda t}.
\end{gathered}
\tag{17}
\]
Since \(D_t(1_{\{t\ge0\}}e^{i\lambda t})=-i\delta_0+
\lambda1_{\{t\ge0\}}e^{i\lambda t}\), multiplication by \(c\,i/c\) gives \(P(D)E=\delta_0\). Compact tests make the integral continuous regardless of the imaginary part of \(\lambda\). The principal component is the positive halfline and so is its polar.

**Exercise 2 — intermediate: why a single stage seminorm matters.** Explain why continuity of (9) is not justified merely by assigning each compact forcing its own Fourier decay constant, and identify the role of the endpoint.

**Solution.** A continuity estimate must bound \(E(\phi)\) by finitely many fixed stage seminorms, with constants independent of the particular test. The statement that every individual \(\phi\) has rapid small-Gevrey Fourier decay does not itself supply this uniform dependence. In (11), the integration-by-parts estimate keeps the derivative bound as the linear factor \(q_{K,\varepsilon}(\phi)\). The remaining support, coordinate and optimization constants depend only on the stage and chosen scale. Thus one sufficiently small fixed \(\varepsilon_K\) gives (12) for every test in that stage. At \(1/\delta=1-1/m\), Fourier decay and time-kernel growth have the same power. Sending \(\varepsilon\) downward makes \(B_\varepsilon\) exceed the fixed growth constant on the chosen interval, leaving an integrable positive remainder. The scale can depend on \(K\); final-topology continuity requires exactly these separate stage estimates.

**Exercise 3 — advanced: an explicit sideways heat fundamental functional.** In coordinates \((x,t)\), consider \(P(D)=\partial_t-\partial_x^2\), whose principal part is hyperbolic in the positive \(x\)-direction. Prove that the following series defines a continuous functional on \(\gamma_0^{(2)}\), is supported on \(\{x\ge0,t=0\}\), and solves the fundamental equation:
\[
\begin{gathered}
E_{\rm heat}(\phi)=
 -\sum_{k=0}^\infty(-1)^k
       \\
\int_0^\infty\frac{x^{2k+1}}{(2k+1)!}
                         \partial_t^k\phi(x,0)\,dx.
\end{gathered}
\tag{18}
\]

**Solution.** On a stage supported in \(|x|,|t|\le R\), take \(R\ge1\) and a scale \(\varepsilon\) with \(\varepsilon R^2<1\). Each integral has modulus at most
\[
 q_{K,\varepsilon}(\phi)\,
 \varepsilon^k(k!)^2\,\frac{R^{2k+2}}{(2k+2)!}
 \le q_{K,\varepsilon}(\phi)R^2(\varepsilon R^2)^k,
\]
because \((k!)^2\le(2k+2)!\). The geometric sum proves absolute convergence and a single-seminorm stage bound. Every term evaluates jets on the positive \(x\)-axis at \(t=0\), so a test supported off that closed ray has value zero.

The formal transpose of \(P\), in ordinary derivatives, is \(-\partial_t-\partial_x^2\). Put \(b_k(x)=x^{2k+1}/(2k+1)!\). Twice integrating by parts on \([0,\infty)\) gives
\[
\begin{gathered}
\int_0^\infty b_0(x)\phi_{xx}(x,0)\,dx\\
=\phi(0,0)
\end{gathered}
\]
and, for \(k\ge1\),
\[
\begin{gathered}
\int_0^\infty b_k(x)\partial_x^2\partial_t^k\phi(x,0)\,dx
\\
=\int_0^\infty b_{k-1}(x)\partial_t^k\phi(x,0)\,dx
\end{gathered}
\].
The spatial terms with \(k\ge1\) cancel the time terms after shifting their index by one; their signs are respectively \((-1)^k\) and \((-1)^{k-1}\). Only the \(k=0\) boundary value remains. Each series is absolutely convergent by the same estimate with fixed additional derivatives and a smaller scale, so the cancellation is legitimate. Thus \(E_{\rm heat}(P^{\rm t}\phi)=\phi(0,0)\).

In frequency coordinates \((\xi_x,\xi_t)\), the principal part is \(\xi_x^2\). Its component is \(\{\xi_x>0\}\), with \(\xi_t\) unrestricted, and its positive polar is exactly \(\{x\ge0,t=0\}\). This example realizes the precise thin support cone. It is an explicit generalized functional, not a claim that an infinite derivative series has finite distribution order.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
