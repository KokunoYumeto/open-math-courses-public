# A matrix estimate with a semipositive imaginary part

This is the matrix argument (5.8) and the argument in Exercise 8 from the AN-04 lesson *Positive Lagrangian ideals and distributions*. All vectors in the estimate are real; transposes in the complex quadratic form are bilinear transposes.

The real symmetric diagonalization used for the nonnegative matrix is proved in [Point sources and complex Gaussian kernels](../../src/point-sources-and-complex-gaussian-kernels.md), Section 2. The [finite algebra foundation](stable-prerequisite-bridges.md), §10, and [scalar foundation](metric-foundation-bridges.md), §§12–13, provide matrix rules and compactness of the unit sphere.

Programme exposition by the AN-04 course contributors. CC0 1.0 Universal for the original expression.

## The matrix estimate

For a complex symmetric invertible matrix \(A=B+iC\), with \(C\ge0\), and a real \(Y\),
\[
 -\operatorname{Im}\bigl((u-iY)^tA(u-iY)\bigr)
    =Y^tCY-u^tCu+2u^tBY.
 \tag{5.8}
\]
Choose \(u=\varepsilon BY\), with \(\varepsilon>0\) small. The right side is at least \(Y^tCY+\varepsilon|BY|^2\ge c|Y|^2\). The last inequality holds because a zero vector for both quadratic terms satisfies \(CY=BY=0\), contradicting invertibility unless \(Y=0\).

**Quantitative bound.** If the sum is zero, nonnegative symmetry gives \(C^{1/2}Y=0\), so \(CY=0\), while \(BY=0\) directly. Thus \((B+iC)Y=0\), forcing \(Y=0\). Compactness of the real unit sphere gives a positive lower bound for this sum. With \(u=\varepsilon BY\), (5.8) equals \(Y^tCY+2\varepsilon|BY|^2-\varepsilon^2(BY)^tC(BY)\). Choosing \(\varepsilon\|C\|\le1\) bounds it below by \(Y^tCY+\varepsilon|BY|^2\), which has a positive lower bound on that sphere. The same bound survives sufficiently small matrix perturbations.
