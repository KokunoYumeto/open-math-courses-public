# Cauchy bounds, root counts and analytic extensions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A contour gives both a derivative bound and an exact count of a root cluster. We derive polydisk estimates, maximum modulus and weighted disk root counts, then explain how a real analytic series supplies a local complex neighborhood.

[Cauchy kernels and distributional boundary limits](../prerequisites/cauchy-kernels-and-boundary-limits.html), Theorem 1.1 and Corollary 2.2, proves the disk Cauchy formula. [Holomorphic boundaries in convex cones](../prerequisites/holomorphic-boundaries-in-convex-cones.html), formula (3.1) and Lemma 3.1, proves its polydisk iteration and the identity principle. [Boundary flux and weak identities](../prerequisites/boundary-flux-and-weak-identities.html), Corollary 2.3, gives the complex Green identity.

Zeff’s notes give a basic account of the Cauchy formula, and Hörmander explains its uses in polynomial equations. We work on open subsets of complex Euclidean space and orient each boundary circle counterclockwise.

## Cauchy estimates and parameter contours

**Lemma 1.1 (the needed polydisk estimate).** Suppose \(f\) is holomorphic on a neighborhood of the closed polydisk \(\{|z_j-a_j|\le r_j\}_{j=1}^d\), where all \(r_j>0\). Let \(M\) be its supremum on the product of boundary circles. Then

\[
|\partial_z^\alpha f(a)|
\le \alpha! M\prod_{j=1}^d r_j^{-\alpha_j}.
\tag{1}
\]

If \(f\) is holomorphic on a neighborhood of a closed complex Euclidean ball of radius \(r>0\), the estimate at its center is in particular \(\alpha!M(\sqrt d/r)^{|\alpha|}\) for \(d\ge1\), where \(M\) now bounds the entire ball.

**Proof.** [Cauchy kernels and distributional boundary limits](../prerequisites/cauchy-kernels-and-boundary-limits.html) Corollary 2.2, formulas (2.3)–(2.4), gives the disk coefficient integral and the bound \(Mr^{-j}\). Applying that formula successively in the \(d\) coordinates is legal: the continuous integrand lies on a compact product of circles. The fully written iteration in [Holomorphic boundaries in convex cones](../prerequisites/holomorphic-boundaries-in-convex-cones.html) formula (3.1) identifies its coefficient with \(\partial_z^\alpha f(a)/\alpha!\) and bounds it by \(M\prod r_j^{-\alpha_j}\). This is (1). The polydisk of equal radius \(r/\sqrt d\) lies in the closed ball, including its corners, so the asserted ball estimate follows. Dimension zero is evaluation at a point, with empty product 1. \(\square\)

**Lemma 1.2 (uniform holomorphic limits and compact contour differentiation).** A sequence of holomorphic functions on an open complex domain which converges uniformly on every compact subset has a holomorphic limit, and each fixed derivative converges uniformly on smaller compact subsets. If \(G(w,z)\) and each needed \(w\)-derivative are continuous on a product of a parameter neighborhood and a fixed compact piecewise C¹ contour, then the integral over that contour can be differentiated under the integral sign. If \(G\) is holomorphic in the complex parameters there, its contour integral is holomorphic in those parameters.

**Proof.** Enclose any point in two concentric closed polydisks lying in the domain, with the first strictly smaller than the second. Pass the uniform limit through the iterated Cauchy integral on the outer product of circles. On the inner polydisk its denominator series and every fixed differentiated denominator series converge uniformly, with a summable geometric majorant. The limit therefore has that convergent power series, and its derivatives are the limits of the derivative integrals. The same estimates are uniform on the inner closed polydisk. Finite coverings prove the compact-subset assertion.

For a contour, parametrize its finitely many C¹ pieces on compact intervals. A real parameter difference quotient of \(G\) is the integral of its parameter derivative along the corresponding short parameter segment. Continuity on a slightly smaller compact parameter neighborhood gives uniform convergence of this difference quotient on the contour and a uniform bound. Integrating proves the differentiation assertion, piece by piece. Repeat for each fixed higher derivative. In complex parameters the resulting first derivatives obey the coordinate Cauchy–Riemann equations, because those of \(G\) do. Lemma 1.1 and the written polydisk argument then give holomorphy. \(\square\)

This proof applies to the moving-root sums in the polynomial approximation lesson and the subspace-detection lesson by first choosing a fixed circle on which their denominator is nonzero. A positive lower bound on the compact circle persists in a sufficiently small parameter neighborhood. 

## Modulus and multiplicity on a disk

**Lemma 2.1 (maximum modulus).** If a holomorphic function on a connected open complex domain of one variable has a local maximum of its modulus, it is constant. In particular a function holomorphic near a closed disk attains its maximum modulus on its boundary. For a zero-free such function the same assertion applies to its reciprocal.

**Proof.** At a local maximum \(a\), choose a small disk on which \(M=|f(a)|\) is an upper bound. If \(M=0\), the function vanishes on this disk. Otherwise multiply \(f\) by the unit complex number which makes \(f(a)=M>0\). The disk Cauchy formula at \(a\) gives the circle mean of \(f\) as \(M\). The continuous nonnegative function \(M-\operatorname{Re}f\) has mean zero on that circle and hence is zero everywhere on the circle. Since \(|f|\le M\), this forces \(f=M\) on the circle. Cauchy's formula then gives \(f=M\) inside it. The identity principle in [Holomorphic boundaries in convex cones](../prerequisites/holomorphic-boundaries-in-convex-cones.html) Lemma 3.1 propagates this constant over the connected domain. On a closed disk compactness gives a maximum; an interior maximum is covered by the result just proved. If \(f\ne0\) near the disk, \(1/f\) is holomorphic by the quotient rule, so the same proof applies. \(\square\)

**Theorem 2.2 (argument principle and weighted root count on a disk).** Let \(f\) be holomorphic near a closed disk \(\overline D\) and nonzero on its positive boundary circle. Its zeros \(a_1,\ldots,a_s\) in \(D\) have finite multiplicities \(m_1,\ldots,m_s\ge1\). For every \(b\) holomorphic near \(\overline D\),

\[
\frac1{2\pi i}\int_{\partial D} b(z)\frac{f'(z)}{f(z)}\,dz
=\sum_{j=1}^s m_j b(a_j).
\tag{2}
\]

The empty sum is zero. Taking \(b=1\) counts the zeros with multiplicity.

**Proof.** The local Cauchy series shows that either the first nonzero coefficient at a zero occurs at a finite order \(m\), or the function vanishes on a neighborhood. The latter case would force it to vanish on the component containing the disk, contradicting the boundary hypothesis. Thus every zero is isolated and has the representation \(f(z)=(z-a)^m g(z)\), with \(g(a)\ne0\). Nonvanishing on the compact boundary gives a zero-free annular neighborhood of it. Infinitely many zeros in the remaining compact interior would have an accumulation point, contradicting their isolation. There are therefore finitely many.

Division by their local power factors defines a holomorphic function \(h=f/\prod_j(z-a_j)^{m_j}\) on a neighborhood of the closed disk, with the quotients at zeros defined by those convergent series. It is zero-free on the closed disk and on a possibly smaller neighborhood of it. Consequently

\[
\frac{f'}f=\sum_{j=1}^s\frac{m_j}{z-a_j}+\frac{h'}h
\quad\text{on }\partial D.
\tag{3}
\]

The disk Cauchy formula gives \(\int_{\partial D} b(z)/(z-a_j)\,dz=2\pi i b(a_j)\). The function \(b h'/h\) is holomorphic near the closed disk and its circle integral is zero. For this last statement, multiply it by a compact smooth cutoff equal to one near the disk and apply [Boundary flux and weak identities](../prerequisites/boundary-flux-and-weak-identities.html) Corollary 2.3: its \(\bar\partial\) is zero on the disk. The area integral is zero, including the correct positive orientation. Substitution in (3) proves (2). \(\square\)

**Corollary 2.3 (Rouché and persistent clusters).** If \(f,g\) are holomorphic near the closed disk and \(|g|<|f|\) on its boundary, \(f\) and \(f+g\) have the same number of interior zeros counted with multiplicity. In particular the number of roots in a fixed disk persists under a sufficiently small uniform perturbation of its boundary values.

**Proof.** Put \(f_t=f+tg\), for real \(0\le t\le1\). On the boundary,

\[
|f_t|\ge |f|-|g|\ge c>0,
\tag{4}
\]

because the strict inequality is uniform on a compact circle. The integral in (2) with \(b=1\) is a continuous function of \(t\): its numerator and denominator are continuous there, with the common lower bound \(c\). The theorem identifies it with a nonnegative integer for every \(t\). A continuous integer-valued function on an interval is constant; otherwise the intermediate value theorem would give a noninteger value. This proves the assertion and its perturbation consequence. \(\square\)

The relevant contours in the polynomial approximation lesson Lemma 4.2 and the subspace-detection lesson Lemma 3.2 are precisely positive circles. Formula (2) with \(b(z)=e^{i y z}\) also supplies the exponential root average in the subspace-detection lesson, including repeated roots. 

## A complex neighborhood of a real analytic function

**Lemma 3.1 (local complex extension).** Use the usual real-analytic convention: near each real point \(a\in\mathbb R^d\), the function has a real power series which is absolutely convergent in a real coordinate neighborhood. Then it has a holomorphic extension to a complex neighborhood of that point. On each compact real set its complex extension yields local factorial derivative bounds with uniform constants after taking a finite cover.

**Proof.** Write the real series as \(\sum_\alpha c_\alpha(x-a)^\alpha\). Choose positive radii \(R_j\) such that the closed real box lies strictly inside its absolute-convergence region. At the real point \(a+(R_1,\ldots,R_d)\), absolute convergence says

\[
\sum_\alpha |c_\alpha|R^\alpha<\infty.
\tag{5}
\]

Use the same coefficients for complex \(z\) with \(|z_j-a_j|<R_j\). The series converges absolutely and uniformly on every smaller closed polydisk. Each fixed derivative does too: the factors polynomial in the indices are bounded after multiplication by \(\prod_j(r_j/R_j)^{\alpha_j}\), where \(r_j<R_j\); the finitely many low indices can be treated separately. Termwise differentiation is therefore valid, the coordinate Cauchy–Riemann equations hold, and the resulting function is holomorphic. On the real neighborhood it equals the original series.

To get a bound at every real point in a smaller box, choose one common positive radius in each coordinate whose centered polydisk stays in a fixed larger closed polydisk. Its extension has a finite supremum there. Formula (1) gives \(M\alpha!r^{- |\alpha|}\), with equal coordinate radii \(r\) if desired. A compact real set has a finite cover of these smaller boxes; the largest \(M\) and reciprocal radius provide common constants. Dimension zero is the scalar extension at its one point. \(\square\)

The converse local factorial-bound-to-real-series argument remains the Taylor proof in the anisotropic-derivative lesson Proposition 2.1. Lemmas 3.1 and 1.1 supply precisely its other direction and the directional Cauchy estimates; there is no assumption of a globally single-valued complex extension of the entire real domain.

## Exercises with complete solutions

**Exercise 1 (intermediate: multiplicity).** Let \(f(z)=(z-a)^2(z-b)\), where \(a\ne b\) are inside a disk. Evaluate the weighted root integral in (2) with \(b(z)=e^{iyz}\). Prove that any sufficiently small holomorphic boundary perturbation has three zeros counted with multiplicity in the disk.

**Solution 1.** Rename the weight \(B(z)=e^{iyz}\) to distinguish it from the point \(b\). Formula (2) gives \(2e^{iya}+e^{iyb}\). Since \(f\) is nonzero on the compact boundary, \(c=\min_{\partial D}|f|>0\). For any perturbation \(g\) with \(\sup_{\partial D}|g|<c\), Corollary 2.3 preserves the count \(2+1=3\). It does not preserve each root multiplicity individually: a small perturbation can split the double root while preserving the total.

**Exercise 2 (basic: a zero-free disk).** A function \(h\) is holomorphic near the closed unit disk, is zero-free there, and has \(|h|\ge c>0\) on its boundary. Prove \(|h(0)|\ge c\). Explain why the zero-free hypothesis is needed.

**Solution 2.** The reciprocal is holomorphic near the disk. Maximum modulus gives \(|1/h(0)|\le\max_{|z|=1}|1/h(z)|\le1/c\), so \(|h(0)|\ge c\). If zeros are permitted, \(h(z)=z\) has boundary modulus 1 and value zero at the center.

**Exercise 3 (intermediate: the complex extension radius).** For \(f(x)=1/(1-x)\) near \(x=0\), construct its complex extension by its real series, find \(f^{(j)}(0)\), and explain why the extension argument is local.

**Solution 3.** The real geometric series has every coefficient equal to 1 and is absolutely convergent for \(|x|<1\). The same series defines \(1/(1-z)\) on \(|z|<1\), with uniformly convergent differentiated series on every smaller disk. Therefore \(f^{(j)}(0)=j!\). Its pole at \(z=1\) prevents a holomorphic extension through that point, so local real analyticity does not imply an entire extension.

## References

- Avi Zeff, Complex Analysis lecture on Pompeiu’s formula, March 2026, Section 2. [Lecture](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_12.html).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983. Used for the equation-theoretic context.
