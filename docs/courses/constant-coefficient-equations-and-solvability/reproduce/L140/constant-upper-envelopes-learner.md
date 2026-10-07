# Constant upper envelopes and scaled plurisubharmonic averages

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Original proof exposition, examples, solutions and diagrams: CC0 1.0.

When a family of plurisubharmonic functions changes with a large parameter, individual values may oscillate or stay singular. Its largest limiting values can nevertheless have a simple shape. A locally uniform upper bound, followed by a global upper bound on the pointwise upper limit, forces that upper limit to be constant almost everywhere.

The [complete proof UE1–UE10](constant-upper-envelopes-formal.md) constructs the needed upper semicontinuous envelopes. Its precise earlier inputs are [local integrability and smoothing, L131 NP2](../../AN02-L131.html#NP2), and [bounded-above PSH Liouville, L139 Theorem C2](../../AN02-L139.html#psh-liouville). A final application uses [the finite support function in L139](../../AN02-L139.html#recession-support-function) to control averages along expanding complex lines.

## 1. The statement concerns an upper limit

Let \(v_j\) be plurisubharmonic, or PSH, on all of \(\mathbb C^n\), \(n\ge1\). This means upper semicontinuity and the subharmonic circle inequality on each complex line; a restriction identically equal to \(-\infty\) is allowed.

Assume one common finite upper bound for all \(v_j\) on each compact set. The bound may change from one compact set to another. Define

\[
 v(z)=\limsup_{j\to\infty}v_j(z)
     =\inf_{k\ge1}\sup_{j\ge k}v_j(z).
 \tag{L140.1}
\]

The inner supremum looks only at the tail of the sequence. Increasing \(k\) removes early members, so these tail suprema decrease. Suppose that their limiting value \(v\) is bounded above by a single finite constant on the whole space. Then

\[
 v(z)=A\quad\hbox{for almost every }z,
 \qquad A=\sup_{\mathbb C^n}v\in[-\infty,\infty).
 \tag{L140.2}
\]

“Almost every” uses ordinary real \(2n\)-dimensional volume. The constant can be \(-\infty\). The functions themselves need not converge: constants alternating between 0 and \(-1\) have upper limit 0 and lower limit \(-1\), everywhere.

The whole-space bound on \(v\) is essential. The constant sequence \(v_j(z)=|z|^2\) is locally uniformly bounded above on compact sets and is PSH, but its upper limit is the same unbounded, nonconstant function.

## 2. Why regularization is needed

A supremum of arbitrarily many upper semicontinuous functions need not be upper semicontinuous. For a locally upper-bounded function \(f\), its regularization is

\[
 f^*(z)=\lim_{r\downarrow0}\sup_{|\zeta-z|<r}f(\zeta).
 \tag{L140.3}
\]

It records the largest value visible in every small neighborhood and includes the center itself, so \(f\le f^*\). For the tail supremum \(f_k=\sup_{j\ge k}v_j\), let \(U_k=f_k^*\).

The main construction proves two facts: \(U_k\) is PSH, and \(U_k=f_k\) outside a set of measure zero. It also proves this for an uncountable family, which will matter when the index is a real dilation parameter.

To see the mechanism, start with finite maxima. A finite maximum is PSH: choose a function attaining the maximum at a circle center, use its mean inequality, then bound its circle values by the maximum. These maxima increase to the full countable supremum and converge in local \(L^1\), because a nontrivial first member supplies an integrable lower bound and the hypothesis supplies a common upper bound.

Smooth each maximum with a positive radial kernel. The result is smooth and PSH and lies above that maximum. Passing to the local \(L^1\) limit gives smooth majorants of the full supremum. A summable sequence of smoothing errors shows that the regularization and the original supremum agree almost everywhere. The smooth majorants converge to the regularization at every point; reverse Fatou passes their circle inequalities to it. [UE2–UE3](constant-upper-envelopes-formal.md#UE3) give every step, including minus-infinite values.

## 3. A logarithmic hole which persists

In one complex variable consider

\[
 v_j(z)=\frac1j\log|z|,
 \tag{L140.4}
\]

with value \(-\infty\) at zero. The logarithm is subharmonic, and multiplication by the positive number \(1/j\) preserves that property. Each compact disk has a common finite upper bound for the whole sequence. At every nonzero point the sequence tends to zero, but at zero it remains \(-\infty\).

For \(r=|z|>0\), the tail supremum is 0 when \(r\le1\), and \((\log r)/k\) when \(r>1\). At zero its value remains \(-\infty\). Regularization produces

\[
 U_k(z)=\frac{\max(0,\log|z|)}k,
 \qquad U_k(0)=0.
 \tag{L140.5}
\]

These envelopes decrease to zero everywhere. The raw upper limit still has its one singular value. This is why the theorem's conclusion is almost everywhere. In \(\mathbb C^n\), replace \(z\) by the first coordinate \(z_1\); the exceptional set is the hyperplane \(z_1=0\), which has real codimension two and volume zero. [Example 1 in UE8](constant-upper-envelopes-formal.md#UE8) verifies the PSH line restrictions and the exact tails.

![Logarithmic functions and the regularized envelopes of their tails.](figures/logarithmic-tail-envelopes.png)

*Figure 1.* The left panel shows exact radial sections \(\log r/j\), for \(j=1,2,4,8\), on \(10^{-3}\le r\le3\); the logarithmic radius axis does not include the singular center. The right panel shows \(\max(0,\log r)/k\), including its regularized value zero at the center. The raw tail has value \(-\infty\) at that marked point. No finite number has been assigned to the original singularity. The curves illustrate (L140.4)–(L140.5).

## 4. The decreasing tail limit becomes constant

The envelopes \(U_k\) decrease. Their limit \(U\) is upper semicontinuous and PSH: after subtracting from a common upper bound, monotone convergence passes the circle inequality to the limit.

For each \(k\), discard the null set where \(f_k\ne U_k\). There are only countably many tails, so their combined exceptional set is still null. Consequently

\[
 v=U\quad\hbox{almost everywhere},\qquad v\le U\quad\hbox{everywhere}.
 \tag{L140.6}
\]

If \(U\equiv-\infty\), the everywhere inequality makes \(v\equiv-\infty\) as well. Otherwise \(U\) is locally integrable. Its almost-everywhere agreement with the globally upper-bounded \(v\) gives the same bound almost everywhere. The real ball-mean inequality then gives the bound at every center.

Now the [PSH Liouville theorem](../../AN02-L139.html#psh-liouville) applies: \(U\) must be constant. Equation (L140.6) makes \(v\) equal to that constant almost everywhere and no larger anywhere. Its global supremum is therefore that same constant. [UE5](constant-upper-envelopes-formal.md#UE5) is the complete proof of (L140.2).

## 5. Real dilation parameters are included

For a family \(v_t\), \(t\ge1\), the tail \(\{v_t:t\ge k\}\) is usually uncountable. Sampling only integers can miss members of this tail. A family of spatial constants which is zero at integers and one at every other parameter has full upper limit one; sampling integers would give zero.

The proof handles the entire family. Take a countable base of rational balls and rational thresholds. For every threshold below the family's supremum on such a ball, select one function which exceeds that threshold somewhere in the ball. These countably many selections reproduce every ball supremum and hence the full upper semicontinuous regularization. Almost-everywhere equality for the selected functions squeezes the whole family's supremum to that same regularization.

Apply this construction separately to the countably many tails \(t\ge k\). The rest of the proof is unchanged. Thus a locally uniformly upper-bounded PSH family with a globally bounded-above pointwise \(\limsup_{t\to\infty}\) has a constant upper limit almost everywhere. No integration or measurability in \(t\) is needed. [UE4 and UE6](constant-upper-envelopes-formal.md#UE4) prove the selection and real-parameter assertions.

## 6. A scaled-average application

Let \(q\) satisfy the linear imaginary-growth hypothesis from [L139](../../AN02-L139.html#psh-envelope-theorem). Its finite continuous support function \(H\) obeys

\[
 q(x+iy)\le M(0)+H(y),
 \qquad H(a+b)\le H(a)+H(b),\quad H(ra)=rH(a)\quad(r\ge0).

\]

For a fixed real vector \(y\) and a compact planar set \(K\), average translations along the complex line in direction \(y\):

\[
 a_t(\zeta)=\frac1t\int_K q(\zeta+twy)\,dA(w),
 \qquad L=\int_K H((\operatorname{Im}w)y)\,dA(w).
 \tag{L140.7}
\]

Positive translation averages are PSH: integrate each translated circle inequality, and use the local upper bound to justify Tonelli and upper semicontinuity. Subadditivity and positive homogeneity give the precise estimate

\[
 a_t(\zeta)\le L+\frac{m(K)}t
                 \bigl(M(0)+H(\operatorname{Im}\zeta)\bigr).
 \tag{L140.8}
\]

This supplies a common upper bound on compact center sets and a pointwise upper limit at most \(L\) on the whole space. The envelope theorem consequently makes that upper limit a constant \(A\le L\) almost everywhere.

There is a useful distinction between spatial constancy and the value of the constant. To prove \(A=L\), one needs a lower estimate. If one center already has upper limit at least \(L\), the everywhere majorization in (L140.6) forces equality. An absolute error integral requires the corresponding lower integral estimate as well. [UE7](constant-upper-envelopes-formal.md#UE7) states exactly what this application proves.

## 7. An average which can be computed completely

Take \(q(\zeta)=|\operatorname{Im}\zeta|\), \(y=1\), and the rectangle \(-1\le\operatorname{Re}w\le1\), \(0\le\operatorname{Im}w\le1\). Then \(H(b)=|b|\), the rectangle has area two, and \(L=1\). Write \(s=\operatorname{Im}\zeta\). Integrating the real coordinate first gives

\[
 a_t(\zeta)=2\int_0^1|b+s/t|\,db.
 \tag{L140.9}
\]

If \(s\ge0\), this is \(1+2s/t\). If \(s\le-t\), it is \(-1-2s/t\). Between these ranges, split at the zero \(b=-s/t\), obtaining \(1+2s/t+2(s/t)^2\). At every fixed center the answer tends to one, and the triangle inequality bounds it by \(1+2|s|/t\). The calculation proves the exact limit for this example.

![The rectangle of translations and the exact scaled averages.](figures/scaled-translation-averages.png)

*Figure 2.* The rectangle in the left panel is the integration set, with area two. The middle panel fixes \(s=-1\) and shows the integrand \(|b-1/t|\); twice its area gives the average. The right panel uses the exact piecewise integral for \(-2\le s\le2\). The fixed-center limit is the horizontal line 1. The values at \(s=-1\), for \(t=1,2,4,8\), are \(1,1/2,5/8,25/32\). The finite-parameter averages need not approach their limit monotonically. See (L140.7)–(L140.9) and formal Example 4.

## 8. Exercises and complete solutions

**Exercise 1.** What do the upper limit and lower limit equal for a sequence of constants alternating between 2 and \(-3\)?

**Solution.** Every tail contains both values, so its supremum is 2 and its infimum is \(-3\). The upper limit is 2 and the lower limit is \(-3\), everywhere. Both values are PSH constants. The envelope theorem concerns the upper limit and does not make the sequence converge.

**Exercise 2.** For \(v_j=\log|z|/j\), find the tail supremum at radius \(1/4\) and radius 4. Does a function attain each supremum?

**Solution.** At radius \(1/4\), the values are \(-\log4/j\), so the supremum over \(j\ge k\) is zero, approached as \(j\to\infty\) and never attained. At radius 4 the values are \(\log4/j\), so their maximum is \(\log4/k\), attained at \(j=k\). At the center every value is \(-\infty\); the regularized envelope's center value zero is supplied by nearby points.

**Exercise 3.** Why can an almost-everywhere upper bound for the PSH limit \(U\) be upgraded to an everywhere upper bound?

**Solution.** If \(U\not\equiv-\infty\), it is real subharmonic and locally integrable. On a ball its volume integral is unchanged by removing a null set. Therefore a bound \(U\le C\) almost everywhere makes its volume average at most \(C\). The ball-mean inequality gives \(U\) at the center no larger than that average. Every point can be such a center. In the identically minus-infinite case the bound is immediate.

**Exercise 4.** Why do real parameters introduce no uncountable union of exceptional null sets in the proof?

**Solution.** Inside each tail \(t\ge k\), rational balls and rational thresholds select a countable family with the same regularization as the entire tail. That envelope agrees with the full tail supremum almost everywhere. Only the countably many integer thresholds \(k\) then produce exceptional sets to combine. Their union is null, even though each tail contains uncountably many functions.

**Exercise 5.** Compute the rectangle average at \(s=-1\) for \(t=2\) and \(t=8\).

**Solution.** For \(t=2\), split the integral at \(b=1/2\). The two triangular areas sum to \(1/4\); multiplying by two gives \(1/2\). For \(t=8\), use \(1+2(-1/8)+2(1/64)=1-1/4+1/32=25/32\). Both differ from the fixed-center limit 1 because their dilation factors are finite.

**Exercise 6.** Suppose a scaled-average upper limit equals a constant \(A\le L\) almost everywhere and is at most \(A\) everywhere. If one center has upper limit at least \(L\), what follows? Does that alone imply convergence at every center?

**Solution.** At that center the two inequalities give \(L\le A\le L\), hence \(A=L\). It follows that the upper limit is \(L\) almost everywhere. An upper limit does not control the lower limit: alternating constants already demonstrate this. The pointwise convergence and absolute integral convergence need additional estimates.

## Source credit

Lars Hörmander, *The Analysis of Linear Partial Differential Operators II* (1983 edition; second revised printing 1990; reprint 2005), §16.2, Lemma 16.2.3 and the following real-parameter remark, printed p. 316 (PDF p. 329). The [complete original proof](constant-upper-envelopes-formal.md) establishes the upper-envelope construction and almost-everywhere constancy. The scaled-average application uses the explicitly linked support-function theorem.
