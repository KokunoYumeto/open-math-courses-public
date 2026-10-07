# Fourier indicators and the convex hull of a measure's support

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Original proof exposition, examples, solutions and diagrams: CC0 1.0.

Fourier transforms of complex measures can cancel. A zero at frequency zero says that the total complex mass cancels; it need not mean the measure is zero. Even a whole imaginary ray may vanish. When we take the largest modulus over each real-frequency slice, however, the exponential growth in imaginary directions recovers the convex hull of the measure's support exactly.

The [complete proof MI1–MI9](compact-measure-indicators-formal.md) includes the support and measure-determination arguments. Its exact earlier inputs are [the compact-convex growth converse and uniqueness, L122 CF2.1](../../AN02-L122.html#2-the-compact-support-growth-criterion), [the scalar logarithm circle proof, L137 Z2](../../AN02-L137.html#proof-Z2), and [the finite PSH indicator and growth refinement, L139](../../AN02-L139.html#recession-support-function).

## 1. Which support and which Fourier sign?

Let \(u\) be a compactly supported complex Radon measure on \(\mathbb R^n\), \(n\ge1\). Its total variation \(|u|\) is positive, and its support consists of points whose every neighborhood has positive variation. A neighborhood can have total complex integral zero through cancellation while still containing support points.

For \(u\ne0\), write \(S=\operatorname{supp}u\), \(K=\operatorname{conv}S\), and \(m=|u|(\mathbb R^n)>0\). The hull \(K\) is compact, including when it is a point or a line segment. Its support function is

\[
 h_K(y)=\max_{s\in K}s\cdot y=\max_{s\in S}s\cdot y.
 \tag{L142.1}
\]

Use the negative-exponential Fourier convention:

\[
 F(z)=\int e^{-is\cdot z}\,du(s),\qquad z=x+iy.
 \tag{L142.2}
\]

The modulus of the integrand is \(e^{s\cdot y}\). A positive imaginary direction therefore detects the largest support pairing in that direction. Reversing the Fourier sign would reverse these directions as well.

Compact support makes the transform entire: the exponential's parameter power series converges uniformly and absolutely on the support for parameters in compact sets, so it can be integrated term by term. [MI3](compact-measure-indicators-formal.md#MI3) writes the series and proves joint analyticity.

## 2. The direct growth bound

The triangle inequality for a complex measure uses its total variation:

\[
 |F(x+iy)|\le\int e^{s\cdot y}\,d|u|(s)
               \le m e^{h_K(y)}.
 \tag{L142.3}
\]

Thus, with \(\log0=-\infty\),

\[
 v(x+iy)=\log|F(x+iy)|\le\log m+h_K(y)
                                      \le\log m+R|y|,
 \tag{L142.4}
\]

where \(R=\max_{s\in S}|s|\). The constant is \(\log m\), even when the total complex mass \(u(\mathbb R^n)\) is zero.

The transform is not identically zero. Otherwise Fourier uniqueness would make the measure's associated distribution zero, and the measure-determination argument in [MI2](compact-measure-indicators-formal.md#MI2) would make the measure zero.

The logarithm is PSH. On each complex line, the restricted transform is an entire function of one variable. If it vanishes identically, its logarithm is identically \(-\infty\). Otherwise [L137's complete logarithm proof](../../AN02-L137.html#proof-Z2) gives its subharmonic circle inequality, including its zero values. Continuity of \(F\) gives upper semicontinuity of the logarithm on the whole space. These are exactly the PSH conditions needed by L139.

## 3. The horizontal envelope gives an indicator

Define

\[
 M(y)=\sup_{x\in\mathbb R^n}\log|F(x+iy)|,
 \qquad H(y)=\lim_{t\to\infty}\frac{M(ty)}t.
 \tag{L142.5}
\]

[L139](../../AN02-L139.html#psh-envelope-theorem) proves that the upper growth bound makes \(M\) finite and convex and \(H\) finite, continuous and sublinear. It constructs a nonempty compact convex set \(K_H\) whose support function is \(H\). Its precise additional estimate is

\[
 M(y)\le M(0)+H(y).
 \tag{L142.6}
\]

The direct bound (L142.4), evaluated at \(ty\), gives \(M(ty)/t\le\log m/t+h_K(y)\). Taking the limit proves \(H\le h_K\).

This definition includes a supremum over every real frequency. For example, the planar measure \(\delta_{(-1,0)}-\delta_{(1,0)}\) has transform \(2i\sin z_1\). On the ray \((0,it)\) it vanishes at every height. But varying the first real frequency gives \(M(t(0,1))=\log2\), hence \(H(0,1)=0\), consistent with its horizontal support segment. A fixed imaginary ray alone would miss this indicator.

## 4. Why the reverse inequality holds despite cancellation

Estimate (L142.6) yields

\[
 |F(x+iy)|\le e^{M(0)}e^{H(y)}
             =e^{M(0)}e^{h_{K_H}(y)}.
 \tag{L142.7}
\]

This is precisely the compact-convex Fourier growth hypothesis from [CF2.1](../../AN02-L122.html#2-the-compact-support-growth-criterion), with polynomial order zero. Its converse constructs a distribution supported in \(K_H\), with entire Fourier transform \(F\). Its uniqueness identifies that distribution with the one given by the original measure.

The support of a Radon measure is the same as the support of its distribution. To see the nontrivial direction, vanishing on all smooth compact tests implies vanishing on all continuous compact tests by uniform smoothing. Continuous functions between zero and one then approximate the indicator of each compact subset. Total variation and dominated convergence give zero measure on those compact subsets. Inner regularity of total variation extends this to every Borel subset. [MI2](compact-measure-indicators-formal.md#MI2) gives the explicit approximants and estimates.

We obtain \(S\subset K_H\), and hence \(K\subset K_H\). Maximizing linear pairings gives \(h_K\le h_{K_H}=H\). Combining this with the earlier inequality proves

\[
 H(y)=h_K(y)\quad\hbox{for every }y,
 \qquad K_H=K.
 \tag{L142.8}
\]

Equality of the sets follows from the elementary separating plane of a nearest point in a compact convex set. [MI5](compact-measure-indicators-formal.md#MI5) proves the whole reverse inequality and this separation argument. Complex coefficients and nonatomic measures are both included.

## 5. A triangle whose coefficients cancel

Consider the planar measure

\[
 u=\delta_{(-1,0)}+i\delta_{(1,0)}-(1+i)\delta_{(0,2)}.
 \tag{L142.9}
\]

Its coefficients sum to zero. Its variation is \(2+\sqrt2\), and its support hull is the triangle joining the three vertices. Its transform is

\[
 F(z)=e^{iz_1}+i e^{-iz_1}-(1+i)e^{-2iz_2}.
 \tag{L142.10}
\]

It vanishes at \(z=0\). Nevertheless the real part \((\pi/4,-\pi/2)\) aligns all three complex phases. At imaginary height \(y\), the triangle bound is therefore attained and

\[
 M(y)=\log(e^{-y_1}+e^{y_1}+\sqrt2e^{2y_2}),
 \qquad H(y)=\max(-y_1,y_1,2y_2).
 \tag{L142.11}
\]

The envelope at height zero is \(\log(2+\sqrt2)\), although the logarithm at frequency zero is \(-\infty\). The displayed maximum is exactly the triangle's support function. This explicit alignment is a calculation for the example; the general theorem uses the support converse and uniqueness.

![A complex triangle measure and its exact Fourier envelope.](figures/complex-triangle-envelope.png)

*Figure 1.* The left panel gives the actual atom locations and coefficients in (L142.9), with an equal Euclidean scale on both axes. The supporting line \(s_1+s_2=2\) touches the top vertex. The right panel follows \(y=t(1,1)\), drawing the exact envelope and the hull profile. Their gap is at most \(\log(2+\sqrt2)\). The marked height-zero envelope is finite even though the transform cancels at frequency zero. See (L142.9)–(L142.11) and formal Example 2.

## 6. A signed density with no endpoint atoms

On the real line set

\[
 du(s)=\mathbf1_{[-1,0]}(s)\,ds-\mathbf1_{[0,1]}(s)\,ds.
 \tag{L142.12}
\]

Its total mass is zero, its variation is two, and its support is the whole interval \([-1,1]\). Neither endpoint has an atom. Each endpoint is still in the support because every neighborhood meets a positive-length interval of nonzero variation.

Integrating the two exponentials gives

\[
 F(z)=\frac{2(\cos z-1)}{iz},\qquad F(0)=0,
 \tag{L142.13}
\]

where the value at zero is its entire extension. Its series begins \(iz+O(z^3)\). The indicator theorem gives \(H(y)=|y|\). On the positive imaginary ray we can check this slope directly:

\[
 \frac{\log|F(it)|}t
 =1-\frac{\log t}t+\frac{2\log(1-e^{-t})}t\longrightarrow1.
 \tag{L142.14}
\]

The same modulus on the negative ray gives the other endpoint slope. This is a nonatomic example of the full theorem.

![The signed interval density and its exact large-height growth.](figures/signed-density-growth.png)

*Figure 2.* The density is +1 on the left half interval and −1 on the right half interval. The endpoints have zero atomic mass. The right panel uses the exact quotient in (L142.14) on \(1/2\le t\le32\), together with the limiting slope 1 and the upper bound \(1+\log2/t\) from variation two. Cancellation at zero does not remove either endpoint from the support. See formal Example 3 for the transform and moment calculations.

## 7. Location, lower-dimensional supports and zero measure

A nonzero atom \(c\delta_a\) has \(F(z)=ce^{-ia\cdot z}\), \(M(y)=\log|c|+a\cdot y\), and \(H(y)=a\cdot y\). This retains the actual position \(a\); when \(a\ne0\), the indicator in direction \(-a\) is negative. A support function need not be nonnegative.

For a lower-dimensional example, push forward Lebesgue measure on \([-1,1]\) under \(s\mapsto(s,2s)\). Its hull is a segment in the plane, and its indicator is \(|y_1+2y_2|\). The transform is \(2\sin(z_1+2z_2)/(z_1+2z_2)\), with value 2 on the denominator's zero set. The theorem requires no support interior.

For \(u=0\), every transform value is zero and \(v=\log|F|\equiv-\infty\). The support is empty, and the extended convention is \(H=h_\varnothing=-\infty\), including at the zero direction. For a nonzero measure, \(H(0)=0\), even when \(F(0)=0\). These two meanings of a zero value must be distinguished. [MI6](compact-measure-indicators-formal.md#MI6) treats the zero and translation conventions in full.

## 8. Exercises and complete solutions

**Exercise 1.** For \(u=-2i\delta_3\) on the line, find its variation, horizontal envelope and indicator at \(y=-1\).

**Solution.** Its variation is two and its transform is \(-2i e^{-3iz}\). Thus \(M(y)=\log2+3y\) and \(H(y)=3y\). At \(y=-1\) the indicator is \(-3\), the support function of the point 3 in the negative direction. Its negative value records location.

**Exercise 2.** Why is \(\log|u(\mathbb R^n)|\) an unsuitable constant in the growth bound for the triangle measure?

**Solution.** Its total complex mass is zero, so that expression would be \(-\infty\). But the transform is not identically zero and its horizontal supremum at height zero has modulus \(2+\sqrt2\). The triangle inequality integrates against total variation, giving the correct finite constant \(\log(2+\sqrt2)\).

**Exercise 3.** For \(\delta_{(-1,0)}-\delta_{(1,0)}\), compare the log modulus on \((0,it)\) with its envelope at imaginary height \((0,t)\).

**Solution.** The transform is \(2i\sin z_1\), so it is zero on that pure imaginary ray and its logarithm there is \(-\infty\). On the same imaginary slice choose first real frequency \(x_1=\pi/2\), giving modulus two. No real frequency can give larger modulus, so \(M(0,t)=\log2\). Dividing by the dilation gives indicator zero in the vertical direction, as the horizontal support segment requires.

**Exercise 4.** Why does the signed interval measure have support endpoints even though it has no endpoint atoms? What is its first moment?

**Solution.** Every neighborhood of −1 or 1 intersects a positive-length interval on which the absolute density is one, so it has positive variation. A single endpoint has zero Lebesgue mass and hence no atom. Its first moment is \(\int_{-1}^0s\,ds-\int_0^1s\,ds=-1\), giving transform derivative \(F'(0)=i\). Thus zero total mass does not make the transform zero as a function.

**Exercise 5.** Identify the two logical roles of CF2.1 in proving the reverse support-function inequality.

**Solution.** First, the growth-to-support converse constructs an inverse Fourier distribution supported in the compact convex set represented by the PSH indicator. Second, uniqueness identifies that inverse with the distribution of the original measure. The equality of measure and distribution support then puts the original support in that convex set. The construction alone would not identify the original measure's support.

**Exercise 6.** What are \(H(0)\) for a nonzero measure with canceled total mass and for the zero measure? Why do they differ?

**Solution.** For the nonzero measure, its logarithm is a nontrivial PSH function and the finite recession construction gives \(H(0)=0\). A zero at Fourier frequency zero is only one singular value. For the zero measure, the transform is zero at every frequency, its logarithm is identically \(-\infty\), and the support is empty. The empty-set support function is \(-\infty\) even at zero. The finite indicator theorem is applied only to the nonzero case.

## Source credit

Lars Hörmander, *The Analysis of Linear Partial Differential Operators II* (1983 edition; second revised printing 1990; reprint 2005), §16.3, Lemma 16.3.1, printed p. 319 (PDF p. 332). The [complete original proof](compact-measure-indicators-formal.md) identifies the PSH indicator with the compact measure's support function using the exact linked growth converse and support-set construction.
