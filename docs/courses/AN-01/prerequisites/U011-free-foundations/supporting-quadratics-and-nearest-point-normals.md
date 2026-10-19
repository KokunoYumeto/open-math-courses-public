# Supporting quadratics and nearest-point normals

*Programme proof text: AN-03 course-writing task, OpenAI Codex. CC0 1.0. Selection and prerequisite connections: GPT-6 Astra (OpenAI), Ultra.*

These are the complete quadratic-contact argument (S6–S7) and the nearest-point normal construction from Sections 1 and 7 of *Curved weights and the directions in which support can end*. The original notation and equation labels are retained. The associated differential-equation theorem is not needed here.

For a relatively closed set \(F\) in an open \(X\), an exterior normal \((x_0,N)\) means \(N\ne0\) and a real \(C^2\) function \(f\), defined near \(x_0\), with \(df(x_0)=N\) and \(f(x)\le f(x_0)\) on the nearby part of \(F\). The notation \(N_e(F)\) below denotes all such pairs.

The used foundation proofs are supplied in the [metric foundation](metric-foundation-bridges.md), Sections 12–13, for compactness, minima, the fundamental theorem and the chain rule. [When a kernel is smooth](../../src/when-a-kernel-is-smooth.md), Section “Taylor estimates on compact neighborhoods,” proves the full integral Taylor remainder for finite differentiability. For a twice continuously differentiable function and its quadratic Taylor polynomial at zero, subtracting the constant Hessian term from that proved formula gives

\[
 f(h)-f_2(h)=\int_0^1(1-s)\bigl(D^2f(sh)-D^2f(0)\bigr)[h,h]\,ds
                 =o(|h|^2).
\]

Indeed the absolute value divided by \(|h|^2\) is at most half the maximum Hessian difference on the segment, tending to zero by continuity. This supplies the precise remainder in (S6). The full inverse and coordinate-completion proofs are [Regular level sets and transverse convolution](../../src/regular-level-sets-and-transverse-convolution.md), Lemmas 0.1–0.2. The [analytic pullback lesson](../../src/analytic-pullback-and-cotangent-directions.md), Lemma 3, additionally proves that the polynomial coordinate completion in the first argument has a real analytic local inverse. These exact earlier proofs supply the calculus used in the selection.

## Quadratic contact with the same differential

Here is the local form of a support normal. Translate \(x_0\) to zero. If \(f\) witnesses \(N_e(F)\), let \(f_2\) be its quadratic Taylor polynomial there and choose any \(\kappa>0\). On a sufficiently small neighborhood,
\[
 g(x)=f_2(x)-f(0)-\kappa|x|^2<0\quad(x\in F\setminus\{0\}),\qquad
 dg(0)=N.                                                        \tag{S6}
\]
Indeed \(f-f_2=o(|x|^2)\), so \(g\leq f-f(0)-\kappa|x|^2/2\) after shrinking. Complete \(g\) to smooth coordinates with last coordinate \(y_n=g(x)\). The inverse-function theorem applies because \(N\ne0\). In these coordinates
\[
 F\cap\{y_n\geq0\}\subset\{0\}.                                   \tag{S7}
\]
The transformation is smooth even though the original witness was only \(C^2\); using the polynomial in (S6) avoids imposing \(C^m\) regularity on that witness.

## Nearest-point normals

For completeness, a nonempty proper relatively closed set \(F\) in a connected open \(X\) has an exterior normal at some boundary point. Choose \(x_0\in\partial_XF\), a closed ball \(\overline B(x_0,r)\subset X\), and points \(y\notin F\) arbitrarily close to \(x_0\). For \(|y-x_0|<r/4\), choose a point \(z\) of \(F\cap\overline B(x_0,r)\) minimizing distance to \(y\); it exists by compactness. Since \(x_0\in F\), the distance is at most \(|y-x_0|<r/4\), and the minimizing point lies in \(B(x_0,r/2)\). In a neighborhood of \(z\), the function
\[
                         f(x)=-|x-y|^2
\]
has a maximum on \(F\) at \(z\), and \(df(z)=2(y-z)\ne0\). Thus \(N_e(F)\ne\varnothing\).
