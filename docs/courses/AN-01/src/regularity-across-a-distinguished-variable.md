# Regularity across a distinguished variable

*Reconstructed and checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Public domain (CC0).*

A differential equation can force smooth dependence on time while leaving point masses in space. We prove this for equations monic in the time derivative, with arbitrary differential operators in the transverse variables. The proof uses finite continuous primitives, lowers their number of time derivatives, and then applies the fundamental theorem of calculus in distribution pairings. At an endpoint, the same construction explains exactly what must extend.

All pairings are complex linear. The earlier proofs used below are [U008](order-positivity-and-limits.md), Proposition 1.2 and Theorem 5.1, for finite-order actions on \(C^k\) tests and uniform convergence on bounded smooth test families; [U021](convolution-as-addition-of-supports.md), B0–B3 and Theorems 1.1–2.1, for localization, gluing and finite-regularity convolution; and [U031](fundamental-solutions-continuation-and-approximation.md), Theorem 6.1, for the full mixed continuous-primitive construction, including its finite compact version. Completeness of the support test spaces and the complete-metric Baire theorem are proved in [functional foundations](../prerequisites/U011-free-foundations/functional-foundations-U008.md), Sections 6 and 14.1–14.2. We prove the required arbitrary-family estimate here.

## A curve of distributions is a joint distribution

Let \(Y\subset\mathbb R^d\) be open and \(I\subset\mathbb R\) an open interval. Write \(x'\) for the transverse variable. A curve \(T:I\to\mathcal D'(Y)\) is weakly continuous if every \(T(t)(\varphi)\) is continuous. A bounded test family \(B\) means a family with a common compact support and uniform bounds for every derivative. The strong seminorms are
\[
 q_B(v)=\sup_{\varphi\in B}|v(\varphi)|.
\]
Strong \(C^m\) means that successive difference quotients converge for all these seminorms, and the resulting derivatives are strongly continuous.

**Lemma 1.1 (one order on a compact time interval).** For compact \(K\Subset Y\) and a compact time interval \(J_0\), a weakly continuous curve defined on \(J_0\) obeys
\[
 \begin{gathered}
 |T(t)(\varphi)|\le C p_{K,k}(\varphi)
       \quad(t\in J_0,\ \varphi\in\mathcal D_K),\\
 p_{K,k}(\varphi)=\max_{|\alpha|\le k}\sup_K|\partial^\alpha\varphi|
 \end{gathered}                                                     \tag{1.1}
\]
for some finite \(C,k\). This includes a closed interval with endpoint values.

**Proof.** For \(N\ge1\), set
\[
 E_N=\{\varphi\in\mathcal D_K:
                   |T(t)(\varphi)|\le N\text{ for all }t\in J_0\}.
\]
Each \(E_N\) is closed, as an intersection of inverse images of closed disks under continuous linear functionals. For each \(\varphi\), compactness of \(J_0\) bounds its continuous scalar pairing, so \(\bigcup_NE_N=\mathcal D_K\). The supplied completeness and Baire proofs imply that some \(E_N\) has nonempty interior. Choose \(\varphi_0\) in that interior and \(k,\varepsilon>0\) with
\(\varphi_0+\{\psi:p_{K,k}(\psi)<\varepsilon\}\subset E_N\).
Since also \(\varphi_0\in E_N\), subtraction bounds every \(T(t)(\psi)\) by \(2N\) in that seminorm ball. For \(p_{K,k}(\psi)>0\), apply this to
\(\varepsilon\psi/(2p_{K,k}(\psi))\); it yields \(C=4N/\varepsilon\). If the seminorm is zero, arbitrary scalar multiples remain in the ball, forcing every pairing to be zero. The zero test space causes no exception. No enumeration of the time family is involved. \(\square\)

A weakly continuous curve now defines a joint distribution by
\[
 \mathscr T(\Phi)=\int_I T(t)(\Phi(\cdot,t))\,dt.                    \tag{1.2}
\]
Indeed the support of a compact joint test projects into \(K\Subset Y\) and \(J_0\Subset I\). To prove continuity of the integrand at \(t_0\), split its change into the pairing with \(\Phi_t-\Phi_{t_0}\), bounded by (1.1), and the change of \(T(t)(\Phi_{t_0})\), which tends to zero by weak continuity. The same bound gives
\[
 |\mathscr T(\Phi)|\le C|J_0|
         \max_{|\alpha|\le k}\sup_{K\times J_0}
                                 |\partial_{x'}^\alpha\Phi|.
\]
Linearity and this fixed-support estimate prove distributional continuity. Finite vectors are treated componentwise.

**Lemma 1.2 (uniqueness and strong continuity).** The map (1.2) is injective on weakly continuous curves, and each such curve is strongly continuous.

**Proof.** Equality on \(\Phi(x',t)=\varphi(x')\eta(t)\) says that the continuous scalar difference \(g(t)\) integrates to zero against every compact smooth \(\eta\). If \(g(t_0)\ne0\), multiply by a complex scalar so its real part is positive at \(t_0\); it stays positive in a small interval. A nonzero nonnegative bump in that interval gives a nonzero integral, a contradiction. Thus the curves agree for every test and time.

For a sequence \(t_j\to t\), weak continuity and U008, Theorem 5.1, give
\(q_B(T(t_j)-T(t))\to0\) for every bounded \(B\). If the corresponding neighbourhood estimate for one \(B\) failed, choose \(t_j\) within \(1/j\) of \(t\) with that estimate failing; this contradicts the sequential conclusion. Hence every strong seminorm is continuous along the curve. The argument applies with one-sided time neighbourhoods as well. \(\square\)

We also need a joint version of the zero-derivative fact.

**Lemma 1.3 (constant transverse distribution).** If \(S\in\mathcal D'(Y\times I)\) and \(\partial_tS=0\), there is a unique \(w\in\mathcal D'(Y)\) such that \(S=w\otimes1\).

**Proof.** Choose \(\rho\in\mathcal D(I)\) with \(\int\rho=1\), and define
\(w(\varphi)=S(\varphi(x')\rho(t))\). On every compact transverse support, the joint finite-order bound for \(S\) and the fixed derivatives of \(\rho\) give a finite-order bound for \(w\).
For any \(\Phi\in\mathcal D(Y\times I)\), put
\[
 \psi(x')=\int_I\Phi(x',t)\,dt,\qquad
 R(x',t)=\Phi(x',t)-\psi(x')\rho(t),\qquad
 \Psi(x',t)=\int_{-\infty}^t R(x',s)\,ds,
\]
extending the compact integrand by zero. Differentiation under this finite integral makes \(\Psi\) smooth. Since \(\int R(x',s)\,ds=0\), its time support lies in the convex hull of the two compact time supports, still compactly inside the interval \(I\); its transverse support is also compact in \(Y\). Therefore \(\Psi\) is a joint test and
\(\Phi=\psi\rho+\partial_t\Psi\). Pairing with \(S\) gives \(S(\Phi)=w(\psi)\), the required tensor identity. Testing with \(\varphi\rho\) proves uniqueness. \(\square\)

## Removing distinguished derivatives

**Lemma 2.1 (continuous transverse primitives).** A continuous distribution curve is locally a finite sum of transverse derivatives of jointly continuous functions. This holds on a compact time interval, including its finite endpoints.

**Proof.** Fix a relatively compact transverse region and a smooth compact cutoff \(\chi=1\) near its closure. Set \(g(t)=\chi F(t)\), extended by zero to \(\mathbb R^d\). Lemma 1.1 and the product rule give one order \(k\) and one bound for all \(g(t)\) on the compact time interval. Insert one further fixed cutoff near their common support to act on noncompact kernels.
For an integer \(M>k\), let
\[
 \begin{gathered}
 A_M(x')=\prod_{\ell=1}^d\frac{(x'_\ell)_+^M}{M!},\qquad
 Q_M=(\partial_1\cdots\partial_d)^{M+1},\\
 b(x',t)=(A_M*g(t))(x').
 \end{gathered}                                                     \tag{2.1}
\]
U031, Theorem 6.1, proves \(Q_MA_M=\delta_0\) by repeated scalar integration by parts. The kernel is \(C^{M-1}\), hence \(C^k\), and U008 extends the common order-\(k\) action to its cut-off translates. U021, Theorem 2.1, identifies this pairing with convolution and proves \(Q_Mb(t)=g(t)\).

Here is the needed parameter check at this finite regularity. If \(t_j\to t\), a fixed compact \(C^k\) test \(\theta\) can be approximated in \(C^k\) on a slightly larger fixed compact support by smooth tests \(\theta_\nu\), using the proved mollification. The bound
\[
 |(g(t_j)-g(t))(\theta)|
 \le 2C\|\theta-\theta_\nu\|_{C^k}
                    +|(g(t_j)-g(t))(\theta_\nu)|
\]
first lets \(j\to\infty\), then \(\nu\to\infty\). Thus the pairing converges for \(\theta\). If also \(x'_j\to x'\), the cut-off kernels
\(A_M(x'_j-\cdot)\) converge to \(A_M(x'-\cdot)\) in \(C^k\), by uniform continuity of the finitely many derivatives on a compact set. Split off that kernel difference and use the same bound. This proves joint continuity of \(b\). Where \(\chi=1\), \(F=Q_Mb\). The estimates include endpoint parameters. When \(d=0\) the assertion is simply scalar continuity; when \(Y\) is empty it is vacuous. \(\square\)

Multiplication by smooth coefficients must preserve the number of distinguished derivatives in such a representation. The exact identity, for a multi-index in all variables, is
\[
 a\,\partial^\alpha b
 =\sum_{\gamma\le\alpha}(-1)^{|\gamma|}
       \binom{\alpha}{\gamma}
       \partial^{\alpha-\gamma}\big((\partial^\gamma a)b\big).
                                                                    \tag{2.2}
\]
To prove the one-derivative case, pair both sides of
\(a\partial_jb=\partial_j(ab)-(\partial_ja)b\) with a test, expand
\(\partial_j(a\varphi)\), and cancel. Induction repeats that identity in each coordinate. At each step the choices of which derivatives hit \(a\) give the binomial coefficient, their negative signs give \((-1)^{|\gamma|}\), and commuting coordinate derivatives gives the displayed formula. This proves (2.2) for distributions directly.

**Lemma 2.2 (a first-order equation gives continuity).** Suppose a finite distribution vector \(U\) satisfies
\[
                  \partial_tU+A(t)U=F(t),                          \tag{2.3}
\]
where \(F\) is a continuous \(\mathcal D'(Y)\)-valued vector and \(A\) is a matrix of transverse differential operators with smooth coefficients. Then \(U\) has a unique strongly continuous curve representative. Arbitrary locally finite transverse orders are allowed.

**Proof.** Fix a product box whose closure is inside \(Y\times I\). A cutoff of \(U\) equal to \(U\) near a slightly larger box is compactly supported. The finite compact construction in U031 writes, on that larger box,
\[
             U=\sum_{\beta,r}\partial_{x'}^\beta
                                  \partial_t^r b_{\beta r},         \tag{2.4}
\]
with finitely many continuous vector coefficients. Let \(q\) bound the occurring integers \(r\). We show that whenever \(q\ge1\), another representation has bound \(q-1\) on a smaller transverse box and the same smaller time interval.

Lemma 2.1 gives \(F\) a representation with only transverse derivatives. Acting by \(A\) on (2.4) and using (2.2) gives
\[
 F-AU=\sum_{\beta,\,0\le r\le q}
                      \partial_{x'}^\beta\partial_t^r c_{\beta r},
\]
with finitely many continuous coefficients. In fact the transverse differentiations cannot increase \(r\), and moving a smooth multiplier inside the derivatives subtracts time derivatives rather than adding any. Choose \(t_0\) inside the time interval and set
\[
 \begin{aligned}
 B={}&\sum_{\beta,r\ge1}\partial_{x'}^\beta
                                    \partial_t^{r-1}c_{\beta r}\\
    &+\sum_\beta\partial_{x'}^\beta
                          \int_{t_0}^t c_{\beta0}(x',s)\,ds.
 \end{aligned}                                                       \tag{2.5}
\]
The new coefficients are continuous and the largest time derivative is at most \(q-1\). The scalar fundamental theorem, or its integration-by-parts version against a joint test, gives \(\partial_tB=F-AU=\partial_tU\). Lemma 1.3 therefore gives
\[
                         U-B=w(x')\otimes1.                        \tag{2.6}
\]
Localize \(w\) in a slightly smaller transverse box. U031's transverse continuous-primitive construction expresses it with finitely many continuous coefficients and no time derivatives. Combining this with \(B\) proves the reduction.

There are only \(q\) reductions. Predetermine \(q+1\) nested transverse boxes around the point with compact inclusions; at each step choose cutoffs on the next larger box. All steps are therefore available, and the final representation has \(r=0\). Its scalar pairings with transverse tests are continuous: they are finite integrals of continuous coefficients against fixed differentiated tests. Fubini and the definition of distributional derivatives identify their joint distribution with \(U\).

To pass from boxes to all of \(Y\times I\), first compare local representatives on overlapping boxes. Tensor tests and Lemma 1.2 force equality at every common time on the overlap. At a fixed time, U021 B0 glues these compatible local distributions. For continuity near any time, decompose a fixed compact transverse test into finitely many subordinate tests, choose a common time neighbourhood for that finite cover, and use continuity of its finitely many local pairings. This gives a global weakly continuous curve; Lemma 1.2 makes it strongly continuous and proves uniqueness. \(\square\)

## The full monic equation

**Theorem 3.1 (regularity in the distinguished variable).** If \(m\ge1\), \(u\in\mathcal D'(Y\times I)\), and
\[
       \partial_t^m u+\sum_{j=0}^{m-1}a_j(t)\partial_t^j u=f(t),      \tag{3.1}
\]
where each \(a_j\) is a transverse differential operator with smooth coefficients and \(f\) is a continuous distribution curve, then \(u\) has a unique representative in \(C^m(I;\mathcal D'(Y))\), in the strong topology. Its curve derivatives give its joint distribution derivatives. No commutativity of the \(a_j\)'s is required.

**Proof.** First take the continuous representative supplied by Lemma 2.2. Its curve
\(G(t)=F(t)-A(t)U(t)\) is continuous. Indeed a fixed transverse test \(\varphi\) is sent by the transpose to \(A(t)^t\varphi\), with the same compact support and smoothly varying derivatives. Here the transpose is defined by
\(A(t)^t\varphi=\sum_\alpha(-1)^{|\alpha|}
\partial_{x'}^\alpha(a_\alpha(x',t)\varphi)\); there is no conjugation. Split its moving-test pairing into a test difference, controlled by Lemma 1.1, and a fixed-test difference, controlled by weak continuity.

Define \(V(t)(\varphi)=\int_{t_0}^tG(s)(\varphi)\,ds\), with oriented integrals. A common order on the compact interval between \(t_0\) and nearby \(t\)'s proves that \(V(t)\) is a distribution and a weakly continuous curve. Fubini and scalar integration by parts, with the same common-order bound, give \(\partial_t\mathscr V=\mathscr G\). Lemma 1.3 applied to \(U-V\), and uniqueness of continuous representatives, give
\[
                       U(t)=w+\int_{t_0}^tG(s)\,ds.                \tag{3.2}
\]
For every bounded test family,
\[
 q_B\!\left(\frac{U(t+h)-U(t)}h-G(t)\right)
 \le\sup_{s\text{ between }t\text{ and }t+h}q_B(G(s)-G(t)).
\]
The right side tends to zero by strong continuity of \(G\). Thus \(U\) is strongly \(C^1\) with derivative \(G\).

For (3.1) apply this result to the companion vector
\[
                     U=(u,\partial_tu,\ldots,\partial_t^{m-1}u).
                                                                    \tag{3.3}
\]
Its first \(m-1\) equations are \(\partial_tU_j=U_{j+1}\) and its last is (3.1). All entries in the resulting operator matrix are transverse operators, and its forcing is \((0,\ldots,0,f)\). Each component is strongly \(C^1\). Starting with the first component, the successive identities identify its first \(m-1\) derivatives with the remaining components; differentiating the last gives the \(m\)-th continuous derivative. Integration by parts gives all the corresponding joint derivatives. Uniqueness follows from Lemma 1.2. \(\square\)

For \(m=0\), the equation is \(u=f\), with the conclusion \(C^0\). Empty \(Y\), \(d=0\), disconnected \(Y\), and unbounded intervals are included; all arguments above are local.

We give a direct point-parameter proof for the examples. If \(q,c\) are smooth scalar functions with \(q\) real and \(k\ge0\), then \(t\mapsto c(t)\delta_{q(t)}^{(k)}\) is strongly smooth and
\[
 \frac d{dt}\big(c(t)\delta_{q(t)}^{(k)}\big)
   =c'(t)\delta_{q(t)}^{(k)}
                  -c(t)q'(t)\delta_{q(t)}^{(k+1)}.
\]
Pairing with \(\varphi\) gives \(F_\varphi(t)=c(t)(-1)^k\varphi^{(k)}(q(t))\), whose scalar chain rule yields the formula. To justify it strongly, fix a compact time interval and a bounded test family. The product and chain rules bound every \(F_\varphi''\) there by a common constant \(C_B\): the derivatives of \(q,c\) are bounded and the test derivatives through order \(k+2\) are uniformly bounded. Twice applying the scalar fundamental theorem gives
\[
 F_\varphi(t+h)-F_\varphi(t)-hF_\varphi'(t)
       =\int_0^h\int_0^s F_\varphi''(t+v)\,dv\,ds,
\]
whose absolute value is at most \(C_B|h|^2/2\), for either sign of \(h\). Division by \(h\) proves the first strong derivative. Each subsequent derivative is a finite sum of the same form, so induction proves all orders. Their first-derivative bounds also give strong continuity by the fundamental theorem. The uniform bounds hold when the point lies outside the common test support as well.

**Example 3.2 (a smooth curve of moving point sources).** For \(u(t)=\delta_{t^2}\),
\[
 \mathscr U(\Phi)=\int_{\mathbb R}\Phi(t^2,t)\,dt,\qquad
             (\partial_t+2t\partial_x)\mathscr U=0.
\]
The equation follows by integrating the total derivative of the compactly supported function \(t\mapsto\Phi(t^2,t)\). The just proved formula gives
\[
 u'(t)=-2t\delta'_{t^2},\qquad
 u''(t)=-2\delta'_{t^2}+4t^2\delta''_{t^2},
\]
and proves all higher strong derivatives. These distributions remain spatial point masses at every time.

## What a boundary hypothesis must control

At a finite endpoint, \(C^m\) means strong continuity of the derivatives through order \(m\), with the derivatives defined one-sidedly there. No condition is imposed at an infinite endpoint.

**Example 4.1 (extendible distributions with a divergent trace).** On \(Y=(-1,1)\) and \(0<t<1\), put \(u(x',t)=1/t\) and \(a_0(x',t)=1/t\). Then \(\partial_tu+a_0u=0\). The forcing extends continuously by zero, and \(u\) extends distributionally across zero. To check the latter without assuming a principal-value theorem, for a test \(\eta\) on an interval containing zero choose \(c>0\) inside that interval and write
\[
 \lim_{\varepsilon\downarrow0}
       \int_{|t|>\varepsilon}\frac{\eta(t)}t\,dt
 =\int_0^c\frac{\eta(t)-\eta(-t)}t\,dt
                  +\int_{|t|\ge c}\frac{\eta(t)}t\,dt.
\]
Extend the test by zero when needed. The first integrand has absolute value at most \(2\sup|\eta'|\), by the scalar fundamental theorem. On a fixed test support the remaining integral is bounded by a constant times \(\sup|\eta|\). The formula is therefore a distribution, restricts to \(1/t\) for positive \(t\), and is denoted \(\operatorname{pv}(1/t)\). Tensoring it with the constant transverse function gives the extension of \(u\), for example to \(Y\times(-1,2)\).

Nevertheless, a transverse test of integral one pairs with \(u(t)\) as \(1/t\), so there is no distributional trace at zero. The coefficient fails to extend smoothly there. Distributional extendibility of the solution alone is insufficient.

**Theorem 4.2 (regularity up to a boundary).** In Theorem 3.1, suppose the coefficients of all \(a_j\) extend smoothly to \(Y\times J\), where \(J\) is an open neighbourhood of \(\overline I\); suppose \(u\) extends as a distribution there; and suppose \(f\) is continuous on \(\overline I\) with values in \(\mathcal D'(Y)\). Then
\[
                         u\in C^m(\overline I;\mathcal D'(Y)).      \tag{4.1}
\]
The assertion is local at each finite endpoint. The extended distribution need not satisfy the equation outside \(I\).

**Proof.** Consider the left endpoint \(a\); the right endpoint is identical with reversed one-sided intervals. Differentiate a chosen extension of \(u\) to form an extension of its companion vector. Cut it off on a product box crossing \(a\). U031's finite compact primitive theorem gives (2.4) with finitely many coefficients continuous across \(a\), so their restrictions extend continuously to the closed half-box.

On the same one-sided compact time interval, Lemmas 1.1–2.1 give the forcing a representation by transverse derivatives of coefficients continuous up to \(a\). These functions can be extended continuously across \(a\) by their endpoint values. We now perform the reduction of Lemma 2.2 only on the open side \(t>a\), keeping track of continuous endpoint values of every coefficient.

In forming \(F-AU\), all coefficient derivatives in (2.2) extend smoothly, and therefore are bounded and continuous on the smaller closed box. Multiplying them by the continuous primitive coefficients preserves continuous endpoint values. The integrals in (2.5), taken from a fixed interior \(t_0\), also have continuous limits at \(a\), because their integrands are continuous on a compact half-box. Lemma 1.3 on the interior supplies \(w(x')\), whose transverse continuous-primitive representation is independent of time. Thus each reduction lowers the normal degree and preserves continuous extension of the coefficients. Finitely many nested spatial boxes permit all reductions. The final degree-zero representation defines a weakly continuous curve up to \(a\), and Lemma 1.2 makes it strongly continuous.

These endpoint curves agree on overlaps: they agree for \(t>a\) by interior uniqueness, and their scalar pairings have the same limits at \(a\). U021 B0 therefore glues them at the endpoint. The finite test decomposition used in Lemma 2.2 proves continuity of the resulting global curve on \(Y\).

The right side \(G=F-AU\) of the companion system is now continuous on the closed half-interval, by the moving-test estimate in Theorem 3.1. Identity (3.2), initially valid for interior \(t\), extends to \(a\) in every scalar pairing; a common order controls the integral. The same strong average estimate, with \(h>0\) at \(a\), gives its one-sided derivative \(G(a)\). The companion identities then give all \(m\) one-sided derivatives and their strong continuity. Every equation used in this argument was on the original interior or was its continuous limit. \(\square\)

## Traces create boundary sources under zero extension

**Proposition 5.1 (all normal derivatives of a zero extension).** Let \(a<b\) be finite and \(u\in C^m([a,b];\mathcal D'(Y))\). Its zero extension is the distribution
\[
                     W(\Phi)=\int_a^b u(t)(\Phi(\cdot,t))\,dt.       \tag{5.1}
\]
For \(1\le r\le m\),
\[
 \begin{aligned}
 \partial_t^rW={}&1_{(a,b)}u^{(r)}\\
 &+\sum_{j=0}^{r-1}u^{(r-1-j)}(a)\otimes\delta_a^{(j)}\\
 &-\sum_{j=0}^{r-1}u^{(r-1-j)}(b)\otimes\delta_b^{(j)} .
 \end{aligned}                                                       \tag{5.2}
\]
The first term denotes the joint distribution of the restricted curve extended by zero, not a product of arbitrary distributions.

**Proof.** Lemma 1.1 gives the fixed-support bound for (5.1). For a joint test set \(\Phi_t=\Phi(\cdot,t)\). Its scalar pairing obeys
\[
 \frac d{dt}\big(u(t)(\Phi_t)\big)
           =u'(t)(\Phi_t)+u(t)(\partial_t\Phi_t).
\]
To verify this, split the difference quotient as
\[
 \frac{u(t+h)-u(t)}h(\Phi_t)
       +u(t+h)\left(\frac{\Phi_{t+h}-\Phi_t}h\right).
\]
The first term tends to \(u'(t)(\Phi_t)\). In the second, the test quotient tends in every derivative norm to \(\partial_t\Phi_t\); its error is controlled uniformly by Lemma 1.1, and its fixed limiting test is handled by weak continuity of \(u\). The two terms on the resulting right side are continuous, by the same moving-test argument. Scalar integration by parts consequently gives
\[
 \partial_tW=1_{(a,b)}u'+u(a)\otimes\delta_a-u(b)\otimes\delta_b
\]
on every joint test. Apply this to \(u'\) and differentiate the two existing endpoint masses. Repeating the step gives exactly the two sums in (5.2). Tensor derivatives are defined by
\((w\otimes\delta_c^{(j)})(\Phi)=(-1)^jw(\partial_t^j\Phi(\cdot,c))\),
which also checks every sign. \(\square\)

This specifies one particular extension. Another extension can include distributions supported on the endpoint slices, and need not obey (5.2). For a homogeneous equation, the zero extension must include the displayed boundary forcing unless those terms cancel.

## Exercises

**Exercise 1 (basic: a curve with two spatial jets).** Solve on \(\mathbb R_x\times(0,1)_t\)
\[
                 \partial_tu=(1+2t)\delta_2+3t^2\delta'_{-1}.
\]
Describe every joint-distribution solution as a curve. For the solution with \(u(0)=\delta_3\), compute the first derivative of its zero extension.

**Exercise 2 (basic: coefficients acting on a normal jet).** For \(p(t)=1+3t+2t^2\) and \(V=\delta_0(x)\otimes\delta''_0(t)\), find \(pV\) with all signs. Show that \(V\) is not a continuous distribution curve and cannot solve a homogeneous first-order equation (2.3) with smooth transverse coefficients.

**Exercise 3 (intermediate: all initial jets for a pure normal equation).** Given \(m\ge1\), a continuous curve \(f:I\to\mathcal D'(Y)\), \(t_0\in I\), and arbitrary \(v_0,\ldots,v_{m-1}\in\mathcal D'(Y)\), prove that the unique solution of \(\partial_t^mu=f\) with these initial derivatives is
\[
 u(t)=\sum_{j=0}^{m-1}\frac{(t-t_0)^j}{j!}v_j
       +\int_{t_0}^t\frac{(t-s)^{m-1}}{(m-1)!}f(s)\,ds.
\]
Include \(t<t_0\) and all strong derivative assertions.

**Exercise 4 (intermediate: sharp time regularity).** For \(0<\sigma<1\), \(m\ge1\) and \(w=\delta'_0\) on \(\mathbb R_x\), set \(u(t)=|t|^{m+\sigma}w\). Find \(u^{(m)}\), including its value at zero. Prove that this gives continuous forcing in a pure normal equation, but \(u\notin C^{m+1}\).

**Exercise 5 (intermediate: second-order boundary forcing).** For \(u(t)=e^t\delta'_0+t^2\delta_0\) on \(0<t<1\), let \(W\) be its zero extension. Compute \((\partial_t^2-1)W\), distinguishing spatial derivatives from time derivatives in every endpoint term.

**Exercise 6 (advanced: arbitrarily high apparent normal degree).** For \(r\ge1\), put \(b_r(x,t)=(x-t)_+^r/r!\). Prove
\[
           \delta_t(x)=(-1)^r\partial_x\partial_t^rb_r
                            =\partial_x^{r+1}b_r.
\]
Check the transport equation and strong smoothness of the curve. Explain why the largest normal degree of a chosen representation is not intrinsic.

**Exercise 7 (advanced: a variable spatial drift and every point jet).** For \(k\ge0\), \(q_0\in\mathbb R\), \(c_0\ne0\), find all smooth real \(q\) and complex \(c\), with these initial values at zero, for which \(u(t)=c(t)\delta_{q(t)}^{(k)}\) solves
\(\partial_tu+(1+t)x\partial_xu=0\). Check the joint equation and the boundary masses in the first derivative of its zero extension from \((0,1)\).

**Exercise 8 (advanced: why distributional extension is needed).** For \(t>0\), consider
\[
             u(x,t)=\sum_{\ell=1}^\infty
                              e^{\sqrt\ell-\ell^2t}e^{i\ell x}.
\]
Prove smoothness, periodicity and the heat equation. Construct compact spatial tests isolating each Fourier mode. Show that there is no distributional trace at zero and no joint distributional extension across zero; use time tests at scale \(\ell^{-2}\) for the latter.

## Complete solutions

**Solution 1.** The curve \(u_0(t)=(t+t^2)\delta_2+t^3\delta'_{-1}\) has the required derivative. Lemma 1.3 applied to any other solution minus \(u_0\) gives all solutions
\[
                       u(t)=u_0(t)+w,\qquad w\in\mathcal D'(\mathbb R).
\]
Multiplication of a fixed distribution by a smooth scalar function has the corresponding strong derivatives: for every bounded \(B\), the seminorm of the error is the scalar error times the finite number \(q_B(w)\). Thus all these curves are strongly smooth. The initial value selects \(w=\delta_3\), giving \(u(1)=2\delta_2+\delta'_{-1}+\delta_3\). Formula (5.2) gives
\[
 \begin{aligned}
 \partial_tW={}&1_{(0,1)}u'
            +\delta_3(x)\otimes\delta_0(t)\\
       &-(2\delta_2+\delta'_{-1}+\delta_3)(x)\otimes\delta_1(t).
 \end{aligned}
\]

**Solution 2.** Directly,
\[
 (p\delta''_0)(\eta)=(p\eta)''(0)
       =\eta''(0)+6\eta'(0)+4\eta(0),
\]
so
\[
              pV=\delta_0(x)\otimes
                           (\delta''_0-6\delta'_0+4\delta_0)(t).
\]
If \(V\) came from a continuous curve, pair in \(x\) with a test equal to one at zero. The resulting continuous function of \(t\) would represent \(\delta''_0\). Its restriction off zero would be zero, by the continuous-function test argument in Lemma 1.2; continuity would then make it zero also at zero. But \(\delta''_0\ne0\), as seen by testing with \(t^2/2\) times a cutoff equal to one near zero. This is a contradiction. Lemma 2.2 would make any solution of the proposed homogeneous equation a continuous curve, so \(V\) cannot be one.

**Solution 3.** Denote the integral term by \(R(t)\). Lemma 1.1 bounds all its test pairings by a single finite-order seminorm on compact time intervals, proving it is a distribution. Scalar differentiation of the oriented integral gives
\[
 R^{(r)}(t)=\int_{t_0}^t
           \frac{(t-s)^{m-1-r}}{(m-1-r)!}f(s)\,ds
       \quad(0\le r<m),\qquad R^{(m)}(t)=f(t).
\]
For \(r<m-1\) the upper-end kernel is zero; for \(r=m-1\) the next derivative is the fundamental-theorem derivative. These identities follow also for \(t<t_0\) by writing the integral as minus the integral from \(t\) to \(t_0\). Each displayed curve is weakly continuous, using the common bound and continuity of its scalar integrands, hence strongly continuous by Lemma 1.2. Differences of successive curves are integrals of the next curve by scalar calculus and Fubini; the strong average estimate from Theorem 3.1 proves that their derivatives are strong derivatives. All derivatives of \(R\) of order less than \(m\) vanish at \(t_0\).

Differentiating the polynomial term gives initial derivative \(v_r\) at order \(r<m\), and zero at order \(m\). This proves existence with the claimed data. Any joint solution is \(C^m\) by Theorem 3.1. The difference of two solutions with the same initial data has zero \(m\)-th derivative. In each scalar pairing its \((m-1)\)-st derivative is constant by the scalar fundamental theorem and zero at \(t_0\). Repeating downward makes every lower derivative zero. Test pairings separate distributions, proving uniqueness.

**Solution 4.** Put \(C_{m,\sigma}=\prod_{j=1}^m(\sigma+j)\). Direct differentiation on each half-line gives
\[
 u^{(m)}(t)=
 \begin{cases}
 C_{m,\sigma}\operatorname{sgn}(t)^m|t|^\sigma w,&t\ne0,\\
 0,&t=0.
 \end{cases}
\]
For any \(r\le m\), the half-line derivative of order \(r\) is a constant times a sign and \(|t|^{m+\sigma-r}\). Inductively its claimed value zero at the origin is its true derivative value: the previous derivative's difference quotient has magnitude a constant times \(|t|^{m+\sigma-r}\to0\). Thus all these derivatives are continuous. Multiplication by fixed \(w\) gives strong derivatives as in Solution 1, and scalar integration by parts shows that the joint derivatives are the same.

Choose \(\varphi\) with \(w(\varphi)\ne0\), for example \(x\) times a cutoff near zero. The magnitude of the difference quotient of \(u^{(m)}(t)(\varphi)\) at zero is
\(C_{m,\sigma}|w(\varphi)||t|^{\sigma-1}\), which tends to infinity. There is no next weak derivative there, hence no next strong derivative. The displayed \(m\)-th derivative is the continuous forcing.

**Solution 5.** Calculation in the interior gives \(u''-u=(2-t^2)\delta_0(x)\). The endpoint values are
\[
 \begin{array}{ll}
 u(0)=\delta'_0,&u'(0)=\delta'_0,\\
 u(1)=e\delta'_0+\delta_0,&u'(1)=e\delta'_0+2\delta_0.
 \end{array}
\]
Use (5.2) at order two and subtract \(W\):
\[
 \begin{aligned}
 (\partial_t^2-1)W={}&1_{(0,1)}(t)(2-t^2)\delta_0(x)\\
 &+\delta'_0(x)\otimes\delta_0(t)
       +\delta'_0(x)\otimes\delta'_0(t)\\
 &-(e\delta'_0+2\delta_0)(x)\otimes\delta_1(t)\\
 &-(e\delta'_0+\delta_0)(x)\otimes\delta'_1(t).
 \end{aligned}
\]
Every prime on the \(x\) factor differentiates space; every prime on the \(t\) factor differentiates time.

**Solution 6.** The function \(b_r\) is continuous. In the linear coordinates \(s=x-t,\ t=t\), the operator \(\partial_t+\partial_x\) differentiates only the second coordinate, and \(b_r=s_+^r/r!\) is independent of it. The linear substitution has Jacobian one; integration by parts against joint tests proves \(\partial_tb_r=-\partial_xb_r\) as distributions. Repeated scalar integration by parts gives
\(\partial_x^rb_r=1_{\{x>t\}}\), and one further derivative pairs with \(\Phi\) as \(\int\Phi(t,t)\,dt\). This is the joint distribution of \(\delta_t\), proving both representations.

Its transport equation can also be checked without coordinates:
\[
       -\int_{\mathbb R}(\partial_t+\partial_x)\Phi(t,t)\,dt
             =-\int_{\mathbb R}\frac d{dt}\Phi(t,t)\,dt=0.
\]
The point-parameter proof in Section 3 gives every strong derivative
\((-1)^j\delta_t^{(j)}\). One representation of the same curve has normal degree \(r\), and another has degree zero. Since \(r\) is arbitrary, this degree describes the representation rather than the curve's regularity.

**Solution 7.** Section 3 and the test product rule give
\[
 \partial_t(c\delta_q^{(k)})
     =c'\delta_q^{(k)}-cq'\delta_q^{(k+1)},\qquad
 x\delta_q^{(k+1)}
     =q\delta_q^{(k+1)}-(k+1)\delta_q^{(k)}.
\]
For the second identity, differentiating \(x\varphi(x)\) \(k+1\) times at \(q\) yields
\(q\varphi^{(k+1)}(q)+(k+1)\varphi^{(k)}(q)\), with the delta-derivative signs producing the formula. Substitution into the equation gives
\[
 [c'-(k+1)(1+t)c]\delta_q^{(k)}
                  +c[(1+t)q-q']\delta_q^{(k+1)}=0.
\]
The two point jets are independent: cutoff multiples of
\((x-q)^k/k!\) and \((x-q)^{k+1}/(k+1)!\) prescribe the two derivatives separately. Let \(r(t)=t+t^2/2\). The first scalar equation says
\((e^{-(k+1)r}c)'=0\), hence \(c=c_0e^{(k+1)r}\), which never vanishes. Dividing the second equation by \(c\) gives \((e^{-r}q)'=0\). The only possibilities are therefore
\[
               c(t)=c_0e^{(k+1)(t+t^2/2)},\qquad
               q(t)=q_0e^{t+t^2/2}.
\]
They satisfy the initial data and make the two coefficients zero, including when \(q_0=0\). Their curve is strongly smooth by Section 3. The moving-test product rule in Proposition 5.1 integrates the curve equation to the joint equation.

For the zero extension from \((0,1)\), the first derivative is \(1_{(0,1)}u'\) plus
\[
 c_0\delta_{q_0}^{(k)}(x)\otimes\delta_0(t)
 -c_0e^{3(k+1)/2}\delta_{q_0e^{3/2}}^{(k)}(x)\otimes\delta_1(t).
\]
In particular the amplitude exponent is \(k+1\), not merely the exponent of the point trajectory.

**Solution 8.** On \(t\ge\varepsilon>0\), any mixed derivative of a summand is bounded by \(\ell^N e^{\sqrt\ell-\varepsilon\ell^2}\) for some fixed \(N\). For sufficiently large \(\ell\), \(\sqrt\ell\le\varepsilon\ell^2/2\), and a further quadratic exponential dominates \(\ell^N\). The tail is bounded by a convergent geometric series. Thus all differentiated series converge uniformly on compact subsets. Passing the scalar fundamental theorem through uniform limits identifies these series as the derivatives of the sum, successively in each coordinate. This proves smoothness and periodicity. Both \(\partial_t\) and \(\partial_x^2\) multiply each summand by \(-\ell^2\), proving the heat equation.

Choose a nonnegative smooth \(\rho\) supported in \((-2\pi,2\pi)\) and equal to one on \([-\pi,\pi]\). Put
\[
 S(x)=\sum_{j\in\mathbb Z}\rho(x+2\pi j),\qquad \eta(x)=\rho(x)/S(x).
\]
The sum is locally finite, smooth, \(2\pi\)-periodic and at least one. Therefore \(\eta\) is a smooth compact test and
\(\sum_j\eta(x+2\pi j)=1\). Splitting the integral into periods gives, for integer \(h\),
\[
 \int_{\mathbb R}\eta(x)e^{ihx}\,dx
 =\int_{-\pi}^{\pi}e^{ihx}\,dx
 =\begin{cases}2\pi,&h=0,\\0,&h\ne0.\end{cases}
\]
Only finitely many translates contribute on this period; the last equality is the elementary exponential integral. Hence the tests
\(\varphi_\ell(x)=\eta(x)e^{-i\ell x}\) have one fixed compact support, derivative bounds
\(p_N(\varphi_\ell)\le C_N\ell^N\), and
\[
                       u(t)(\varphi_\ell)=2\pi e^{\sqrt\ell-\ell^2t}.
\]
The pairing follows by uniform convergence of the series on the compact test support at each fixed \(t>0\).

Suppose there were a trace \(T\in\mathcal D'(\mathbb R)\). For each fixed \(\ell\), let \(t\downarrow0\) in the last identity to obtain
\(T(\varphi_\ell)=2\pi e^{\sqrt\ell}\). On the common compact support \(T\) has some finite order \(N\), so these values would be bounded by \(C C_N\ell^N\), an impossibility. Indeed \(\sqrt\ell-N\log\ell\to+\infty\). For an elementary check, put \(y=\sqrt\ell\); the exponential series implies \(e^{y/2}\ge (y/2)^M/M!\) for every fixed \(M\), so \(e^y/y^{2N}\to\infty\) by choosing \(M>2N\).

Finally, take nonzero \(h\ge0\) in \(\mathcal D((1/2,3/2))\) and
\(\Phi_\ell(x,t)=\varphi_\ell(x)h(\ell^2t)\). For all sufficiently large \(\ell\), these tests lie in one fixed compact product box crossing zero, inside any proposed extension neighbourhood. Their derivatives of total order at most \(N\) are bounded by \(C_N\ell^{2N}\). Since their supports have \(t>0\), any extension \(\widetilde U\) must give
\[
 \widetilde U(\Phi_\ell)
       =2\pi\ell^{-2}e^{\sqrt\ell}
                            \int_0^\infty e^{-s}h(s)\,ds.
\]
This follows from the isolated-mode identity and \(s=\ell^2t\). The last integral is strictly positive and independent of \(\ell\). These pairings grow faster than every \(\ell^{2N}\), contradicting the finite-order bound of a distribution on that box. There is no joint distributional extension. Constant coefficients and zero forcing therefore do not dispense with the solution-extension hypothesis in Theorem 4.2.

## Programme proof locations and freely accessible sources

- Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, version October 2, 2026, [freely accessible MIT notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), Sections 3.1–3.2, Proposition 3.2 and the direct proof of Proposition 3.4, Section 5.2.3, and Proposition 6.3. These give the read derivative, zero-integral primitive, product-rule, principal-value and parameter-pairing arguments. The proofs above supply the joint-parameter extension, finite normal-degree reduction and endpoint theorem.
- [Functional foundations](../prerequisites/U011-free-foundations/functional-foundations-U008.md), Sections 6 and 14.1–14.2: complete-metric Baire and completeness of every smooth compact-support test space. Lemma 1.1 above proves the arbitrary-family estimate. This supplied component retains CC0 1.0.
- [Order, positivity and distributional limits](order-positivity-and-limits.md), Proposition 1.2 and Theorem 5.1: finite-order \(C^k\) action, common-order sequence estimates and convergence uniform on bounded smooth test families.
- [Convolution as addition of supports](convolution-as-addition-of-supports.md), B0–B3 and Theorems 1.1–2.1: finite cutoff decompositions, local distribution gluing, tensor operations, finite-regularity convolution and mollification. [Fundamental solutions, continuation and approximation](fundamental-solutions-continuation-and-approximation.md), Theorem 6.1: complete mixed continuous primitives, with finitely many compact coefficients after compact localization.
- [Metric and scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 12–13, give compactness, scalar integration, product and chain rules, exponential functions and smooth cutoffs; [measure and integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.4 and 16, give the convergence and Fubini results, linear changes of variables and test mollification used here. Both components retain CC0 1.0. The retained [finite algebra foundations](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), Section 10, also retain CC0 1.0.
