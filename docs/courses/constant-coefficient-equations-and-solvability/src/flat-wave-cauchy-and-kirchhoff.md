# The wave Cauchy problem and Kirchhoff's formula

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A wave equation needs two initial traces: the displacement and its time derivative. A causal fundamental solution converts these traces into distributions on the initial plane. This gives uniqueness without any assumption about growth at spatial infinity. To obtain a classical solution from finitely differentiable data, we must also control the order of the kernel at the cone vertex.

We use the properly supported convolution rules developed in [Wave kernels with complex coefficients](wave-kernels-with-complex-coefficients.md). The flat wave kernel in [Causal kernels, initial data, and short-time geometry][flat] supplies the fundamental-solution identity, cone formula, homogeneity and initial traces stated below. The compact finite-jet extension theorem in [Compatible jets on closed sets][jets] supplies one precisely stated extension step. We prove its consequence for a whole initial plane here.

## The causal kernel and its normalization

Fix \(c>0\), let \(x\in\mathbb R^n\), \(n\geq1\), and put
\[
\begin{aligned}
W_c&=c^{-2}\partial_t^2-\Delta_x,\\
H&=\{t\geq0\},\\
C_c^+&=\{ct\geq|x|\}.
\end{aligned}
\tag{1}
\]
The inequality defining the cone includes \(t\geq0\). We write \(C^r(H)\) for functions whose derivatives through order \(r\) extend continuously to its boundary.

Here is the exact flat-kernel input. For unit speed there is a distribution \(E_1\) such that
\[
\begin{gathered}
(\partial_t^2-\Delta)E_1=\delta_{(0,0)},\\
\operatorname{supp}E_1\subset C_1^+.
\end{gathered}
\tag{2}
\]
It is homogeneous of degree \(1-n\). Away from the vertex, on the positive-time branch, its cone formula is
\[
E_1=\frac12\pi^{(1-n)/2}
 \chi_+^{(1-n)/2}(t^2-|x|^2).
\tag{3}
\]
Here \(\chi_+^a=s_+^a/\Gamma(a+1)\) for \(a>-1\), extended by the recurrence
\(\partial_s\chi_+^a=\chi_+^{a-1}\). In particular, \(\chi_+^{-1}=\delta_0\). Its one-sided distribution-valued traces are
\[
E_1(0+)=0,\qquad \partial_tE_1(0+)=\delta_x.
\tag{4}
\]
These statements are the flat case of WHK-002–004 in [flat]. We use no variable-coefficient Cauchy theorem.

Define \(E_c(t,x)=cE_1(ct,x)\) by linear pullback. A change of time variable gives
\[
W_cE_c=c\,\delta(ct)\delta_x=\delta_{(0,0)}.
\tag{5}
\]
Its support is \(C_c^+\), its homogeneity degree is \(1-n\), and
\(\partial_tE_c(0+)=c^2\delta_x\). Thus \(E_c\) is normalized for \(W_c\). The kernel for a unit initial velocity is \(c^{-2}E_c\).

## The boundary jump and uniqueness

Addition is proper on \(C_c^+\times H\): the inverse image of every compact set under addition is compact. Indeed, if \((a,b)+(s,y)\) lies in a fixed compact set, then \(a,s\geq0\) and their sum is bounded. Consequently both times are bounded, \(|b|\leq ca\) is bounded, and the bounded spatial sum bounds \(y\). Closedness completes the proof. This argument allows arbitrary spatial support in \(H\).

**Theorem 1.** A \(C^2(H)\) solution of \(W_cu=f\) is uniquely determined by \(f\), \(u(0,\cdot)\), and \(u_t(0,\cdot)\). If \(U\) denotes its extension by zero to negative times, then
\[
\begin{aligned}
W_cU&=1_Hf+c^{-2}\delta(t)u_1(x)\\
&\quad+c^{-2}\delta'(t)u_0(x),
\end{aligned}
\tag{6}
\]
where \(u_0=u(0,\cdot)\), \(u_1=u_t(0,\cdot)\). Moreover,
\[
\begin{aligned}
U=E_c*&\bigl(1_Hf+c^{-2}\delta(t)u_1\\
&\quad+c^{-2}\delta'(t)u_0\bigr).
\end{aligned}
\tag{7}
\]

**Proof.** Integrating \(1_Hu\) twice against a temporal derivative of a compact test produces \(1_Hu_{tt}\), \(u_t(0,x)\delta(t)\), and \(u(0,x)\delta'(t)\). The latter two coefficients each occur once. Spatial integration by parts produces no boundary term because the boundary is the time plane. This proves (6).

The two supports in the convolution \(E_c*U\) have proper addition. We may therefore differentiate either convolution factor:
\[
U=(W_cE_c)*U=E_c*(W_cU).
\tag{8}
\]
This is (7). Apply it to the difference of two solutions with identical data. Its wave image and both boundary traces vanish, so its zero extension is zero. No estimate at spatial infinity has entered the argument. \(\square\)

## How much differentiation the kernel costs

**Lemma 2.** If \(n\geq2\), the kernel \(E_c\) has local distribution order at most
\[
v_0=\left\lceil\frac{n-3}{2}\right\rceil.
\tag{9}
\]
For \(n=1\), \(E_c\) and all its first derivatives are locally finite measures.

**Proof.** First suppose \(n\geq2\), set \(a=(1-n)/2\), and observe that \(v_0\geq0\). The recurrence gives
\[
\chi_+^a=\partial_s^{v_0}\chi_+^{a+v_0}.
\tag{10}
\]
For odd \(n\), the last factor is \(\chi_+^{-1}=\delta_0\). For even \(n\), it is \(\chi_+^{-1/2}\), a locally integrable function. Both have order zero. At every nonvertex point of the cone, \(c^2t^2-|x|^2\) is a submersion. Coordinates with this function as their first variable show that pulling back (10) has order at most \(v_0\): at most \(v_0\) derivatives fall on the test and its smooth Jacobian. Off the cone the same conclusion is immediate. Thus \(E_c\) has that order on each annulus about zero.

We still need the vertex. Write \(N=n+1\); the degree of the kernel is \(2-N\). Choose a smooth dyadic partition
\(\sum_{j\in\mathbb Z}\eta(2^jz)=1\) on punctured space, with \(\eta\) supported in a fixed annulus. For a compact test \(\phi\), abbreviate \(\phi_j(z)=\phi(2^{-j}z)\) and define
\[
T(\phi)=\sum_{j\in\mathbb Z}2^{-2j}
\left\langle E_c,\eta\phi_j\right\rangle_{\!z\ne0}.
\tag{11}
\]
Only finitely many negative \(j\) contribute. The annular order estimate and the product rule bound the pairing for \(j\geq0\) by
\(C\max_{|\alpha|\leq v_0}\|\partial^\alpha\phi\|_\infty\).
Indeed, derivatives of the rescaled test bring factors \(2^{-j|\alpha|}\leq1\). The series converges absolutely. Its tail from \(j=J\) is bounded by
\[
C2^{-2J}\|\phi\|_{C^{v_0}}.
\tag{12}
\]
It defines an extension of order at most \(v_0\).

This extension is homogeneous for every positive scale. To verify that point, remove a smooth radial neighborhood of radius \(\epsilon\) from the punctured pairing. The dyadic tail bounds the change by
\(C\epsilon^2\|\phi\|_{C^{v_0}}\). On the finitely many shells meeting the transition of the cutoff, rescaling gives the same bounded annular derivatives. Thus any fixed smooth cutoff profile has the limit (11). Rescaling the test by \(s>0\) rescales the removed radius. Passing to the limit in the punctured homogeneity identity gives
\[
T(\phi(s\,\cdot))=s^{-2}T(\phi).
\tag{13}
\]

The actual \(E_c\) has the same homogeneity and agrees with \(T\) off zero. Their difference is supported at zero. A point-supported distribution is a finite sum of delta derivatives: if its order is at most \(r\), subtract from a test a cutoff times its Taylor polynomial of degree \(r\). The remainder has derivatives
\(o(|z|^{r-|\alpha|})\). Multiplying it by a cutoff of radius \(\epsilon\) tends to zero in the \(C^r\) norm. Support at zero then makes the distribution annihilate that remainder, so it depends only on the finite Taylor jet.

But \(\partial^\alpha\delta\) has degree \(-N-|\alpha|\), and none of these degrees is \(2-N\). Independence of the Taylor jets in (13) forces every coefficient of \(E_c-T\) to vanish. The annular order bound therefore holds at the vertex too.

For \(n=1\), the kernel is explicitly
\[
E_c(t,x)=\frac c2\,1_{\{ct\geq|x|\}}.
\tag{14}
\]
Integration by parts over this wedge shows that each first derivative is a measure on its two boundary rays. The boundary divergence formula has no extra point mass at their meeting point. The kernel itself is locally integrable. This proves the last assertion. \(\square\)

For dimensions \(n=1,2,3,4,5\), the smallest admissible integer in the existence theorem below is respectively \(-1,0,0,1,1\). The value \(-1\) records a gain supplied by the first derivatives of (14); it does not denote a negative distribution order.

## Extending a finite collection of normal jets

We use the following exact compact theorem from [jets, Theorem 3.1]. Let \(F\) be a nonempty compact subset of Euclidean space. For a finite jet \((f_\alpha)_{|\alpha|\leq M}\), put
\[
T_{\alpha,w}(z)=\sum_{|\beta|\leq M-|\alpha|}
\frac{f_{\alpha+\beta}(w)}{\beta!}(z-w)^\beta.
\]
It is compatible if its Taylor comparisons have uniform remainders
\[
\begin{aligned}
f_\alpha(z)-T_{\alpha,w}(z)
&=o(|z-w|^{M-|\alpha|})
\end{aligned}
\tag{15}
\]
as distinct \(z,w\in F\) approach each other; at order \(M\) this means continuity. Every such jet is the restriction of the derivatives of some \(C_c^M\) function.

**Lemma 3.** Given \(g_j\in C^{M-j}(\mathbb R^n)\) for \(0\leq j\leq M\), there is \(v\in C^M(\mathbb R^{n+1})\) with
\[
\partial_t^jv(0,x)=g_j(x),\qquad 0\leq j\leq M.
\tag{16}
\]

**Proof.** Take a locally finite smooth spatial partition of unity \(\eta_i\) with compact supports. Its neighborhoods may be chosen with locally finite enlarged neighborhoods. In each choose a compact ball \(K_i\) containing the support of \(\eta_i\), and a smooth spatial cutoff \(\theta_i\) supported inside \(K_i\) and equal to one near that support.

On the compact set \(F_i=\{0\}\times K_i\), prescribe
\[
\begin{gathered}
f_{(j,\beta)}(0,x)=\partial_x^\beta(\eta_i g_j)(x),\\
j+|\beta|\leq M.
\end{gathered}
\tag{17}
\]
Two points of \(F_i\) have zero temporal difference. Consequently the normal-power terms in (15) vanish, and the remaining comparison is the ordinary spatial Taylor remainder of
\(\partial^\beta(\eta_i g_j)\), through degree \(M-j-|\beta|\). Its \(C^{M-j}\) regularity gives the required uniform little-oh on the compact ball. Top-order components are continuous. The compact theorem applies.

Let \(v_i\in C_c^M\) be the resulting extension. Multiplication by \(\theta_i(x)\) leaves its temporal trace equal to \(\eta_i g_j\), including globally outside \(K_i\), where both sides vanish. The sum
\[
v(t,x)=\sum_i\theta_i(x)v_i(t,x)
\tag{18}
\]
is locally finite in space, hence \(C^M\) on spacetime. Its temporal traces are \(\sum_i\eta_i g_j=g_j\). This proves the consequence for a noncompact plane using only the compact extension theorem. \(\square\)

## Classical existence at the integer endpoint

**Theorem 4.** Let \(k\geq2\), and let \(v\) be an integer satisfying
\[
v\geq(n-3)/2.
\tag{19}
\]
If
\[
\begin{aligned}
f&\in C^{k+v}(H),\\
u_0&\in C^{k+v+2}(\mathbb R^n),\\
u_1&\in C^{k+v+1}(\mathbb R^n),
\end{aligned}
\tag{20}
\]
then there is a \(C^k(H)\) solution of \(W_cu=f\) with initial traces \(u_0,u_1\). It is unique among all \(C^2(H)\) solutions with these data.

**Proof.** Put \(M=k+v+2\), so \(M\geq3\). Set \(g_0=u_0\), \(g_1=u_1\), and define recursively
\[
\begin{gathered}
g_{j+2}=c^2\bigl(\partial_t^jf(0,x)+\Delta g_j\bigr),\\
0\leq j\leq M-2.
\end{gathered}
\tag{21}
\]
Induction gives \(g_j\in C^{M-j}\): both terms defining \(g_{j+2}\) have regularity \(C^{M-j-2}\). Lemma 3 produces \(v_*\in C^M\) with these normal jets.

On \(H\), the residual \(h=f-W_cv_*\) belongs to \(C^{M-2}\), and (21) gives \(\partial_t^jh(0,x)=0\) for \(j\leq M-2\). Differentiating these identities spatially shows that every mixed boundary jet of total order at most \(M-2\) vanishes. Extension by zero gives
\[
\begin{gathered}
F\in C^{M-2}(\mathbb R^{n+1}),\\
\operatorname{supp}F\subset H.
\end{gathered}
\tag{22}
\]
One can verify this last regularity by joining the derivatives on the two sides, whose boundary traces all agree, and integrating along coordinate lines to identify them as classical derivatives.

Set \(w=E_c*F\). Proper addition makes this convolution legitimate and gives \(W_cw=F\). For \(v\geq0\), Lemma 2 bounds the kernel order by \(v\). On a compact output neighborhood, properness gives a common compact pairing region. Differentiating through order \(k\) puts those derivatives on \(F\); they remain \(C^v\). Translated cutoff pairings vary continuously in that norm, so all distributional derivatives of \(w\) through order \(k\) are continuous.

In the remaining case \(n=1,v=-1\), \(F\) is \(C^{k-1}\). In a derivative of total order \(k\), put one derivative on \(E_c\) and the other \(k-1\) on \(F\). The former is a measure by Lemma 2, so again the compact translated pairing is continuous. Lower derivatives use the measure \(E_c\) itself. A distribution whose derivatives through order \(k\) are continuous has a \(C^k\) representative: locally mollify, pass to the uniform limits of these derivatives on smaller compact sets, and use the fundamental theorem of calculus along coordinate lines. Thus \(w\in C^k\) in every case.

Its support is in \(H\), so its value and first derivatives vanish at the initial plane. Therefore \(u=v_*+w\), restricted to \(H\), solves the equation with the required traces. Theorem 1 gives uniqueness. \(\square\)

The non-strict inequality in (19) matters. In three dimensions \(v=0\) is allowed; in one dimension \(v=-1\) permits a source of class \(C^{k-1}\).

## Kirchhoff's formula in three spatial dimensions

For \(n=3\), (3) becomes a measure on the cone. The speed change gives
\[
\langle E_c,\phi\rangle=
\frac1{4\pi}\int_{\mathbb R^3}
\frac{\phi(|y|/c,y)}{|y|}\,dy.
\tag{23}
\]
For \(t>0\), polar integration yields
\[
(E_c(t)*g)(x)=c^2t\,A_{ct}g(x),
\tag{24}
\]
where the spherical average is
\[
A_rg(x)=\frac1{4\pi}\int_{S^2}g(x+r\omega)\,d\omega.
\]
Reflection of the sphere changes the convolution displacement from minus to plus. Insert (23)–(24) into (7). The initial-value delta derivative differentiates (24) in time, and each initial-data factor \(c^{-2}\) cancels its \(c^2\). For a compact expression of the full formula, write
\(f_{t,x}(y)=f(t-|y|/c,x-y)\) and \(z_\omega=x+ct\omega\).
We obtain
\[
\begin{aligned}
u(t,x)&=\frac1{4\pi}\int_{|y|\leq ct}
\frac{f_{t,x}(y)}{|y|}\,dy\\
&\quad+\frac1{4\pi}\int_{S^2}
\bigl[u_0(z_\omega)+t u_1(z_\omega)\\
&\qquad+ct\,\omega\cdot\nabla u_0(z_\omega)\bigr]\,d\omega.
\end{aligned}
\tag{25}
\]
This formula holds for every solution in Theorem 4, and hence for every \(C^2\) solution for which the displayed terms are defined, by the same jump representation.

At \(t=0\) the sphere average gives \(u_0\). Its first spatial moment is zero, so differentiating at zero gives \(u_1\). The forcing term is \(O(t^2)\). More explicitly, with \(y=ctz\) it becomes
\[
\frac{c^2t^2}{4\pi}\int_{|z|\leq1}
\frac{f(t(1-|z|),x-ctz)}{|z|}\,dz.
\tag{26}
\]
The weight is integrable in dimension three. Dominated differentiation on compact sets gives \(C^k\) regularity from \(f\in C^k(H)\); the other terms use at most the regularity specified in (20) with \(v=0\). Thus the formula also checks the three-dimensional endpoint directly.

Initial data are sampled on the sphere of radius \(ct\). The source is sampled on the backward cone between the initial plane and the observation point. For zero source, this sphere dependence is the sharp-front property of three-dimensional waves. A continuous source contributes over the full cone. The next lesson, [Spacelike Cauchy surfaces and the Riesz formula](spacelike-cauchy-surfaces-and-riesz-formula.md), replaces the initial plane by a curved surface.

## Exercises with complete solutions

**Exercise 1 (basic: the two jump coefficients).** Let \(a,b,h\) be constants and set \(u(t,x)=a+bt+c^2ht^2/2\) for \(t\geq0\). Compute \(W_cu\) and \(W_c(1_Hu)\). Check the initial terms in (25).

**Solution.** The spatial Laplacian is zero, and \(c^{-2}u_{tt}=h\). Formula (6) gives
\[
W_c(1_Hu)=1_Hh+c^{-2}b\delta(t)
+c^{-2}a\delta'(t).
\]
In (25) the initial sphere integral is \(a+bt\). The source integral is
\[
\frac{h}{4\pi}4\pi\int_0^{ct}r\,dr
=\frac{c^2ht^2}{2}.
\]
Their sum is the given solution. An extra copy of the \(\delta\) coefficient would give the wrong velocity term.

**Exercise 2 (intermediate: regularity by dimension).** For \(k=2\) and dimensions \(n=1,2,3,4,5\), list the weakest data regularities supplied by Theorem 4. Explain the separate treatment of \(n=1\).

**Solution.** The smallest integers \(v\) are \(-1,0,0,1,1\). The corresponding triples \((f,u_0,u_1)\) have classes
\[
\begin{array}{c|ccc}
n&f&u_0&u_1\\ \hline
1&C^1&C^3&C^2\\
2,3&C^2&C^4&C^3\\
4,5&C^3&C^5&C^4
\end{array}
\]
These are sufficient conditions from the theorem, rather than assertions of necessity. For \(n=1\), putting a derivative on the measure-valued first derivative of the kernel recovers the derivative missing from \(f\). In higher dimensions the proof instead differentiates the source and pays the nonnegative kernel order.

**Exercise 3 (intermediate: disappearance behind the front).** In three dimensions let \(f=0\), and suppose both initial data are supported in \(\{|y|\leq R\}\). Prove that \(u(t,x)=0\) whenever \(ct>|x|+R\). Also prove vanishing when \(|x|>ct+R\).

**Solution.** If \(ct>|x|+R\), every sampled point satisfies
\[
|x+ct\omega|\geq ct-|x|>R.
\]
Both data and the gradient of \(u_0\) vanish there, so every term in the homogeneous sphere integral is zero. If \(|x|>ct+R\), use
\(|x+ct\omega|\geq|x|-ct>R\).
This gives the usual outer propagation bound and the additional inner disappearance. The latter uses the three-dimensional sphere formula and zero source.

**Exercise 4 (advanced: compatibility on a plane).** For \(M=3\), let \(g_0\in C^3\), \(g_1\in C^2\), \(g_2\in C^1\), \(g_3\in C^0\). Verify the Whitney comparisons on \(\{0\}\times K\) for the jet used in Lemma 3, where \(K\) is compact and a smooth spatial cutoff has been applied.

**Solution.** A component \((j,\beta)\) has remaining order \(3-j-|\beta|\). Between \((0,x)\) and \((0,y)\), every term containing a positive temporal power is zero. The comparison is precisely the spatial Taylor expansion of
\(\partial^\beta(\eta g_j)\) through that remaining order. Since \(\eta g_j\in C^{3-j}\), its remainder is uniformly
\(o(|x-y|^{3-j-|\beta|})\) on the compact set. For \(j+|\beta|=3\), uniform continuity gives the order-zero remainder. These verify all components, including mixed jets; no relation between different \(g_j\) is needed for extension alone.

**Exercise 5 (advanced: the one-dimensional formula).** Derive the formula for the one-dimensional Cauchy problem from (7) and (14). Retain the normalization for \(W_c\).

**Solution.** The initial-velocity term is
\[
\frac1{2c}\int_{x-ct}^{x+ct}u_1(y)\,dy.
\]
Differentiating \(c^{-2}E_c(t)*u_0\) gives
\(\tfrac12[u_0(x-ct)+u_0(x+ct)]\), by differentiation of its moving endpoints. The source convolution is the integral over the wedge. Together,
\[
\begin{aligned}
u(t,x)&=\tfrac12[u_0(x-ct)+u_0(x+ct)]\\
&\quad+\frac1{2c}\int_{x-ct}^{x+ct}u_1(y)\,dy\\
&\quad+\frac c2\int_0^t
\int_{x-c(t-s)}^{x+c(t-s)}f(s,y)\,dy\,ds.
\end{aligned}
\]
For constant source \(h\), the last term equals
\(\frac c2\int_0^t2c(t-s)h\,ds=c^2ht^2/2\), agreeing with Exercise 1. Initial values at interior points of the interval contribute in one dimension.

**Exercise 6 (advanced: no correction at the vertex).** Suppose two homogeneous distributions on \(\mathbb R^N\) have degree \(2-N\) and agree away from zero. Prove that they coincide. Explain why changing the degree to \(-N\) changes the answer.

**Solution.** Their difference is point supported, hence has the form
\(\sum_{|\alpha|\leq r}a_\alpha\partial^\alpha\delta\) by the Taylor-jet argument in Lemma 2. On \(\phi(s\,\cdot)\), each term scales by \(s^{|\alpha|}\); degree \(2-N\) instead demands scaling by \(s^{-2}\). Choose tests with just one prescribed Taylor jet. The identity
\(a_\alpha s^{|\alpha|}=a_\alpha s^{-2}\) for all \(s>0\) implies \(a_\alpha=0\). At degree \(-N\), the required test scaling is one, so a multiple of \(\delta\) is allowed. Thus homogeneity rules out the vertex correction specifically for the wave kernel's degree.

## References

[flat]: ../prerequisites/wave-hadamard-kernels.html
[jets]: ../prerequisites/compatible-jets-on-closed-sets.html

[flat] *Causal kernels, initial data, and short-time geometry*, WHK-002–004: the flat fundamental solution, cone power, homogeneity and initial traces.

[jets] *Compatible jets on closed sets*, Theorem 3.1: extension of compatible finite jets on a compact set.

M. Riesz, *L'intégrale de Riemann-Liouville et le problème de Cauchy pour l'équation des ondes*, Bulletin de la Société Mathématique de France 67 (1939), 153–170, [primary paper](https://www.numdam.org/article/BSMF_1939__67__S153_0.pdf), for causal integrals and wave Cauchy representations.
