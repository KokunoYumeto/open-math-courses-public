# Learning local compactness and Hartogs bounds

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Original learner exposition, examples and solutions: CC0 1.0.

A locally uniform upper bound controls positive peaks. For a subharmonic function, the mean inequality then says that a single finite value also controls the amount of negative mass nearby. Connectedness carries that control to the rest of the domain. This is the mechanism behind the compactness alternative.

The exact formal argument is in [Local compactness and Hartogs bounds](psh-local-compactness-formal.md#psh-local-compactness). Its classical real-subharmonic comparison is Hörmander I, Theorem 4.1.9, in *Distribution Theory and Fourier Analysis*, first edition 1983, second edition 1990, reprint 2003. The proof and illustrations here are original.

<a id="learner-statement"></a>

## The statement to keep in view

Let \(\Omega\subset\mathbb C^n\) be nonempty, open and connected, with \(n\ge1\). Suppose each \(v_j\) is plurisubharmonic, abbreviated PSH, and the family is bounded above on every compact subset:

\[
\forall K\subset\Omega\text{ compact},\quad
\exists C_K\in\mathbb R,\quad
v_j(z)\le C_K\quad(z\in K,\ j\ge1).
\]

PSH functions may take the value minus infinity. Their restrictions to complex lines obey the subharmonic circle-mean inequality or are identically minus infinite. We call a function proper if it is not identically minus infinite.

Exactly one alternative holds:

- The entire sequence tends to minus infinity uniformly on every compact set.
- A subsequence of proper members converges in local \(L^1\) to a proper PSH function \(v\).

For the convergent subsequence, written \(w_m\),

\[
\limsup_m w_m(z)\le v(z)\quad\text{at every point},\qquad
\limsup_m w_m(z)=v(z)\in\mathbb R\quad\text{almost everywhere}.
\]

A further subsequence converges almost everywhere. This does not make every original index converge pointwise.

The Hartogs bound adds something that an almost-everywhere statement cannot supply. If a proper PSH sequence converges in distributions to a proper PSH \(v\) under the same local upper bounds, then for every compact \(K\subset\Omega\) and every continuous real \(f\) on \(K\),

\[
\limsup_j\sup_K(v_j-f)\le\sup_K(v-f).
\]

It holds even when \(K\) is a singleton or the right side is minus infinity. If \(v\le f\) on \(K\), every positive error allowance eventually bounds the whole compact set: \(v_j\le f+\varepsilon\).

<a id="learner-mechanism"></a>

## From one finite value to a local integral bound

Failure of uniform collapse produces infinitely many indices and moving points \(x_m\) in one compact set with \(w_m(x_m)\ge-A\). Choose a subsequence so the points tend to \(x_0\). Pick \(r>0\) with the closed ball of radius \(4r\) about \(x_0\) inside the domain. Let \(C\) be a common upper bound there. Eventually \(|x_m-x_0|<r/2\).

Set \(q_m=C-w_m\). This is nonnegative. The subharmonic mean inequality for \(w_m\) reverses into a supermean inequality for \(q_m\):

\[
\int_{B(x_m,2r)}q_m
\le |B(0,2r)|q_m(x_m)
\le |B(0,2r)|(|C|+A).
\]

That moving ball contains the fixed ball \(B(x_0,r)\). The elementary inequality \(|w_m|\le |C|+q_m\) gives

\[
\int_{B(x_0,r)}|w_m|
\le |C|\,|B(0,r)|+(|C|+A)|B(0,2r)|.
\]

The PSH-to-real-subharmonic and local-integrability steps used here are the local statements [L140, UE2](../../AN02-L140.html#UE2) and [L131, NP2](../../AN02-L131.html#NP2).

![A controlled ball supplies a finite centre for a larger mean ball; connectedness carries the construction to other points.](figures/mean-propagation-and-components.png)

To move the control, suppose a small ball already has \(\int |w_m|\le B\) for every \(m\). If its volume is \(b>0\), then each member has a finite point \(y_m\) in that ball with

\[
w_m(y_m)\ge-D,\qquad D=B/b+1.
\]

Otherwise the integral would exceed \(Db>B\). If this controlled ball lies close to a new target point \(x\), a mean ball about \(y_m\) contains a fixed target ball about \(x\). Repeating the estimate bounds the integral on that target ball.

The set of points reached in this way is nonempty and open. The calculation also reaches every point in its relative closure, so the set is closed. Connectedness makes it the whole domain. Finite covers then give a uniform integral bound on each compact set. The full ball radii and constants are in [HC2–HC3](psh-local-compactness-formal.md#HC2).

<a id="learner-selection"></a>

## Why this really produces a subsequence

The integral bounds do not by themselves give strong convergence. We first select a distributional limit, then use subharmonicity to strengthen it.

Take a countable family of continuous compactly supported tests made from rational grids, rational vertex values and fixed smooth cutoffs. Uniform continuity shows that every continuous compact test can be approximated uniformly by members of this family with one common compact support. For each test, the integrals against \(w_m\) form a bounded scalar sequence. Select successive convergent subsequences, one for each test, and take the diagonal.

Uniform approximation extends convergence from this countable family to every test, because

\[
\left|\int (w_m-w_k)(\phi-\psi)\right|
\le 2\sup_\ell\int_Q|w_\ell|\,\|\phi-\psi\|_\infty
\]

when \(Q\) contains the common supports. The resulting functional \(T\) is a distribution of order zero. Its Laplacian is positive, since for nonnegative smooth \(\phi\),

\[
\langle\Delta T,\phi\rangle
=\lim_m\int w_m\Delta\phi\ge0.
\]

The selection and its explicit cutoff construction are proved in [HC4](psh-local-compactness-formal.md#HC4); no compactness theorem for PSH functions is assumed.

How does a distribution become a function? By [L131, NP3–NP7](../../AN02-L131.html#NP3), its positive Laplacian is a measure \(\mu\). On a relatively compact region, cut this measure off outside a slightly larger region and form its Newtonian or logarithmic potential \(P\). Then \(T-P\) has zero Laplacian and is represented by a smooth harmonic function \(h\). Thus \(P+h\) is a proper real subharmonic representative. Radial recovery makes these local representatives agree at all overlap points, including their minus-infinite values. See [HC5](psh-local-compactness-formal.md#HC5).

We must still check PSH. At a fixed small radius, positive radial smoothing makes each \(w_m*\rho_t\) PSH. The integral bounds and a finite net of translated kernels show that these smoothings converge uniformly on compact sets to \(v*\rho_t\). Their complex-circle inequalities pass to that limit. Now decrease the radius to zero: radial recovery gives the point values of \(v\), and Fatou applied to a common upper bound minus the functions passes the circle inequality once more. This is the explicit closure proof in [HC6](psh-local-compactness-formal.md#HC6).

Finally [L134, SC1](../../AN02-L134.html#SC1) upgrades this subharmonic distributional convergence to local \(L^1\). [SC6](../../AN02-L134.html#SC6) supplies the everywhere upper-limit ceiling.

<a id="learner-ae"></a>

## What almost everywhere does and does not mean

From local \(L^1\) convergence, select a further sequence with error less than \(2^{-q}\) on the \(q\)-th set of a compact exhaustion. On any fixed exhaustion set, the sum of those errors is integrable:

\[
\int_{Q_p}\sum_{q\ge p}|w_{m_q}-v|
\le\sum_{q\ge p}2^{-q}<\infty.
\]

The summands therefore tend to zero almost everywhere. At these points the upper limit of the larger convergent sequence is at least \(v\), because one further subsequence tends to \(v\); the everywhere ceiling makes it equal to \(v\).

Ordinary pointwise convergence of the larger sequence can fail. The complete moving logarithmic-well construction in [L134, SC9](../../AN02-L134.html#SC9) gives this failure despite local \(L^1\) convergence. Those functions are PSH in one complex variable because they are positive multiples of logarithms of distances plus constants.

<a id="learner-hartogs"></a>

## Why moving maxima are controlled

Fix a compact \(K\), a continuous \(f\) on \(K\), and a small smoothing radius \(t\). Strong local \(L^1\) convergence gives

\[
\sup_K |v_j*\rho_t-v*\rho_t|
\le \|\rho_t\|_\infty\int_{K_t}|v_j-v|
\longrightarrow0.
\]

Also \(v_j\le v_j*\rho_t\). Choose maximizing points \(x_j\in K\) along indices realizing the upper limit of the compact suprema, and select \(x_j\to x_*\in K\). For each fixed \(t\),

\[
\limsup_j\sup_K(v_j-f)
\le (v*\rho_t)(x_*)-f(x_*).
\]

Let \(t\) tend to zero and recover \(v(x_*)\). This is at most \(\sup_K(v-f)\). If that value is minus infinity, the same inequalities force the left side to minus infinity. This is [HC8](psh-local-compactness-formal.md#hartogs-compact-comparison). It is a pointwise smoothing argument, so it works on zero-measure compact sets too.

<a id="learner-examples"></a>

## Worked examples

**1. Collapse on a connected domain.** On \(|z|<1\), \(v_j(z)=j\log|z|\) is PSH. On a compact set choose \(r<1\) bounding all radii. Then \(v_j\le j\log r\to-\infty\) uniformly there. A compact set cannot include the boundary circle \(|z|=1\), which lies outside the domain.

**2. A singular limit in local \(L^1\).** On \(|z|<2\), take \(v_j=\max(\log|z|,-j)\) and \(v=\log|z|\). The functions are PSH and bounded above by \(\log2\). Their difference is supported in \(|z|<e^{-j}\), and

\[
\int_{|z|\le1}|v_j-v|\,dA
=2\pi\int_0^{e^{-j}}(-j-\log r)r\,dr
=\frac{\pi}{2}e^{-2j}.
\]

The error over any compact set is at most this full difference integral. On \(K=\{|z|\le e^{-2}\}\) the compact suprema are \(\max(-2,-j)\to-2\). On \(K=\{0\}\) they are \(-j\to-\infty\). The point at zero is a valid Hartogs test despite having area zero.

![The same truncated logarithms exhibit small integral error, a finite disc maximum, and a minus-infinite singleton limit.](figures/truncated-logs-and-hartogs.png)

**3. A subsequence ceiling needs its indices.** If even terms are the constant \(0\) and odd terms the constant \(-1\), the odd subsequence has limit \(-1\), while the whole upper limit is \(0\). The theorem bounds the selected upper limit.

**4. A disconnected domain.** On two disjoint unit discs let \(v_j=0\) on one and \(v_j=-j\) on the other. The upper bound is zero. The first disc prevents whole-domain collapse; the second prevents a locally integrable global subsequential limit because its integrals tend to minus infinity on every ball of positive area.

**5. The upper bound is necessary.** On the unit disc the smooth PSH functions \(j|z|^2\) do not collapse, but their integrals on any fixed disc of positive radius tend to positive infinity. They have no locally \(L^1\)-convergent subsequence, and fail the locally uniform upper-bound hypothesis.

<a id="learner-exercises"></a>

## Exercises and complete solutions

**Exercise 1.** Derive the seed estimate using a centre within \(r/3\) of the target centre.

**Solution.** Use the mean ball of radius \(4r/3\). It contains the target ball of radius \(r\) and lies inside the ball of radius \(5r/3\) about the target centre. For \(w_m(x_m)\ge-A\) and common upper bound \(C\), integrate \(C-w_m\), use the supermean inequality, and obtain
\[
\int_{B(x_0,r)}|w_m|
\le |C|\,|B(0,r)|+(|C|+A)|B(0,4r/3)|.
\]
All relevant balls lie inside the closed \(4r\) ball used for the upper bound.

**Exercise 2.** If the controlled ball has volume \(3\) and the integral bound is \(12\), give a uniform finite lower bound at one chosen point for each function.

**Solution.** Use \(D=12/3+1=5\). If every value were below \(-5\), the integral of the absolute value would be at least \(15>12\). A point with value at least \(-5\) therefore exists for each member; a locally integrable function has finite values almost everywhere. The point may vary with the member.

**Exercise 3.** Why does the diagonal limit apply to a smooth test that was not in the chosen countable family?

**Solution.** Approximate that test uniformly, to error \(\varepsilon\), by a countable-family test with the same fixed compact support bound. If the integral norm bound there is \(A\), the difference between the two pairings is at most \(A\varepsilon\) for every sequence member. Thus the difference between two late pairings of the original test is at most \(2A\varepsilon\) plus the Cauchy difference for the approximating test. First make \(\varepsilon\) small, then take the indices large. This proves convergence.

**Exercise 4.** Explain why taking a distributional limit of PSH functions requires more than positivity of the real Laplacian.

**Solution.** A positive real Laplacian only gives a real subharmonic representative. In complex dimension at least two, real subharmonicity alone does not enforce all complex-line means. For example, \(u(z_1,z_2)=|z_1|^2-\tfrac12|z_2|^2\) has positive real Laplacian \(4-2=2\), but its restriction to the second coordinate line has negative planar Laplacian \(-2\), so is not subharmonic. HC6 retains the complex-line inequalities by passing through the uniformly convergent fixed-radius PSH smoothings and then radial recovery.

**Exercise 5.** Verify the exact error for the truncated logarithms without numerical integration.

**Solution.** A primitive of \((-j-\log r)r\) is \(r^2(-j-\log r)/2+r^2/4\). At \(r=e^{-j}\) this equals \(e^{-2j}/4\), and at zero its limiting value is zero. Multiply by \(2\pi\) to obtain \((\pi/2)e^{-2j}\). This calculation also proves local \(L^1\) convergence, since the entire difference is supported in that radius.

**Exercise 6.** If \(v<f\) at every point of a compact set, prove the eventual strict bound for the approximating functions.

**Solution.** Upper semicontinuity of \(v-f\) makes its finite maximum \(S\) strictly negative; if every value is minus infinite then \(S=-\infty\). In the finite case choose \(0<\delta<-S\). The Hartogs inequality makes \(\sup_K(v_j-f)<-\delta\) for all sufficiently large \(j\). In the minus-infinite case it makes that supremum less than \(-1\) eventually. In both cases \(v_j<f\) throughout the compact set.

**Exercise 7.** If neither of two disconnected components has whole-sequence collapse, must there be one proper locally \(L^1\)-convergent subsequence on both?

**Solution.** No. At odd index \(j\), use constants \(0\) on the first component and \(-j\) on the second; at even index \(j\), interchange them. Each component has a zero subsequence and hence no whole-sequence collapse. Any infinite selection contains infinitely many odd or infinitely many even indices. On one component the integrals along those indices then tend to minus infinity. A common locally integrable limit on both components is impossible. Connectedness avoids this failure of synchronized selection.

The [formal exercises](psh-local-compactness-formal.md#HC12) also give the finite-net convolution estimate and the singleton version of the Hartogs proof. [Reproduction notes](README-reproduce.md) link the native figures, source code and exact geometry.
