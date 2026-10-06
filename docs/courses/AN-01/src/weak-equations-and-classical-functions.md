# Weak equations and classical functions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Self-checked by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

*Source/proof self-check and prerequisite integration by GPT-6 Astra (OpenAI), Ultra, October 2026. Historical authorship and component terms are retained.*

Distributional differentiation always exists, but its result need not be an ordinary function. A jump contributes a point mass. In the other direction, a differential equation with a continuous right side can force a distribution to become a classical function. The distinction depends on the equation and its coefficients.

We use [Local data and compatible products](local-data-and-compatible-products.md) for restriction, derivative signs and the product rule, and [Tensor products and parameter-dependent distributions](tensor-products-and-parameters.md) for separated variables and smooth parameter pairings. The [smooth-kernel lesson](when-a-kernel-is-smooth.md) supplies compact pairings, integration through a distribution and the complete integral Taylor proof. The supplied [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, proves calculus, cutoffs and differentiation of uniformly convergent series; the [finite-dimensional algebra foundation](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §10, and [measure foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1, supply matrix algebra and integration. We preserve the radial matrix-transport route and prove its full ordered-series construction here, including its inverse and smooth parameter dependence.

## A zero derivative determines a constant

**Theorem 1.1 (distributional constants).** If \(I\subset\mathbb R\) is a nonempty open interval and \(u\in\mathcal D'(I)\) satisfies \(u'=0\), there is a unique scalar \(c\) such that

\[
u(\phi)=c\int_I\phi(t)\,dt.
\tag{1.1}
\]

The interval may be unbounded. On a disconnected open set the constant can differ between its interval components.

**Proof.** A test \(\psi\in C_c^\infty(I)\) with integral zero is the derivative of a test in the same interval. Extend it by zero and put

\[
\Phi(t)=\int_{-\infty}^t\psi(s)\,ds.
\]

It is zero to the left of its support and, because the integral is zero, also zero to its right. The interval hull of the compact support lies compactly inside \(I\), so \(\Phi\in C_c^\infty(I)\). Hence \(u(\psi)=u(\Phi')=-u'(\Phi)=0\).

Choose \(\eta\in C_c^\infty(I)\) with integral one. The test \(\phi-(\int\phi)\eta\) has integral zero, so \(u(\phi)=u(\eta)\int\phi\). Take \(c=u(\eta)\). Its uniqueness follows by testing on \(\eta\). Restriction proves the componentwise statement. \(\square\)

**Corollary 1.2 (continuous right side).** If \(u\in\mathcal D'(I)\) and \(u'=f\) with \(f\in C(I)\), then \(u\) is represented by a \(C^1\) function, and its classical derivative is \(f\).

**Proof.** Fix \(t_0\in I\). The function \(F(t)=\int_{t_0}^t f(s)\,ds\) is \(C^1\), and integration by parts shows its distributional derivative is \(f\). Thus \((u-F)'=0\), so Theorem 1.1 gives \(u=F+c\). \(\square\)

This argument rules out hidden point-supported terms when the derivative is prescribed by a continuous function.

## Independence of one coordinate

**Theorem 2.1 (a constant distributional parameter).** Let \(Y\subset\mathbb R^d\) be open and \(I\) be a nonempty open interval. If \(u\in\mathcal D'(Y\times I)\) satisfies \(\partial_tu=0\), there is a unique \(u_0\in\mathcal D'(Y)\) with

\[
\begin{aligned}
g_\phi(x)&=\int_I\phi(x,t)\,dt,\\
u(\phi)&=u_0(g_\phi).
\end{aligned}
\tag{2.1}
\]

Equivalently \(u=u_0\otimes1\), where \(1\) is the distribution of integration on \(I\). The same formula equals \(\int_Iu_0(\phi(\,\cdot\,,t))\,dt\).

**Proof.** Choose \(\eta\in C_c^\infty(I)\) with integral one, and define \(u_0(g)=u(g(x)\eta(t))\). The map \(g\mapsto g\otimes\eta\) is continuous on every test support space, with compact image support. Thus \(u_0\) is a distribution.

For \(\phi\in\mathcal D(Y\times I)\), its integral \(g(x)=\int_I\phi(x,t)\,dt\) is smooth and compactly supported in the projection of \(\operatorname{supp}\phi\). Extend tests in \(t\) by zero and set

\[
\begin{aligned}
q(x,s)&=\phi(x,s)-g(x)\eta(s),\\
\Psi(x,t)&=\int_{-\infty}^t q(x,s)\,ds.
\end{aligned}
\tag{2.2}
\]

The integrand has total integral zero for each \(x\). Therefore \(\Psi\) is zero before and after one compact interval in \(I\) containing both \(t\)-supports. Its \(x\)-support lies in a compact subset of \(Y\); differentiation under the integral proves smoothness. Hence \(\Psi\in\mathcal D(Y\times I)\) and \(\partial_t\Psi=\phi-g\otimes\eta\). Pairing with \(u\) gives \(u(\phi)=u_0(g)\).

Tests \(g\otimes\eta\) give uniqueness. The tensor theorem in the prerequisite identifies (2.1) with \(u_0\otimes1\) and gives its other iterated formula. The parameter pairing has one common compact \(x\)-support and compact \(t\)-support, so its ordinary integral is well-defined. \(\square\)

**Corollary 2.2 (a continuous weak derivative is classical).** Let \(u,f\) be continuous functions on open \(X\subset\mathbb R^n\), and suppose \(\partial_j u=f\) as distributions. Then the classical partial derivative \(\partial_j u(x)\) exists at every point and equals \(f(x)\).

If all first distributional partial derivatives of a continuous \(u\) are continuous functions, then \(u\in C^1(X)\).

**Proof.** This is local, so work on a box \(Y\times I\) where the distinguished coordinate is \(t\). Fix \(t_0\in I\) and put

\[
V(x,t)=\int_{t_0}^t f(x,s)\,ds.
\]

The function is continuous and has continuous classical \(t\)-derivative \(f\). Fubini and one-dimensional integration by parts against a compact test show \(\partial_tV=f\) distributionally; no derivative in \(x\) is needed.

The continuous function \(w=u-V\) has zero distributional \(t\)-derivative. By Theorem 2.1 it is \(u_0\otimes1\). The proof identifies \(u_0\) with the continuous function

\[
h(x)=\int_I w(x,t)\eta(t)\,dt.
\]

Thus \(w\) and \(h(x)\) give the same distribution. Two continuous functions with that property agree pointwise, by the nonnegative-bump argument in the localization lesson. Hence \(u(x,t)=V(x,t)+h(x)\), and its classical \(t\)-derivative is \(f\) at every point. Covering \(X\) proves the assertion. If every partial derivative is continuous, telescope along a short coordinate polygon from \(x\) to \(x+h\) and use the one-dimensional fundamental theorem on its segments. After subtracting \(\sum_j h_j\partial_j u(x)\), the error is at most \(\sum_j|h_j|\) times the maximum variation of these partials within distance \(\sum_j|h_j|\) of \(x\). Continuity makes this \(o(|h|)\), proving total differentiability and hence \(C^1\) regularity. \(\square\)

For this single-coordinate assertion, continuity of \(u\) is a necessary hypothesis. The distribution \(\delta_0(x)\otimes1(t)\) has zero \(t\)-derivative but is not a continuous function.

## All weak partials control regularity

**Theorem 2.3 (all continuous weak partials).** Let \(X\subset\mathbb R^n\) be open, \(n\ge1\), and \(u\in\mathcal D'(X)\). Suppose every first distributional partial is represented by a continuous complex function:
\[
\begin{aligned}
\partial_j u&=f_j,\\
f_j&\in C(X),\quad 1\le j\le n.
\end{aligned} \tag{2.3a}
\]
Then exactly one \(g\in C^1(X)\) represents \(u\), and its classical partials are the given \(f_j\). Neither continuity nor local integrability of \(u\) is a hypothesis. The statement applies componentwise to finite vectors.

**Proof.** Fix a ball \(B=B(b,r)\) with compact closure in \(X\). Choose \(a>0\) so small that the closed \(2a\)-neighborhood of \(\overline B\) is a compact subset of \(X\). This follows from compactness of \(\overline B\) and openness of \(X\). Fix a nonnegative smooth test \(\rho\), supported in the unit ball, with integral one; the exact smooth cutoff construction in [Metric and topological foundations, Section 13.10](../prerequisites/U011-free-foundations/metric-foundation-bridges.md) provides such a test by normalization. Put \(\rho_\varepsilon(z)=\varepsilon^{-n}\rho(z/\varepsilon)\), \(0<\varepsilon<a\), and define on the open \(a\)-neighborhood of \(\overline B\)
\[
                    u_\varepsilon(x)
                    =u_y(\rho_\varepsilon(x-y)).        \tag{2.3b}
\]
For fixed \(\varepsilon\), kernels on each compact parameter neighborhood are tests supported in one compact subset of \(X\). The parameter-differentiation lemma in [Tensor products and parameter-dependent distributions](tensor-products-and-parameters.md) therefore proves smoothness and differentiation of this actual pairing. The two derivative signs give
\[
\begin{gathered}
 \partial_j u_\varepsilon(x)
 =u_y(\partial_{x_j}\rho_\varepsilon(x-y))\\
 =(\partial_j u)_y(\rho_\varepsilon(x-y))\\
 =\int f_j(x-\varepsilon z)\rho(z)\,dz\\
 =:f_{j,\varepsilon}(x).
\end{gathered}                                                \tag{2.3c}
\]
In the second equality the minus in the distribution derivative cancels \(\partial_{y_j}\rho_\varepsilon(x-y)=-\partial_{x_j}\rho_\varepsilon(x-y)\). Uniform continuity on the fixed compact neighborhood gives
\[
\begin{gathered}
 \sup_{\overline B}|f_{j,\varepsilon}-f_j|
 \\ \le \sup_{\substack{x\in\overline B\\ |z|\le\varepsilon}}
             |f_j(x-z)-f_j(x)|\\
 \longrightarrow0.
\end{gathered} \tag{2.3d}
\]

We first justify convergence of (2.3b) to the original distribution. For \(\phi\in\mathcal D(B)\), extend \(\phi\) by zero and define
\[
\begin{gathered}
 K_\varepsilon\phi(y)\\
 =\int \rho_\varepsilon(x-y)\phi(x)\,dx\\
 =\int \rho(z)\phi(y+\varepsilon z)\,dz.
\end{gathered} \tag{2.3e}
\]
All these tests, for sufficiently small \(\varepsilon\), have support in one compact subset of \(X\). For every multiindex \(\alpha\), differentiating the ordinary integral and using uniform continuity of \(\partial^\alpha\phi\) proves uniform convergence
\(\partial^\alpha K_\varepsilon\phi\to\partial^\alpha\phi\).
Thus \(K_\varepsilon\phi\to\phi\) in a fixed test-support space. Moreover
\[
\begin{aligned}
 \int u_\varepsilon(x)\phi(x)\,dx
 &=u(K_\varepsilon\phi)\\
 &\longrightarrow u(\phi).
\end{aligned} \tag{2.3f}
\]
Here the interchange with \(u\) is justified without a Fubini assertion about an arbitrary functional. On the fixed compact kernel support, choose the actual finite derivative seminorm controlling \(u\). Riemann sums for the \(x\)-integral of \(\phi(x)\rho_\varepsilon(x-y)\) converge in that seminorm, because all the required \(y\)-derivatives are continuous on a compact product. Their scalar pairings converge to the ordinary integral on the left. This is the same finite-seminorm integral argument proved in the smooth-approximation lemma in [When a kernel is smooth](when-a-kernel-is-smooth.md). No uniform estimate in \(\varepsilon\) is needed for this identity at each fixed \(\varepsilon\).

Retain the value \(c_\varepsilon=u_\varepsilon(b)\). The ordinary fundamental theorem on the segment \(\gamma_x(t)=b+t(x-b)\), \(0\le t\le1\), in the convex ball gives
\[
\begin{aligned}
 u_\varepsilon(x)&=c_\varepsilon+v_\varepsilon(x),\\
 v_\varepsilon(x)
 &=\sum_{j=1}^n(x_j-b_j)\\
 &\quad{}\cdot\int_0^1 f_{j,\varepsilon}(\gamma_x(t))\,dt.
\end{aligned}                                                \tag{2.3g}
\]
By (2.3d), \(v_\varepsilon\) converges uniformly on \(\overline B\) to
\[
\begin{aligned}
 F(x)&=\sum_{j=1}^n(x_j-b_j)\\
 &\quad{}\cdot\int_0^1 f_j(\gamma_x(t))\,dt,\\
 F(b)&=0.
\end{aligned} \tag{2.3h}
\]
This formula defines a continuous function; we have not assumed that the continuous list \(f_j\) already has a potential. For any coordinate segment inside \(B\), the classical derivatives in (2.3c) give
\[
 v_\varepsilon(x+h e_j)-v_\varepsilon(x)
            =\int_0^h f_{j,\varepsilon}(x+s e_j)\,ds.
\]
Uniform convergence yields the exact limiting identity
\[
\begin{gathered}
 F(x+h e_j)-F(x)\\
 =\int_0^h f_j(x+s e_j)\,ds.
\end{gathered} \tag{2.3i}
\]
It includes negative \(h\) with the oriented integral. Dividing by \(h\) proves the classical partial \(\partial_jF(x)=f_j(x)\).

For completeness, these continuous partials give total differentiability by a direct estimate. For \(h\) sufficiently small, the coordinate polygon from \(x\) to \(x+h\) stays in \(B\). Telescope (2.3i) along it and subtract \(\sum_j f_j(x)h_j\). The absolute remainder is at most
\[
\begin{gathered}
 \sum_j |h_j|
 \\ {}\cdot\sup_{\substack{|y-x|\le\sum_k|h_k|\\y\in B}}
                       |f_j(y)-f_j(x)|\\
 =o(|h|).
\end{gathered} \tag{2.3j}
\]
Indeed \(\sum|h_j|\le\sqrt n\,|h|\) and the suprema tend to zero. Hence \(F\in C^1(B)\).

It remains essential to recover the actual constant. Choose \(\eta\in\mathcal D(B)\) with integral one. Equations (2.3f)–(2.3h) give
\[
\begin{aligned}
 c_\varepsilon
 &=\int u_\varepsilon\eta-\int v_\varepsilon\eta\\
 &\longrightarrow u(\eta)-\int F\eta=:c.
\end{aligned}                                                \tag{2.3k}
\]
For each \(\phi\in\mathcal D(B)\), pass to the limit in (2.3g), using (2.3f), to obtain
\[
                  u(\phi)=\int_B(c+F(x))\phi(x)\,dx.           \tag{2.3l}
\]
Thus \(g_B=c+F\) represents the original \(u|_B\), with \(c=g_B(b)\).

Continuous representatives are unique: if a continuous difference \(q\) has a nonzero value at \(x_0\), choose a complex scalar \(\lambda\) making \(\Re(\lambda q(x_0))>0\). This remains strictly positive on a smaller ball. Pairing with a nonnegative nonzero bump there contradicts that \(q\) represents zero. Therefore the functions \(g_B\) agree on all overlaps. They form a unique \(C^1\) function \(g\) on \(X\). To identify its global distribution, apply the finite test partition of the local uniqueness theorem in [Local data and compatible products](local-data-and-compatible-products.md) to \(u-g\,dx\), which is zero on each ball. Its derivatives are locally the \(f_j\), hence are so globally. This proves the theorem without connectedness or a prescribed normalization. \(\square\)

**Corollary 2.4 (higher regularity from weak partials).** If every \(f_j\) in (2.3a) belongs to \(C^k(X)\), \(k\ge0\), the representative is in \(C^{k+1}(X)\): the first derivatives supplied by Theorem 2.3 are precisely the given \(C^k\) functions, so all successive classical derivatives through order \(k+1\) exist and are continuous. Their distributional identities follow by integration by parts locally, then restriction and uniqueness. Smooth \(f_j\) yield a smooth representative.

More generally, fix an integer \(m\ge1\). Suppose every distributional derivative \(\partial^\alpha u\) with \(|\alpha|=m\) is continuous. For each \(|\beta|=m-1\), all first weak partials of \(\partial^\beta u\) are among these continuous functions, because distributional partials commute by the differential rules in [Local data and compatible products](local-data-and-compatible-products.md). Theorem 2.3 gives a unique \(C^1\) representative for each such derivative. Descend one order at a time. If every derivative of order \(r+1\) has a \(C^{m-r-1}\) representative, all first partials of any derivative of order \(r\) have that regularity. The preceding paragraph makes it \(C^{m-r}\). At \(r=0\) this yields the unique \(C^m\) representative of \(u\). There is no hypothesis on lower-order derivatives in advance, and uniqueness identifies their classical and weak versions at every step.

This assertion uses **all** multiindices of the fixed total order. It makes no claim that a list of only pure high-order derivatives, or one selected directional derivative, supplies the same conclusion.

## First-order systems without commuting matrices

For a scalar smooth coefficient \(a\), the integrating factor \(E(t)=\exp(\int_{t_0}^t a(s)\,ds)\) satisfies \(E'=Ea\). For matrices the same exponential expression generally fails. We need the order of multiplication fixed.

The following normalized radial transport statement supplies the matrix factor: on a star-shaped open \(V\subset\mathbb R^N\) containing zero, any smooth matrix \(h\) with \(h(0)=0\) has a smooth invertible normalized solution

\[
2(v\cdot\partial_v)S=hS,\qquad S(0)=I.
\tag{3.1}
\]

**Proof of the radial transport statement.** Use the matrix norm \(\|B\|=\max_i\sum_j|B_{ij}|\). Summing \(|(BC)_{ij}|\le\sum_l|B_{il}||C_{lj}|\) first in \(j\) proves \(\|BC\|\le\|B\|\|C\|\). Define, for \(0\le s\le1\),
\[
\begin{aligned}
A_v(s)&=\frac{h(sv)}{2s}\\
&=\frac12\sum_jv_j\int_0^1(\partial_jh)(\theta sv)\,d\theta .
\end{aligned}
\]
The second expression follows from the fundamental theorem and defines the value at \(s=0\). It is jointly smooth in \(s,v\). For every compact parameter set \(K\subset V\), its radial hull is the compact image of \([0,1]\times K\), lies inside \(V\), and controls all derivatives in this formula.

Let \(Q_0(t,v)=I\) and recursively set
\[
\begin{gathered}
Q_{k+1}(t,v)=\int_0^t A_v(s)Q_k(s,v)\,ds,\\
Y_v(t)=\sum_{k=0}^{\infty}Q_k(t,v).
\end{gathered}
\]
Unrolling the recursion integrates the ordered product
\(A_v(s_1)\cdots A_v(s_k)\) over \(0<s_k<\cdots<s_1<t\). Induction by the outer integral gives the simplex volume \(t^k/k!\). If \(M_l\ge1\) bounds the coefficient and all its parameter derivatives through order \(l\) on the compact set, each list of \(l\) differentiations has \(k^l\) assignments to the \(k\) factors. Consequently, for \(k\ge1\),
\[
\|\partial_v^\alpha Q_k(t,v)\|
\le k^{|\alpha|}M_{|\alpha|}^k\,\frac{t^k}{k!}.
\]
For each fixed derivative order, the ratio of consecutive scalar bounds tends to zero, so the bound is eventually dominated by a geometric series. The series of every such derivative converges uniformly. The proved uniform differentiation theorem in scalar §13.7 shows these are the actual parameter derivatives. Summing the integral recursions gives \(Y_v(t)=I+\int_0^t A_v(s)Y_v(s)\,ds\); the fundamental theorem gives \(Y'_v=A_vY_v\). Repeated differentiation of this equation supplies all \(t\)-derivatives as well.

For the inverse, use \(R_0=I\), \(R_{k+1}(t,v)=-\int_0^t R_k(s,v)A_v(s)\,ds\), and \(Z_v=\sum_kR_k\). The same bounds apply while retaining the reverse factor order. Thus \(Z'_v=-Z_vA_v\), and \((Z_vY_v)'=0\) gives \(Z_vY_v=I\). A square matrix with a left inverse is injective, hence surjective by finite-dimensional linear algebra; therefore \(Y_vZ_v=I\) too. Both matrices are smooth in all their parameters.

Uniqueness uses the same estimate. The difference \(D\) of two solutions with the same initial value satisfies \(D(t)=\int_0^t A_v(s)D(s)\,ds\). Iterating this \(k\) times bounds it by \(\sup_{[0,1]}\|D\|\,M_0^k/k!\), which tends to zero. Hence \(D=0\).

Set \(S(v)=Y_v(1)\). For \(0\le r\le1\), the identity \(A_{rv}(s)=rA_v(rs)\) and uniqueness give \(Y_{rv}(t)=Y_v(rt)\), and hence \(S(rv)=Y_v(r)\). Differentiating at \(r=1\) from the left proves \(2(v\cdot\partial_v)S(v)=h(v)S(v)\). At \(v=0\), the coefficient is zero, so \(S(0)=I\); the equation holds there too. The inverse is \(Z_v(1)\). Finally, any other smooth normalized radial solution restricted to a ray solves the same regular initial-value equation, so it equals \(S\). This proves (3.1) on the whole star-shaped domain, with no commutativity assumption. \(\square\)

To obtain the integrating factor we need on \(I\), take \(N=1\), \(V=I-t_0\), and

\[
h(v)=2v\,A(t_0+v)^{\mathsf T}.
\tag{3.2}
\]

This is smooth, vanishes at zero, and \(V\) is star-shaped. Equation (3.1) gives \(S'=A(t_0+v)^{\mathsf T}S\) for \(v\ne0\), hence at zero too by continuity. Its ordinary transpose, with no complex conjugation, gives

\[
\begin{aligned}
E(t)&=S(t-t_0)^{\mathsf T},\\
E'&=EA,\quad E(t_0)=I.
\end{aligned}
\tag{3.3}
\]

The matrix \(E\) and its inverse are smooth on all of \(I\). This is an exact specialization of the transport proof just supplied.

**Theorem 3.1 (distributional systems become classical).** Let \(A\in C^\infty(I;\mathbb C^{r\times r})\), \(f\in C(I;\mathbb C^r)\), and \(u\in\mathcal D'(I;\mathbb C^r)\). If

\[
u'+Au=f,
\tag{3.4}
\]

then \(u\) is represented by a \(C^1\) vector function and satisfies (3.4) classically. With \(E\) as in (3.3), every distributional solution has the form

\[
\begin{aligned}
v(t)&=c+\int_{t_0}^t E(s)f(s)\,ds,\\
u(t)&=E(t)^{-1}v(t),\quad c\in\mathbb C^r.
\end{aligned}
\tag{3.5}
\]

**Proof.** Apply the distributional product rule entry by entry. Retaining the multiplication order,

\[
(Eu)'=Eu'+E'u=E(u'+Au)=Ef.
\]

The right side is continuous. Corollary 1.2 applied to each component gives \(Eu=c+\int_{t_0}^t Ef\), a \(C^1\) vector. Multiplying by the smooth inverse proves (3.5) and the regularity claim. Conversely, classical differentiation of (3.5) gives the equation. The constant is its value at \(t_0\), because \(E(t_0)=I\). \(\square\)

This also applies componentwise to open subsets of the line, with one independent constant vector on each interval component.

**Corollary 3.2 (higher-order scalar equations).** Let \(m\ge1\), let \(a_0,\ldots,a_{m-1}\) be smooth on open \(X\subset\mathbb R\), and let \(f\in C(X)\). If \(u\in\mathcal D'(X)\) satisfies

\[
u^{(m)}+\sum_{j=0}^{m-1}a_j u^{(j)}=f,
\tag{3.6}
\]

then \(u\in C^m(X)\) and (3.6) holds classically.

**Proof.** Work on an interval component. Set \(U=(u,u',\ldots,u^{(m-1)})^{\mathsf T}\). It satisfies \(U'+AU=F\), with \(F=(0,\ldots,0,f)^{\mathsf T}\), the first \(m-1\) rows of \(A\) having a single \(-1\) in their next column, and its last row \((a_0,\ldots,a_{m-1})\). Theorem 3.1 makes every component of \(U\) \(C^1\).

The distributional identities \(U_j'=U_{j+1}\) now agree with the classical derivatives of those \(C^1\) components. Starting with \(u=U_1\), induction gives \(u\in C^m\); its \(m\)-th derivative is \(U_m'\), which is continuous. The last equation is then classical. \(\square\)

A smooth nonvanishing leading coefficient can be divided out, so the same conclusion holds locally wherever it is nonzero. If it vanishes, singular solutions may remain: \(xH'=x\delta_0=0\), although \(H\) is discontinuous.

## Jumps produce concentrated derivatives

**Theorem 4.1 (derivative across a jump).** Let \(a\in X\subset\mathbb R\), with \(X\) open, and let \(g\) be \(C^1\) on \(X\setminus\{a\}\). Suppose its ordinary derivative \(v=g'\) there is integrable on a neighborhood of \(a\). Then the finite one-sided limits \(g(a-)\), \(g(a+)\) exist. Any assignment of \(g(a)\) gives the same locally integrable distribution, whose derivative is

\[
\begin{aligned}
g'&=v+[g]_a\delta_a,\\
[g]_a&=g(a+)-g(a-).
\end{aligned}
\tag{4.1}
\]

**Proof.** For fixed \(b>a\) sufficiently close to \(a\),

\[
g(x)=g(b)-\int_x^b v(s)\,ds,\qquad a<x<b.
\]

Absolute integrability makes the right side have a finite limit as \(x\downarrow a\). The same argument to the left gives the other limit. In particular \(g\) is bounded near \(a\), hence locally integrable; its value at one point does not affect its integrals.

For a compact smooth test, integrate by parts separately to the left of \(a-\varepsilon\) and to the right of \(a+\varepsilon\). The outer boundary terms vanish, and

\[
\begin{gathered}
-\int_{|x-a|>\varepsilon}g(x)\phi'(x)\,dx\\
=\int_{|x-a|>\varepsilon}v(x)\phi(x)\,dx\\
\quad+g(a+\varepsilon)\phi(a+\varepsilon)\\
\quad-g(a-\varepsilon)\phi(a-\varepsilon).
\end{gathered}
\]

Local boundedness of \(g\), integrability of \(v\), and the one-sided limits justify passage to \(\varepsilon\downarrow0\). This gives \(v(\phi)+[g]_a\phi(a)\), exactly (4.1). The argument is local near \(a\); on the rest of the support ordinary integration by parts applies. \(\square\)

The coefficient is the right limit minus the left limit. The sign is determined by the distributional convention, not by a choice of a value at the discontinuity.

For a piecewise \(C^m\) function whose derivatives through order \(m-1\) have finite one-sided limits and whose ordinary \(m\)-th derivative is locally integrable at \(a\), iteration gives

\[
\begin{aligned}
\partial^m g
&=g_{\mathrm{ordinary}}^{(m)}\\
&\quad+\sum_{l=0}^{m-1}
[g^{(m-1-l)}]_a\,\delta_a^{(l)}.
\end{aligned}
\tag{4.2}
\]

To justify the iteration, Theorem 4.1 applied first to \(g\) gives its first jump term. Apply it to the ordinary derivative on each side at each subsequent step. Each previously obtained delta derivative is differentiated once, while the new ordinary derivative contributes its own jump. Induction produces precisely the indices in (4.2). The stated hypotheses ensure all those ordinary derivatives define locally integrable functions.

## Exercises

1. **No hidden singularity — foundation.** Determine every distributional solution of \(u'+2xu=0\) on the line. Explain why the integrating-factor argument also excludes delta terms.
2. **Two derivative levels — intermediate.** Let \(g(x)=0\) for \(x<0\) and \(g(x)=e^{-x}\) for \(x>0\). Compute its first and second distributional derivatives. Check each concentrated coefficient from (4.2).
3. **An unsmoothed transverse variable — intermediate.** On \(\mathbb R_x\times\mathbb R_t\), let \(u=\delta_0(x)\otimes1(t)\). Prove \(\partial_tu=0\), but \(u\) is not a continuous function. Identify the missing hypothesis if one tries to apply Corollary 2.2.
4. **A degenerate leading coefficient — foundation.** Verify \(xH'=0\) distributionally and explain why this does not contradict Corollary 3.2. Give another distributional solution obtained by adding a constant.
5. **Matrix order — advanced.** Put \(B=\begin{pmatrix}0&1\\0&0\end{pmatrix}\), \(C=\begin{pmatrix}0&0\\1&0\end{pmatrix}\), and \(A(t)=B+tC\). Let \(E'=EA\), \(E(0)=I\). Compare the coefficient of \(t^3\) in \(E(t)\) with that in \(\exp(tB+t^2C/2)\). Show the difference is \((BC-CB)/12\), so the naive exponential is not the integrating factor.

**Exercise 6 (foundation: recover a polynomial and its constant).** On \(\mathbb R^2\), suppose \(u\) is a distribution with \(\partial_xu=2x\) and \(\partial_yu=6y\). Determine every such \(u\) without assuming it is a function.

**Exercise 7 (intermediate: a Hessian prescribes the affine ambiguity).** Let \(u\in\mathcal D'(\mathbb R^2)\) satisfy \(\partial_x^2u=2\), \(\partial_x\partial_yu=4\), and \(\partial_y^2u=6\). Determine all solutions and explain why the mixed derivative belongs in the hypotheses.

**Exercise 8 (advanced: local curl compatibility does not remove a global period).** On the punctured plane \(X=\mathbb R^2\setminus\{0\}\), put
\[
\begin{aligned}
f_1(x,y)&=-\frac{y}{x^2+y^2},\\
f_2(x,y)&=\frac{x}{x^2+y^2}.
\end{aligned}
\]
Check \(\partial_y f_1=\partial_x f_2\). Prove no \(u\in\mathcal D'(X)\) can have both weak partials equal to this list.

**Exercise 9 (intermediate: a quantitative first-order remainder).** Under Theorem 2.3, let \(B\Subset X\) be a convex ball, and define
\[
 \omega_B(s)=\max_j\sup_{\substack{x,y\in\overline B\\|x-y|\le s}}
                                  |f_j(x)-f_j(y)|.
\]
Prove, when the segment from \(x\) to \(x+h\) lies in \(\overline B\),
\[
\begin{aligned}
R_x(h)&=g(x+h)-g(x)-\sum_j h_jf_j(x),\\
|R_x(h)|&\le\sqrt n\,|h|\,\omega_B(|h|).
\end{aligned}
\]
Deduce the corresponding local \(C^{1,\alpha}\) estimate if \(\omega_B(s)\le M s^\alpha\), \(0<\alpha\le1\).

## Complete solutions

**Solution 1.** The scalar factor \(E(x)=e^{x^2}\) has \(E'=2xE\). The product rule gives \((Eu)'=0\), so Theorem 1.1 makes \(Eu=c\), as a distribution on the whole connected line. Thus \(u=ce^{-x^2}\), an ordinary smooth function. Conversely these functions solve the equation. The constant theorem applies to arbitrary distributions, including those with possible concentrated terms; none can survive after multiplication by the smooth nonzero factor \(E\).

**Solution 2.** The jump of \(g\) is \(1\). Its ordinary derivative is \(-He^{-x}\), so

\[
g'=-He^{-x}+\delta_0.
\]

The ordinary first derivative has right limit \(-1\) and left limit \(0\), hence jump \(-1\). Its ordinary derivative away from zero is \(He^{-x}\). Differentiate the first formula to get

\[
g''=He^{-x}-\delta_0+\delta'_0.
\]

Formula (4.2) for \(m=2\) has \([g']_0\delta_0+[g]_0\delta'_0=-\delta_0+\delta'_0\), verifying both coefficients.

**Solution 3.** On a test, \(u(\phi)=\int_{\mathbb R}\phi(0,t)\,dt\). Thus

\[
(\partial_tu)(\phi)=-\int_{\mathbb R}\partial_t\phi(0,t)\,dt=0.
\]

It is supported on the line \(x=0\) and is nonzero. If represented by a continuous function, that function would be zero off this line, because the distribution is zero there, and then zero on the line by continuity. This contradicts a product bump whose value at \(x=0\) and \(t\)-integral are both one. The missing hypothesis is continuity of \(u\); the right side \(f=0\) is continuous. Theorem 2.1 allows a distributional transverse coefficient, so there is no contradiction. The all-partials Theorem 2.3 also does not apply: the transverse derivative is \(\delta'_0(x)\otimes1(t)\), which is not represented by a continuous function.

**Solution 4.** By (4.1), \(H'=\delta_0\). Smooth multiplication gives \((x\delta_0)(\phi)=\delta_0(x\phi)=0\), hence \(xH'=0\). The coefficient of the highest derivative is \(x\), which vanishes at zero; Corollary 3.2 has a monic highest derivative, or equivalently applies after division only where the leading coefficient is nonzero. On either half-line \(H\) is constant and regular, consistent with that local conclusion. Adding any constant \(c\) gives another solution \(H+c\).

**Solution 5.** Write \(E=I+tE_1+t^2E_2+t^3E_3+O(t^4)\), using its smoothness and the differential equation. Comparing coefficients in \(E'=E(B+tC)\) gives

\[
\begin{aligned}
E_1&=B,\quad E_2=\frac{B^2+C}{2},\\
E_3&=\frac{B^3}{6}+\frac{CB}{6}+\frac{BC}{3}.
\end{aligned}
\]

For the exponential, define \(\exp R=\sum_{j\ge0}R^j/j!\). The submultiplicative norm bounds this by the convergent scalar exponential series; when \(\|R\|\le1\), the sum from \(j=4\) onwards is bounded by \(C\|R\|^4\). Thus expand \(I+R+R^2/2+R^3/6\), where \(R=tB+t^2C/2\), with an \(O(t^4)\) remainder. Its cubic coefficient is \(B^3/6+(BC+CB)/4\). The difference is therefore \((BC-CB)/12\). Here \(B^2=0\), \(BC=\operatorname{diag}(1,0)\), and \(CB=\operatorname{diag}(0,1)\), so it is the nonzero diagonal matrix \(\operatorname{diag}(1,-1)/12\). This proves failure of the exponential even with smooth polynomial coefficients. The ordered transport construction and the right-sided equation \(E'=EA\) are essential.

**Solution 6.** Theorem 2.3 gives a \(C^1\) representative \(g\) with the prescribed gradient. Subtract \(x^2+3y^2\). The resulting \(C^1\) function has both partials zero. Along the segment from \((0,0)\) to \((x,y)\), the chain rule and the ordinary fundamental theorem give value difference zero, so it equals a single constant \(c\). Hence \(u=(x^2+3y^2+c)\,dx\,dy\). Conversely each such polynomial has exactly the required weak partials by integration by parts. If \(c\) is changed, a unit-integral test detects the change; no concentrated term or extra distribution is possible.

**Solution 7.** These are all three multiindices of total order two. Corollary 2.4 gives a \(C^2\) representative \(g\). The polynomial \(p=x^2+4xy+3y^2\) has exactly this Hessian. Each first partial of \(g-p\) has both first partials zero, so Solution 6's segment argument makes it a constant, say \(a\) for its \(x\)-partial and \(b\) for its \(y\)-partial. Subtract \(ax+by\) once more; the same argument makes the remainder \(c\). Therefore every solution is \(p+ax+by+c\). Conversely these functions give all three weak identities. The mixed identity is part of the exact all-multiindices theorem and fixes the \(xy\) coefficient; no inference from only the two pure identities was used.

**Solution 8.** With \(r^2=x^2+y^2\), direct differentiation gives
\[
 \partial_yf_1=\frac{y^2-x^2}{r^4}
                         =\partial_xf_2 .
\]
Thus the list is smooth and locally satisfies the mixed-partial compatibility. If such a distribution existed, Theorem 2.3 would give one globally defined \(C^1\) representative \(g\). Along \(\gamma(t)=(\cos t,\sin t)\), \(0\le t\le2\pi\), the chain rule would give
\[
\begin{gathered}
 \frac d{dt}g(\gamma(t))\\
 =(-\sin t)(-\sin t)+(\cos t)(\cos t)\\
 =1.
\end{gathered}
\]
Integration yields \(g(\gamma(2\pi))-g(\gamma(0))=2\pi\), whereas the endpoints are the same point. This contradiction excludes even a singular distributional potential. The proof of Theorem 2.3 never assumes that an arbitrary compatible continuous list has a global potential; it starts with the actual distribution \(u\).

**Solution 9.** Theorem 2.3 has already proved the classical \(C^1\) representative. The fundamental theorem along the actual straight segment, with the chain rule, gives
\[
\begin{aligned}
 R_x(h)
 &=\int_0^1\sum_jh_j\big(f_j(x+th)-f_j(x)\big)\,dt.
\end{aligned}
\]
Every summand difference is bounded by \(\omega_B(|h|)\). The triangle inequality and \(\sum|h_j|\le\sqrt n\,|h|\) prove the displayed bound, including \(h=0\). Under the stated modulus hypothesis it is at most \(\sqrt n\,M|h|^{1+\alpha}\). The gradient components themselves have \(\alpha\)-Hölder seminorm at most \(M\) on the ball. Thus \(g\) is locally \(C^{1,\alpha}\), with the stated Taylor remainder. This estimate assumes regularity of all actual weak partials, and does not silently bound the additive constant or the size of \(g\).

## References

- The supplied [local operations and gluing proofs](local-data-and-compatible-products.md), [tensor and parameter proofs](tensor-products-and-parameters.md) and [smooth pairings and integral Taylor proof](when-a-kernel-is-smooth.md) provide the earlier programme arguments. The scalar, algebra and measure foundations linked above retain their stated licences.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), 2003 reprint, ISBN 978-3-642-61497-2, §3.1, pp. 56–59: Theorems 3.1.3, 3.1.4, 3.1.4′ and 3.1.7, and Corollaries 3.1.5–3.1.6. The exact approved purchased copy supplies the jump, constant-distribution, system and continuous-partial comparisons. The all-partials regularization argument and every needed matrix construction are fully proved here.
- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2 October 2026, §3.1.3, p. 40, Proposition 3.2 and its proof; §3.2, pp. 40–41, for multiplication and the product rule. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
- *Building a local inverse from radial singularities*, §§5–6 and §6.2, formulas HS3, HM1–HM3 and MC5–MC8. The exact earlier programme text supplied the radial transport route retained here. Its CC0 1.0 terms remain with that work; the complete independently expressed proof needed in this lesson is now given above. Exact earlier course source.
