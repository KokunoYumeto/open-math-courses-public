# Analytic forcing and smooth convolution solutions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A convolution equation can have a very small Fourier multiplier. Analytic forcing still admits a smooth solution on a convex domain. We prove this by building bounded smooth solutions on smaller domains and correcting their differences by homogeneous solutions. The local estimate comes from analytic functionals and a complete space of entire quotients.

Basic references are [Grubb's notes on Fourier transformation of distributions](https://web.math.ku.dk/~grubb/dist5.pdf), [Melrose's introduction to tempered distributions](https://math.mit.edu/~rbm/iml/Chapter1.pdf), and Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. The arguments needed here are given below or in the linked preceding lessons.

The main prerequisite is Exponential-polynomial solutions and convex approximation: Theorem 3.1 proves the convex carrier and growth of an entire quotient, Lemma 4.1 proves uniform Gaussian approximation in a complex neighborhood of a compact real set, and Theorem 5.1 proves density in the homogeneous convolution kernel. We also use Fourier transforms of analytic functionals on a real convex carrier, Theorems AF1 and AF8; Fourier indicators and the convex hull of a measure's support, Theorem MI1; and Compact Fourier division and multiplicity-sensitive annihilators, for Fourier injectivity. The complete-metric Baire theorem and normed Hahn–Banach are proved in Sections 6 and 5 of Banach estimates, quotient spaces and compact parameter arguments. The required endpoint representation of an \(L^1\) functional is Theorem 3.1 of Lebesgue duality and the functionals on Fourier spaces.

Smooth cutoffs near compact sets are proved in Section 13.10 of Metric and topological foundations. We construct the convex exhaustion explicitly rather than assuming an exhaustion with the necessary kernel margins.

## 1. The domain where the equation makes sense

Let \(0\ne\mu\in\mathcal E'(\mathbb R^n)\), write \(S=\operatorname{supp}\mu\), and use the bilinear distribution pairing. Reflection is
\[
 \check\mu(\phi)=\mu(\phi(-\,\cdot)),\qquad
 \check\psi(x)=\psi(-x).
 \tag{1.1}
\]
For an open convex \(X\subset\mathbb R^n\), set
\[
 X_\mu=\{x:x-S\subset X\}.
 \tag{1.2}
\]
If \(u\in C^\infty(X)\), then
\[
 (\mu*u)(x)=\mu_y\bigl(u(x-y)\bigr),\qquad x\in X_\mu.
 \tag{1.3}
\]
Compactness of \(S\) provides a fixed neighborhood of \(S\) on which the test in (1.3) is defined for all \(x\) near any given point. A cutoff on that neighborhood makes the pairing precise and independent of cutoff. Finite distributional order permits differentiation in \(x\), so (1.3) is smooth. Compactness also makes \(X_\mu\) open. It is convex because \(X_\mu=\bigcap_{y\in S}(X+y)\). It may be empty.

**Theorem 1.1 (analytic forcing).** Every real-analytic, possibly complex-valued function \(f\) on \(X_\mu\) has a solution \(u\in C^\infty(X)\) satisfying
\[
 \mu*u=f\quad\hbox{on }X_\mu.
 \tag{1.4}
\]
The distribution \(\mu\) need not be invertible and need not have finite support. The domain need not be bounded. The conclusion concerns smooth solutions; it imposes no uniform bound on their growth and no analytic regularity on them.

Empty \(X\) or empty \(X_\mu\) gives the assertion by taking the zero function. We prove the remaining case in Section 5 after establishing the local estimate.

## 2. A complete space of entire quotients

For a compact distribution \(a\), write
\[
 F_a(\zeta)=a_x(e^{-ix\cdot\zeta}),\qquad \zeta\in\mathbb C^n.
 \tag{2.1}
\]
For a compact convex real set \(D\), its support function is
\[
 H_D(\eta)=\sup_{x\in D}x\cdot\eta.
 \tag{2.2}
\]
Fix a nonzero \(\psi\in C_c^\infty(\mathbb R^n)\) and put
\[
 \rho=\check\mu*\psi,\quad
 A=F_\rho=F_\mu(-\,\cdot)F_\psi,\quad
 L=\operatorname{conv}\operatorname{supp}\rho .
 \tag{2.3}
\]
The function \(\rho\) is smooth and compactly supported. It is nonzero: both factors of its entire transform are nonzero by Fourier injectivity, their product is nonzero, and injectivity applies again. Thus \(A\not\equiv0\), and \(L\) is nonempty and compact. Finite-dimensional affine dependence reduces convex combinations to at most \(n+1\) points; this proves compactness of the hull.

We first establish the local estimate that allows zeros of \(A\).

**Lemma 2.1 (bounded division on compact sets).** For every compact \(Q\subset\mathbb C^n\), there are a compact \(Q'\subset\mathbb C^n\) and \(c_Q<\infty\) such that
\[
 \sup_Q|\Phi|\le c_Q\sup_{Q'}|A\Phi|
 \tag{2.4}
\]
for every entire \(\Phi\).

*Proof.* Fix \(z_0\). The first nonzero homogeneous Taylor term of \(A\) at \(z_0\) is a nonzero polynomial \(P\). Choose a complex vector \(\theta\) with \(P(\theta)\ne0\), so the one-variable function \(t\mapsto A(z_0+t\theta)\) is not identically zero. Its zeros are isolated. Choose \(r>0\) so it has no zero on \(|t|=r\). The positive minimum there persists for \(z\) in a sufficiently small closed neighborhood \(Q_0\) of \(z_0\): for one \(a_0>0\),
\[
 |A(z+t\theta)|\ge a_0
        \quad(z\in Q_0,\ |t|=r).
 \tag{2.5}
\]
Continuity on the compact circle supplies this persistence. Cauchy's formula applied to the entire function \(t\mapsto\Phi(z+t\theta)\) gives
\[
 |\Phi(z)|\le \sup_{|t|=r}|\Phi(z+t\theta)|
      \le a_0^{-1}\sup_{z\in Q_0,\ |t|=r}|A(z+t\theta)\Phi(z+t\theta)|.
 \tag{2.6}
\]
Cover \(Q\) by finitely many interiors of such \(Q_0\). Their finitely many translated circles form a compact \(Q'\); the maximum of the finitely many reciprocal lower bounds proves (2.4). This proof does not divide at a zero or assume a lower bound for \(A\) on \(Q\). \(\square\)

Fix a nonempty compact convex real \(D\). Define
\[
 \mathcal B_D=\left\{\Phi\hbox{ entire}:
 \|\Phi\|_{\mathcal B_D}
 :=\sup_{\zeta\in\mathbb C^n}|A(\zeta)\Phi(\zeta)|
       e^{-H_L(\operatorname{Im}\zeta)-H_D(\operatorname{Im}\zeta)}
       <\infty\right\}.
 \tag{2.7}
\]

**Lemma 2.2.** Formula (2.7) is a norm and makes \(\mathcal B_D\) complete. Its norm convergence implies locally uniform convergence of the entire functions and of all their derivatives.

*Proof.* The triangle inequality and scalar homogeneity follow from the supremum. If the norm is zero, then \(A\Phi=0\); on the nonempty open set where \(A\ne0\), \(\Phi=0\), and the identity theorem gives \(\Phi=0\) everywhere.

On a compact \(Q'\), the exponential weight and its reciprocal are bounded, because support functions are continuous. Lemma 2.1 therefore gives
\[
 \sup_Q|\Phi|\le C_Q\|\Phi\|_{\mathcal B_D}.
 \tag{2.8}
\]
Cauchy's formula on slightly larger compact polydisks gives the corresponding bound for each derivative. Thus a norm-Cauchy sequence \(\Phi_j\) converges uniformly on every compact, with all derivatives, to an entire \(\Phi\). Entirety follows by the local Cauchy formula, or by convergence of its derivative formulas.

Given \(\varepsilon>0\), choose \(N\) so \(\|\Phi_j-\Phi_k\|_{\mathcal B_D}\le\varepsilon\) for \(j,k\ge N\). For each \(\zeta\), pass to the limit \(k\to\infty\) in the weighted pointwise inequality. Taking the supremum gives \(\|\Phi_j-\Phi\|_{\mathcal B_D}\le\varepsilon\) for \(j\ge N\). One such \(j\) also proves that \(\Phi\) has finite norm. This proves completeness and convergence in the original norm. \(\square\)

## 3. From individual carriers to one uniform bound

**Lemma 3.1 (the carrier of a quotient).** Every \(\Phi\in\mathcal B_D\) is the Fourier transform of a unique analytic functional \(v_\Phi\) carried by \(D\). For every complex neighborhood \(V\) of \(D\), this functional has a bound by the supremum on a compact subset of \(V\). It acts on holomorphic germs near \(D\), and
\[
 v_\Phi(P)=P(i\partial_\zeta)\Phi(0)
 \tag{3.1}
\]
for every polynomial \(P\) on the real variables.

*Proof.* The zero function is immediate. For nonzero \(\Phi\), put
\[
 p_1=\log|A|,\quad p_2=\log|\Phi|,\quad p_3=\log|A\Phi|.
 \tag{3.2}
\]
These are proper plurisubharmonic functions, and \(p_3=p_1+p_2\) with their values at zeros interpreted by their logarithms. The precise proper-logarithm statement is Lemma Z2 of Fourier endpoints and the asymptotic density of zeros.

The compact-measure indicator theorem applied to the nonzero smooth density \(\rho\) gives the horizontal-envelope indicator \(H_1=H_L\), as well as an imaginary-linear upper bound for \(p_1\). The defining norm gives
\[
 p_3(\zeta)\le
 \log\|\Phi\|_{\mathcal B_D}
       +H_L(\operatorname{Im}\zeta)+H_D(\operatorname{Im}\zeta).
 \tag{3.3}
\]
In particular \(p_3\) has an imaginary-linear upper bound and its indicator satisfies \(H_3\le H_L+H_D\).

The full quotient-carrier theorem, Theorem 3.1 of Exponential-polynomial solutions and convex approximation, now gives a nonempty compact convex real \(K_\Phi\) such that
\[
 H_{K_\Phi}=H_3-H_L\le H_D,\qquad
 |\Phi(\zeta)|\le C_{\Phi,\varepsilon}
 e^{H_{K_\Phi}(\operatorname{Im}\zeta)+\varepsilon|\zeta|}
          \quad(\varepsilon>0).
 \tag{3.4}
\]
The support-function separation characterization, proved with the support-function theorem in Plurisubharmonic envelopes and support functions, gives \(K_\Phi\subset D\). Replacing \(H_{K_\Phi}\) by \(H_D\) preserves (3.4). Theorem AF1 supplies the unique analytic functional carried by \(D\), and Theorem AF8 supplies its action on germs and its local supremum bounds. Differentiating \(v_\Phi(e^{-ix\cdot\zeta})=\Phi(\zeta)\) at zero yields \(v_\Phi(x^\alpha)=i^{|\alpha|}\partial^\alpha\Phi(0)\), proving (3.1). These are real convex carriers; no assertion about an arbitrary complex carrier is used. \(\square\)

**Lemma 3.2 (uniform moments).** Let \(K\subset\mathbb C^n\) be compact and have \(D\) in its interior. There is a constant \(C_K<\infty\), independent of \(\Phi\) and \(P\), such that
\[
 |v_\Phi(P)|\le C_K\|\Phi\|_{\mathcal B_D}\sup_K|P|
       \quad(\Phi\in\mathcal B_D,\ P\hbox{ polynomial}).
 \tag{3.5}
\]
The same bound holds for every entire function in place of \(P\).

*Proof.* For a positive integer \(m\), let
\[
 \mathcal C_m=\{\Phi\in\mathcal B_D:
       |P(i\partial)\Phi(0)|\le m\sup_K|P|
                \text{ for every polynomial }P\}.
 \tag{3.6}
\]
Each polynomial-moment map is norm-continuous by Lemma 2.2 and Cauchy's derivative bounds. Thus \(\mathcal C_m\), an intersection of closed inequalities, is closed. It is convex and balanced. Each \(\Phi\) belongs to some \(\mathcal C_m\): Lemma 3.1 bounds its functional by the supremum on a compact neighborhood of \(D\) contained in \(\operatorname{int}K\), hence by the supremum on \(K\).

Completeness from Lemma 2.2 and the complete-metric Baire theorem imply that some \(\mathcal C_m\) contains an open norm ball \(B(\Phi_0,r)\), \(r>0\). If \(\|h\|<r\), both \(\Phi_0+h\) and \(\Phi_0\) are in \(\mathcal C_m\). Subtracting their moment inequalities gives
\[
 |P(i\partial)h(0)|\le2m\sup_K|P|.
 \tag{3.7}
\]
For \(\Phi\ne0\), take \(h=r\Phi/(2\|\Phi\|)\). This proves (3.5) with \(C_K=4m/r\); the zero function is trivial. The argument also covers the zero Banach space by taking any finite constant.

For an entire \(F\), its Taylor polynomials at zero converge uniformly on \(K\) and on a compact neighborhood of \(D\): use a polydisk containing these compact sets and the absolutely convergent Taylor series on a larger polydisk. Continuity of \(v_\Phi\) from Lemma 3.1 permits passing to the limit in (3.5). Hence
\[
 |v_\Phi(F)|\le C_K\|\Phi\|_{\mathcal B_D}\sup_K|F|.
 \tag{3.8}
\]
The Baire theorem is applied to the complete space of quotients. No completeness of the polynomials or of the space of restrictions of entire functions on \(K\) is needed. \(\square\)

## 4. A bounded smooth solution on a smaller domain

**Theorem 4.1 (local smoothing estimate).** Let \(Y\) be bounded, open and convex, with \(\overline Y\subset X\). For every nonzero \(\psi\in C_c^\infty(\mathbb R^n)\), there is a bounded smooth function \(U\) on \(\mathbb R^n\) such that
\[
 \mu*U=f\ \hbox{on }Y_\mu,\qquad
 \|\partial^\alpha U\|_\infty\le
       C\sup_K|\widetilde f|\,\|\partial^\alpha\psi\|_1
             \quad(\alpha\in\mathbb N^n).
 \tag{4.1}
\]
Here \(\widetilde f\) is a holomorphic extension near
\(D=\overline{Y_\mu}\), \(K\) is a sufficiently small compact complex neighborhood of \(D\), and \(C\) depends on \(\mu,\psi,D,K\), but not on \(\alpha\). If \(Y_\mu\) is empty, take \(U=0\) and omit \(D,K\).

*Proof.* Assume \(Y_\mu\ne\varnothing\). Since \(S\ne\varnothing\), choosing \(s_0\in S\) gives \(Y_\mu\subset Y+s_0\), so its closure \(D\) is bounded. It is compact and convex. Also
\[
 D-S\subset\overline Y\subset X,\qquad D\subset X_\mu.
 \tag{4.2}
\]
The first inclusion follows by taking limits in \(x-s\in Y\) for each fixed \(s\). The second uses the definition (1.2); compactness then supplies a positive margin inside the open set \(X_\mu\).

Real-analytic power series extend \(f\) to a complex neighborhood of \(D\). They agree on overlapping sufficiently small real-centered polydisks: their real values agree, and repeated one-variable identity theorems extend that agreement to the connected complex intersections. The gluing argument and the Gaussian conclusion are proved in Lemma 4.1 of the preceding approximation lesson.

Choose \(\chi\in C_c^\infty(X_\mu)\) equal to one near \(D\), and extend \(g=\chi f\) by zero to a smooth compactly supported function on the real space. The Gaussian entire functions
\[
 G_j(z)=\left(\frac j\pi\right)^{n/2}
       \int_{\mathbb R^n}e^{-j\sum_k(z_k-t_k)^2}g(t)\,dt
 \tag{4.3}
\]
converge uniformly to \(\widetilde f\) on a fixed complex neighborhood of \(D\). Lemma 4.1 of the preceding lesson proves this for a general nonzero germ, including all vertical contour faces. Thus for sufficiently small \(\delta>0\), the compact convex set
\[
 K=D+\{z\in\mathbb C^n:|z|\le\delta\}
 \tag{4.4}
\]
is contained in that neighborhood and in the domain of \(\widetilde f\), and \(G_j\to\widetilde f\) uniformly on \(K\). The set \(D\) lies in its interior.

Use this \(D\) in \(\mathcal B_D\). Lemma 3.1 gives continuity of \(v_\Phi\) on the holomorphic germs near \(D\). Pass to the limit in (3.8), with \(F=G_j\), to obtain the single bound
\[
 |v_\Phi(\widetilde f)|
       \le C_K\|\Phi\|_{\mathcal B_D}\sup_K|\widetilde f|.
 \tag{4.5}
\]
For \(\phi\in C_c^\infty(Y_\mu)\), take \(\Phi=F_\phi\) and
\(q=\rho*\phi=\check\mu*\psi*\phi\). Its support is contained in \(L+D\), so direct integration gives
\[
 |A(\zeta)\Phi(\zeta)|=|F_q(\zeta)|
       \le\|q\|_1e^{H_L(\operatorname{Im}\zeta)+H_D(\operatorname{Im}\zeta)}.
 \tag{4.6}
\]
Consequently \(\Phi\in\mathcal B_D\) and
\(\|\Phi\|_{\mathcal B_D}\le\|q\|_1\). The compact smooth distribution \(\phi\) itself is an analytic functional carried by \(D\) with transform \(F_\phi\). Uniqueness in Theorem AF1 identifies it with \(v_\Phi\). Its germ action is ordinary integration. Formula (4.5) becomes
\[
 \left|\int f(x)\phi(x)\,dx\right|
 \le C_K\sup_K|\widetilde f|\
                 \|\check\mu*\psi*\phi\|_1.
 \tag{4.7}
\]
This is a uniform estimate over every test function in \(Y_\mu\); the constants do not depend on its support, order or individual Fourier quotient.

On the linear subspace
\(\mathcal R=\{\check\mu*\psi*\phi:\phi\in C_c^\infty(Y_\mu)\}\)
of \(L^1(\mathbb R^n)\), define
\[
 T(\check\mu*\psi*\phi)=\int f\phi .
 \tag{4.8}
\]
Inequality (4.7) makes this well-defined, including two tests giving the same image, and bounds its norm by \(C_K\sup_K|\widetilde f|\). Normed complex Hahn–Banach extends it to all of \(L^1\). The full \(p=1\) representation in the linked Lebesgue-duality theorem gives a \(v\in L^\infty\) such that
\[
 T(q)=\int v(x)q(x)\,dx,\qquad
 \|v\|_\infty\le C_K\sup_K|\widetilde f|.
 \tag{4.9}
\]
That theorem writes a conjugate on its representing density; absorb it into \(v\). Our distribution pairing remains bilinear.

Set
\[
 U=v*\check\psi,\qquad
 U(x)=\int v(t)\psi(t-x)\,dt.
 \tag{4.10}
\]
Every derivative of the translated compact kernel is integrable. Difference quotients converge in \(L^1\), by the fundamental theorem of calculus and translation continuity, so differentiation under (4.10) gives
\[
 \partial^\alpha U(x)=(-1)^{|\alpha|}
       \int v(t)(\partial^\alpha\psi)(t-x)\,dt,\qquad
 \|\partial^\alpha U\|_\infty\le
              \|v\|_\infty\|\partial^\alpha\psi\|_1.
 \tag{4.11}
\]
Translation continuity of these \(L^1\) kernels makes every derivative continuous. This proves smoothness and (4.1).

For a test \(\phi\) in \(Y_\mu\), compact supports, finite order of \(\mu\), and boundedness of \(v\) justify the two transposes below. Equivalently first differentiate the compact smooth kernels, use their uniform integrable bounds, and then apply the finite-order pairing:
\[
\begin{aligned}
 \langle\mu*U,\phi\rangle
 &=\int U(x)(\check\mu*\phi)(x)\,dx\\
 &=\int v(t)(\psi*\check\mu*\phi)(t)\,dt\\
 &=T(\check\mu*\psi*\phi)=\int f\phi.
\end{aligned}
\tag{4.12}
\]
In the middle equality the inner integral is
\(\int\psi(t-x)(\check\mu*\phi)(x)\,dx\);
it uses \(\psi\), whereas \(U\) uses \(\check\psi\). Thus \(\mu*U=f\) distributionally on \(Y_\mu\). Both sides are smooth there, so the equality is pointwise. \(\square\)

## 5. Summable corrections across a convex exhaustion

*Proof of Theorem 1.1.* We give the domain and convergence details. If \(X=\mathbb R^n\), interpret distance to its empty complement as \(+\infty\). Choose an integer \(N\) so the following sets are nonempty, and put \(r_j=N+j\):
\[
 Y_j=\{x:|x|<r_j,\ 
             \operatorname{dist}(x,\mathbb R^n\setminus X)>1/r_j\},
 \qquad K_j=\overline{Y_j}.
 \tag{5.1}
\]
Each \(Y_j\) is open, bounded and convex. For the last assertion, its distance condition is equivalent to
\(x+\overline B(0,1/r_j)\subset X\), an intersection of translates of the convex set \(X\); intersect with the open ball. Compactness of the closed ball makes the strict distance condition open. Closure satisfies \(|x|\le r_j\) and distance at least \(1/r_j\), so
\[
 K_j\subset Y_{j+1},\qquad \bigcup_jY_j=X.
 \tag{5.2}
\]
The union assertion follows from positive distance at each point of the open set and \(r_j\to\infty\).

Write \(Z_j=(Y_j)_\mu\). They are nested open convex sets and
\[
 \overline{Z_j}\subset Z_{j+1},\qquad
 \bigcup_j Z_j=X_\mu .
 \tag{5.3}
\]
Indeed \(\overline{Z_j}-S\subset K_j\subset Y_{j+1}\). For \(x\in X_\mu\), its entire compact set \(x-S\) is contained in \(X\), hence in one \(Y_j\) by a finite subcover of this nested exhaustion. This proves the union. The same argument applies to \(Q-S\) for any compact \(Q\subset X_\mu\).

Theorem 4.1 supplies a global smooth \(V_j\) satisfying
\(\mu*V_j=f\) on \(Z_j\). If \(Z_j\) is empty, use \(V_j=0\). Set \(u_1=V_1\) and \(u_2=V_2\). For \(j\ge3\), suppose \(u_{j-1}\) is globally smooth and satisfies the equation on \(Z_{j-1}\). Then
\[
 \mu*(V_j-u_{j-1})=0\quad\hbox{on }Z_{j-1}.
 \tag{5.4}
\]
Apply Theorem 5.1 of the preceding approximation lesson on the domain \(Y_{j-1}\). Its compact set is \(K_{j-2}\subset Y_{j-1}\), its derivative order is \(j\), and its tolerance is \(2^{-j}\). It gives a finite exponential-polynomial global homogeneous solution \(h_j\) such that
\[
 \max_{|\alpha|\le j}\sup_{K_{j-2}}
       |\partial^\alpha(V_j-u_{j-1}-h_j)|<2^{-j}.
 \tag{5.5}
\]
Define \(u_j=V_j-h_j\). Subtracting \(h_j\) preserves the equation on \(Z_j\), and (5.5) says precisely that the successive corrected solutions differ by a summable amount on the indicated compact set.

Fix any compact \(Q\subset X\) and derivative order \(m\). There is \(J\ge\max(3,m)\) with \(Q\subset K_{J-2}\). For \(j\ge J\), nesting and (5.5) give the bound \(2^{-j}\) for each derivative of order at most \(m\) on \(Q\). Therefore, for \(b>a\ge J-1\),
\[
 \max_{|\alpha|\le m}\sup_Q
       |\partial^\alpha(u_b-u_a)|
       \le \sum_{j=a+1}^{b}2^{-j}\le2^{-a}.
 \tag{5.6}
\]
The sequence is Cauchy in every \(C^\infty(X)\) seminorm. The full completeness proof in Section 14.2 of the Banach foundation, obtained from uniform limits of derivatives on small balls and the fundamental theorem of calculus, gives a smooth limit \(u\) on all of \(X\). Equivalently the same small-ball argument shows that the limiting derivative fields are the derivatives of the limiting function. There is no need for a common global bound on the \(u_j\).

Finally take a compact \(Q\subset X_\mu\). The compact set \(Q-S\) lies in \(X\), and hence \(Q\subset Z_N\) for some \(N\). All \(j\ge N\) satisfy \(\mu*u_j=f\) near \(Q\). A slightly larger compact neighborhood of \(Q\) inside \(X_\mu\), together with a fixed cutoff near \(S\), bounds each derivative of \(\mu*(u_j-u)\) by finitely many derivatives of \(u_j-u\) on a compact subset of \(X\). Their limits are zero. Thus \(\mu*u=f\) on \(Q\). As \(Q\) was arbitrary, (1.4) holds everywhere on \(X_\mu\). This completes the proof for every nonzero compact kernel. \(\square\)

The local construction controls derivatives through the chosen smooth kernel \(\psi\). The summable corrections impose compatibility on compact sets, not a global boundedness or analytic-regularity conclusion. Homogeneous solutions may be added to any solution.

## References

- Gerd Grubb, *Distributions and Operators*, Chapter 5, “Fourier transformation of distributions,” freely readable [lecture notes](https://web.math.ku.dk/~grubb/dist5.pdf).
- Richard B. Melrose, *Introduction to Microlocal Analysis*, MIT, 2007, Chapter 1, “Tempered distributions and the Fourier transform,” freely readable [notes](https://math.mit.edu/~rbm/iml/Chapter1.pdf).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 1990.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
- The exact internal proofs used above are the linked quotient-carrier theorem, analytic-functional transform and germ theorems, Gaussian localization and convex approximation theorems, Baire and Hahn–Banach proofs, and the full endpoint Lebesgue-duality theorem.
