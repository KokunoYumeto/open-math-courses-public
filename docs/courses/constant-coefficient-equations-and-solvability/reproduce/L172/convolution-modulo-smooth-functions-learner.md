# Learning convolution modulo smooth functions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Ordinary convolution samples the full support of its kernel. An equation modulo smooth functions can ignore the kernel's smooth part. This changes which open domains can be used. It also changes the compactness question: singularities must stay away from the equation boundary, while smooth tails may extend much farther.

Basic references are [Grubb's Fourier-distribution notes](https://web.math.ku.dk/~grubb/dist5.pdf), [Melrose's differential-analysis course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/), and Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. The accompanying formal chapter constructs the quotient operation and proves its two necessary conditions. Use Frequency-selective singularities and smooth convolutions for the isolated-singularity obstruction, Recovering singularities from convolution profiles for bounded singular hulls, and Singular supports and arbitrary distribution data for the increasing-order Sobolev mechanism.

## 1. The operation and the geometric test

Write \(Q(X)=\mathcal D'(X)/C^\infty(X)\). Two distributions define the same class when their difference is smooth on all of \(X\). If \(\mu\) is compact, the condition for its quotient operation is
\[
 X_2-\operatorname{sing\,supp}\mu\subset X_1.
 \tag{E1.1}
\]
Near any compact output set, replace \(\mu\) by a compact kernel supported close to its singular support and differing from \(\mu\) by a smooth function. Ordinary convolution with that replacement is defined there. Different replacements differ smoothly, and a partition of unity patches the local answers into one class. Theorem 1.2 of the formal chapter proves every step.

Two compact kernels whose difference is smooth induce the same quotient operation. Their compositions agree with convolution of the kernels, whenever the singular sampling conditions allow the composition. A smooth product induces the zero map. These facts concern classes; they do not assign an ordinary convolution to every distribution on every domain.

Surjectivity on \(Q(X_2)\) forces kernel invertibility and this condition: for each compact \(K_1\subset X_1\), one compact \(K_2\subset X_2\) must contain the singular support of every compact \(v\) on \(X_2\) whose adjoint image has singularities only in \(K_1\). The adjoint image is \(\check\mu*v\), with a reflected kernel and a bilinear pairing.

For an invertible kernel, that condition is exactly
\[
 d_{X_2}(\operatorname{sing\,supp}v)
   =d_{X_1}(\operatorname{sing\,supp}(\check\mu*v)).
 \tag{E1.2}
\]
Distance to an empty complement and the distance of an empty singular set are infinite. Invertibility is an essential hypothesis of this equivalence. Singular sets are not preserved by mollification: every mollified compact distribution is smooth. The proof instead cuts off smooth tails and translates the actual singularities towards a boundary.

## 2. Four worked examples

For the smooth bumps below, let
\[
 \rho(t)=
 \begin{cases}
 c\exp[-1/(1-16t^2)],&|t|<1/4,\\
 0,&|t|\ge1/4,
 \end{cases}
 \qquad \int_{\mathbb R}\rho(t)\,dt=1.
 \tag{E2.1}
\]
The positive normalizing constant exists because the unnormalized continuous bump has a finite positive integral. Its zero extension is smooth: each derivative near an endpoint is a polynomial in reciprocal powers of \(1-16t^2\), times the exponential, and the exponential dominates every such power. Thus its support is exactly \([-1/4,1/4]\).

### Example 1. A smooth tail changes ordinary sampling

Let
\[
 \mu=\delta_{1/3}+\rho(\,\cdot-3),\qquad
 X_1=(-1,1),\qquad X_2=(-2/3,4/3).
 \tag{E2.2}
\]
The singular support of \(\mu\) is \(\{1/3\}\), so (E1.1) holds with equality:
\(X_2-\{1/3\}=X_1\). The ordinary support also contains \([11/4,13/4]\). At output \(x=0\), that tail would sample an input near \(-3\), outside \(X_1\). Ordinary convolution with an arbitrary distribution on \(X_1\) therefore has no such full-domain definition.

In the quotient, the tail is discarded and the operation is translation by \(1/3\). For every \(f\in\mathcal D'(X_2)\), define \(u\in\mathcal D'(X_1)\) by
\[
 u(\theta)=f\bigl(x\longmapsto\theta(x-1/3)\bigr),
          \qquad\theta\in C_c^\infty(X_1).
 \tag{E2.3}
\]
The displayed test has compact support in \(X_2\). For regular functions, this says \(u(y)=f(y+1/3)\). Distributional translation gives
\(\delta_{1/3}*u=f\), hence \(\mu_*[u]=[f]\).

The kernel is invertible, consistently with Theorem 2.1. Here is a direct slow-decrease check. On real frequencies,
\[
 F_\mu(\xi)=e^{-i\xi/3}+e^{-3i\xi}F_\rho(\xi).
 \tag{E2.4}
\]
Integration by parts makes \(F_\rho\) tend rapidly to zero. Thus \(|F_\mu(\xi)|\ge1/2\) for sufficiently large \(|\xi|\). The entire transform is not zero, since that real lower bound holds. For real centers in a fixed bounded interval, the maximum of \(|F_\mu|\) on the closed complex unit disk about the center is a continuous positive function: continuity follows from compact parameterization, and positivity from the entire identity principle. Its minimum there is positive. Choose a sufficiently large slow-decrease constant so its logarithmic windows contain those unit disks and its polynomial lower threshold is smaller than that minimum and \(1/2\). The complex-window characterization in the linked slow-decrease theorem then proves invertibility.

![The singular atom samples inside the solution interval while the smooth kernel tail would sample outside it; only the atom is needed for the quotient operation.](figures/singular-sampling-and-a-remote-smooth-tail.png)

At the output \(x=0\), the atom samples \(y=-1/3\), and the tail samples the band \(y\in[-13/4,-11/4]\). The solution interval is \((-1,1)\). The dashed tail band describes the unavailable ordinary sampling, while the quotient operation uses the singular atom. These are support-set diagrams, with schematic vertical placement and exact horizontal interval differences from (E2.2).

### Example 2. Cutting off a smooth input tail

Take \(v=\delta_0+\rho(\,\cdot-3)\), \(X_2=(-1,1)\), and \(\mu=\delta_{1/3}\). Its ordinary support does not lie in \(X_2\), but its singular support does. Choose \(\chi\in C_c^\infty((-1,1))\) equal to one near zero. The smooth tail has support disjoint from \(\chi\), so \(\chi v=\delta_0\), and the removed part is smooth.

Use \(X_1=(-4/3,2/3)\). The full adjoint image is
\[
 \check\mu*v=\delta_{-1/3}+\rho(\,\cdot-8/3).
 \tag{E2.5}
\]
Only \(-1/3\) is singular. Its singular distance to \(X_1^c\) is one, as is the distance of \(\{0\}\) to \(X_2^c\). Cutting off \(v\) leaves both singular sets unchanged.

This is the precise extension used in the translation argument of Theorem 3.2. A full support may leave the domain while the singular support stays inside it. The cutoff extension of confinement allows that situation.

### Example 3. One datum with orders increasing towards the boundary

Set \(X_1=(-2,2)\), \(X_2=(-1,1)\), and \(\mu=\delta_0\). Define
\[
 x_j=1-2^{-j},\qquad
 f=\sum_{j\ge1}\delta_{x_j}^{(j)}\quad\text{on }X_2,
 \tag{E2.6}
\]
where the superscript denotes the ordinary \(j\)-th distributional derivative. Every compact subset of \(X_2\) meets only finitely many \(x_j\), so this sum is a distribution there.

It has no extension to \(X_1\), even modulo a smooth function on \(X_2\). Suppose \(u|_{X_2}=f+g\) with \(u\in\mathcal D'(X_1)\) and \(g\) smooth on \(X_2\). On the fixed compact test support \([0,3/2]\subset X_1\), \(u\) has a finite order \(N\). Choose \(j>N\). A small interval about \(x_j\) contains no other \(x_\ell\) and lies inside \(X_2\).

Choose \(\eta_j\in C_c^\infty((-1,1))\) with \(\eta_j^{(j)}(0)=1\), for example \(t^j/j!\) times a cutoff equal to one near zero. For sufficiently small \(\varepsilon>0\), put
\[
 \theta_\varepsilon(x)=\varepsilon^j
                   \eta_j((x-x_j)/\varepsilon).
 \tag{E2.7}
\]
All derivatives through order \(N\) tend uniformly to zero, with bounds \(C_j\varepsilon^{j-N}\). But
\[
 f(\theta_\varepsilon)=(-1)^j,\qquad
 g(\theta_\varepsilon)=O(\varepsilon^{j+1})\longrightarrow0.
 \tag{E2.8}
\]
The bound on the smooth term is local near this one fixed \(x_j\). Thus \(u(\theta_\varepsilon)\) tends to a nonzero value, contradicting its finite-order estimate. No global growth bound on \(g\) was assumed.

The corresponding compact witnesses are \(v_j=\delta_{x_j}\). Their unchanged image singularities all lie in the one compact \([1/2,1]\subset X_1\), while no compact subset of \(X_2\) contains all their singular points. The two distances are
\[
 d_{X_2}(\{x_j\})=2^{-j},\qquad
 d_{X_1}(\{x_j\})=1+2^{-j}.
 \tag{E2.9}
\]
The failure of compact confinement and the increasing-order datum express the same boundary obstruction.

![Singular points tend to the excluded equation boundary; their derivative orders increase, and the equation-domain distances tend to zero while the solution-domain distances stay positive.](figures/escaping-singularities-and-increasing-orders.png)

The first panel shows the first five points, their derivative orders and the excluded boundary at \(1\). The second shows the exact distances in (E2.9) for further points. The contradiction applies to the full infinite distribution (E2.6), not just to the plotted samples.

### Example 4. Infinite distances do not detect a smooth kernel

Let \(\mu=\rho\), and \(X_1=X_2=\mathbb R\). Its quotient map is zero, because its singular support is empty. Hence it cannot solve the class of any point mass. For every compact \(v\), \(\check\rho*v\) is smooth.

Nevertheless the distance identity alone reads
\[
 d_{\mathbb R}(\operatorname{sing\,supp}v)=\infty
        =d_{\mathbb R}(\varnothing).
 \tag{E2.10}
\]
It holds for every compact input. Confinement fails: the point masses \(\delta_x\), for all \(x\in\mathbb R\), have smooth images, while no one compact contains all their singular points. Theorem 3.2 explicitly assumes invertibility, and therefore makes no erroneous inference from (E2.10).

## 3. How the increasing-order proof handles a general kernel

The formal argument uses compact \(v_j\) with singular points escaping every compact subset of \(X_2\), while their image singularities remain inside one \(K_1\subset X_1\). Each \(v_j\) has some negative Sobolev order \(s_j\). Its derivatives cannot all remain in the one space \(H^{s_j-a_{j-1}}_{\rm loc}\) near its singular point, so choose a derivative of order \(a_j>a_{j-1}\) that leaves that space.

The full kernel may have an unusable smooth tail. It is replaced, separately near each compact test family, by \(\kappa_j=\theta_j\mu\). The removed part is smooth. Every \(\kappa_j\) has one common finite kernel order \(r\), although its constants may vary. This gives
\[
 \check\kappa_j*v_j\in H^{s_j-r}.
 \tag{E3.1}
\]
A cutoff of the image near \(K_1\) places its singular part on a fixed compact set in \(X_1\). Any proposed solution has one finite order \(c\) there. All other terms are smooth and can be estimated at any chosen Sobolev order. For large \(j\), \(a_{j-1}\ge c+r\), and the equation forces the forbidden derivative back into \(H^{s_j-a_{j-1}}_{\rm loc}\). That is the contradiction.

The supports of every ordinary pairing lie inside its domain. The common quantity is \(c+r\); constants and smooth errors need not be common across all \(j\).

## 4. Exercises and full solutions

**Exercise 1 (10 points).** Let \(\mu=i\delta_{-2/5}+b\), with \(b\) compact and smooth, and let \(X_1=(0,2)\), \(X_2=(-2/5,8/5)\). Construct a quotient solution for every datum. Compute the reflected kernel modulo smooth functions, and solve for \(f=\delta_{3/5}\). Keep the complex pairing bilinear.

*Solution.* The singular kernel samples \(u(x+2/5)\), so set \(u(y)=f(y-2/5)/i\) in the distributional translation sense. More explicitly, \(u(\theta)=f(x\mapsto\theta(x+2/5))/i\); its test has compact support in \(X_2\). Then \(i\delta_{-2/5}*u=f\), and the smooth part \(b\) does not change the quotient class. Reflection gives \(\check\mu=i\delta_{2/5}+\check b\): the coefficient remains \(i\). For the point datum, \(u=-i\delta_1\), and \(i\delta_{-2/5}*(-i\delta_1)=\delta_{3/5}\). Conjugating the coefficient in the reflected kernel would contradict this bilinear calculation.

**Exercise 2 (10 points).** With \(X=(-1,1)\), \(Y=(-2/3,4/3)\), take \(a=\delta_{1/3}+b\) and \(c=\delta_{-1/3}+d\), where \(b,d\) are compact smooth functions. Prove that their quotient maps are mutual inverses on the translated domains.

*Solution.* The singular sets are \(\{1/3\}\) and \(\{-1/3\}\); the compatibility relations are \(Y-\{1/3\}=X\) and \(X-\{-1/3\}=Y\). Their product is
\[
 c*a=\delta_0+\delta_{-1/3}*b+d*\delta_{1/3}+d*b.
 \tag{E4.1}
\]
The last three terms are compact smooth functions by differentiation in the smooth factor. The composition lemma therefore gives \(c_*a_*=(\delta_0)_*\), the identity on \(Q(X)\). Compact convolution is commutative, so the reverse composition is the identity on \(Q(Y)\). This conclusion uses only proper local representatives of the two kernels and does not require their full supports to satisfy ordinary sampling inclusions.

**Exercise 3 (8 points).** For \(v=\delta_0-2\delta_{1/2}+\rho(\,\cdot-3)\), \(X_2=(-1/2,1)\), \(\mu=\delta_{1/4}\), and \(X_1=(-3/4,3/4)\), compute the singular sets and their distances. Explain why the full input support need not lie in \(X_2\).

*Solution.* The singular set is \(T=\{0,1/2\}\). The reflected kernel is \(\delta_{-1/4}\), so the image singular set is \(W=\{-1/4,1/4\}\), with the coefficients unchanged. Each distance is \(1/2\), measured to the closer endpoint of the respective interval. The smooth tail is supported in \([11/4,13/4]\), outside \(X_2\), but a cutoff inside \(X_2\) equal to one near \(T\) removes it and preserves both singular sets. Condition (E1.2) and its compact-confinement extension concern this cutoff class, not the full ordinary support.

**Exercise 4 (10 points).** Apply the compact receiver in Theorem 3.2 to \(\mu=\delta_0\), \(X_1=X_2=(-3,-1)\cup(1,3)\), and \(K_1=\{-2,2\}\). Compute \(B,\delta,K_2\), and show why requiring \(B\subset X_1\) would be an incorrect extra assumption.

*Solution.* The kernel singular hull is \(\{0\}\). Thus \(B=[-2,2]\) and \(d_{X_1}(K_1)=1\), so \(\delta=1\). The points of \(B\) with distance at least one from \(X_2^c\) are exactly \(-2\) and \(2\); hence \(K_2=\{-2,2\}\). The identity image has the same singular support as its input, so this receiver works. The hull \(B\) contains the entire gap \([-1,1]\), outside the open domain. Its role is to give a bounded ambient set; the positive-distance condition then trims it into the domain.

**Exercise 5 (8 points).** Prove directly that a compact smooth kernel fails the real-window slow-decrease condition. Then explain the infinite-distance example without concluding invertibility.

*Solution.* Integration by parts gives, for every integer \(M\), \(|F_\mu(\xi)|\le C_M(1+|\xi|)^{-M}\). Fix a real logarithmic window radius constant, for example one. For large \(q=|\xi|\), every real displacement \(|h|<\log(2+q)\) has \(|\xi+h|\ge q/2\). Given any proposed lower-bound constant \(A>0\), choose \(M>A\). For sufficiently large \(q\), \(C_M(1+q/2)^{-M}<(A+q)^{-A}\). Thus the window supremum fails that lower bound, and no \(A\) works. The real-window characterization proves noninvertibility. On the full real line, both complement distances are infinite independently of this decay, so the distance equality alone cannot encode invertibility. Point masses at arbitrary locations prove that compact singularity confinement still fails.

**Exercise 6 (10 points).** Prove that the nonzero distribution \(\delta_{x_0}^{(m)}\) has order exactly \(m\) in a neighborhood of \(x_0\), for \(m\ge0\). Show that adding a smooth function does not lower this local order when \(m>0\).

*Solution.* Its action is \((-1)^m\theta^{(m)}(x_0)\), so order at most \(m\) is immediate. For \(m\ge1\), choose a compact \(\eta\) with \(\eta^{(m)}(0)=1\), and test on \(\theta_\varepsilon(x)=\varepsilon^m\eta((x-x_0)/\varepsilon)\). All derivatives through order \(m-1\) tend uniformly to zero, while the distribution's value stays \((-1)^m\). Thus no order-\((m-1)\) estimate exists. A smooth added term has value \(O(\varepsilon^{m+1})\) on these tests and does not change this contradiction. For \(m=0\), order zero is the smallest allowed nonnegative distributional order, and the nonzero point mass attains it.

**Exercise 7 (12 points).** On \(X_2=(0,2)\), set \(x_j=2-3^{-j}\) and \(f=\sum_{j\ge1}\delta_{x_j}^{(2j)}\). Prove that it is a distribution there but has no extension modulo a smooth function to \(X_1=(-1,3)\). Identify a compact set witnessing failure of singular confinement for the identity kernel.

*Solution.* Each compact subset of \(X_2\) has positive distance from \(2\) and meets only finitely many \(x_j\). Thus the sum is locally finite. If \(u|_{X_2}=f+g\) with \(g\) smooth, \(u\) has one order \(N\) on the fixed compact test support \([1,5/2]\subset X_1\). Choose \(2j>N\), and a small interval around \(x_j\) avoiding all other points. With \(\eta^{(2j)}(0)=1\), the tests \(\varepsilon^{2j}\eta((x-x_j)/\varepsilon)\) have every derivative through order \(N\) tending to zero. The datum acts by \(1\), and the smooth term tends to zero, contradicting the order bound. The compact image-singularity set \(K_1=[5/3,2]\subset X_1\) contains all \(x_j\). The compact witnesses \(\delta_{x_j}\) have no uniform compact singular support bound inside \(X_2\), since their limit point is the excluded boundary \(2\).

**Exercise 8 (12 points).** Explain why the locally truncated kernels in Theorem 4.1 have one common order \(r\), but need not have common constants. Deduce the Fourier loss \(H^{s_j}\to H^{s_j-r}\), and explain which part of the proposed solution has one common order \(c\).

*Solution.* On a fixed compact neighborhood of \(\operatorname{supp}\mu\), the kernel satisfies \(|\mu(h)|\le C\max_{|\alpha|\le r}\sup|\partial^\alpha h|\). Multiplication by \(\theta_j\) replaces \(h\) by \(\theta_jh\). The full Leibniz sum has only derivatives of \(h\) through order \(r\); derivatives of \(\theta_j\) change the constant \(C_j\) but not \(r\). Cutoffs with supports shrinking towards a singular set can indeed have growing derivative constants. Applying the bound to a real exponential gives \(|F_{\kappa_j}(\xi)|\le C_j\langle\xi\rangle^r\). Fourier multiplication therefore sends \(v_j\in H^{s_j}\) to \(\check\kappa_j*v_j\in H^{s_j-r}\). Multiplication by the fixed smooth cutoff \(\chi\) preserves that Sobolev order. The singular image part convolved with any test on \(Y_j\) has support in the one compact \(\operatorname{supp}\chi+\overline Y_1\subset X_1\); the distribution \(u\) has one order \(c\) on that compact test space. Smooth image parts and smooth errors may use constants depending on \(j\), because they can be estimated at every real Sobolev order. Thus the necessary common bound is the fixed loss \(c+r\).

**Exercise 9 (10 points).** Let \(\mu=\delta_{1/4}\), \(X_2=(-1,1)\), \(X_1=(-3/2,3/2)\). Use translated point tests to exhibit strict failure of (E1.2) and to disprove uniform singular confinement. Compute a single swept compact containing all the image singularities.

*Solution.* For \(v=\delta_0\), the input distance is one, while the image \(\delta_{-1/4}\) has distance \(5/4\). Translate by \(s\in[0,1)\). Each \(v_s=\delta_s\) lies in \(\mathcal E'(X_2)\), but its singular point tends to the excluded boundary \(1\). Every image is \(\delta_{s-1/4}\), with singular support in \(K_1=[-1/4,3/4]\subset X_1\). That compact has distance \(3/4\) from \(X_1^c\). No compact \(K_2\subset X_2\) can contain all the points \(s<1\). Compatibility still holds, since \(X_2-\{1/4\}=(-5/4,3/4)\subset X_1\). This example separates compatibility from the stronger boundary condition.

**Exercise 10 (10 points).** Suppose a compact \(v\) is singular exactly at zero and \(\mu*v\) is smooth. Prove that the quotient equation for a point mass in a nonempty equation domain cannot be solved, using the canonical composition law rather than assuming that the full kernels have proper ordinary sampling domains.

*Solution.* Let \(x_0\in X_2\) and suppose \(\mu_*[u]=[\delta_{x_0}]\), where the singular sampling condition defines the map from \(X_1\) to \(X_2\). Since \(S_v=\{0\}\), \(v_*\) is an endomorphism of \(Q(X_2)\). Composition gives \(v_*\mu_*[u]=(\mu*v)_*[u]=0\), because a smooth compact kernel induces zero. On the right, \(v_*[\delta_{x_0}]\) is the class of the translate of \(v\), singular at \(x_0\), so it is nonzero. This contradiction uses local proper representatives of the kernels; their smooth tails may lie outside the ordinary sampling region. If \(\mu\) itself is smooth, its quotient map is already zero and the same point datum cannot be solved.

## References

- Gerd Grubb, *Distributions and Operators*, Chapter 5, “Fourier transformation of distributions,” freely readable [lecture notes](https://web.math.ku.dk/~grubb/dist5.pdf).
- Richard B. Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004, freely readable [course materials](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 1990.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
- The full quotient-operation, invertibility-necessity, compact-confinement and distance proofs are in the accompanying formal chapter. The examples and exercises here are original.
