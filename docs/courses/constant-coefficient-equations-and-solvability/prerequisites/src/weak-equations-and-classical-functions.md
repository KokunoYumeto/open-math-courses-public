# Weak equations and classical functions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

Distributional differentiation always exists, but its result need not be an ordinary function. A jump contributes a point mass. In the other direction, a differential equation with a continuous right side can force a distribution to become a classical function. The distinction depends on the equation and its coefficients.

We use [Local data and compatible products](local-data-and-compatible-products.md) for restriction, derivative signs and the product rule, and [Tensor products and parameter-dependent distributions](tensor-products-and-parameters.md) for separated variables. Integration, smooth cutoffs and elementary finite-dimensional linear algebra are prerequisites. The distribution perspective is [Dyatlov 2026], Chapter 3. For systems we use the proved noncommuting matrix transport in Building a local inverse from radial singularities, “Matrix transport and the order of multiplication”, with an explicit specialization below.

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
u(\phi)=u_0\!\left(x\longmapsto\int_I\phi(x,t)\,dt\right).
\tag{2.1}
\]

Equivalently \(u=u_0\otimes1\), where \(1\) is the distribution of integration on \(I\). The same formula equals \(\int_Iu_0(\phi(\,\cdot\,,t))\,dt\).

**Proof.** Choose \(\eta\in C_c^\infty(I)\) with integral one, and define \(u_0(g)=u(g(x)\eta(t))\). The map \(g\mapsto g\otimes\eta\) is continuous on every test support space, with compact image support. Thus \(u_0\) is a distribution.

For \(\phi\in\mathcal D(Y\times I)\), its integral \(g(x)=\int_I\phi(x,t)\,dt\) is smooth and compactly supported in the projection of \(\operatorname{supp}\phi\). Extend tests in \(t\) by zero and set

\[
\Psi(x,t)=\int_{-\infty}^t
[\phi(x,s)-g(x)\eta(s)]\,ds.
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

Thus \(w\) and \(h(x)\) give the same distribution. Two continuous functions with that property agree pointwise, by the nonnegative-bump argument in the localization lesson. Hence \(u(x,t)=V(x,t)+h(x)\), and its classical \(t\)-derivative is \(f\) at every point. Covering \(X\) proves the assertion. If every partial derivative is continuous, the standard multivariable differentiability criterion gives \(C^1\) regularity. \(\square\)

Continuity of \(u\) is a real hypothesis here. The distribution \(\delta_0(x)\otimes1(t)\) has zero \(t\)-derivative but is not a continuous function.

## First-order systems without commuting matrices

For a scalar smooth coefficient \(a\), the integrating factor \(E(t)=\exp(\int_{t_0}^t a(s)\,ds)\) satisfies \(E'=Ea\). For matrices the same exponential expression generally fails. We need the order of multiplication fixed.

The matrix transport result in the linked prerequisite proves this exact statement: on a star-shaped open \(V\subset\mathbb R^N\) containing zero, any smooth matrix \(h\) with \(h(0)=0\) has a smooth invertible normalized solution

\[
2(v\cdot\partial_v)S=hS,\qquad S(0)=I.
\tag{3.1}
\]

Its proof uses ordered iterated integrals, with factorial bounds and a separately constructed inverse. It does not assume the matrices commute.

To obtain the integrating factor we need on \(I\), take \(N=1\), \(V=I-t_0\), and

\[
h(v)=2v\,A(t_0+v)^{\mathsf T}.
\tag{3.2}
\]

This is smooth, vanishes at zero, and \(V\) is star-shaped. Equation (3.1) gives \(S'=A(t_0+v)^{\mathsf T}S\) for \(v\ne0\), hence at zero too by continuity. Its ordinary transpose, with no complex conjugation, gives

\[
E(t)=S(t-t_0)^{\mathsf T},\qquad
E'=EA,\quad E(t_0)=I.
\tag{3.3}
\]

The matrix \(E\) and its inverse are smooth on all of \(I\). This is an exact specialization of the existing transport proof.

**Theorem 3.1 (distributional systems become classical).** Let \(A\in C^\infty(I;\mathbb C^{r\times r})\), \(f\in C(I;\mathbb C^r)\), and \(u\in\mathcal D'(I;\mathbb C^r)\). If

\[
u'+Au=f,
\tag{3.4}
\]

then \(u\) is represented by a \(C^1\) vector function and satisfies (3.4) classically. With \(E\) as in (3.3), every distributional solution has the form

\[
u(t)=E(t)^{-1}
\left(c+\int_{t_0}^t E(s)f(s)\,ds\right),
\qquad c\in\mathbb C^r.
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
g'=v+[g]_a\delta_a,\qquad
[g]_a=g(a+)-g(a-).
\tag{4.1}
\]

**Proof.** For fixed \(b>a\) sufficiently close to \(a\),

\[
g(x)=g(b)-\int_x^b v(s)\,ds,\qquad a<x<b.
\]

Absolute integrability makes the right side have a finite limit as \(x\downarrow a\). The same argument to the left gives the other limit. In particular \(g\) is bounded near \(a\), hence locally integrable; its value at one point does not affect its integrals.

For a compact smooth test, integrate by parts separately to the left of \(a-\varepsilon\) and to the right of \(a+\varepsilon\). The outer boundary terms vanish, and

\[
-\int_{|x-a|>\varepsilon}g(x)\phi'(x)\,dx
=\int_{|x-a|>\varepsilon}v(x)\phi(x)\,dx
+g(a+\varepsilon)\phi(a+\varepsilon)
-g(a-\varepsilon)\phi(a-\varepsilon).
\]

Local boundedness of \(g\), integrability of \(v\), and the one-sided limits justify passage to \(\varepsilon\downarrow0\). This gives \(v(\phi)+[g]_a\phi(a)\), exactly (4.1). The argument is local near \(a\); on the rest of the support ordinary integration by parts applies. \(\square\)

The coefficient is the right limit minus the left limit. The sign is determined by the distributional convention, not by a choice of a value at the discontinuity.

For a piecewise \(C^m\) function whose derivatives through order \(m-1\) have finite one-sided limits and whose ordinary \(m\)-th derivative is locally integrable at \(a\), iteration gives

\[
\partial^m g
=g_{\mathrm{ordinary}}^{(m)}
+\sum_{l=0}^{m-1}
[g^{(m-1-l)}]_a\,\delta_a^{(l)}.
\tag{4.2}
\]

To justify the iteration, Theorem 4.1 applied first to \(g\) gives its first jump term. Apply it to the ordinary derivative on each side at each subsequent step. Each previously obtained delta derivative is differentiated once, while the new ordinary derivative contributes its own jump. Induction produces precisely the indices in (4.2). The stated hypotheses ensure all those ordinary derivatives define locally integrable functions.

## Exercises

1. **No hidden singularity — foundation.** Determine every distributional solution of \(u'+2xu=0\) on the line. Explain why the integrating-factor argument also excludes delta terms.
2. **Two derivative levels — intermediate.** Let \(g(x)=0\) for \(x<0\) and \(g(x)=e^{-x}\) for \(x>0\). Compute its first and second distributional derivatives. Check each concentrated coefficient from (4.2).
3. **An unsmoothed transverse variable — intermediate.** On \(\mathbb R_x\times\mathbb R_t\), let \(u=\delta_0(x)\otimes1(t)\). Prove \(\partial_tu=0\), but \(u\) is not a continuous function. Identify the missing hypothesis if one tries to apply Corollary 2.2.
4. **A degenerate leading coefficient — foundation.** Verify \(xH'=0\) distributionally and explain why this does not contradict Corollary 3.2. Give another distributional solution obtained by adding a constant.
5. **Matrix order — advanced.** Put \(B=\begin{pmatrix}0&1\\0&0\end{pmatrix}\), \(C=\begin{pmatrix}0&0\\1&0\end{pmatrix}\), and \(A(t)=B+tC\). Let \(E'=EA\), \(E(0)=I\). Compare the coefficient of \(t^3\) in \(E(t)\) with that in \(\exp(tB+t^2C/2)\). Show the difference is \((BC-CB)/12\), so the naive exponential is not the integrating factor.

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

It is supported on the line \(x=0\) and is nonzero. If represented by a continuous function, that function would be zero off this line, because the distribution is zero there, and then zero on the line by continuity. This contradicts a product bump whose value at \(x=0\) and \(t\)-integral are both one. The missing hypothesis is continuity of \(u\); the right side \(f=0\) is continuous. Theorem 2.1 allows a distributional transverse coefficient, so there is no contradiction.

**Solution 4.** By (4.1), \(H'=\delta_0\). Smooth multiplication gives \((x\delta_0)(\phi)=\delta_0(x\phi)=0\), hence \(xH'=0\). The coefficient of the highest derivative is \(x\), which vanishes at zero; Corollary 3.2 has a monic highest derivative, or equivalently applies after division only where the leading coefficient is nonzero. On either half-line \(H\) is constant and regular, consistent with that local conclusion. Adding any constant \(c\) gives another solution \(H+c\).

**Solution 5.** Write \(E=I+tE_1+t^2E_2+t^3E_3+O(t^4)\), using its smoothness and the differential equation. Comparing coefficients in \(E'=E(B+tC)\) gives

\[
E_1=B,\qquad
E_2=\frac{B^2+C}{2},\qquad
E_3=\frac{B^3}{6}+\frac{CB}{6}+\frac{BC}{3}.
\]

For the exponential, expand \(I+R+R^2/2+R^3/6\), where \(R=tB+t^2C/2\). Its cubic coefficient is \(B^3/6+(BC+CB)/4\). The difference is therefore \((BC-CB)/12\). Here \(B^2=0\), \(BC=\operatorname{diag}(1,0)\), and \(CB=\operatorname{diag}(0,1)\), so it is the nonzero diagonal matrix \(\operatorname{diag}(1,-1)/12\). This proves failure of the exponential even with smooth polynomial coefficients. The ordered transport construction and the right-sided equation \(E'=EA\) are essential.

## References

- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2026, Chapter 3. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
- *Building a local inverse from radial singularities*, “Matrix transport and the order of multiplication.” The ordered-series theorem is used only through (3.1)–(3.3) here. Course lesson.
