# Disk comparison and Poisson integrals

The argument P1 below is from the earlier AN-04 lesson *Complex involutive normal forms and regularity propagation*, Section 4. Its superharmonic convention is harmonic comparison from below: on a disk, a harmonic function bounded above by the given function on the boundary remains below it inside. The functions may be lower semicontinuous and take the value positive infinity; the continuous finite case suffices for boundary-smallness estimates.

The [scalar foundation](metric-foundation-bridges.md), §§12–13, supplies compactness, polar calculus, finite derivative rules and geometric-series convergence. The [integration foundation](banach-foundation-bridges.md), §§15–16, supplies integration and monotone convergence.

Programme exposition by the AN-04 course contributors. CC0 1.0 Universal for the original expression.

## Comparison and disk averages

**P1. Comparison on domains and the mean inequality.** Disk comparison implies comparison on any relatively compact bounded planar domain. To prove it, subtract the proposed harmonic minorant and call the result \(u\). If \(u\ge0\) at the boundary but \(u\) is negative somewhere inside, then for sufficiently small \(\varepsilon>0\), \(u(z)-\varepsilon|z|^2\) attains a finite minimum strictly below its boundary minimum at an interior point \(z_0\). On a small circle of radius \(r\) about that point,
\[
 u(z)\ge u(z_0)+2\varepsilon\operatorname{Re}(\bar z_0(z-z_0))+\varepsilon r^2.
 \tag{CI18}
\]
The right side is harmonic in \(z\), so comparison at the center contradicts \(\varepsilon r^2>0\). Lower semicontinuity and compactness justify attainment; the value is finite because there is a negative point. Subtracting a harmonic function preserves disk comparison.

Here is also the connection with the usual circle mean definition. On a circle a lower semicontinuous function \(v\), bounded below by \(-M\), is an increasing limit of continuous minorants: take
\(v_j(t)=\min\{j,\inf_s(v(s)+j\,d(s,t))\}\), with \(j>M\) and arc distance \(d\). Each is Lipschitz, the sequence increases, and its limit is \(v\). The last assertion follows by compactness: an almost-minimizing sequence staying away from \(t\) incurs unbounded distance cost, while a sequence approaching \(t\) is controlled by lower semicontinuity. If all values are infinite the assertion is immediate. For continuous boundary data \(b\), the Poisson integral in a disk of radius \(R\) is harmonic and extends continuously to \(b\). To verify these claims directly, its kernel is
\(1+2\sum_{k\ge1}(r/R)^k\cos(k\vartheta)\), obtained by summing two geometric series, hence harmonic and of mean one for \(r<R\). It is positive, and its mass away from any fixed angular interval tends to zero as \(r\uparrow R\), by the formula \((1-r^2/R^2)/(1-2(r/R)\cos\vartheta+r^2/R^2)\). Uniform continuity of \(b\) now proves the boundary limit. Apply comparison to the Poisson integrals of \(v_j\) and evaluate at the center. Monotone convergence after adding \(M\) proves the circle mean inequality for \(v\). Conversely, that inequality gives harmonic comparison: at a negative interior minimum of \(v-h-\varepsilon|z|^2\), (CI18) makes the circle average strictly greater than the central value, a contradiction. Thus the comparison definition used here is exactly the mean-inequality definition.
