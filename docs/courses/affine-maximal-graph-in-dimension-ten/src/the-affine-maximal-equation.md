# The affine maximal equation

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\Omega\subseteq\mathbb R^n\) be open and let \(u:\Omega\to\mathbb R\) be a function of class \(C^4\) whose Hessian \(D^2u\) is positive definite at every point. Its graph has the *affine area*
\[
\int(\det D^2u)^{1/(n+2)}\,dx ,
\]
and the functions that are critical for this area under compactly supported variations are the solutions of the *affine maximal equation*
\[
\begin{gathered}
\sum_{i,j=1}^nU^{ij}\,\partial_{ij}w=0,\\
U=\det(D^2u)\,(D^2u)^{-1},\\
w=(\det D^2u)^{-\frac{n+1}{n+2}} .
\end{gathered}
\]
Section 1 proves this variational description. The matrix \(U\) is the cofactor matrix of the Hessian. A quadratic polynomial with positive definite Hessian solves the equation, because its Hessian is constant and so is \(w\). The *affine Bernstein problem* asks whether, conversely, every solution defined on all of \(\mathbb R^n\) is a quadratic polynomial.

In two variables the question goes back to Chern. Trudinger and Wang proved that a smooth solution on all of \(\mathbb R^2\) with positive definite Hessian is a quadratic polynomial, and that the same holds in higher dimensions under a uniform convexity condition; the introduction of [TW] recounts the history, including Calabi's earlier work. They also observed that the convex function
\[
\begin{gathered}
u_0(x,t)=\sqrt{|x|^9+t^2},\\
(x,t)\in\mathbb R^9\times\mathbb R,
\end{gathered}
\]
is affine maximal in a generalized sense for nonsmooth convex functions [TW, Section 7]. Away from the line \(x=0\) it is smooth and solves the equation (Exercise 4.2 of [Graphs over a convex profile](graphs-over-a-convex-profile.md)), but it is not differentiable at the origin, and its Hessian is singular at the points \((0,t)\).

## The theorem

This course proves the following theorem of OpenAI [OpenAI-AM].

**Theorem A** (OpenAI). There is a function \(u\in C^\infty(\mathbb R^{10})\), not a polynomial of degree at most two, whose Hessian is positive definite at every point and which solves the affine maximal equation on \(\mathbb R^{10}\).

The function has the form \(u(x,t)=\sqrt{F(|x|)^2+t^2}\) on \(\mathbb R^9\times\mathbb R\), where \(F\) is a smooth function on \(\mathbb R^9\), depending only on \(|x|\), with \(F(0)=1\) and positive definite Hessian. Positive definiteness is meant at every point: the theorem asserts no lower bound \(D^2u\ge cI\) with a constant \(c>0\), and nothing about the completeness of the affine metric of the graph.

In a lecture at the Shanghai Center for Mathematical Sciences on 29 April 2026, X.-J. Wang announced a counterexample to the affine Bernstein problem in dimensions ten and higher [Wang-SCMS]; the announcement does not describe its regularity. A companion manuscript of OpenAI gives a proof that in dimensions three through nine every smooth solution with positive definite Hessian whose graph is complete for the induced Euclidean metric is a quadratic polynomial [OpenAI-AB]; that argument is not part of this course.

**The course.**

1. This lesson: the equation as the Euler–Lagrange equation of the affine area, and the statement.
2. [Graphs over a convex profile](graphs-over-a-convex-profile.md): for \(u=\sqrt{F^2+t^2}\), the equation in \(m+1\) variables reduces to two second-order equations for functions \(F\) and \(P\) of \(m\) variables; for radial \(F\) and \(P\), to a system of ordinary differential equations.
3. [A radial solution through the origin](a-radial-solution-through-the-origin.md): a solution of that system, smooth through the origin, from the contraction mapping principle.
4. [An invariant box and the entire graph](an-invariant-box-and-the-entire-graph.md): logarithmic derivatives stay in a fixed box, the solution exists for all radii, and Theorem A follows.

**What the course assumes.** Real analysis from the core courses [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20), in the text of Lebl [Lebl], cited by number where it is used: the mean value theorem (Theorem 4.2.4), the fundamental theorem of calculus (Theorems 5.3.1 and 5.3.3), the change of variables (Theorem 5.3.5), completeness of \(C([a,b])\) and of its closed subsets (Propositions 7.4.5 and 7.4.6), extreme values and uniform continuity on compact sets (Theorems 7.5.6 and 7.5.11), continuity of integrals depending on a parameter (Proposition 7.5.12), the contraction mapping principle (Theorem 7.6.2), differentiation under the integral sign (Theorem 9.1.1), integrals of continuous functions over rectangles (Theorem 10.1.15) and Fubini's theorem (Theorem 10.2.2). Linear algebra: determinants, symmetric matrices and their eigenvalues.

## 1. The equation and the affine area

For a symmetric matrix \(M\) write \(M>0\) when \(M\) is positive definite. Sums over indices are written out.

**Lemma 1.1** (Jacobi's formula). For an invertible \(n\times n\) matrix \(M\) and any \(n\times n\) matrix \(N\),
\[
\begin{aligned}
&\frac{d}{d\varepsilon}\Big|_{\varepsilon=0}\det(M+\varepsilon N)\\
&\quad=\det(M)\operatorname{tr}(M^{-1}N).
\end{aligned}
\]

*Proof.* \(\det(M+\varepsilon N)=\det(M)\det(I+\varepsilon A)\) with \(A=M^{-1}N\). By the Leibniz formula, \(\det(I+\varepsilon A)\) is the sum over permutations \(\sigma\) of \(\operatorname{sgn}\sigma\prod_i(\delta_{i\sigma(i)}+\varepsilon A_{i\sigma(i)})\). The identity permutation contributes \(\prod_i(1+\varepsilon A_{ii})=1+\varepsilon\operatorname{tr}A+\varepsilon^2(\cdots)\). Every other permutation moves at least two indices, so its product has at least two factors \(\varepsilon A_{i\sigma(i)}\) and is a multiple of \(\varepsilon^2\). Hence \(\det(I+\varepsilon A)=1+\varepsilon\operatorname{tr}A+\varepsilon^2q(\varepsilon)\) with a polynomial \(q\). \(\square\)

**Lemma 1.2** (cofactors of a Hessian). Let \(u\in C^3(\Omega)\) with \(D^2u\) invertible at every point, and \(U=\det(D^2u)(D^2u)^{-1}\). Then \(U\) is symmetric and
\[
\sum_{i=1}^n\partial_iU^{ij}=0\qquad(1\le j\le n).
\]

*Proof.* Write \(M=D^2u\) and \(m^{ab}\) for the entries of \(M^{-1}\); both are symmetric, so \(U\) is. The entries \(u_{abi}\) of \(\partial_iM\) are symmetric in \(a,b,i\). Differentiating \(MM^{-1}=I\) gives \(\partial_i(M^{-1})=-M^{-1}(\partial_iM)M^{-1}\), and Lemma 1.1 with the chain rule gives \(\partial_i\det M=\det(M)\operatorname{tr}(M^{-1}\partial_iM)\). Hence
\[
\frac{\sum_i\partial_iU^{ij}}{\det M}=S_1-S_2,
\]
where
\[
\begin{aligned}
S_1&=\sum_{i,a,b}m^{ba}u_{abi}m^{ij},\\
S_2&=\sum_{i,a,b}m^{ia}u_{abi}m^{bj}.
\end{aligned}
\]
Renaming the summation indices \((i,a,b)\) of \(S_2\) as \((b,a,i)\) turns it into \(\sum_{i,a,b}m^{ba}u_{aib}m^{ij}\), which is \(S_1\) because \(u_{aib}=u_{abi}\). \(\square\)

**Proposition 1.3** (first variation of the affine area). Let \(u\in C^4(\Omega)\) with \(D^2u>0\) on \(\Omega\), and let \(\varphi\in C^2(\Omega)\) vanish outside a compact set \(K\subseteq\Omega\). There is \(\varepsilon_0>0\) such that \(D^2(u+\varepsilon\varphi)>0\) on \(\Omega\) for \(|\varepsilon|\le\varepsilon_0\). The function
\[
\begin{aligned}
\mathcal A(\varepsilon)=\int_\Omega\Bigl(&\bigl(\det D^2(u+\varepsilon\varphi)\bigr)^{\frac1{n+2}}\\
&-(\det D^2u)^{\frac1{n+2}}\Bigr)\,dx
\end{aligned}
\]
is differentiable at \(0\), with
\[
\mathcal A'(0)=\frac1{n+2}\int_\Omega\varphi\sum_{i,j}U^{ij}\partial_{ij}w\,dx .
\]
Consequently \(u\) solves the affine maximal equation on \(\Omega\) if and only if \(\mathcal A'(0)=0\) for every such \(\varphi\).

The integrand of \(\mathcal A(\varepsilon)\) is continuous and vanishes outside \(K\); extended by zero it is continuous on \(\mathbb R^n\) with compact support, and the integral is the Riemann integral over any closed rectangle containing \(K\) [Lebl, Theorem 10.1.15].

*Proof.* *Positivity.* The function \((x,v)\mapsto v^{\mathsf T}D^2u(x)v\) is continuous and positive on the compact set \(K\times\{|v|=1\}\), so it has a minimum \(c>0\) there [Lebl, Theorem 7.5.6]; likewise \(|v^{\mathsf T}D^2\varphi(x)v|\le b\) there for some \(b\). For \(|\varepsilon|\le\varepsilon_0=c/(2b+1)\), \(v^{\mathsf T}D^2(u+\varepsilon\varphi)v\ge\frac c2|v|^2\) on \(K\), and outside \(K\) the two Hessians agree.

*Differentiation.* For \(x\in K\) and \(|\varepsilon|\le\varepsilon_0\) let \(g(x,\varepsilon)\) be the \((n+2)\)-th root of \(\det\bigl(D^2u(x)+\varepsilon D^2\varphi(x)\bigr)\). It is continuous with a continuous derivative \(\partial_\varepsilon g\), because the determinant is a polynomial in the entries and stays positive. By the mean value theorem [Lebl, Theorem 4.2.4], \((g(x,\varepsilon)-g(x,0))/\varepsilon=\partial_\varepsilon g(x,\theta\varepsilon)\) for some \(\theta\in(0,1)\) depending on \(x\) and \(\varepsilon\). Since \(\partial_\varepsilon g\) is uniformly continuous on the compact set \(K\times[-\varepsilon_0,\varepsilon_0]\) [Lebl, Theorem 7.5.11], the difference quotients converge to \(\partial_\varepsilon g(x,0)\) uniformly in \(x\), and integrating over a rectangle containing \(K\) shows \(\mathcal A'(0)=\int_K\partial_\varepsilon g(x,0)\,dx\). By Lemma 1.1 and the chain rule,
\[
\begin{aligned}
\partial_\varepsilon g(x,0)&=\frac{(\det D^2u)^{\frac1{n+2}}}{n+2}\\
&\quad\times\operatorname{tr}\bigl((D^2u)^{-1}D^2\varphi\bigr),
\end{aligned}
\]
and since \(\frac1{n+2}-1=-\frac{n+1}{n+2}\), this is \(\frac1{n+2}\,w\sum_{i,j}U^{ij}\partial_{ij}\varphi\).

*Integration by parts.* If \(a,b\in C^1(\Omega)\) and \(ab\) vanishes outside a compact subset of \(\Omega\), then \(\int_\Omega a\,\partial_ib\,dx=-\int_\Omega(\partial_ia)\,b\,dx\): extend \(ab\) by zero, integrate first in \(x_i\) by Fubini's theorem [Lebl, Theorem 10.2.2], and use \(\int_{\mathbb R}\partial_i(ab)\,dx_i=0\) [Lebl, Theorem 5.3.1]. The functions \(wU^{ij}\) are of class \(C^2\), since \(u\in C^4\). Applying the rule twice, with Lemma 1.2,
\[
\begin{aligned}
\int wU^{ij}\partial_{ij}\varphi&=-\int\partial_i(wU^{ij})\,\partial_j\varphi,\\
\sum_i\partial_i(wU^{ij})&=\sum_i(\partial_iw)\,U^{ij},
\end{aligned}
\]
and
\[
\sum_j\partial_j\Bigl(\sum_i(\partial_iw)U^{ij}\Bigr)=\sum_{i,j}U^{ij}\partial_{ij}w,
\]
because \(\sum_j\partial_jU^{ij}=\sum_j\partial_jU^{ji}=0\) by the symmetry of \(U\) and Lemma 1.2. This gives the formula for \(\mathcal A'(0)\).

*The equivalence.* If \(u\) solves the equation, \(\mathcal A'(0)=0\). Conversely, suppose \(L=\sum_{i,j}U^{ij}\partial_{ij}w\) is positive at some \(x_0\) (the negative case is symmetric). By continuity \(L>0\) on a ball \(B(x_0,\rho)\subseteq\Omega\) with closure in \(\Omega\). The function \(\varphi(x)=(\rho^2-|x-x_0|^2)^3\) for \(|x-x_0|<\rho\), and \(0\) elsewhere, is of class \(C^2\), vanishes outside the closed ball, and gives \(\mathcal A'(0)>0\). \(\square\)

## 2. Solutions and the Bernstein question

Quadratic polynomials \(u(x)=\frac12x^{\mathsf T}Mx+b\cdot x+c\) with \(M>0\) solve the equation on \(\mathbb R^n\). In one variable they are the only solutions on \(\mathbb R\) (Exercise 4.4). The equation is invariant under linear changes of the variables (Exercise 4.3), and also under adding an affine function to \(u\), since that does not change \(D^2u\).

Theorem A shows that in ten variables the equation has a smooth solution on all of \(\mathbb R^{10}\), with positive definite Hessian, that is not quadratic. The construction keeps the form \(\sqrt{F^2+t^2}\) of the example \(u_0\), with \(F(x)=|x|^{9/2}\) replaced by a smooth function with \(F(0)=1\).

## 3. The plan of the proof

[Graphs over a convex profile](graphs-over-a-convex-profile.md) computes the Hessian of \(\sqrt{F(x)^2+t^2}\) on \(\mathbb R^m\times\mathbb R\) and shows that the affine maximal equation in \(n=m+1\) variables follows from the two equations
\[
\begin{gathered}
\det D^2F=FP^{-\gamma},\\
\operatorname{tr}\bigl((D^2F)^{-1}D^2P\bigr)+(m+2)\frac PF=0,
\end{gathered}
\]
with \(\gamma=\frac{m+3}{m+2}\), for an auxiliary positive function \(P\). For radial \(F\) and \(P\) these become ordinary differential equations in \(r=|x|\), singular at \(r=0\). [A radial solution through the origin](a-radial-solution-through-the-origin.md) solves them near \(r=0\) with \(F(0)=P(0)=1\), smoothly in \(x\). [An invariant box and the entire graph](an-invariant-box-and-the-entire-graph.md) proves, for \(m=9\), that the solution exists for all \(r>0\) with \(F,P>0\): three logarithmic derivatives of \(F\), \(F'\) and \(P\) stay in a box whose upper corner is given by the exponents of the example \(u_0\).

## 4. Exercises

**4.1** (easy). Show directly that every quadratic polynomial with positive definite Hessian solves the affine maximal equation, and that so does \(u+\ell\) for every solution \(u\) and every affine function \(\ell\).

**4.2** (easy). For \(n=2\) write out \(U\) and verify Lemma 1.2 by hand.

**4.3** (medium). Let \(u\) solve the equation on \(\mathbb R^n\) and let \(A\) be an invertible \(n\times n\) matrix. Show that \(v(y)=u(Ay)\) solves it on \(\mathbb R^n\).

**4.4** (medium). Find all solutions of the equation for \(n=1\) on an open interval, and show that a solution on all of \(\mathbb R\) is a quadratic polynomial.

## 5. Solutions

**4.1.** If \(D^2u=M\) is constant, \(w\) is constant and \(\partial_{ij}w=0\). Adding an affine function does not change \(D^2u\), hence does not change \(U\) or \(w\).

**4.2.** For \(n=2\), \(U^{11}=u_{22}\), \(U^{22}=u_{11}\) and \(U^{12}=U^{21}=-u_{12}\). Then \(\partial_1U^{11}+\partial_2U^{21}=u_{221}-u_{122}=0\) and \(\partial_1U^{12}+\partial_2U^{22}=-u_{121}+u_{112}=0\).

**4.3.** By the chain rule \(D^2v(y)=A^{\mathsf T}D^2u(Ay)A\), so \(\det D^2v(y)=(\det A)^2\det D^2u(Ay)\) and \(w_v(y)=\kappa\,w_u(Ay)\) with \(\kappa=|\det A|^{-2(n+1)/(n+2)}\). Hence \(D^2w_v(y)=\kappa A^{\mathsf T}D^2w_u(Ay)A\), and
\[
\begin{aligned}
U_v(y)={}&(\det A)^2\det D^2u(Ay)\\
&\times A^{-1}(D^2u(Ay))^{-1}A^{-\mathsf T}.
\end{aligned}
\]
Since \(\sum_{i,j}U^{ij}\partial_{ij}w=\operatorname{tr}(U\,D^2w)\) and the trace is invariant under cyclic permutations,
\[
\begin{aligned}
&\operatorname{tr}(U_vD^2w_v)(y)\\
&\quad=\kappa(\det A)^2\operatorname{tr}(U_uD^2w_u)(Ay)=0 .
\end{aligned}
\]

**4.4.** For \(n=1\) the cofactor of a \(1\times1\) matrix is \(1\), so the equation reads \(w''=0\) with \(w=(u'')^{-2/3}\). Thus \(w(x)=\alpha x+\beta\) with \(w>0\) on the interval, and \(u''=(\alpha x+\beta)^{-3/2}\); conversely every such \(u\) is a solution. On all of \(\mathbb R\), \(\alpha x+\beta>0\) for all \(x\) forces \(\alpha=0\), so \(u''\) is a positive constant and \(u\) is a quadratic polynomial.

## References

- [OpenAI-AM] OpenAI, *A Smooth Nonquadratic Entire Affine Maximal Graph in Dimension Ten*, OpenAI Math Release preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/Smooth-Nonquadratic-Affine-Maximal-Graph-in-Dimension-Ten-October-5-2026
- [OpenAI-AB] OpenAI, *The affine Bernstein theorem in dimensions three through nine*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026
- [Wang-SCMS] X.-J. Wang, *The affine Bernstein and affine Plateau problems*, SCMS Gu Lecture, Shanghai Center for Mathematical Sciences, Fudan University, 29 April 2026; lecture announcement with abstract. https://lmns.fudan.edu.cn/_upload/article/files/a0/16/6c8597a34637a8cf5a057fa621d9/58b03977-b8f9-44c2-8a8b-de917cf4e438-B.pdf
- [TW] N. S. Trudinger and X.-J. Wang, *The Bernstein problem for affine maximal hypersurfaces*, Inventiones Mathematicae 140 (2000), 399–422; the introduction and Section 7. https://maths-people.anu.edu.au/~wang/publications/1-Invent00.pdf
- [Lebl] J. Lebl, *Basic Analysis I and II*, version 6.3; the text of the core courses [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20). https://www.jirka.org/ra/
