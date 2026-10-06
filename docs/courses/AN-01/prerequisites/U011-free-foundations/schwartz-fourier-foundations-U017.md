# Schwartz functions and Fourier inversion

*Written by GPT-6 Astra (OpenAI), Ultra reasoning effort, 4 October 2026. Public domain (CC0).*

This proof supplies the Fourier operations used in [Complex powers at a boundary](../../src/complex-powers-at-a-boundary.md). Its inputs are the [scalar foundations](metric-foundation-bridges.md), Sections 12.4, 13.1–13.5 and 13.7–13.10, and the [integration foundations](banach-foundation-bridges.md), Sections 15.0–15.1 and 16.1–16.2. These give square roots, calculus, the exponential, arctangent, smooth cutoffs, Lebesgue convergence, Fubini and affine substitution. The Gaussian mass is proved below, including its constant.

## F1. Seminorms, operations and compact approximation

Fix an integer \(n\ge1\). A multiindex is a vector of nonnegative integers; \(x^\alpha=\prod_jx_j^{\alpha_j}\), \(\partial^\beta=\prod_j\partial_{x_j}^{\beta_j}\), and \(|\alpha|=\sum_j\alpha_j\). Define

\[
 \mathcal S(\mathbb R^n)
 =\{\phi\in C^\infty(\mathbb R^n):
       q_{\alpha,\beta}(\phi)<\infty\text{ for all }\alpha,\beta\},
 \qquad
 q_{\alpha,\beta}(\phi)=\sup_x|x^\alpha\partial^\beta\phi(x)|.
 \tag{F1}
\]

The topology has neighborhoods given by finitely many inequalities \(q_{\alpha,\beta}(\phi)<\eta\). A sequence converges exactly when each seminorm of its difference tends to zero. Bounds with \((1+|x|)^N|\partial^\beta\phi|\) are equivalent to finitely many of these bounds: use \(|x_j|\le|x|\le\sum_j|x_j|\), expand the integer power of \(1+\sum_j|x_j|\), and apply the triangle inequality.

The product rule proves that differentiation and multiplication by a coordinate map \(\mathcal S\) continuously into itself. For example,

\[
 q_{\alpha,\beta}(\partial_j\phi)=q_{\alpha,\beta+e_j}(\phi),
 \qquad
 q_{\alpha,\beta}(x_j\phi)
 \le q_{\alpha+e_j,\beta}(\phi)
       +\beta_jq_{\alpha,\beta-e_j}(\phi),
 \tag{F2}
\]

where the last term is omitted if \(\beta_j=0\). Reflection \(R\phi(x)=\phi(-x)\) preserves every seminorm. For fixed \(t>0\), \(\phi(x/t)\) has seminorm \(t^{|\alpha|-|\beta|}q_{\alpha,\beta}(\phi)\). Translations are continuous: expand \(x^\alpha=((x-c)+c)^\alpha\) after changing variables. More generally, multiplication by a smooth function whose derivatives have polynomial growth is continuous, by the product rule and the weighted bounds just proved.

Choose \(\chi\in C_c^\infty\), equal to one on \(|x|\le1\), and put \(\chi_T(x)=\chi(x/T)\), \(T\ge1\). Such a cutoff follows by taking products of the scalar cutoffs from Section 13.10 and adjusting the inner and outer cubes. Then

\[
 \chi_T\phi\longrightarrow\phi\quad\hbox{in }\mathcal S
 \quad(T\longrightarrow\infty).
 \tag{F3}
\]

Indeed the term with no derivative on \(\chi_T\) is bounded in \(q_{\alpha,\beta}\) by a constant times
\(\sup_{|x|\ge T}|x^\alpha\partial^\beta\phi(x)|\). This tends to zero, because one extra weight \(1+|x|\) is bounded and is at least \(1+T\) there. A term with a nonzero multiindex \(\nu\) on the cutoff is bounded by
\[
 C_\nu T^{-|\nu|}
 \sup_{|x|\ge T}|x^\alpha\partial^{\beta-\nu}\phi(x)|,
\]
and tends to zero by the same argument. There are only finitely many terms. Thus compact smooth tests are dense in \(\mathcal S\).

Here is an integrable bound with an explicit justification. Set \(w(x)=\prod_{j=1}^n(1+x_j^2)\). Arctangent and its limits at the two infinite endpoints, proved in the scalar foundation, give \(\int_{\mathbb R}(1+s^2)^{-1}\,ds=\pi\). Fubini therefore gives

\[
 \|\phi\|_1\le\pi^n\sup_x w(x)|\phi(x)|
 \le\pi^n\sum_{\alpha\in\{0,2\}^n}q_{\alpha,0}(\phi).
 \tag{F4}
\]

The same estimate applies to every polynomial times every derivative of \(\phi\).

## F2. Every Fourier seminorm

Define
\[
 F\phi(\xi)=\int_{\mathbb R^n}e^{-ix\cdot\xi}\phi(x)\,dx,
 \qquad
 G\psi(x)=(2\pi)^{-n}\int_{\mathbb R^n}e^{ix\cdot\xi}\psi(\xi)\,d\xi.
 \tag{F5}
\]

Both integrals exist by (F4). The exponential series and addition rule imply \(|e^{is}|=1\) for real \(s\): complex conjugation gives \(\overline{e^{is}}=e^{-is}\), whose product is one. The real fundamental theorem consequently bounds the difference quotient in \(\xi_j\) of \(e^{-ix\cdot\xi}\) by \(|x_j|\). Dominated convergence, followed repeatedly by the same argument, yields
\[
 \partial_\xi^\beta F\phi=F[(-ix)^\beta\phi].
 \tag{F6}
\]
Continuity of these derivatives follows by dominated convergence as well.

For integration by parts, hold the other coordinates fixed, integrate over \([-A,A]\) in \(x_j\), and let \(A\to\infty\). The endpoint terms vanish by rapid decrease. All full-space integrals of \(\phi\) and \(\partial_j\phi\) are absolutely integrable by (F4), so Fubini permits integrating the resulting equality in the other coordinates. We obtain \(F(\partial_j\phi)=i\xi_jF\phi\). Repetition gives
\[
 \xi^\alpha\partial_\xi^\beta F\phi
   =F\bigl[(-i\partial_x)^\alpha((-ix)^\beta\phi)\bigr].
 \tag{F7}
\]
The absolute value of the right side is at most the \(L^1\) norm of its argument. Expand its finite product derivatives and apply (F4) to each term. Each output seminorm is bounded by a constant times a finite sum of input seminorms. Thus \(F:\mathcal S\to\mathcal S\) is continuous. Direct substitution in (F5) gives
\[
 FR=RF,\qquad G=(2\pi)^{-n}RF,
 \tag{F8}
\]
so \(G\) is also continuous.

## F3. Gaussian mass and its Fourier transform

The integral \(I=\int_{\mathbb R}e^{-s^2}\,ds\) is finite and positive. For finiteness, the exponential series implies \(e^{s^2/2}\ge s^2/2\), so \(e^{-s^2}\le2/s^2\) for \(|s|\ge1\). Tonelli and symmetry give
\[
 I^2=2\int_0^\infty\int_{\mathbb R}e^{-x^2-y^2}\,dy\,dx.
\]
For each fixed \(x>0\), the affine substitution \(y=xt\) changes the inner integral to \(\int_{\mathbb R}x e^{-(1+t^2)x^2}\,dt\). Tonelli applies to this nonnegative function. The elementary primitive \(-e^{-a x^2}/(2a)\), for \(a>0\), then gives
\[
 I^2
 =2\int_{\mathbb R}\left(\int_0^\infty
       x e^{-(1+t^2)x^2}\,dx\right)dt
 =\int_{\mathbb R}\frac{dt}{1+t^2}=\pi.
 \tag{F9}
\]
Hence \(I=\sqrt\pi\). This uses one-dimensional affine substitutions and Tonelli, with no polar-coordinate change.

For \(b>0\), let \(g_b(s)=e^{-bs^2}\) and \(J_b=Fg_b\) in dimension one. Every derivative of \(g_b\) is a polynomial times \(g_b\), by induction. Every polynomial times \(g_b\) is bounded and integrable, since the positive exponential series bounds \(e^{bs^2/2}\) below by any chosen even power, leaving the integrable factor \(e^{-bs^2/2}\). Thus \(g_b\in\mathcal S\), and (F6)–(F7) apply. The identity \(g_b'=-2bs g_b\) gives
\[
 J_b'(\xi)=-\frac{\xi}{2b}J_b(\xi).
\]
The derivative of \(e^{\xi^2/(4b)}J_b(\xi)\) is zero, so the fundamental theorem makes it constant. At zero its value is \(\sqrt{\pi/b}\), by scaling (F9). Therefore
\[
 \int_{\mathbb R}e^{-bs^2-is\xi}\,ds
    =\sqrt{\pi/b}\,e^{-\xi^2/(4b)}.
 \tag{F10}
\]
Fubini factors the \(n\)-dimensional integral into these \(n\) one-dimensional integrals. In particular,
\[
 (2\pi)^{-n}\int_{\mathbb R^n}
       e^{iz\cdot\xi-\varepsilon|\xi|^2}\,d\xi
 =k_\varepsilon(z),\qquad
 k_\varepsilon(z)=(4\pi\varepsilon)^{-n/2}
                   e^{-|z|^2/(4\varepsilon)}.
 \tag{F11}
\]
The integral of \(k_\varepsilon\) is one, again by affine substitution and (F9).

## F4. Both inverse identities

Fix \(\phi\in\mathcal S\), \(x\in\mathbb R^n\), and \(\varepsilon>0\). Inserting the factor \(e^{-\varepsilon|\xi|^2}\) makes the double integral absolutely integrable, with bound \(\|\phi\|_1\int e^{-\varepsilon|\xi|^2}\). Fubini and (F11) show
\[
 \begin{aligned}
 (2\pi)^{-n}\int e^{ix\cdot\xi-\varepsilon|\xi|^2}
                         F\phi(\xi)\,d\xi
 &=\int k_\varepsilon(x-y)\phi(y)\,dy\\
 &=\pi^{-n/2}\int e^{-|z|^2}
                      \phi(x+2\sqrt\varepsilon z)\,dz.
 \end{aligned}
 \tag{F12}
\]
On the left, \(F\phi\in L^1\) dominates the integrand and the limit is \(GF\phi(x)\). On the right, the integrable Gaussian times \(\|\phi\|_\infty\) dominates, so the limit is \(\phi(x)\), with coefficient one by (F9). Therefore \(GF=I\) on \(\mathcal S\). Equations (F8) imply
\[
 FG=(2\pi)^{-n}FRF=(2\pi)^{-n}RFF=GF=I.
 \tag{F13}
\]
This supplies the second inverse identity explicitly. Multiplying \(GF=I\) by \(R\) also gives \(F^2=(2\pi)^nR\).

## F5. Tempered distributions and transposes

Define \(\mathcal S'\) as the continuous complex-linear functionals on the seminorm space (F1). Equivalently, \(u\in\mathcal S'\) if and only if
\[
 |u(\phi)|\le C\sum_{(\alpha,\beta)\in E}q_{\alpha,\beta}(\phi)
 \tag{F14}
\]
for some finite set \(E\) and constant \(C\). A bound implies continuity. Conversely, continuity at zero provides a finite set of seminorm constraints on which \(|u|<1\); rescaling \(\phi\) by the maximum of those seminorms proves (F14). If that maximum is zero, every multiple of \(\phi\) is in the same neighborhood, forcing \(u(\phi)=0\). No completeness assertion is needed.

On a fixed compact support the monomial weights are bounded, so (F14) is a finite compact-test derivative bound. Thus \(u\) restricts to a distribution. Restriction is injective by (F3). Derivatives, coordinate multiplication, reflection, translations and positive dilations act by their usual test-function transposes; (F2) and its following estimates prove that these operations preserve \(\mathcal S'\).

Define, without complex conjugation,
\[
 (Fu)(\phi)=u(F\phi),\qquad
 (Gu)(\phi)=u(G\phi),\qquad
 (Ru)(\phi)=u(R\phi).
 \tag{F15}
\]
The continuity bounds from F2 make these tempered. Transposing (F8), (F13) and \(F^2=(2\pi)^nR\) proves
\[
 FG=GF=I,\qquad FR=RF,\qquad F^2=(2\pi)^nR
 \quad\hbox{on }\mathcal S'.
 \tag{F16}
\]
For example, \((FG u)(\phi)=u(GF\phi)=u(\phi)\). For weak convergence, defined by \(u_\nu(\phi)\to u(\phi)\) for every \(\phi\in\mathcal S\), (F15) immediately gives \(Fu_\nu\to Fu\), and likewise for \(G\) and every fixed transpose just listed.

If \(f\in L^1\), then \(f\) defines a tempered distribution by \(|\int f\phi|\le\|f\|_1q_{0,0}(\phi)\). Fubini applies to \(f(x)\phi(\xi)e^{-ix\cdot\xi}\), whose absolute integral is \(\|f\|_1\|\phi\|_1\). It proves that (F15) agrees with the ordinary integral transform. The differential identities on distributions also follow directly from tests:
\[
 F(\partial_j u)=i\xi_jFu,\qquad
 F(x_ju)=i\partial_{\xi_j}Fu.
 \tag{F17}
\]
For the first, \(-u(\partial_jF\phi)=i\,u(F(\xi_j\phi))\) by (F6). For the second, \(x_jF\phi=(1/i)F(\partial_j\phi)\) by (F7), and \(1/i=-i\) gives precisely the distributional derivative on the right. This proves the identities without assuming any density result in the dual space.

For completeness, \(F\delta_0=1\) because \(F\phi(0)=\int\phi\); applying \(F\) once more gives \(F1=(2\pi)^n\delta_0\). Every derivative of the delta is tempered by (F14). A locally integrable function bounded by a polynomial outside a compact set is tempered when it has finite integral of its absolute value on that compact set: use a sup norm there and a sufficiently high Schwartz weight outside. These facts cover the functions and point jets used in the boundary lesson.

## Freely accessible proof comparison

[Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), Sections 11.1–11.2.2, supplies freely accessible proofs of the Fourier seminorm estimates, the Gaussian differential identity and Gaussian regularization for inversion. All arguments used here are supplied above. In particular, (F9) proves the Gaussian constant, (F3) proves compact-test density, (F13) supplies both inverse identities, and (F15)–(F17) prove the required transposed identities directly.
