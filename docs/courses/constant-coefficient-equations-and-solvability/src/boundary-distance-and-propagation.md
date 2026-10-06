# Boundary distance and propagation

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The support criteria in the preceding lessons quantify over compact distributions. In several important classes of equations, that quantifier can be replaced by a geometric test for the distance to the boundary. The sets along which one tests the distance depend on the symbol: characteristic hyperplanes give a necessary condition, elliptic active subspaces give an exact support criterion, and bicharacteristic lines give an exact singular-support criterion for operators of real principal type.

We prove these statements and then explain why the last criterion also gives solutions for every distribution. That final passage uses analytic wavefront propagation. Smooth wavefront propagation alone does not supply it.

Basic references are Kalmes's two papers on surjectivity listed below and Grubb's open chapters on distributions, Fourier transformation, and Sobolev spaces.

Throughout, \(P\ne0\) is a complex polynomial with constant coefficients, \(D=-i\partial\), and \(P^t=P(-D)\). Write \(m=\deg P\) and \(P_m\) for its homogeneous principal part. Lower order coefficients may be complex. All distances and orthogonal complements use the Euclidean inner product.

The support-normal, analytic elliptic and analytic propagation statements specified below are planned prerequisites of [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html). The geometric implications in this lesson use those exact statements.

## Distance tests and continuation inputs

For a proper open set \(X\subset\mathbb R^n\), set
\[
\begin{aligned}
d_X(x)&=\operatorname{dist}(x,\mathbb R^n\setminus X),\\
d_X(A)&=\inf_{x\in A}d_X(x).
\end{aligned}
\tag{1}
\]
The function \(d_X\) is 1-Lipschitz. On the empty set the infimum is \(+\infty\). If \(X=\mathbb R^n\), all these distances are \(+\infty\), and the support and singular-support hull theorems already give both convexity conditions.

Let \(F\) be an affine subspace of positive dimension. We say that \(d_X\) satisfies the **minimum principle on \(F\)** when, for every nonempty compact \(K\subset F\cap X\),
\[
\min_K d_X=\min_{\partial_F K}d_X.
\tag{2}
\]
The boundary is relative to \(F\). A nonempty compact subset of a positive dimensional affine space has nonempty relative boundary. If it has no relative interior, that boundary is the whole set and the test is automatic.

Here are the two distance criteria proved in [Approximation and global solvability from support geometry](approximation-and-global-support-solvability.md), Theorem 4.1, and [Singular supports and arbitrary distribution data](singular-supports-and-distribution-data.md), Theorem 2.1:
\[
\begin{gathered}
X\text{ is }P\text{-convex for supports}\\
\Longleftrightarrow\\
d_X(\operatorname{supp}v)=d_X(\operatorname{supp}P^tv),\\
0\ne v\in\mathcal E'(X);
\end{gathered}
\tag{3}
\]
\[
\begin{gathered}
X\text{ is }P\text{-convex for singular supports}\\
\Longleftrightarrow\\
d_X(\operatorname{singsupp}v)\\
\quad=d_X(\operatorname{singsupp}P^tv),\\
v\in\mathcal E'(X).
\end{gathered}
\tag{4}
\]
For sufficiency in (3), it is enough to establish the distance equality for test functions: the proof there then constructs the required compact support bound. Empty singular supports in (4) cause no problem, by the singular-support hull identity.

We assume the following distribution and wavefront results. They concern the operator \(A\) itself, and will be used with \(A=P^t\). They do not require its lower order coefficients to be real.

- **Halfspace solution.** If the principal part of \(A\) vanishes at a real nonzero normal \(N\), each closed halfspace with that normal is the exact support of a global smooth solution of \(Au=0\). This exact construction is supplied by Theorem1 of [Smooth solutions with an exact characteristic halfspace as support](exact-solutions-on-characteristic-half-spaces.md#exact-characteristic-halfspace-theorem). Reverse its normal as needed, translate the boundary plane and apply it to the transposed polynomial. That lesson’s written scalar-calculus and algebra entries remain explicit.
- **Analytic elliptic regularity.** A homogeneous distributional solution of a constant-coefficient elliptic operator is real analytic. In particular it vanishes throughout a connected open set if it vanishes on a nonempty open subset.
- **Smooth wavefront propagation and realization.** Suppose \(A_m\) is real and \(\nabla A_m(\xi)\ne0\) for every nonzero characteristic \(\xi\). If \((x,\xi)\in\operatorname{WF}(u)\setminus\operatorname{WF}(Au)\), then \(A_m(\xi)=0\), and the wavefront point propagates along any segment in direction \(\nabla A_m(\xi)\) avoiding \(\operatorname{WF}(Au)\) at the same covector. Conversely, for each such \(\xi\) there is a global \(u\in C^m\) for which \(Au\) is smooth and
  \[
  \begin{gathered}
  \operatorname{WF}(u)=\{(t\nabla A_m(\xi),s\xi):\\
  t\in\mathbb R,\ s>0\}.
  \end{gathered}
  \tag{5}
  \]
- **Analytic wavefront propagation.** Under the same principal type hypothesis, the preceding propagation statement holds with \(\operatorname{WF}_A\) in place of \(\operatorname{WF}\).
- **A support normal is an analytic singularity.** If a real analytic function \(h\) attains its maximum on \(\operatorname{supp}u\) at \(x\), with \(dh(x)\ne0\), then \((x,\pm dh(x))\in\operatorname{WF}_A(u)\).

Both wavefront sets are closed conic subsets of the cotangent bundle with the zero covectors removed. Their projections are respectively the smooth and analytic singular supports; the latter lies in the support. Differential operators do not increase either wavefront set. Elliptic regularity at a covector means
\[
\begin{gathered}
\operatorname{WF}(u)\subset
\operatorname{Char}A\cup\operatorname{WF}(Au),\\
\operatorname{WF}_A(u)\subset
\operatorname{Char}A\cup\operatorname{WF}_A(Au).
\end{gathered}
\tag{6}
\]
The arguments below use these prerequisites with their stated hypotheses. In particular, smooth and analytic propagation are separate results.

## What a characteristic hyperplane forces

An affine hyperplane with normal \(N\ne0\) is **characteristic** when \(P_m(N)=0\). A nonzero constant polynomial has no characteristic hyperplanes.

**Theorem 2.1.** If \(X\) is \(P\)-convex for supports, then \(d_X\) satisfies the minimum principle on every characteristic hyperplane.

**Proof.** Assume the principle fails on \(\Pi\). There is a compact \(K\subset\Pi\cap X\) with
\[
\min_K d_X=2a<\min_{\partial_\Pi K}d_X,
\qquad a>0.
\tag{7}
\]
Choose a minimizing point \(y\in K\) and a nearest complement point \(q\), so \(|y-q|=2a\). The strict inequality makes \(y\) an interior point of \(K\) relative to \(\Pi\). For any tangent vector \(w\), both \(y+\varepsilon w\) and \(y-\varepsilon w\) belong to \(K\) for small \(\varepsilon\). Since
\[
2a\le d_X(y\pm\varepsilon w)
\le |y\pm\varepsilon w-q|,
\]
expanding the squared norms and using both signs gives \((y-q)\cdot w=0\). Thus the nearest boundary vector is normal to \(\Pi\).

Set \(t=(y-q)/2\), \(\nu=t/a\), \(\Pi'=\Pi-t\), and \(K'=K-t\). Use coordinates \(x=z+s\nu\), with \(z\in\Pi'\). Let \(H=\{s\ge0\}\), the closed halfspace bounded by \(\Pi'\) toward \(K\). The halfspace input gives a smooth \(u\) with \(P^tu=0\) and \(\operatorname{supp}u=H\).

For \(k\in K\) and \(0\le s\le a\), the Lipschitz estimate gives
\[
\begin{aligned}
d_X(k-t+s\nu)&\ge 2a-|t-s\nu|\\
&=a+s.
\end{aligned}
\tag{8}
\]
On \(\partial_{\Pi'}K'\) there is the better bound \(d_X\ge a+\gamma\), where
\(\gamma=\min_{\partial_\Pi K}d_X-2a>0\).

Here is a cutoff with all its image support strictly farther than \(a\) from the complement. Choose
\[
0<h<\min(a/4,\gamma/4),\qquad 0<\varepsilon<h/4.
\]
Let \(b\) be a smooth cutoff in \(s\), equal to one near zero, supported in \((-h,h)\), whose derivatives on \(s\ge0\) are supported where \(h/2\le s\le h\). Choose a tangential cutoff \(c\) equal to one near \(K'\), supported in its \(\varepsilon\)-neighborhood in \(\Pi'\). Its derivatives can be supported outside \(K'\), within \(\varepsilon\) of its relative boundary. Put \(\chi(z+s\nu)=c(z)b(s)\).

The entire support of \(\chi\) lies in \(X\), since its distance from \(K'\) is less than \(h+\varepsilon<a\). On \(H\), any derivative of \(\chi\) is of one of two kinds. A tangential derivative is within \(\varepsilon+h\) of \(\partial_{\Pi'}K'\), so its distance exceeds \(a\). A normal derivative has \(s\ge h/2\) and \(z\) within \(\varepsilon\) of \(K'\); (8) gives distance at least \(a+h/2-\varepsilon>a\). Derivatives on the negative side do not meet \(\operatorname{supp}u\).

For \(v=\chi u\in C_c^\infty(X)\), locality of the commutator gives
\[
\begin{gathered}
\operatorname{supp}P^tv
\subset H\cap\operatorname{supp}d\chi,\\
d_X(\operatorname{supp}P^tv)>a.
\end{gathered}
\tag{9}
\]
The point \(y-t=q+t\) belongs to \(\operatorname{supp}v\): it lies on the boundary of \(H\), where \(\chi=1\) nearby and \(H\) is the exact support of \(u\). Its distance is exactly \(a\), by (8) and its distance \(a\) from \(q\). Thus (9) contradicts (3). \(\square\)

The use of an exact halfspace support matters: vanishing on one side of a characteristic plane alone would not ensure that the selected point belongs to the support.

## Ellipticity and the active subspace

**Theorem 3.1.** Every open set is \(P\)-convex for supports if and only if \(P\) is elliptic.

**Proof.** Suppose first that \(P\) is elliptic. Extend \(v\in\mathcal E'(X)\) by zero to \(\mathbb R^n\), and let \(r=d_X(\operatorname{supp}P^tv)>0\). For any \(q\notin X\), the ball \(B(q,r)\) avoids that image support. On this ball, \(v\) is analytic by elliptic regularity. It is zero near \(q\), because its support is compactly contained in \(X\). The analytic identity theorem gives \(v=0\) throughout the ball. Taking all such \(q\) proves \(d_X(\operatorname{supp}v)\ge r\); the reverse inequality is locality. Apply (3). The case \(X=\mathbb R^n\) was already covered, and a constant nonzero \(P\) simply preserves supports.

If \(P\) is nonelliptic, choose a real characteristic normal \(N\) of unit length. Take \(X=\mathbb R^n\setminus\{0\}\), so \(d_X(x)=|x|\), and take the characteristic plane \(\Pi=\{x:x\cdot N=1\}\). On a positive radius closed ball in \(\Pi\) centered at \(N\), the minimum is 1, while every relative boundary point has norm greater than 1. Theorem 2.1 excludes support convexity. Such a nonelliptic scalar polynomial cannot occur in dimension one, where its nonzero leading monomial has no nonzero real zero. \(\square\)

An operator **acts along** a linear subspace \(V\) when its polynomial depends only on the orthogonal projection of \(\xi\) onto \(V\). It is elliptic along \(V\) if that polynomial, regarded on \(V\), is elliptic. For a positive order operator elliptic along \(V\), the subspace \(V\ne0\) is its active subspace: a missing direction inside \(V\) would give a zero of its principal part.

**Theorem 3.2.** Let \(P\) have positive order, act along \(V\), and be elliptic there. Then \(X\) is \(P\)-convex for supports if and only if \(d_X\) satisfies the minimum principle on every affine translate of \(V\).

For an order zero operator, every open set is support convex; no positive dimensional choice of \(V\) is imposed. This separates the constant case from the geometric statement.

**Proof of necessity.** First construct a homogeneous distribution with exact support \(V\). The restricted nonconstant complex polynomial \(P(-z)\), \(z\in V_\mathbb C\), has a zero \(z_0\). Indeed choose a real direction where its leading part is nonzero and apply the fundamental theorem of algebra to that one-variable restriction. In coordinates \(x=x_V+x_\perp\), set
\[
u=e^{i x_V\cdot z_0}\otimes\delta_0(x_\perp).
\tag{10}
\]
Because the exponential never vanishes and \(P\) differentiates only along \(V\), this has \(P^tu=0\) and exact support \(V\). Translate it to any affine \(F\) parallel to \(V\).

If the minimum principle failed on \(F\), choose compact \(K\subset F\cap X\) with \(\min_Kd_X<\min_{\partial_F K}d_X\). A tangential cutoff \(c\), equal to one near \(K\) and supported in a sufficiently small relative neighborhood, has every derivative supported close to \(\partial_F K\), where the distance remains strictly larger than \(\min_Kd_X\). Extend it to a compact smooth \(\chi\) in a thin normal tube inside \(X\), taking the normal factor equal to one near \(F\). Since \(P\) has no normal derivatives, \(P^t(\chi u)\) is supported on \(F\) at those tangential cutoff derivatives. Meanwhile \(\operatorname{supp}(\chi u)\) contains \(K\). This violates (3).

**Proof of sufficiency.** Take \(v\in C_c^\infty(X)\) and put \(r=d_X(\operatorname{supp}P^tv)\). Fix \(y_0\in\operatorname{supp}v\), and let
\[
F=y_0+V,\qquad K=F\cap\operatorname{supp}v.
\tag{11}
\]
We claim that every relative boundary point \(y\) of \(K\) satisfies \(d_X(y)\ge r\).

Otherwise, since the image support has distance at least \(r\), there is a ball \(B(y,R)\) on which \(P^tv=0\). A relative boundary point admits a \(z\in F\setminus\operatorname{supp}v\) with \(|z-y|<R/4\). On a small full neighborhood of \(z\), the function \(v\) vanishes. For each sufficiently small normal displacement \(w\in V^\perp\), the slice
\[
\{y+w+a:a\in V,\ |a|<R/2\}
\]
lies in \(B(y,R)\). On that connected slice \(v\) is an analytic homogeneous solution of the elliptic operator on \(V\), and is zero on a neighborhood of \(z+w\). It is therefore zero on the whole slice. Uniformly small \(w\) give an open tube around \(y\) on which \(v=0\), contradicting \(y\in\operatorname{supp}v\). This proves the claim even if the restriction of \(v\) to the original slice happened to be identically zero.

Apply (2) to \(K\). Its relative boundary has distance at least \(r\), so the whole of \(K\), including \(y_0\), has that distance. Since \(y_0\) was arbitrary, (3) holds for every test function. Its test-function form proves support convexity. \(\square\)

This includes real directional differentiation \(P(\xi)=t\cdot\xi+c\) acting along \(\mathbb Rt\), and the Laplacian in a selected collection of variables. It does not replace the active-subspace test by a characteristic-hyperplane test in higher dimension.

## Real principal type and singular support

A positive order polynomial is **of real principal type** if its principal part is real and
\[
\begin{gathered}
\nabla P_m(\xi)\ne0\\
\text{whenever }\xi\ne0\text{ and }P_m(\xi)=0.
\end{gathered}
\tag{12}
\]
Equivalently, its gradient is nonzero at every nonzero real \(\xi\): Euler's identity \(\xi\cdot\nabla P_m=mP_m\) already gives that fact where \(P_m\ne0\). For a nonzero characteristic covector \(\xi\), the affine lines in direction \(\nabla P_m(\xi)\) are its **bicharacteristic lines**. Transposition changes this gradient by \((-1)^m\), leaving the lines unchanged.

**Theorem 4.1.** If \(P\) is of real principal type, then \(X\) is \(P\)-convex for singular supports if and only if \(d_X\) satisfies the minimum principle on every bicharacteristic line.

**Proof of necessity.** Suppose the minimum principle fails on a line \(L\). Choose a minimizing point in a compact witness. It is an interior point relative to the line. The closure \(I=[a,b]\) of the component of that relative interior containing it is a compact interval in \(X\), with endpoints in the relative boundary of the witness. Thus
\[
\min_I d_X<\min(d_X(a),d_X(b)).
\tag{13}
\]
The realization input (5), translated to \(L\) and applied to \(P^t\), gives a \(C^m\) distribution \(u\) with \(\operatorname{singsupp}u=L\) and \(P^tu\) smooth. Choose \(\chi\in C_c^\infty(X)\) equal to one near \(I\), so that \(L\cap\operatorname{supp}d\chi\) lies in small neighborhoods of the endpoints where the distance is greater than \(\min_I d_X\). Such a cutoff is the product of an interval cutoff and a thin normal cutoff whose derivatives miss \(L\). For \(v=\chi u\),
\[
\begin{gathered}
I\subset\operatorname{singsupp}v,\\
\operatorname{singsupp}P^tv
\subset L\cap\operatorname{supp}d\chi.
\end{gathered}
\tag{14}
\]
Here \(P^t(\chi u)=\chi P^tu+[P^t,\chi]u\), and its first term is smooth. Inequality (13) contradicts (4).

**Proof of sufficiency.** Let \(v\in\mathcal E'(X)\), and write \(S=\operatorname{singsupp}P^tv\). If \(S\) is empty, the compact singular-support hull theorem makes \(v\) smooth. Otherwise put \(r=d_X(S)>0\). Points of \(\operatorname{singsupp}v\) already in \(S\) have distance at least \(r\). At any other such point \(y_0\), choose a nonzero \(\xi\) with \((y_0,\xi)\in\operatorname{WF}(v)\). By (6), \(P_m(\xi)=0\). On the corresponding line set
\[
\begin{gathered}
L=y_0+\mathbb R\nabla P_m(\xi),\\
K_\xi=\{y\in L:(y,\xi)\in\operatorname{WF}(v)\}.
\end{gathered}
\tag{15}
\]
This is a nonempty compact subset of \(X\): closedness follows with the covector fixed, and its projection lies in the compact singular support of \(v\).

Every relative boundary point of \(K_\xi\) belongs to \(S\). Indeed if \(y\in\partial_LK_\xi\) were outside \(S\), a small segment around \(y\) would avoid \(\operatorname{WF}(P^tv)\) at \(\xi\). Since \(K_\xi\) is closed, it contains \(y\); smooth propagation then makes the entire small segment belong to \(K_\xi\), contradicting the boundary property. Consequently the minimum principle gives
\[
\min_{K_\xi}d_X
=\min_{\partial_LK_\xi}d_X\ge r.
\tag{16}
\]
In particular \(d_X(y_0)\ge r\). All singular points have that bound; locality supplies the opposite inequality between the two distances. Apply (4). \(\square\)

If the characteristic set is empty, the line condition is vacuous. The sufficiency proof still works: (6) would preclude a singular point outside \(S\). Thus the theorem includes elliptic operators with real principal part.

## Why the line test also controls support

**Theorem 5.1.** For a real principal type \(P\), the following are equivalent:

1. \(P(D):\mathcal D'(X)\to\mathcal D'(X)\) is onto.
2. \(X\) is \(P\)-convex for singular supports.
3. \(d_X\) satisfies the minimum principle on every bicharacteristic line.

In this class each condition also implies support convexity. No continuous linear choice of solutions is asserted.

**Proof.** Surjectivity implies both convexity conditions by Theorem 6.1 of the singular-support lesson, and Theorem 4.1 gives the equivalence of the last two items. It remains to show that the line condition implies support convexity.

Take \(0\ne v\in\mathcal E'(X)\). If (3) failed, locality would give
\[
\begin{gathered}
a=d_X(\operatorname{supp}v),\\
a<b=d_X(\operatorname{supp}P^tv),\\
y_0\in\operatorname{supp}v,\quad q\notin X,\\
|y_0-q|=a.
\end{gathered}
\tag{17}
\]
Here \(a>0\), and both minima are finite for a proper \(X\). Put \(\xi_0=y_0-q\ne0\). The real analytic function \(h(x)=-|x-q|^2\) attains its maximum on \(\operatorname{supp}v\) at \(y_0\). The support-normal input gives
\((y_0,\xi_0)\in\operatorname{WF}_A(v)\).

The strict inequality in (17) puts \(y_0\) outside the image support. Thus \(P^tv=0\) near \(y_0\), and analytic elliptic regularity at a covector in (6) gives \(P_m(\xi_0)=0\). Define
\[
\begin{gathered}
L=y_0+\mathbb R\nabla P_m(\xi_0),\\
K_A=\{y\in L:(y,\xi_0)\in\operatorname{WF}_A(v)\}.
\end{gathered}
\tag{18}
\]
This is compact, lies in \(\operatorname{supp}v\subset X\), and contains \(y_0\). Any relative boundary point outside \(\operatorname{supp}P^tv\) has an interval around it where the image is identically zero, hence analytically regular. Analytic propagation makes that interval belong to \(K_A\), a contradiction. Therefore
\[
\partial_LK_A\subset\operatorname{supp}P^tv.
\tag{19}
\]
The line minimum principle gives \(d_X(y_0)\ge\min_{K_A}d_X\ge b\), contradicting \(d_X(y_0)=a<b\). This proves (3).

We now have both convexity conditions. The all-distribution criterion already proved in the preceding lesson supplies surjectivity, completing the equivalences. \(\square\)

The analytic wavefront set is essential here because its support-normal theorem detects the boundary of the support even for a smooth function. The smooth wavefront set of a smooth compact function is empty, so it cannot carry this argument.

## Worked domains

For \(P(\xi)=\xi_1+c\) on \(\mathbb R^2\), with arbitrary complex \(c\), the active subspace and every bicharacteristic direction are horizontal. On
\[
X=\mathbb R\times(0,1),
\]
the distance is \(d_X(x_1,x_2)=\min(x_2,1-x_2)\), constant on every horizontal line. Theorems 3.2 and 5.1 give both support convexity and solvability for every distribution. Changing \(c\) changes the equation, but not this domain test.

On the punctured plane, the same operator fails the test. On \(L=\mathbb R\times\{1\}\) take \(I=[-2,2]\times\{1\}\). Its distance minimum is 1 at \((0,1)\), whereas the endpoint distances are \(\sqrt5\). Thus the punctured plane is neither support convex nor singular-support convex for this operator, and it does not admit solutions for every distribution datum.

For \(P(\xi)=\xi_1^2+\xi_2^2\) in \(\mathbb R^3\), the active subspace is \(V=\mathbb R^2\times\{0\}\). On \(X=\mathbb R^2\times(0,1)\), the distance is constant on each affine \(V\)-slice, so Theorem 3.2 gives support convexity. Its principal part has gradient zero at nonzero covectors along the third axis, so it is not of real principal type. Theorem 5.1 cannot be invoked to infer singular-support convexity or unrestricted distribution solvability from that argument alone.

## Exercises

**Exercise 1 (introductory: nearest normals).** Let \(F\) be an affine subspace, \(K\subset F\cap X\) compact, and \(y\) a minimizing point of \(d_X\) with \(d_X(y)<\min_{\partial_FK}d_X\). For a nearest \(q\notin X\), prove \(y-q\perp(F-F)\). Explain why the strict inequality is needed.

**Exercise 2 (intermediate: a compact slice can be misleading).** Let \(v\in C_c^\infty(\mathbb R^2)\), and suppose \(D_1v=0\) on a ball. Prove that a relative boundary point of \(\operatorname{supp}v\) on a horizontal line cannot lie in that ball. Your argument must also cover the case where \(v\) restricts to zero on the entire line.

**Exercise 3 (intermediate: a full higher dimensional equation).** For \(P(\xi)=\xi_1+\xi_2+i\) in \(\mathbb R^3\), test the domain
\[
X=\{x:0<x_1-x_2<1\}.
\]
Identify its active subspace, characteristic hyperplanes, and bicharacteristic lines. Determine whether the equation is onto \(\mathcal D'(X)\).

**Exercise 4 (advanced: the failed smooth argument).** Explain why replacing every analytic wavefront set in the proof of Theorem 5.1 by a smooth wavefront set does not prove support convexity. Then show that a nonzero smooth compact function has nonempty analytic wavefront set at a nearest support point to any external point.

**Exercise 5 (advanced: the constant case).** Show that a constant nonzero operator is elliptic along any subspace if ellipticity is read using its order zero principal part. Give a domain and a positive dimensional subspace for which the distance minimum principle fails. Explain the separate order zero clause in Theorem 3.2.

## Complete solutions

**Solution 1.** The strict gap puts \(y\) in the relative interior of \(K\). For any \(w\in F-F\), the points \(y\pm\varepsilon w\) belong to \(K\) for small \(\varepsilon\). Their distances to the complement are at least \(|y-q|\), and no greater than their distances to \(q\). Squaring yields
\[
0\le\pm2\varepsilon(y-q)\cdot w+\varepsilon^2|w|^2.
\]
Divide by \(\varepsilon\) and let it decrease to zero, with each sign. The two inequalities force \((y-q)\cdot w=0\). Without the gap, the minimizer could be on the relative boundary, so both tangent displacements might not stay in \(K\).

**Solution 2.** Let \(y\) be the proposed boundary point and shrink to a ball \(B(y,R)\) where \(D_1v=0\). There is a point \(z\) on the same horizontal line, with \(|z-y|<R/4\), outside the full support of \(v\). Thus \(v=0\) on a small two dimensional neighborhood of \(z\). On every nearby horizontal slice of \(B(y,R/2)\), the derivative in \(x_1\) is zero, so \(v\) is constant, and that constant is zero because the slice meets that neighborhood. These slices fill a neighborhood of \(y\), contradicting \(y\in\operatorname{supp}v\). The argument uses neighboring slices, not merely the value on the original slice.

**Solution 3.** The active subspace is \(V=\mathbb R(1,1,0)\). The principal part is real, with constant nonzero gradient \((1,1,0)\), so the operator is of real principal type. Characteristic normals satisfy \(N_1+N_2=0\); the corresponding characteristic hyperplanes are those with such a nonzero normal. Bicharacteristic lines are parallel to \((1,1,0)\).

The two boundary planes of \(X\) have normal \((1,-1,0)\), of length \(\sqrt2\). Therefore
\[
d_X(x)=\frac{\min(x_1-x_2,1-x_1+x_2)}{\sqrt2}.
\]
It is constant along each bicharacteristic line. The minimum principle holds on every such line, so Theorem 5.1 gives surjectivity on all distributions. The complex lower order term \(i\) does not alter this conclusion.

**Solution 4.** A smooth compact function has empty smooth wavefront set, including at every point of its support boundary. The starting covector in (17) would therefore be unavailable. For the analytic assertion, let \(q\) be external to the compact support and \(y\) a nearest support point. The function \(h(x)=-|x-q|^2\) is real analytic, attains its maximum on the support at \(y\), and has nonzero derivative there. The support-normal input supplies both covectors \(\pm(y-q)\) in the analytic wavefront set. A smooth function can thus be smooth across a boundary while failing to be analytic there.

**Solution 5.** If \(P=c\ne0\), its degree zero principal part is nonzero at every nonzero covector in any subspace, so that interpretation of ellipticity permits every choice of \(V\). Multiplication by \(c\) preserves supports, hence every open set is support convex. On \(X=\mathbb R^2\setminus\{0\}\) and \(V=\mathbb R(1,0)\), however, the interval from \((-2,1)\) to \((2,1)\) has distance minimum 1 and endpoint distances \(\sqrt5\). It violates the minimum principle. A positive order elliptic active subspace has genuine differentiation directions; an arbitrarily assigned subspace for a constant operator does not. The separate clause gives the correct constant case without adding a false geometric restriction.

## References

For an open treatment placing minimum principles in a wider solvability setting, see T. Kalmes, [*Surjectivity of differential operators and linear topological invariants for spaces of zero solutions*](https://arxiv.org/abs/1408.4356), Revista Matemática Complutense 32 (2019), 37–55, particularly its geometric discussion. His [*Some results on surjectivity of augmented differential operators*](https://www.tu-chemnitz.de/mathematik/analysis/kalmes/Preprints/Some_results_on_surjectivity_of_augmented_differential_operators_manuscript.pdf), Journal of Mathematical Analysis and Applications 386 (2012), 125–134, also records the planar geometry and the distinction between support and singular-support conditions.

For the distribution and Fourier background, see G. Grubb, *Distributions and Operators*, open lecture chapters [Distributions](https://web.math.ku.dk/~grubb/dist3.pdf), [Fourier transformation](https://web.math.ku.dk/~grubb/dist5.pdf), and [Sobolev spaces](https://web.math.ku.dk/~grubb/dist6.pdf).
