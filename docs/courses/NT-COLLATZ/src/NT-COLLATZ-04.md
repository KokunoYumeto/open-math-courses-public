# First passage and transport across scales

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, proofs and exercises: CC0 1.0.*

Suppose most starting points of a system eventually enter a smaller region. Can we repeat the statement inside that region? Not without examining where the first stage lands. Its outputs might concentrate on the exceptional starting points of the second stage.

The right object to keep is the **first-passage distribution**: the law of the first point where a trajectory enters the region. We will construct its map, account explicitly for trajectories that never enter, and prove how discrepancies between successive distributions accumulate. A final theorem explains why summable errors across scales give uniform control of orbit minima.

The main results apply to any map on a subset of the positive integers. Collatz supplies the motivating application, but none of the proofs assumes its conjecture. The prerequisites are iteration and well-ordering from [Return maps and exact changes of clock](NT-COLLATZ-01.md), and countable probability masses, pushforwards, \(\ell^1\) contraction and event distance from [Pushforward measures and logarithmic sampling](NT-COLLATZ-03.md). We also use elementary logarithms and geometric series. Tao's first-passage reduction in *Almost all orbits of the Collatz map attain almost bounded values*, §§1.3 and 3, is a reference for the application. Its analytic estimates are a further subject, not assumptions silently inserted into this lesson.

## Why a second application needs a distribution

Let \(Y=\{1,\ldots,M\}\), with \(M>1\). An event can hold at every point of \(Y\) except 1, so it has probability \(1-1/M\) under the uniform law. Yet a previous map can send every one of its inputs to 1. Under that landing law, the same event has probability zero. The size of the exceptional set under one measure is not its size under another.

A quantitative remedy is available from Lemma 2 of the sampling lesson. If a landing law \(\lambda\) is within \(\varepsilon\) in \(\ell^1\) of a law \(\nu\), and \(\nu(E^c)\leq\delta\), then

\[
\lambda(E^c)\leq\delta+\varepsilon/2.
\]

Indeed, the difference on any event is at most half the \(\ell^1\) distance. The next sections construct landing laws for deterministic orbits and make their composition exact.

## A map that remembers unsuccessful entrance

Let \(D\) be a nonempty subset of \(\mathbb N_+\), and let \(F:D\to D\). For a real threshold \(x\geq1\), define

\[
t_x(n)=\min\{j\geq0:F^j(n)\leq x\},
\]

with \(t_x(n)=\infty\) if there is no such time. This is an entrance time, so \(t_x(n)=0\) when \(n\leq x\), unlike the strictly positive return time of the opening lesson.

Adjoin one symbol \(\dagger\notin D\), and write \(\widehat D=D\cup\{\dagger\}\). Define

\[
p_x:\widehat D\longrightarrow\widehat D,
\qquad
p_x(n)=\begin{cases}
F^{t_x(n)}(n),&t_x(n)<\infty,\\
\dagger,&t_x(n)=\infty,
\end{cases}
\quad p_x(\dagger)=\dagger.
\]

The image is contained in \((D\cap[1,x])\cup\{\dagger\}\), and each point of this set is fixed. The symbol \(\dagger\) is not an extra orbit value of \(F\). It records a failure to enter the chosen target. A successful landing at the integer 1 and unsuccessful entrance therefore remain different outcomes.

For example, on \(D=\{1,2,3,4,5,6\}\), take

\[
F(1)=1,\quad F(2)=1,\quad F(3)=2,\quad
F(4)=3,\quad F(5)=6,\quad F(6)=5.
\]

At threshold 2, the first four starting points have passage values \(1,2,2,2\), and the last two have passage value \(\dagger\). At threshold 4, the first four are fixed by \(p_4\), while 5 and 6 still give \(\dagger\). This example allows unsuccessful entrance without any unresolved conjecture.

## Nested targets compose exactly

**Theorem 1 (Nested passage).** For \(1\leq x\leq y\),

\[
p_x\circ p_y=p_x=p_y\circ p_x.
\]

If \(t_x(n)<\infty\), then

\[
t_x(n)=t_y(n)+t_x(p_y(n)),
\]

and for every \(k\geq0\),

\[
F^k(p_x(n))=F^{k+t_x(p_y(n))}(p_y(n)).
\]

**Proof.** If an orbit never reaches a value at most \(y\), it cannot reach one at most \(x\), so both sides of \(p_xp_y=p_x\) are \(\dagger\). Otherwise, all states before its first entrance below \(y\) are greater than \(y\), hence greater than \(x\). The first entrance below \(x\), if one exists, is found by continuing from \(p_y(n)\). This proves the time identity and \(p_xp_y=p_x\), including the case where the continued search fails. The other composition identity holds because a successful value of \(p_x\) is already at most \(y\), and \(\dagger\) is fixed. Finally, iterating from the two points on the same trajectory proves the tail identity. ∎

Taking \(x=y\) shows that \(p_x\) is idempotent: applying it twice gives the same answer as applying it once. It is a retraction onto its image, not generally a one-to-one coordinate change.

## What the induced operator preserves and loses

For a summable signed mass function \(\lambda\) on \(\widehat D\), define

\[
K_x\lambda=(p_x)_*\lambda,
\qquad (K_x\lambda)(z)=\sum_{n:p_x(n)=z}\lambda(n).
\]

Proposition 1 of the sampling lesson proves that \(K_x\) preserves total mass and nonnegativity, and that \(\|K_x\lambda\|_1\leq\|\lambda\|_1\). Theorem 1 and composition of pushforwards give

\[
K_xK_y=K_x=K_yK_x\quad(x\leq y),\qquad K_x^2=K_x.
\]

The kernel consists exactly of the signed masses that sum to zero on every fibre of \(p_x\). This follows directly from the displayed definition. If two starts have the same landing point, the difference of their unit point masses lies in this kernel. The operator retains the distribution of landings, but not how mass was divided among starts with a common landing.

Conversely, any summable signed mass supported on \((D\cap[1,x])\cup\{\dagger\}\) is fixed by \(K_x\), since every point of that set is fixed. Every output is supported there. Thus this is exactly the image, and exactly the set of fixed vectors, of \(K_x\). For an initial probability \(\mu\) on \(D\),

\[
(K_x\mu)(\dagger)=\mu\{n:t_x(n)=\infty\}.
\]

No probability has been discarded by excluding unsuccessful trajectories.

## Adding errors over a finite chain

Let \(1\leq x_0\leq\cdots\leq x_J\). Suppose \(\nu_i\) is a probability law supported on \((D\cap[1,x_i])\cup\{\dagger\}\). Equivalently, \(K_{x_i}\nu_i=\nu_i\). Define

\[
e_i=\|\nu_i-K_{x_i}\nu_{i+1}\|_1\qquad(0\leq i<J).
\]

These errors compare two laws on the same target: the chosen law \(\nu_i\), and the law obtained by transporting the next one down to that target.

**Theorem 2 (Finite-chain transport).**

\[
\|\nu_0-K_{x_0}\nu_J\|_1\leq\sum_{i=0}^{J-1}e_i.
\]

In particular,

\[
(K_{x_0}\nu_J)(\dagger)
\leq\nu_0(\dagger)+\frac12\sum_{i=0}^{J-1}e_i.
\]

**Proof.** For \(J=0\), the first expression is zero because \(K_{x_0}\nu_0=\nu_0\). For \(J\geq1\), use the exact telescoping identity

\[
\nu_0-K_{x_0}\nu_J
=\sum_{i=0}^{J-1}K_{x_0}(\nu_i-K_{x_i}\nu_{i+1}).
\]

To verify it, replace each \(K_{x_0}K_{x_i}\) by \(K_{x_0}\), cancel consecutive terms, and use \(K_{x_0}\nu_0=\nu_0\). Contraction and the triangle inequality give the norm bound. The second bound is its consequence for the event \(\{\dagger\}\), using Lemma 2 of the sampling lesson. ∎

The number of steps matters only through the sum of the errors. Exact compatibility would make every \(e_i\) zero. Small errors that remain nonsummable can accumulate, whereas summable errors can control arbitrarily long chains.

## Geometrically separated logarithmic scales

We now specify a family of blocks rather than a single chain. Fix \(\alpha>1\). For a positive real \(s\), whenever \(D\cap[s,s^\alpha]\) is nonempty, let \(\mu_s\) be a probability supported there. Assume there is \(s_*\geq2\) such that these measures are defined for every real \(s\geq s_*\). No particular choice of weights within a block is assumed.

For \(s\geq s_*\), put

\[
\nu_s=K_s\mu_{s^\alpha},\qquad
d(s)=\nu_s(\dagger),\qquad
e(s)=\|\nu_s-K_s\nu_{s^\alpha}\|_1.
\]

Thus \(\nu_s\) is the first-passage law at threshold \(s\) for starts in the block \([s^\alpha,s^{\alpha^2}]\). The error \(e(s)\) compares it with passage from the next block, whose starts lie in \([s^{\alpha^2},s^{\alpha^3}]\). The intervening entrance is harmless because Theorem 1 composes nested passage maps exactly.

For \(R\geq s_*\), define the possibly infinite quantity

\[
\mathcal E(R)=\sup_{u\geq R}
\left(d(u)+\sum_{i=0}^{\infty}e(u^{\alpha^i})\right).
\]

The thresholds \(u,u^\alpha,u^{\alpha^2},\ldots\) have logarithms \(\log u,\alpha\log u,\alpha^2\log u,\ldots\). This geometric growth of the logarithms is what makes logarithmic error estimates summable.

For each \(n\in D\), define \(F_{\min}(n)=\min_{j\geq0}F^j(n)\). Well-ordering supplies the minimum even for an unbounded orbit. A family of these positive-integer-valued random variables is **uniformly tight** when, for each \(\varepsilon>0\), a finite \(K\) makes the probability of \(F_{\min}>K\) at most \(\varepsilon\) for every law in the family.

**Theorem 3 (Summable transport controls orbit minima).** For every \(K\geq s_*^{\alpha^3}\) and every defined block law \(\mu_s\),

\[
\mu_s\{n:F_{\min}(n)>K\}
\leq\mathcal E(K^{1/\alpha^3}).
\]

Consequently, if \(\mathcal E(R)\to0\) as \(R\to\infty\), the orbit-minimum laws under all the block measures are uniformly tight.

**Proof.** If \(s^\alpha\leq K\), every start in the block is already at most \(K\), and the left side is zero. Otherwise \(s>K^{1/\alpha}>1\). Choose the least integer \(J\geq1\) for which \(y=s^{\alpha^{-J}}<K^{1/\alpha}\). Such an integer exists because \(\alpha^{-J}\log s\to0\). Minimality gives

\[
K^{1/\alpha^2}\leq y<K^{1/\alpha}.
\]

Set \(u=y^{1/\alpha}\). Then

\[
u\geq K^{1/\alpha^3}\geq s_*,\qquad
u<K,\qquad u^{\alpha^J}=s^{1/\alpha}.
\]

Apply Theorem 2 to the thresholds \(x_i=u^{\alpha^i}\), \(0\leq i\leq J\), with laws \(\nu_{x_i}\). They are fixed by their own passage operators. At the last threshold,

\[
\nu_{x_J}=K_{s^{1/\alpha}}\mu_s,
\qquad
K_u\nu_{x_J}=K_u\mu_s.
\]

The second equality uses \(u\leq s^{1/\alpha}\) and nested passage. The failure bound in Theorem 2 therefore gives

\[
(K_u\mu_s)(\dagger)
\leq d(u)+\frac12\sum_{i=0}^{J-1}e(u^{\alpha^i})
\leq\mathcal E(K^{1/\alpha^3}).
\]

If an orbit has minimum greater than \(K\), then, since \(u<K\), it never enters below \(u\). Its start contributes to the failure event just bounded. This proves the theorem. The assertion about tightness is precisely the definition applied to a right-hand side tending to zero. ∎

The factors \(\alpha,\alpha^2,\alpha^3\) in this proof locate the original block, its lower comparison scale, and a threshold at which the failure probability is controlled. They are not interchangeable scale labels.

## Two explicit summable error estimates

Suppose the established error bounds for a particular map and choice of block laws are

\[
d(s)\leq Ds^{-b},\qquad e(s)\leq E(\log s)^{-c}
\quad(s\geq s_*),
\]

where \(D,E,b,c>0\) are fixed. Since \(\log(u^{\alpha^i})=\alpha^i\log u\), summing a geometric series yields

\[
\mathcal E(R)\leq DR^{-b}
+\frac{E}{1-\alpha^{-c}}(\log R)^{-c}.
\]

To verify the infinite geometric sum, its first \(J+1\) terms equal \((1-\alpha^{-c(J+1)})/(1-\alpha^{-c})\); the omitted power tends to zero. Substitution into Theorem 3 gives the fully explicit bound

\[
\mu_s\{F_{\min}>K\}
\leq D K^{-b/\alpha^3}
+\frac{E\alpha^{3c}}{1-\alpha^{-c}}(\log K)^{-c}.
\]

A slower error can also be summable. If \(e(s)\leq E(\log\log s)^{-1-c}\) beyond a fixed threshold, let \(v=\log\log R>0\) and \(h=\log\alpha>0\). The decreasing function \((v+ht)^{-1-c}\) gives

\[
\sum_{i=0}^{\infty}(v+ih)^{-1-c}
\leq v^{-1-c}+\int_0^\infty(v+ht)^{-1-c}\,dt
=v^{-1-c}+\frac{v^{-c}}{ch}.
\]

The inequality follows by comparing the \(i\)-th term, for \(i\geq1\), with the integral on \([i-1,i]\); the integral is evaluated by the substitution \(z=v+ht\). Together with a failure bound tending uniformly to zero on tails, this again proves tightness. Tao notes this slower sufficient error regime after his first-passage proposition.

## The role of the Collatz application

For the Syracuse map, take \(D=\mathcal O\) and \(F(m)=(3m+1)/2^{\nu_2(3m+1)}\). Logarithmic block laws assign an odd \(m\in[s,s^\alpha]\) weight proportional to \(1/m\). The constructions in this lesson then apply literally: \(p_x\) is its first odd iterate at most \(x\), and \(K_x\) transports the chosen starting distribution to that landing distribution.

The algebra of nested passage and the transport theorem are now available. Applying the quantitative conclusion requires estimates for the actual \(d(s)\) and \(e(s)\) of these laws. In Tao's argument, this is where mixing, finite-group Fourier analysis and renewal estimates enter. Those are substantial further arguments; the general transport theorem does not supply their bounds. Conversely, once suitable bounds are proved, the deduction from them to tight orbit minima is the complete argument above, not a separate appeal to the conjecture.

The clock and sampling lessons identify how to transfer the resulting orbit-minimum events back to ordinary positive-integer iteration with the corresponding logarithmic weights. A time bound needs additional clock estimates, because a small landing value alone gives no upper bound for the number of elapsed ordinary steps.

## Exercises with solutions

**Exercise 1.** In the six-state example, start with the uniform law. Compute \(K_2\mu\), including the failure mass, and verify \(K_2K_4\mu=K_2\mu\).

**Solution.** The masses are \(1/6\) at 1, \(3/6\) at 2, and \(2/6\) at \(\dagger\). At threshold 4, the law has mass \(1/6\) at each of 1, 2, 3 and 4, and \(2/6\) at \(\dagger\). Applying \(K_2\) sends 3 and 4 to 2 and fixes the other outputs, giving exactly the same law.

**Exercise 2.** For any summable signed mass \(\lambda\), prove that

\[
\lambda=K_x\lambda+(\lambda-K_x\lambda)
\]

is a unique decomposition into a fixed vector of \(K_x\) and a vector in its kernel.

**Solution.** Idempotence gives \(K_x(K_x\lambda)=K_x\lambda\) and \(K_x(\lambda-K_x\lambda)=0\). If a vector is both fixed and in the kernel, it equals zero. Subtracting two decompositions therefore proves uniqueness. This describes precisely which part of a signed distribution survives passage and which part is cancelled within fibres.

**Exercise 3.** In the first explicit error regime, take \(\alpha=2\), \(D=E=b=c=1\). State the bound for orbit minima, including its range of validity.

**Solution.** If the stated input estimates hold for every \(s\geq s_*\), then for every \(K\geq s_*^8\) and every defined block law,

\[
\mu_s\{F_{\min}>K\}\leq K^{-1/8}+\frac{16}{\log K}.
\]

The coefficient is \(2^3/(1-1/2)=16\). Probabilities are also at most 1, so the smaller of 1 and this expression is a valid bound. This numerical exercise does not assert that these input constants hold for the Syracuse map.

**Exercise 4.** Does \(e(s)\leq E/(\log\log s)\), by itself, provide a finite sum of the displayed upper bounds along the scales \(u^{\alpha^i}\)?

**Solution.** No. The upper bounds form \(E\sum_i(v+ih)^{-1}\), where \(v=\log\log u>0\) and \(h=\log\alpha>0\). For sufficiently large \(i\), \(v+ih\leq2hi\), so this series is bounded below by a positive multiple of \(\sum_i1/i\), which diverges. The harmonic series diverges because the terms from \(2^j\) through \(2^{j+1}-1\) sum to at least \(1/2\) for each \(j\). This proves only that the proposed upper bound is not summable. The actual errors might still be much smaller; no failure of tightness has been proved.

## What carries forward

The four lessons have connected several different kinds of information. Return clocks specify how much time a shorter orbit record omits. Symbolic words give exact affine blocks and their arithmetic domains. Pushforward measures determine how mass moves when starts are identified. First-passage operators then compose these distributional comparisons across scales.

Each construction can be studied for other systems with its hypotheses stated explicitly. The Collatz example keeps their interaction concrete: an orbit identity, a congruence count and a probability estimate each do a different part of the work. Further study can now focus on proving mixing or renewal estimates, with a precise understanding of what those estimates must control and how their conclusions will be used.

## References

Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, [arXiv:1909.03562v7](https://arxiv.org/abs/1909.03562v7), §§1.3 and 3. First-passage stabilization and its use in controlling orbit minima; the discussion following Proposition 1.11 also treats the slower summable error regime.

The preceding lessons, [Return maps and exact changes of clock](NT-COLLATZ-01.md) and [Pushforward measures and logarithmic sampling](NT-COLLATZ-03.md), provide the elementary orbit and measure arguments used here, including the exact probability-distance convention.
