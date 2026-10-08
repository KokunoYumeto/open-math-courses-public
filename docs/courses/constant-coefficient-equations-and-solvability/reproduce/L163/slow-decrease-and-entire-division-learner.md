# Slow decrease and entire Fourier division

Original exposition and proofs: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0. Self-checked by the writing AI; independent mathematical review is not claimed.

The transform of a compact distribution may have zeros. To divide by it, we require the quotient to extend holomorphically across those zeros. The remaining question is whether that entire quotient still comes from a compact distribution. Slow decrease answers this question through lower bounds in logarithmic Fourier neighborhoods.

Basic references are Tao's *246B, Notes 2* and *245B, Notes 9*, and Hörmander's *The Analysis of Linear Partial Differential Operators I* and *II*. The prerequisites are Compact Fourier division and multiplicity-sensitive annihilators, Theorem CF2.1, for the entire compact-support growth criterion; Local compactness and Hartogs bounds, for proper versus collapsed PSH limits; and Frequency-selective singularities and smooth convolutions, Theorem 1.1, for the smoothing obstruction. The [complete proof](slow-decrease-and-entire-division-formal.md) supplies all five equivalences, the Phragmén–Lindelöf and Lindelöf arguments, and the weighted Banach-space proof.

## 1. What slow decrease means

Use \(F_u(\zeta)=\langle u,e^{-ix\cdot\zeta}\rangle\) and
\[
 L_u(z,c)=\frac{\log|F_u(c+z\log|c|)|}{\log|c|},
 \qquad c\in\mathbb R^n,\quad |c|>2.
 \tag{T1}
\]
At transform zeros the logarithm is \(-\infty\). Collapse means uniform convergence to \(-\infty\) on all compact complex parameter sets.

Theorem 1.1 in the complete proof makes these five conditions equivalent:

1. No escaping real sequence produces collapse.
2. One complex logarithmic window has a polynomial lower bound, at every real center.
3. Every prescribed positive real logarithmic radius has a polynomial lower bound, whose exponent may depend on that radius.
4. Every complex parameter ball has an integrated logarithm lower bound.
5. If \(F_w=F_uG\), with \(w\) compact and \(G\) entire, then \(G\) is the transform of a compact distribution.

In exact terms, conditions 2 and 3 say respectively
\[
 \sup_{|\zeta-c|<A\log(2+|c|)}|F_u(\zeta)|>(A+|c|)^{-A}
 \quad\text{for one }A>0,
 \tag{T2}
\]
and, for every \(a>0\), the existence of \(A>0\) with
\[
 \sup_{\substack{h\in\mathbb R^n\\|h|<a\log(2+|c|)}}
       |F_u(c+h)|>(A+|c|)^{-A}.
 \tag{T3}
\]
Condition 2 allows complex displacements; condition 3 requires real displacements and every fixed radius coefficient. Neither condition requires a lower bound at the center itself.

For each \(a>0\), condition 4 is
\[
 \int_{|z|<a}\log|F_u(c+z\log|c|)|\,dV(z)>-A_a\log|c|,
 \qquad |c|>2.
 \tag{T4}
\]
The integral is over complex dimension \(n\), hence real dimension \(2n\), without dividing by the ball volume.

A compact distribution satisfying these conditions is called *invertible*, and its transform is *slowly decreasing*. Here invertibility describes division and convolution regularity. A pointwise reciprocal may have poles, and a compact convolution inverse need not exist.

## 2. How the implications fit together

The absence of collapse bounds the integrals of the normalized PSH family below. Otherwise an escaping sequence of integrals tending to \(-\infty\) would have a proper local \(L^1\) extraction, whose integrals are finite, or a collapsed extraction, which is excluded. Bounded frequency regions are handled by the local integrability of \(\log|F_u|\).

If the real-window bound failed, some sequence would satisfy
\(L_u(x,c_j)\leq-j\) on a fixed real parameter ball. Smallness on that real ball propagates to complex parameters. The proof uses a positive harmonic comparison function on a rectangle in each complex line:
\[
 \omega(t,s)=\sin\!\left(\frac{\pi(t+r)}{2r}\right)
       \frac{\sinh(\pi(r-s)/(2r))}{\sinh(\pi/2)}.
 \tag{T5}
\]
For a common upper bound \(C\), comparison gives
\(g_j(t+is)\leq C-(j+C)\omega(t,s)\).
The positive \(\omega\) forces collapse on the rectangle interior. PSH compactness then extends it along the line and through the complex parameter space. This contradicts (T4).

One real logarithmic lower bound lies inside a sufficiently large complex window. Conversely, uniform collapse on that fixed complex window would violate its polynomial lower bound. This completes the first four conditions.

![A positive harmonic rectangle function propagates real-axis smallness, and a positive three-halves quadrant barrier removes linear growth in the upper half-plane.](figures/real-smallness-and-half-plane-barriers.png)

*Figure 1.* Left: the exact harmonic function (T5) for \(r=1\), on \(-1\leq t\leq1,\ 0\leq s\leq1\). It vanishes on the vertical and upper sides and is positive inside. Right: \(\cos[\frac32(\theta-\pi/4)]\) for \(0\leq\theta\leq\pi/2\), with its positive lower bound \(\cos(3\pi/8)\). Multiplication by \(r^{3/2}\) gives the first-quadrant harmonic barrier, which dominates linear growth on outer arcs. Proof locators: complete proof, Lemmas 2.1 and 3.1. Background: Hörmander and the Phragmén–Lindelöf principle.

For division, Lindelöf's argument first bounds an entire quotient by exponential type. It controls the negative part of the denominator's logarithm by its average, instead of dividing pointwise through zeros. The integrated logarithm lower bound then gives polynomial growth of the quotient on real frequencies.

The remaining step preserves that polynomial order in complex directions. For real \(\xi,\eta\), let \(a=1+|\xi|\), \(b=|\eta|\), and use the harmonic logarithm of \(a-ibz\), whose zero is below the real axis. The half-plane lemma applied on the line \(\xi+z\eta\) gives
\[
 |G(\xi+i\eta)|\leq 2^NC_1
       (1+|\xi+i\eta|)^Ne^{A|\eta|}
 \tag{T6}
\]
from an exponential-type bound \(C_0e^{A|z|}\) and a real bound \(C_1(1+|\xi|)^N\). The earlier compact-support growth theorem recovers a distribution supported in the radius-\(A\) ball.

The converse division implication requires a uniform exponent. The proof forms a complete normed space of entire \(G\) whose products \(F_uG\) have one fixed compact-support growth bound. Baire's theorem supplies
\[
 |G(\xi)|\leq C\|G\|(1+|\xi|)^m
 \tag{T7}
\]
with one \(m\) for that whole space. If \(u\) had a collapsed profile, the preceding smoothing construction would give a compact continuous \(v\notin C^1\) with \(u*v\) smooth. Every derivative transform \((i\zeta)^\alpha F_v\) belongs to the same quotient space. Applying (T7) with the same \(m\) to arbitrarily high derivatives forces \(F_v\) to be rapidly decreasing, hence \(v\) smooth. The contradiction proves the fifth condition implies the first.

## 3. Four worked examples

### Example 1: a double zero and an entire compact quotient

Take \(u=D^2\delta_2\) and \(w=D^2\delta_5\) on \(\mathbb R\), with \(D\) the ordinary distribution derivative. Their transforms are
\[
 F_u(\zeta)=(i\zeta)^2e^{-2i\zeta},\qquad
 F_w(\zeta)=(i\zeta)^2e^{-5i\zeta},\qquad
 G(\zeta)=e^{-3i\zeta}.
 \tag{T8}
\]
The double denominator zero at zero is removable because the numerator has the same multiplicity. The quotient is the transform of \(\delta_3\), and \(u*\delta_3=w\).

The divisor is slowly decreasing: the existing polynomial division theorem preserves compact Fourier growth for division by the nonzero polynomial \((i\zeta)^2\), and division by the point-mass exponential merely translates the compact inverse. Thus condition 5 holds for every compact numerator whose quotient is entire, not just this example.
There is no compact convolution inverse for \(u\). If \(u*v=\delta_0\), the transform equality at \(\zeta=0\) would say \(0=1\). This exhibits the precise difference between the course's invertibility term and a compact convolution inverse.

### Example 2: infinitely many real zeros do not prevent slow decrease

For \(u=\delta_0-\delta_1\),
\[
 F_u(\zeta)=1-e^{-i\zeta},\qquad
 |F_u(\xi)|=2|\sin(\xi/2)|\quad(\xi\in\mathbb R).
 \tag{T9}
\]
The real zeros are \(2\pi k\). Nevertheless every real interval of radius greater than \(\pi\) contains an odd multiple of \(\pi\), where the modulus is two. For every fixed \(a>0\), the radius \(a\log(2+|c|)\) eventually exceeds \(\pi\). The real-window supremum is then two, and the bounded set of remaining centers has a positive minimum window supremum. It therefore has a positive polynomial lower bound at all centers, giving condition 3.

For \(w=\delta_0-\delta_3\), the identity
\[
 \frac{1-e^{-3i\zeta}}{1-e^{-i\zeta}}
      =1+e^{-i\zeta}+e^{-2i\zeta}
 \tag{T10}
\]
extends through every denominator zero. The compact quotient is
\(\delta_0+\delta_1+\delta_2\). Multiplying the finite sums cancels the two interior point masses and gives the stated numerator.

![A real zero at a large center lies inside logarithmic windows with positive transform suprema; an atomic quotient gives the exact compact convolution identity.](figures/zeros-in-logarithmic-windows-and-division.png)

*Figure 2.* Left: the exact function \(2|\sin(t/2)|\), with frequency \(\xi=c+t\) and \(c=2\pi\cdot10^6\). Windows have radii \(a\log(2+c)\), for \(a=0.1\) and \(0.25\). The larger contains the peaks at \(t=\pm\pi\), although the center is a zero. Right: the exact atomic identity \((\delta_0-\delta_1)*(\delta_0+\delta_1+\delta_2)=\delta_0-\delta_3\). Markers show point-mass locations and signs, not continuous densities. Proof locators: Examples 1–2 and complete proof, Theorem 1.1. Background: Tao and Hörmander.

### Example 3: smoothness of a divisor does not give the division property

A nonzero compact smooth function has \(L_u\to-\infty\) uniformly on complex parameter compact sets along all escaping real frequencies. Whole-complex integration by parts proves this: any fixed logarithmic imaginary displacement contributes a fixed polynomial growth factor, and arbitrary derivative orders dominate it.
Thus it fails condition 1 and is not invertible. The theorem implies that there exists a compact numerator with an entire quotient which is not a compact-distribution transform. Entire removability alone is insufficient.

The quotient-space proof gives the reason without asserting a closed formula for that numerator. If every product-controlled entire quotient had polynomial real growth, Baire would give one exponent for all of them. The frequency-selective nonsmooth factor and all its derivatives would then force smoothness, a contradiction. The failure is a growth obstruction, not necessarily a pole.

### Example 4: keeping the polynomial order in complex directions

Let
\(G(\zeta)=(1-i\zeta)^3e^{-2i\zeta}\).
On real frequencies,
\(|G(\xi)|=(1+\xi^2)^{3/2}\leq(1+|\xi|)^3\).
There is a constant \(C_0\) with \(|G(\zeta)|\leq C_0e^{3|\zeta|}\): the exponential contributes at most \(e^{2|\zeta|}\), and the cubic factor is bounded by a constant times \(e^{|\zeta|}\).
Lemma 3.2 gives
\[
 |G(\xi+i\eta)|\leq8(1+|\xi+i\eta|)^3e^{3|\eta|}.
 \tag{T11}
\]
The polynomial order remains three. The compact inverse is explicitly
\((1-D)^3\delta_2\), whose actual carrier is \(\{2\}\). The lemma's radius-three ball is a valid general support bound, not the optimal carrier in this example. Its exact modulus is
\(|1-i(\xi+i\eta)|^3e^{2\eta}\), which records the signed point-mass location.

## Exercises with complete solutions

The exercises total 100 points.

### Exercise 1: translation and double multiplicity (8 points)

For \(u=D^2\delta_{-1}\) and \(w=D^2\delta_4\), compute the entire quotient and its compact inverse. Explain why dividing only one copy of the polynomial zero would give the wrong quotient.

*Solution.* The transforms are \((i\zeta)^2e^{i\zeta}\) and \((i\zeta)^2e^{-4i\zeta}\). Their quotient is \(e^{-5i\zeta}\), the transform of \(\delta_5\). The convolution shifts the derivative point mass from \(-1\) to four.
Both transforms vanish to order two at zero, and both copies of the factor must cancel. Dividing the numerator by only \(i\zeta e^{i\zeta}\) would leave \(i\zeta e^{-5i\zeta}\), the transform of \(D\delta_5\). Its convolution with the actual \(u\) is \(D^3\delta_4\), not \(w\). Entire division retains the exact divisor and its full multiplicity.

### Exercise 2: absorbing a polynomial constant (8 points)

Suppose a real logarithmic window of radius \(0.4\log(2+|c|)\) has supremum at least \(10^{-2}(1+|c|)^{-3}\). Show that \(A=8\) works for the complex-window condition.

*Solution.* The real window is inside the complex window with radius \(8\log(2+|c|)\). For \(q=|c|\),
\[
 (8+q)^8\geq8^5(1+q)^3,\qquad
 (8+q)^{-8}\leq\frac1{32768}(1+q)^{-3}
                         <10^{-2}(1+q)^{-3}.
 \tag{T12}
\]
The supremum over the larger window is at least the assumed real-window supremum, so the required strict inequality holds at every center, including zero. The constant and exponent were absorbed together; no asymptotic exception is needed.

### Exercise 3: why failing-window centers escape (10 points)

For a nonzero entire \(F\) and fixed \(a>0\), prove that
\(S_a(c)=\sup_{|h|<a\log(2+|c|)}|F(c+h)|\) is continuous and positive. Deduce that centers satisfying \(S_a(c_j)\leq(j+|c_j|)^{-j}\) escape.

*Solution.* The open-ball supremum equals the closed-ball maximum by continuity of \(F\). Substitute \(h=a\log(2+|c|)t\), with real \(|t|\leq1\). On each compact set of centers this is a continuous function of \((c,t)\) on a compact product, hence uniformly continuous. The absolute difference of its two maxima is at most the supremum of the corresponding pointwise differences, proving continuity in \(c\).
If a maximum were zero, \(F\) would vanish on an open real ball. A real box inside that ball lets the one-variable identity principle extend one coordinate at a time, showing \(F\equiv0\), a contradiction. Thus \(S_a>0\).
It has a positive minimum on each bounded closed set of centers. But the proposed right side is at most \(j^{-j}\to0\). No subsequence of \(c_j\) can stay in such a set, so \(|c_j|\to\infty\).

### Exercise 4: a quantitative real-to-complex comparison (10 points)

For \(r=1\), evaluate the harmonic function (T5) at \((t,s)=(0,1/2)\). If the real bottom values are at most \(-M\) and the other boundary values at most \(C\geq0\), give a sufficient \(M\) for the center value to be at most \(-K\).

*Solution.* The exact value is
\(\omega_0=\sinh(\pi/4)/\sinh(\pi/2)>0\).
Maximum comparison gives \(g(i/2)\leq C-(M+C)\omega_0\). It is at most \(-K\) whenever
\[
 M\geq\frac{K+C}{\omega_0}-C.
 \tag{T13}
\]
The comparison works because the harmonic function vanishes on the vertical and top sides and its bottom values lie in \([0,1]\). Hence \(C-(M+C)\omega\) is at least \(-M\) on the bottom and equals \(C\) on the remaining boundary. Positive interior harmonic weight transfers arbitrarily strong real smallness to the complex interior.

### Exercise 5: both Phragmén–Lindelöf barriers (10 points)

Let \(c_0=\cos(3\pi/8)\). Show that the power barrier dominates linear growth on every outer first-quadrant arc once \(R\geq(2A/(\varepsilon c_0))^2\). After obtaining the bound \(v\leq C^+\), give a radius making the logarithmic barrier's outer boundary nonpositive.

*Solution.* The power barrier is at least \(c_0R^{3/2}\). The stated inequality gives \(\varepsilon c_0R^{3/2}\geq2AR\). Therefore
\(C+AR-\varepsilon c_0R^{3/2}\leq C-AR\leq C^+\).
On the two straight sides the same upper bound already holds. Maximum comparison then bounds \(v-\varepsilon H_1\), and letting \(\varepsilon\downarrow0\) gives \(v\leq C^+\) in the quadrant. Reflection gives it in the other quadrant.
For the second step, on \(|z|=R\), \(\operatorname{Im}z\geq0\), we have \(|z+i|\geq R-1\). Choose
\(R>1+\exp(C^+/\varepsilon)\).
Then \(v-\varepsilon\log|z+i|\leq C^+-\varepsilon\log(R-1)<0\) on the arc. On the real boundary \(\log|x+i|\geq0\) and \(v\leq0\). Maximum comparison and then \(\varepsilon\downarrow0\) give the exact upper bound zero. The first barrier removes linear growth; the second removes the constant.

### Exercise 6: a harmonic denominator in two dimensions (8 points)

Take \(\xi=(3,4)\), \(\eta=(-1,2)\). Determine \(a,b\), the zero of \(p(z)=a-ibz\), and the denominator at \(z=i\). Explain why the logarithm is harmonic on the upper half-plane.

*Solution.* We have \(a=1+|\xi|=6\), \(b=|\eta|=\sqrt5\). The zero is \(-6i/\sqrt5\), strictly below the real axis. Thus \(p\) never vanishes on a neighborhood of the closed upper half-plane, and \(\log|p|\) is harmonic there as the real part of a local holomorphic logarithm. At \(i\), \(p(i)=6+\sqrt5\).
For real \(t\), \(1+|\xi+t\eta|\leq6+\sqrt5|t|\leq\sqrt2|6-i\sqrt5t|\), which justifies the polynomial normalization on the boundary. At the observation point, \(|\xi+i\eta|=\sqrt{30}\), and
\(6+\sqrt5\leq\sqrt2(1+\sqrt{30})\).
The polynomial factor therefore retains the same exponent after returning from the line parameter to complex vector norm.

### Exercise 7: division through a zero by averages (10 points)

For \(F(z)=z\), \(W(z)=ze^z\), identify the entire quotient. Explain how translating the origin and integrating \(\log|F|\) avoids an invalid pointwise lower bound at zero.

*Solution.* The quotient extends to \(G(z)=e^z\). Translate by the complex point one: the denominator becomes \(F_1(z)=z+1\), with \(\log|F_1(0)|=0\).
Its logarithm is locally integrable even at \(z=-1\). The submean inequality gives a lower bound for its mean on balls centered at zero, while its exponential-type upper bound controls its positive part. Thus the mean of its absolute logarithm is \(O(R+1)\). This controls the negative part on comparison balls used to estimate \(\log|G|\), proving exponential type of the quotient.
There is no positive pointwise lower bound for \(|F|\) near its zero, and none is used. The equality \(\log|G|=\log|W|-\log|F|\) is applied almost everywhere under locally integrable averages; the zero set has real area zero. This example illustrates Lindelöf's exponential-type step alone: \(e^\xi\) is not polynomially bounded on the real axis, so the example does not meet the compact Fourier numerator/divisor assumptions of the main theorem.

### Exercise 8: local control at a double divisor zero (12 points)

Let \(F(z_1,z_2)=z_1^2-z_2\). Use the complex direction \(\theta=(1,0)\), radius \(1/2\), and \(|z_1|,|z_2|\leq1/32\) to prove a local bound for every entire \(G\) in terms of \(FG\).

*Solution.* On \(|t|=1/2\),
\[
 F(z+t\theta)=t^2+2tz_1+z_1^2-z_2,\qquad
 |2tz_1+z_1^2-z_2|
 \leq\frac1{32}+\frac1{1024}+\frac1{32}
 =\frac{65}{1024}<\frac18.
 \tag{T14}
\]
Since \(|t^2|=1/4\), this gives
\(|F(z+t\theta)|\geq1/4-65/1024>1/8\).
Apply the Cauchy formula to \(t\mapsto G(z+t\theta)\). Then
\[
 |G(z)|\leq8\sup_{|t|=1/2}|F(z+t\theta)G(z+t\theta)|.
 \tag{T15}
\]
The circle points over the closed polydisk form a compact set, giving uniform local control. At the center \(F(t,0)=t^2\) has a double zero; the argument avoids it by a nonzero circle and still controls \(G\) at the zero itself. No simple-zero assumption is present.

### Exercise 9: one exponent makes every decay order available (12 points)

In dimension two suppose the quotient-space estimate has exponent \(m=4\). Show how coordinate derivative orders \(s=11\) imply real decay of \(V=F_v\) at least of order seven. Explain why derivative-dependent exponents could fail to prove any decay.

*Solution.* Apply the estimate to \((i\zeta_1)^{11}V\) and \((i\zeta_2)^{11}V\), and take the larger of their finite norm constants. For \(|\xi|\geq1\), one coordinate has modulus at least \(|\xi|/\sqrt2\). Therefore
\[
 |V(\xi)|\leq C\,2^{11/2}|\xi|^{-11}(1+|\xi|)^4
 \leq C\,2^{11/2+4}|\xi|^{-7}
 \leq C\,2^{11/2+11}(1+|\xi|)^{-7}.
 \tag{T16}
\]
Increase the constant to include the bounded frequency ball. Arbitrarily large \(s\) give every inverse polynomial order because the original exponent four does not change.
If instead the estimate for derivative order \(s\) only had exponent \(m_s=s+100\), dividing by \(|\xi|^s\) would leave growth of order one hundred, rather than decay. Separate polynomial bounds do not imply smoothness; Baire's theorem supplies the needed uniform exponent.

### Exercise 10: a finite regularity perturbation threshold (12 points)

Assume the original real-window supremum is at least \(10^{-2}(1+|c|)^{-3}\), with radius \(\log(2+|c|)\). Let a compact \(C^4\) perturbation obey \(|F_v(\xi)|\leq C_v(1+|\xi|)^{-4}\). Give a sufficient tail threshold and a new lower bound, then explain how to include bounded centers.

*Solution.* First take \(|c|=q\) large enough that \(\log(2+q)\leq q/2\). In the window, \(1+|c+h|\geq(1+q)/2\), so
\[
 |F_v(c+h)|\leq16C_v(1+q)^{-4}.
 \tag{T17}
\]
If \(1+q>6400C_v\), this is less than \((10^{-2}/4)(1+q)^{-3}\). Choose a real point where the original modulus exceeds \((3\cdot10^{-2}/4)(1+q)^{-3}\); such a point exists by the supremum lower bound. The perturbed modulus there exceeds
\((10^{-2}/2)(1+q)^{-3}\).
Thus the new transform is nonzero and has the stated polynomial lower bound on the tail.
Its window supremum is positive and continuous on bounded center sets, by Exercise 3. Decrease the positive coefficient to bound those sets too, then absorb it into the exponent by Lemma 2.2. The new distribution is invertible. The regularity order four is fixed by the original exponent three; only the frequency threshold depends on the perturbation's norm or support. A smooth perturbation is in every finite \(C^r\) class, giving the stated smooth invariance.

## References

- Terence Tao, [246B, Notes 2: Some connections with the Fourier transform](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/), 2021. The Fourier normalization differs from (T1).
- Terence Tao, [245B, Notes 9: The Baire category theorem and its Banach space consequences](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/), 2009.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 1983.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Springer, 1983, Chapter XVI. The full slow-decrease and entire-division proof is supplied in the complete proof above.
