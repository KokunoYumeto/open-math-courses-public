# Causal solvability forces hyperbolicity

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A causal solution vanishes before its forcing begins. For a noncharacteristic initial plane, merely asking for a distributional causal solution for every compact smooth forcing already imposes a strong algebraic restriction: complex roots cannot escape arbitrarily far in the negative imaginary time direction. We first turn weak solvability into a continuous smooth inverse, then test that inverse on cutoff exponentials.

Read [Lorentz cones and domain solvability](lorentz-cones-and-domain-solvability.md), the prerequisite statements in [Boundary distance and propagation](boundary-distance-and-propagation.md), [Singular supports and arbitrary distribution data](singular-supports-and-distribution-data.md), and [Symbols at infinity](symbols-at-infinity.md). The exact analytic inputs are the following.

- **Convex continuation.** If \(U\subset V\) are nonempty convex open sets, every characteristic affine hyperplane meeting \(V\) meets \(U\), and a distribution \(w\) satisfies \(P(D)w=0\) in \(V\) and \(w=0\) in \(U\), then \(w=0\) in \(V\). Characteristic normals are nonzero real \(M\) with \(P_m(M)=0\). This is the general theorem declared in the convex-continuation section of the first lesson above; arbitrary complex lower order coefficients are allowed.
- **Characteristic halfspaces.** If \(P_m(N)=0\), a nonzero global smooth homogeneous solution has exact support \(\{x: N\cdot x\geq0\}\). This is the halfspace-solution entry in the second lesson above.
- **Compact singular-support hulls.** For nonzero \(P\) and compact \(v\), the convex hulls of \(\operatorname{singsupp}v\) and \(\operatorname{singsupp}P(D)v\) are equal, with the empty-set convention. This is the singular-support Fourier entry in the third lesson above.
- **Fréchet closed graphs.** A linear map between Fréchet spaces with closed graph is continuous. We use the full Fréchet statement, also used in [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md).

The projection and one-parameter Puiseux lemmas proved in *Symbols at infinity*, Lemmas 2.1 and 3.1, are the semialgebraic tools used below. We also use distribution support, multiplication and differentiation, and the usual topology of smooth functions.

The complete Fréchet closed graph theorem is [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html), Section 14.5. [Continuous functionals, test families and compact limits](continuous-functionals-and-test-families.md) supplies the test-space and seminorm extension tools. General convex continuation and exact characteristic halfspace solutions are planned prerequisites of [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html). The full compact polynomial singular-support hull identity is proved in [Locating singularities through logarithmic Fourier strips](../AN02-L158.html#5-a-nonzero-polynomial-cannot-change-the-compact-singular-hull), Theorem 5.1, including the empty singular-support case. It applies to the transpose because its symbol is the original polynomial evaluated at the negative Fourier variable, which is also nonzero. The bullets below specify the precise statements used.

## Halfspace uniqueness

Let \(P\ne0\) be a complex polynomial of degree \(m\geq0\), with principal homogeneous part \(P_m\), and let \(N\ne0\) be real. Write \(D=-i\partial\) and
\[
H_N=\{x: N\cdot x\geq0\}.
\]
The equation with homogeneous past data means the global distributional equation
\[
P(D)u=f,\qquad \operatorname{supp}u\subset H_N.
\tag{1}
\]
This support condition includes all normal initial traces when a classical solution is extended by zero; no unsupported assertion about arbitrary finite regularity is needed here.

Normalize \(|N|=1\). This leaves the halfspace unchanged. The condition \(P_m(N)\ne0\) is unchanged by a positive scaling, since \(P_m\) is homogeneous. A root barrier for the normalized vector converts to one for the original vector by scaling the imaginary parameter by its positive length.

Suppose \(P_m(N)\ne0\). Let
\[
\mathcal C=\{M\in\mathbb R^n: |M|=1,\ P_m(M)=0\}.
\]
If this set is nonempty, it is compact and contains neither \(N\) nor \(-N\). Consequently
\[
\delta=\min_{M\in\mathcal C}|M-(M\cdot N)N|>0.
\tag{2}
\]
Also \(\delta\leq1\). If \(\mathcal C=\varnothing\), set \(\delta=1\); all arguments about characteristic hyperplanes then have an empty hypothesis list.

If \(P(D)u=0\) globally and \(u\) is supported in \(H_N\), apply the convex continuation theorem with \(V=\mathbb R^n\) and \(U=\{N\cdot x<0\}\). Every characteristic hyperplane meets \(U\): its normal \(M\) is not parallel to \(N\), so \(M\cdot x\) has range all of \(\mathbb R\) on this halfspace. To see this directly, start on that hyperplane and move along the negative projection of \(N\) onto \(M^\perp\); this preserves \(M\cdot x\) and sends \(N\cdot x\) to \(-\infty\). Thus the convex continuation theorem gives \(u=0\).

Conversely, if \(P_m(N)=0\), the characteristic halfspace theorem supplies a nonzero global smooth homogeneous solution with exact support \(H_N\). Hence uniqueness in (1) holds if and only if the boundary is noncharacteristic. The proof retains arbitrary distributions and arbitrary growth. It does not assert uniqueness for characteristic directions on the strength of a familiar well-posedness class.

For \(m=0\), \(P_m=P\ne0\), there are no characteristic normals, and the assertion reduces to the immediate injectivity of multiplication by a nonzero constant.

## A support enclosure with compact time slices

Assume \(P_m(N)\ne0\), and suppose \(u\) is supported in \(H_N\) and \(P(D)u=f\), where \(f\) is compactly supported. Let \(K=\operatorname{supp}f\); if it is empty, the uniqueness argument gives \(u=0\). Choose \(0<\varepsilon<\min(1,\delta^2/2)\), and choose \(A>0\) such that
\[
\theta\cdot x\geq-A\qquad(x\in K,\ |\theta-N|<\varepsilon).
\tag{3}
\]
For example \(A=1+(1+\varepsilon)\max_{x\in K}|x|\) suffices.

For each such \(\theta\), set
\[
\begin{gathered}
V_\theta=\{x: \theta\cdot x<-A\},\\
U_\theta=V_\theta\cap\{x: N\cdot x<0\}.
\end{gathered}
\]
Both sets are convex and open, and \(U_\theta\) is nonempty: points far along \(-N\) belong to it, since \(\theta\cdot N>0\).

We verify the exact hyperplane condition in the convex continuation theorem. For a characteristic unit \(M\), put
\[
v=-\bigl(N-(N\cdot M)M\bigr).
\]
Then \(M\cdot v=0\), \(|v|\leq1\), and
\[
N\cdot v=-|N-(N\cdot M)M|^2\leq-\delta^2.
\]
The equality of the two projection lengths follows by expanding both as \(1-(N\cdot M)^2\). Moreover
\[
\theta\cdot v
=N\cdot v+(\theta-N)\cdot v
<-\delta^2+\varepsilon<-\delta^2/2.
\]
Starting at any point of any affine hyperplane with normal \(M\), the path \(x+\lambda v\), \(\lambda\to+\infty\), eventually lies in \(U_\theta\). Thus every characteristic hyperplane meets \(U_\theta\), in particular every one that meets \(V_\theta\).

On \(V_\theta\), \(P(D)u=0\) by (3); on \(U_\theta\), \(u=0\) by the support condition. The convex continuation theorem gives \(u=0\) on \(V_\theta\). Therefore
\[
\operatorname{supp}u\subset
\bigcap_{|\theta-N|<\varepsilon}\{x: \theta\cdot x\geq-A\}.
\tag{4}
\]
For a nonzero \(x\) in this support choose \(\theta=N-\varepsilon x/(2|x|)\). Equation (4) gives
\[
N\cdot x-\frac{\varepsilon}{2}|x|\geq-A.
\tag{5}
\]
Hence the closed set
\[
\operatorname{supp}u\cap\{x: N\cdot x\leq T\}
\]
is bounded by \(2(T+A)/\varepsilon\) and is compact for each \(T\geq0\). This proves the precise compact-slice property used below, without assuming \(u\) is tempered or globally compact. The enclosure depends on the compact forcing and on the noncharacteristic direction, and does not presuppose hyperbolicity.

## A smooth causal automorphism from weak solvability

Assume that for every globally smooth compactly supported \(f\) with \(\operatorname{supp}f\subset H_N\), there exists \(u\in\mathcal D'(\mathbb R^n)\), supported in \(H_N\), with \(P(D)u=f\). Retain \(P_m(N)\ne0\).

First let \(f\) be one such compact forcing. The uniqueness argument makes its distributional solution unique, and the support enclosure supplies compact time slices. Fix \(T>0\). Choose \(\chi\in C_c^\infty(\mathbb R)\), equal to one on \([-1,T]\), supported in \((-2,T+1)\), and put
\[
v(x)=\chi(N\cdot x)u(x).
\]
It is a compact distribution by the support enclosure. The product rule gives
\[
\begin{aligned}
P(D)v&=\chi(N\cdot x)f\\
&\quad+[P(D),\chi(N\cdot x)]u.
\end{aligned}
\tag{6}
\]
The first summand is smooth. The second summand is supported where \(u\) meets derivatives of \(\chi\). The lower transition has \(N\cdot x<0\) and meets no support of \(u\); the upper transition has \(N\cdot x\geq T\). Thus
\[
\operatorname{singsupp}P(D)v\subset\{x: N\cdot x\geq T\}.
\]
The halfspace on the right is closed and convex. The compact singular-support hull identity now implies \(\operatorname{singsupp}v\subset\{N\cdot x\geq T\}\), including when the image singular support is empty. Since \(v=u\) near \(0\leq N\cdot x<T\), and \(u=0\) in the negative halfspace, \(u\) is smooth where \(N\cdot x<T\). Taking arbitrary \(T\) proves \(u\in C^\infty(\mathbb R^n)\). It remains supported in \(H_N\), so it is flat at its boundary.

To treat arbitrary noncompact smooth forcing supported in \(H_N\), we prove a local dependence statement. If a distribution \(w\) is supported in \(H_N\) and
\[
P(D)w=0\quad\hbox{on }B(0,R),
\]
then
\[
w=0\quad\hbox{on }B(0,\delta R/2).
\tag{7}
\]
Indeed set \(U=B(0,R)\cap\{N\cdot x<0\}\), \(B_*=B(0,\delta R/2)\), and \(V=\operatorname{conv}(U\cup B_*)\). This \(V\) is open and convex, contains \(U,B_*\), and is contained in \(B(0,R)\). For each characteristic unit \(M\), the interval \(M\cdot U\) contains \((-\delta R,\delta R)\): take points approaching \(N\cdot x=0\) in the two opposite tangential directions of the projection of \(M\) onto \(N^\perp\), whose length is at least \(\delta\). The image of \(B_*\) is the smaller interval \((-\delta R/2,\delta R/2)\). Convexity therefore gives
\[
M\cdot V=M\cdot U.
\]
Every characteristic hyperplane meeting \(V\) meets \(U\). The convex continuation theorem applies, since \(w\) vanishes on \(U\), and gives (7). If there are no characteristic normals, the same application has no hyperplane conditions to check. This also covers \(n=1\).

Now take \(f\in C^\infty(\mathbb R^n)\) supported in \(H_N\). Choose \(\chi_j\in C_c^\infty(\mathbb R^n)\), equal to one on \(B(0,j)\), and let \(u_j\) be the unique smooth causal solution for \(f_j=\chi_jf\). If \(l\geq j\), then
\[
P(D)(u_l-u_j)=0\quad\hbox{on }B(0,j).
\]
By (7), \(u_l=u_j\) on \(B(0,\delta j/2)\). Thus the sequence eventually agrees exactly on every compact set, together with all derivatives. Its local limit defines a global \(u\in C^\infty\), supported in \(H_N\), and \(P(D)u=f\). The uniqueness argument proves uniqueness. No convergence estimate on the unbounded tail of \(f\) was used.

Define
\[
E_H=\{u\in C^\infty(\mathbb R^n):\operatorname{supp}u\subset H_N\}.
\]
It is a closed subspace of the usual smooth Fréchet space: convergence in every compact smooth seminorm preserves vanishing on the negative halfspace. The continuous linear map \(P(D):E_H\to E_H\) is bijective by the preceding proof. Its inverse has closed graph: if \(f_j\to f\) and \(u_j\to u\) in \(E_H\), with \(P(D)u_j=f_j\), continuity gives \(P(D)u=f\). The Fréchet closed graph theorem makes the inverse continuous.

For any fixed \(y\) with \(N\cdot y>0\), continuity of evaluation composed with this inverse consequently gives a compact \(K\), an integer \(k\geq0\), and \(C>0\) such that
\[
\begin{gathered}
|u(y)|\leq C\sum_{|\alpha|\leq k}
\sup_{x\in K}|D^\alpha P(D)u(x)|,\\
u\in E_H.
\end{gathered}
\tag{8}
\]
For clarity, a continuous linear functional is bounded by a finite collection of defining seminorms: continuity at zero supplies a basic seminorm neighborhood on which its absolute value is at most one, and scalar dilation gives the inequality. Enlarging the finitely many compact sets to one \(K\), and the derivative orders to one \(k\), gives exactly (8). This is a smooth causal automorphism, with no growth restriction.

## Test a complex root

Take the point \(y\) in (8), and write \(N\cdot y=2c>0\). Choose a smooth scalar \(\chi\), zero for \(t\leq0\), equal to one for \(t\geq c\), with all derivatives bounded. Such a function is obtained by integrating a compact nonnegative bump in \((0,c)\) and dividing by its integral. It need not be compactly supported.

For any complex vector \(\zeta\), the function
\[
u_\zeta(x)=e^{i(x-y)\cdot\zeta}\chi(N\cdot x)
\tag{9}
\]
belongs to \(E_H\), despite its possibly exponential growth, and \(u_\zeta(y)=1\). The differentiation rule gives
\[
\begin{aligned}
P(D)u_\zeta&=e^{i(x-y)\cdot\zeta}F_\zeta(N\cdot x),\\
F_\zeta(t)&=P(\zeta+N D_t)\chi(t).
\end{aligned}
\tag{10}
\]
Expand the polynomial exactly:
\[
P(\zeta+N D_t)\chi
=\sum_{j=0}^m\frac{\partial_N^jP(\zeta)}{j!}D_t^j\chi.
\tag{11}
\]
If \(P(\zeta)=0\), the \(j=0\) term vanishes. Every remaining derivative of \(\chi\) is supported in \([0,c]\). Applying \(D^\alpha\), \(|\alpha|\leq k\), to (10) introduces at most \(k\) further powers of \(\zeta\), and derivatives of \(\chi\) of order at most \(m+k\). Fixed polynomial coefficients and cutoff seminorms therefore give
\[
\begin{gathered}
K_c=K\cap\{x: 0\leq N\cdot x\leq c\},\\
1\leq C_1(1+|\zeta|)^{m+k}
\sup_{x\in K_c}|e^{i(x-y)\cdot\zeta}|.
\end{gathered}
\tag{12}
\]
An empty set on the right is interpreted as zero; it would immediately preclude the corresponding root.

For \(\zeta=\xi+i\tau N\), \(\xi\) real and \(\tau<0\), the absolute value in this strip is
\[
\exp\bigl(-\tau(N\cdot x-2c)\bigr)\leq e^{c\tau}.
\]
Thus every such root satisfies
\[
1\leq C_1(1+|\xi+i\tau N|)^{m+k}e^{c\tau}.
\tag{13}
\]
Increasing \(C_1\) to at least one and taking logarithms yields
\[
\begin{aligned}
-c\tau&\leq\log C_1\\
&\quad+(m+k)\log(1+|\xi+i\tau N|).
\end{aligned}
\tag{14}
\]
The exponential sign follows from the past strip being below the point \(y\). Reversing it would give no useful restriction.

## From logarithmic growth to a fixed root barrier

For \(r\geq0\), define
\[
\begin{gathered}
\mathcal Z_r=\{(\xi,\tau)\in\mathbb R^n\times\mathbb R:\\
\tau\leq0,\quad|\xi|^2+\tau^2\leq r^2,\\
P(\xi+i\tau N)=0\},\\
\begin{aligned}
\mu(r)&=\max\bigl(\{0\}\cup\\
&\quad\{-\tau: (\xi,\tau)\in\mathcal Z_r\}\bigr).
\end{aligned}
\end{gathered}
\tag{15}
\]
The possible root pairs form a compact set, since \(N\) has unit length; the adjoined zero makes the maximum defined even when there are no such roots. Thus \(\mu\) is finite, nonnegative and nondecreasing.

The root condition is a pair of real polynomial equalities: the real and imaginary parts of \(P(\xi+i\tau N)\). Arbitrary complex coefficients simply give fixed real coefficients in these equations. All remaining conditions in (15) are polynomial inequalities. The graph of the maximum can be expressed by the existence of a root attaining a positive maximum, together with the assertion that no root in the same ball has a larger value; the zero case asserts that no negative-imaginary root occurs. The projection lemma above therefore makes \(\mu\) semialgebraic.

If \(\mu(r)>0\), choose a maximizing root and apply (14). We obtain
\[
\begin{gathered}
\mu(r)\geq0,\\
\begin{aligned}
c\mu(r)&\leq\log C_1\\
&\quad+(m+k)\log(1+r).
\end{aligned}
\end{gathered}
\tag{16}
\]
If \(\mu\) were unbounded, the Puiseux theorem above would give
\[
\mu(r)=A r^\alpha(1+o(1)),\qquad A>0,\quad\alpha>0.
\]
Nonnegativity gives \(A>0\), and unboundedness excludes both \(\alpha\leq0\) and the eventually zero alternative. This contradicts (16), since \(r^\alpha/\log(1+r)\to\infty\). Hence \(M=\sup_{r\geq0}\mu(r)<\infty\).

Taking, for example, \(\tau_0=-M-1\), there is no real \(\xi\) and \(\tau<\tau_0\) with \(P(\xi+i\tau N)=0\). This is the full necessary condition:
\[
\begin{gathered}
P_m(N)\ne0,\\
\forall f\in C_c^\infty(\mathbb R^n),\
\operatorname{supp}f\subset H_N,\\
\exists u\in\mathcal D':\
\operatorname{supp}u\subset H_N,\\
P(D)u=f
\end{gathered}
\]
\[
\begin{gathered}
\Longrightarrow\quad
\exists\tau_0\in\mathbb R\
\forall\xi\in\mathbb R^n:\\
P(\xi+i\tau N)\ne0\quad(\tau<\tau_0).
\end{gathered}
\tag{17}
\]
The empty-root, constant-polynomial, one-dimensional and boundary-flat forcing cases are all retained.

Accordingly, a nonzero polynomial is **hyperbolic with respect to \(N\ne0\)** when \(P_m(N)\ne0\) and the final root barrier in (17) holds for some \(\tau_0\). The barrier concerns the full polynomial, including all complex lower order coefficients. For a nonhomogeneous polynomial it is not being replaced here by a statement only about \(P_m\). The converse and the stronger algebraic consequences of this definition are developed in later lessons.

## Exercises with complete solutions

**Exercise 1 (introductory: an elliptic obstruction).** For \(P(\tau,\xi)=\tau^2+|\xi|^2\) in dimension \(n\geq2\), take \(N=e_t\). Check that the boundary is noncharacteristic, and show that compact causal solvability in the theorem cannot hold. Explain the one-dimensional exception.

**Solution.** The principal part takes value one at \(e_t\). For every real spatial \(\xi\), the complex vector \((-i|\xi|,\xi)\) is a root. Its imaginary part is \(-|\xi|e_t\), which escapes arbitrarily far down that direction. The root barrier proved above is therefore impossible, so the weak solvability hypothesis fails. In one dimension there is no spatial \(\xi\): \(P(\tau)=\tau^2\) has only the root zero and is hyperbolic in either time direction.

**Exercise 2 (introductory: the wave barrier).** Verify the hyperbolicity definition directly for \(P(\tau,\xi)=\tau^2-|\xi|^2\), with \(N=e_t\).

**Solution.** Write the complex time coordinate as \(a+ib\), with \(a,b\) real and spatial \(\xi\) real. The imaginary root equation is \(2ab=0\). If \(b\ne0\), then \(a=0\), but the real equation becomes \(-b^2-|\xi|^2=0\), an impossibility. Thus no root has nonzero imaginary time part; \(\tau_0=0\) works. The principal value at \(e_t\) is one. This checks the definition without assuming a general causal sufficiency theorem.

**Exercise 3 (intermediate: an unrestricted growing inverse).** Let \(P(z)=z-ia\) in one variable, \(a\in\mathbb R\). Find an admissible barrier and the smooth causal inverse. Check its complex constant and its regularity at zero.

**Solution.** The only root is \(ia\), so \(\tau_0=a\) is admissible. Since \(P(D)=-i(\partial_t+a)\), the equation is \((\partial_t+a)u=if\). Its causal solution is
\[
\begin{gathered}
u(t)=i\int_0^t e^{-a(t-s)}f(s)\,ds\quad(t\geq0),\\
u(t)=0\quad(t<0).
\end{gathered}
\]
Differentiation verifies the equation and the factor \(i\). Smooth \(f\) supported in the closed positive half-line is flat at zero. The relation \(u'=if-au\), differentiated recursively, makes every derivative of \(u\) zero there too. For \(a<0\), this solution may grow exponentially; the stated solution space permits that growth.

**Exercise 4 (intermediate: why a logarithm is not enough).** Suppose a finite nonnegative semialgebraic function \(h(r)\) on a final interval is \(O(\log(1+r))\). Prove that it is bounded. Explain the role of polynomial algebra in the root-barrier proof.

**Solution.** The Puiseux lemma makes \(h\) eventually zero or asymptotic to \(A r^\alpha\), with \(A>0\) and rational \(\alpha\). If it were unbounded, \(\alpha>0\), and \(r^\alpha/\log(1+r)\to\infty\), a contradiction. The abstract profile \(\log(1+r)\) itself is unbounded and obeys a logarithmic upper estimate. In our proof, the polynomial root equations and the quantified maximum make the root profile semialgebraic, which supplies the additional power law.

**Exercise 5 (advanced: exact stabilization in a concrete geometry).** For the wave principal part and \(N=e_t\), calculate \(\delta\) and the radius in the local dependence statement. Show explicitly how it produces a smooth global solution from the compactly forced solutions.

**Solution.** A unit characteristic normal satisfies \(M_t^2=|M_x|^2\), so \(|M_x|=1/\sqrt2\) and \(\delta=1/\sqrt2\). The local radius is \(R/(2\sqrt2)\). If the cutoffs \(\chi_j,\chi_l\) both equal one on \(B(0,j)\), \(l\geq j\), their solution difference has zero image there and support in the positive time halfspace. It vanishes on \(B(0,j/(2\sqrt2))\). Every fixed compact set lies in these balls for all sufficiently large \(j\), so the sequence agrees exactly there, with every derivative. Its local limit is smooth and solves the desired equation. This conservative radius suffices for stabilization; no sharp wave propagation radius is inferred.

**Exercise 6 (advanced: a barrier without a noncharacteristic direction).** For the forward heat polynomial \(P(\tau,\xi)=i\tau+|\xi|^2\), show that a negative imaginary time barrier holds but the noncharacteristic condition fails. Explain why a familiar causal solution class cannot establish the unrestricted uniqueness used here.

**Solution.** Put \(\tau=a+ib\). The root equations are \(a=0\) and \(b=|\xi|^2\geq0\), so there are no roots with \(b<0\). However the degree-two principal part is \(|\xi|^2\), which vanishes at \(e_t\). The hyperbolicity definition requires both the barrier and the nonzero principal value, so this polynomial fails that definition in the time direction. The characteristic-halfspace theorem supplies a nonzero global smooth homogeneous solution supported in \(t\geq0\), with unrestricted spatial growth. Uniqueness in a smaller growth class does not imply uniqueness in the space used in the lesson.

## References

The exact convex-continuation, characteristic-halfspace and singular-support entries are stated in the linked prerequisite lessons. The original projection and Puiseux proofs used for the root profile are in [Symbols at infinity](symbols-at-infinity.md), Lemmas 2.1 and 3.1.
