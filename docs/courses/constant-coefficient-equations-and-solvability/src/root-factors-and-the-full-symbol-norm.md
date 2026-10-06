# Root factors and the full symbol norm

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The size of a polynomial at one frequency can vanish even when its differential operator retains a substantial derivative norm. Each root factor therefore needs a unit margin and a measure of the root's variation. We prove the precise product comparison, including its leading coefficient. Uniformity requires a larger ball on which that coefficient does not vanish.

Read [Uniform bounds for algebraic analytic branches](uniform-bounds-for-algebraic-analytic-branches.md), [Regular balls, moving roots and complex gauges](regular-balls-moving-roots-and-complex-gauges.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## The exact norm and the local hypotheses

Let \(P(z,s)\ne0\) have total degree at most \(M\ge1\), with \(z\in\mathbb C^d\) and \(s\in\mathbb C\). Let \(q\) be its degree in \(s\), and \(a(z)\) its leading coefficient in that variable. For \(c\in\mathbb C^d\), assume that \(a\) is zero-free on \(B(c,2)\) and that its \(q\) roots have analytic labels there, with multiplicity, so that
\[
\begin{gathered}
P(z,s)=a(z)\prod_{j=1}^q(s-\tau_j(z)),\\
\qquad |z-c|<2.
\end{gathered}
\tag{1}
\]
In the primary regular-fiber setting, the nonvanishing of the leading coefficient times the full-degree discriminant on this ball supplies these labels by the preceding ball-labeling proof. The argument below only needs(1), so it also applies when repeated analytic labels have already been supplied.

At \(\eta=(c,b)\), \(b\in\mathbb C\), define
\[
\begin{gathered}
S_P(\eta)=\left(\sum_{|\beta|\le M}
                       |\partial^\beta P(\eta)|^2\right)^{1/2},
 \\
\quad
 B_j=|b-\tau_j(c)|+1+
                   \sup_{|z-c|<1}|\nabla\tau_j(z)|.
\end{gathered}
\tag{2}
\]
All \(d+1\) polynomial coordinates enter the derivative norm, with the derivative factors retained. The complex gradient norm is Euclidean. Derivatives above the degree are zero, so choosing an upper degree bound does not alter \(S_P\). For \(d=0\), the tangential ball is one point and the gradient term is zero.

**Theorem.** There is a constant \(C\ge1\), depending only on \(M\) and \(d+1\), such that
\[
\begin{gathered}
C^{-1}S_P(c,b)\\
\le |a(c)|\prod_{j=1}^q B_j
                         \\
\le C S_P(c,b).
\end{gathered}
\tag{3}
\]
The product for \(q=0\) is one. The constant is uniform in \(P,c,b\) and the ordering of the labels under the stated hypotheses.

## Polynomial norms and the leading coefficient

Put \(n=d+1\), and in translated coordinates use
\(U=\{(z,w):|z|<1,\ |w|<1\}\). A finite constant \(A=A_{M,n}\ge1\) satisfies
\[
\begin{gathered}
A^{-1}S_P(c,b)\\
\le
       \sup_U|P(c+z,b+w)|\\
\le A S_P(c,b).
\end{gathered}
\tag{4}
\]
For the upper bound, the finite Taylor formula at \((c,b)\) and scalar Cauchy–Schwarz give
\(\sup_U|P|\le S_P(c,b)(\sum_{|\beta|\le M}1/(\beta!)^2)^{1/2}\),
since every coordinate of \((z,w)\) has modulus at most one. For the lower bound, the closed polydisk of common coordinate radius \(1/(2\sqrt n)\) lies strictly inside \(U\). The Cauchy estimate bounds each derivative by
\(\beta!(2\sqrt n)^{|\beta|}\sup_U|P|\).
Take the finite square sum over \(|\beta|\le M\), and choose \(A\) to bound both constants. These estimates are valid at complex centers and are independent of the coefficients.

The zero-free hypothesis gives the particularly simple leading-coefficient comparison
\[
\begin{gathered}
2^{-M}|a(c)|\le |a(c+z)|\le(3/2)^M|a(c)|,
                               \\
\qquad |z|<1.
\end{gathered}
\tag{5}
\]
For \(z\ne0\), restrict \(a\) to the line \(c+\lambda e\), with \(e=z/|z|\). Its value at \(\lambda=0\) is nonzero. Every root \(\lambda_\nu\) of this one-variable polynomial has \(|\lambda_\nu|\ge2\), since the original coefficient is zero-free on the open ball of radius two. Scalar factorization gives the ratio to its center value as \(\prod_\nu(1-\lambda/\lambda_\nu)\). At \(\lambda=|z|<1\), each factor's modulus lies between \(1/2\) and \(3/2\). There are at most \(M\) factors, so(5) follows. A constant line polynomial and \(z=0\) give ratio one. In dimension zero, \(a\) is constant and the same conclusion holds.

In particular both directions of the coefficient estimate are uniform; no reciprocal polynomial estimate is merely asserted.

## The root factors are a fixed-degree graph family

Suppose first that \(q\ge1\). On
\(Z=\{(z,w):|z|<2,\ |w|<2\}\), define
\[
\begin{gathered}
F_j(z,w)=b+w-\tau_j(c+z),\\
\qquad
 P(c+z,b+w-F_j(z,w))=0.
\end{gathered}
\tag{6}
\]
This is a nonzero polynomial relation of total degree at most \(M\) in the joint \((z,w)\) variables and the extra graph variable. The substitution in the original polynomial is surjective in its last argument and does not turn a nonzero polynomial into zero. Hence every \(F_j\) belongs to the fixed graph family \(\mathcal A_M(Z)\), in complex dimension \(d+1\). All constants from the branch lemmas apply on these fixed translated domains, independently of \(c,b\) and the coefficients.

Write \(L_j=\sup_U|F_j|\). There is a constant \(A_1=A_{M,n}\) such that
\[
 L_j\le B_j\le A_1 L_j.
 \tag{7}
\]
The first inequality follows by integration on the straight segment from \(c\) to \(c+z\): the variation of \(\tau_j\) is at most
\(|z|\sup_{B(c,1)}|\nabla\tau_j|\), by the complex directional derivative and scalar Cauchy–Schwarz. Add \(|w|<1\) and the center root distance.

For the reverse inequality, keeping \(z=0\) and varying \(w\) on the unit disk gives
\(|b-\tau_j(c)|+1\le L_j\); the supremum equals that sum by choosing the radial direction of the center difference, with the zero-difference case immediate. Let \(U_+=\{(z,w):|z|<3/2,\ |w|<3/2\}\). The uniform branch comparison gives \(\sup_{U_+}|F_j|\le A_2 L_j\), with \(A_2\) depending only on \(M,n\). For \(|z|<1\), a coordinate disk of radius \(1/4\) about \(z\), with \(w=0\), stays in \(U_+\). The Cauchy derivative bound therefore gives
\[
 \sup_{|z|<1}|\nabla\tau_j(c+z)|
                        \le4\sqrt d\, A_2 L_j.
 \tag{8}
\]
For \(d=0\) this term is zero. Thus \(A_1=1+4\sqrt d\,A_2\) is valid in(7).

The product comparison for these analytic graph functions gives
\[
\begin{gathered}
\prod_{j=1}^qL_j
        \le A_3\sup_U\left|\prod_{j=1}^qF_j\right|,
 \\
\qquad
 \prod_{j=1}^qF_j(z,w)
          =\frac{P(c+z,b+w)}{a(c+z)}.
\end{gathered}
\tag{9}
\]
Here \(A_3\) depends on \(M,n,q\); because \(1\le q\le M\), take its maximum over that finite range for a constant depending only on \(M,n\).

## Both sides of the comparison

Using(4), the upper coefficient bound in(5) and the first inequality in(7), we obtain
\[
\begin{gathered}
S_P(c,b)
 \\
\le A\sup_U|P|
 \\
\le A(3/2)^M |a(c)|\prod_jL_j
 \\
\le A(3/2)^M |a(c)|\prod_jB_j.
\end{gathered}
\tag{10}
\]
For the other direction, use the second inequality in(7), the product comparison, the lower coefficient bound and then(4):
\[
\begin{gathered}
|a(c)|\prod_jB_j
 \\
\le |a(c)|A_1^q A_3\sup_U|P/a|
 \\
\le 2^M A_1^q A_3\sup_U|P|
 \\
\le 2^M A_1^q A_3 A S_P(c,b).
\end{gathered}
\tag{11}
\]
Take \(C\) at least both displayed constants. This proves(3) for \(q\ge1\).

If \(q=0\), then \(P(z,s)=a(z)\). The full derivative norm still includes every tangential derivative, and all normal derivatives are zero. Evaluation gives \(S_P(c,b)\ge|a(c)|\). Conversely(4)–(5) give \(S_P(c,b)\le A(3/2)^M|a(c)|\). Enlarging \(C\) includes this case as well. Nonzero constants have \(S_P=|a|\) and give exact equality.

The labels need not be distinct in this proof. When a repeated factor admits analytic labels on the entire ball, the same graph-family and product arguments count it with its actual multiplicity. This observation does not assert that an arbitrary singular root fiber has analytic labels.

## Exercises with complete solutions

**Exercise 1 — basic: the root variation term.** For \(P(z,s)=s-Az\), compute(2) at \((c,b)\), and compare both sides without unspecified constants. Explain why the gradient term matters.

**Solution.** The single root is \(\tau(z)=Az\), with derivative \(A\), and the leading coefficient is one. The only nonzero first derivatives of \(P\) are \(1\) and \(-A\). With \(u=|b-Ac|\), the exact quantities are
\[
\begin{gathered}
S_P(c,b)=\sqrt{u^2+1+|A|^2},\\
\qquad
 B_1=u+1+|A|,\\
\qquad
 S_P(c,b)\le B_1\le\sqrt3\,S_P(c,b).
\end{gathered}
\tag{12}
\]
The inequalities are the triangle inequality and scalar Cauchy–Schwarz on three nonnegative coordinates. At \(b=Ac\), the pointwise symbol is zero, but its norm is \(\sqrt{1+|A|^2}\). Omitting the gradient term would leave only one at this characteristic center and fail uniformly as \(|A|\to\infty\).

**Exercise 2 — intermediate: retain the nonmonic coefficient.** Let \(P_\varepsilon(z,s)=\varepsilon s-z\), with \(0<\varepsilon\le1\). Compute the comparison at \((0,0)\) and show what happens if its leading coefficient is dropped.

**Solution.** The leading coefficient is the nonzero constant \(\varepsilon\); the analytic root is \(\tau(z)=z/\varepsilon\), and its gradient has modulus \(1/\varepsilon\). Therefore
\[
\begin{gathered}
S_{P_\varepsilon}(0,0)=\sqrt{1+\varepsilon^2},\\
\qquad
 B_1=1+1/\varepsilon,\\
\qquad
 |a(0)|B_1=1+\varepsilon.
\end{gathered}
\tag{13}
\]
The derivative norm and the coefficient-weighted factor stay between one and two and are uniformly comparable. The unweighted \(B_1\) tends to infinity as \(\varepsilon\downarrow0\). Removing the coefficient would therefore turn a valid degree-one uniform estimate into a false one. The limiting polynomial is \(-z\), with last-variable degree zero; this explains why an argument based only on a monic normal form cannot ignore the coefficient.

**Exercise 3 — advanced: the extra zero-free margin.** For \(P_\varepsilon(z,s)=(1+\varepsilon-z)s-1\), \(0<\varepsilon<1\), verify that its analytic root is regular on the unit spatial disk. Show that the right-hand bound in(3) cannot hold with a degree-only constant if the ball of radius two is replaced just by that unit disk.

**Solution.** The leading coefficient vanishes at \(1+\varepsilon\), outside the unit disk but inside the ball of radius two. Its root \(\tau(z)=1/(1+\varepsilon-z)\) is analytic on the unit disk and has no branch point there. Its derivative supremum on that open disk is \(1/\varepsilon^2\), by the reverse triangle inequality and approach along the positive real radius. At \((c,b)=(0,0)\), the nonzero polynomial derivatives are \(P=-1\), \(\partial_sP=1+\varepsilon\) and \(\partial_z\partial_sP=-1\). Thus
\[
\begin{gathered}
S_{P_\varepsilon}(0,0)=\sqrt{2+(1+\varepsilon)^2}\le\sqrt6,\\|a(0)|B_1
  \\
=(1+\varepsilon)\left(\frac1{1+\varepsilon}+1+\frac1{\varepsilon^2}\right).
\end{gathered}
\tag{14}
\]
The second expression tends to infinity, whereas the first remains bounded. These are all degree-two polynomials. Analytic labeling on the smaller ball alone therefore gives no uniform comparison; the larger zero-free coefficient margin controls the root derivatives near the smaller boundary. This counterexample does not satisfy the theorem's radius-two hypothesis.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
