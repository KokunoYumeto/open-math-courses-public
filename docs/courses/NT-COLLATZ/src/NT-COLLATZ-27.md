# Integer thresholds and weighted phase averages

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, proofs and exercises: CC0 1.0.*

An interval can change its integer population even when its endpoints move by an arbitrarily small amount. When the integers also carry unequal probabilities, there are two effects to understand: which integers are admitted, and how much mass they carry. This lesson develops a finite comparison that keeps both effects visible. It then shows how information about the distribution of fractional parts controls the resulting weighted averages.

The application comes from the logarithmic bands in Lech Mazur's *Natural-Density Almost-Bounded Collatz Orbits in Logarithmic Time*. A band contains one integer level and, for certain fractional phases, its successor. The two levels carry neighboring negative-binomial probabilities, not identical weights. We will compare those weights by an exact ratio, count the few terms that enter or leave at the boundary, and prove two ways of averaging the pair. These are reusable methods for lattice probabilities and moving cutoffs. The final section explains how to turn an error proportional to a comparison measure into an error proportional to the actual measure.

Basic references are Mazur's Appendix C and accompanying two-profile comparison, Tao's *Almost all orbits of the Collatz map attain almost bounded values* for the valuation-word model, and Kuipers and Niederreiter's *Uniform Distribution of Sequences* for discrepancy and weighted averaging. Prerequisites are [geometric waiting times](NT-COLLATZ-06.md#counting-waiting-time-words), [weighted rotation averages](NT-COLLATZ-20.md#summation-by-parts-retains-the-actual-weights), and [exact inverse branches and their sampling weights](NT-COLLATZ-26.md#backwards-decoding-proves-positivity-as-well-as-integrality). The finite estimates below are proved in full.

## The first integer strictly above a real number

Write \(\ell=\log 2\). Fix a logarithmic width \(\beta\) with
\[
\ell<\beta<2\ell,\qquad b=\beta/\ell,\qquad \theta=2-b\in(0,1).
\tag{1}
\]
For a real number \(s\), put \(x=\{s\}=s-\lfloor s\rfloor\) and \(L=\lfloor s\rfloor+1\). The integers in the strict interval \((s,s+b)\) are exactly
\[
L,\qquad\text{and also }L+1\text{ precisely when }x>\theta.
\tag{2}
\]
Indeed, every integer strictly above \(s\) is \(L+r\), \(r\geq0\). Its distance from \(s\) is \(1+r-x\). The first distance lies in \((0,1]\), hence below \(b\). The second is below \(b\) exactly when \(x>2-b\). Every later distance exceeds two. This also gives the inverse reindexing \(r=k-\lfloor s\rfloor-1\) for an admitted integer \(k\).

There are two important endpoint cases. If \(s\) is an integer, the first level is \(s+1\), not \(\lceil s\rceil=s\). If \(x=\theta\), the successor lies exactly on the upper endpoint and is excluded. Neither convention is negligible when an individual phase has positive weight.

![Three strict intervals of length three halves in integer-level coordinates. Their lower endpoints have fractional parts one quarter, one half and three quarters. The first two admit only the first integer; the third admits its successor too. At phase one half the successor is the excluded upper endpoint.](../figures/strict-phase.svg)

*For \(b=3/2\), the threshold is \(\theta=1/2\). Solid circles are admitted levels; open circles are excluded endpoints. A level's inclusion is decided before its probability weight is applied.*

## From a sampling band to two probability profiles

For \(\nu\geq1\) independent positive geometric variables with probabilities \(\mathbb P(a_i=k)=2^{-k}\), the total has law
\[
p_\nu(k)=
\begin{cases}\displaystyle\binom{k-1}{\nu-1}2^{-k},&k\geq\nu,\\0,&k<\nu.
\end{cases}
\tag{3}
\]
There are \(\binom{k-1}{\nu-1}\) positive compositions of \(k\): choose the \(\nu-1\) separators between \(k\) consecutive marks. Each word has probability \(2^{-k}\). This proves (3), including its zero extension to signed integer levels. Summing over all words proves that \(\sum_kp_\nu(k)=1\).

For a positive odd endpoint \(M\), the multiplicative part of the affine inverse is
\[
N_0=\frac{2^kM}{3^\nu}.
\]
It lies in the strict band \((z,z e^\beta)\) exactly when
\[
0<(k-s_\nu)\ell<\beta,\qquad
s_\nu=A+\nu\lambda,\quad A=\frac{\log(z/M)}\ell,\quad
\lambda=\frac{\log3}\ell.
\tag{4}
\]
Thus (2) applies, with \(x_\nu=\{s_\nu\}\) and \(L_\nu=\lfloor s_\nu\rfloor+1\).

Choose any finite set \(I\) of positive integer times and any \(W>0\). Define two nonnegative weights at the **same** time \(\nu\):
\[
q_{0,\nu}=p_\nu(L_\nu)\mathbf1_{|L_\nu-2\nu|<W},\qquad
q_{1,\nu}=p_\nu(L_\nu+1)\mathbf1_{|L_\nu+1-2\nu|<W}.
\tag{5}
\]
Here the tube around \(2\nu\) retains totals near the mean of the geometric sum. The two masses
\[
Z_0=\sum_{\nu\in I}q_{0,\nu},\qquad Z_1=\sum_{\nu\in I}q_{1,\nu}
\tag{6}
\]
need not be equal or equal to one. Replacing \(A\) by \(A+1\) increases the integer level by one but leaves its fractional part unchanged. It does not shift the time index.

Put \(\chi(x)=\mathbf1_{x>\theta}\). The two sums to be averaged are
\[
\mathcal H=\sum_{\nu\in I}(q_{0,\nu}+q_{1,\nu}\chi(x_\nu)),
\tag{7}
\]
\[
\mathcal F=\sum_{\nu\in I}
\left(q_{0,\nu}2^{1-x_\nu}
+q_{1,\nu}2^{2-x_\nu}\chi(x_\nu)\right).
\tag{8}
\]
The letters distinguish reciprocal and uniform-counting profiles. To see the difference, suppose a sampling set of odd integers has size \(D\) and harmonic sum \(H\). Let \(\rho_{\nu,k}(M)\) be the fraction of length-\(\nu\), total-\(k\) words satisfying the exact affine endpoint congruence. For that cell, the sum of the reciprocal nominal weights is exactly
\[
\frac{3^\nu}{MH}p_\nu(k)\rho_{\nu,k}(M).
\tag{9}
\]
The sum of the uniform nominal weights is exactly
\[
\frac{3^\nu z}{MD}p_\nu(k)\rho_{\nu,k}(M)
e^{(k-s_\nu)\ell}.
\tag{10}
\]
Both identities follow by multiplying the number of compatible words by the corresponding single-word weight, \(1/(HN_0)\) or \(1/D\). In (10), \(z e^{(k-s_\nu)\ell}=N_0\), so the exponential cancels the reciprocal factor once. Equations (7) and (8) are the geometric profiles remaining when a separate arithmetic mixing argument supplies a common endpoint factor. Until that argument is supplied, (9) and (10) retain \(\rho_{\nu,k}(M)\) explicitly. Replacing the true affine source by \(N_0\) also has the separate weight and boundary costs proved in the preceding lesson. These identities do not assume independent geometric valuations along every integer orbit.

## An exact ratio and a point-probability bound

**Lemma 1.** For \(\nu\geq1\) and integer \(k\geq\nu\),
\[
\frac{p_\nu(k+1)}{p_\nu(k)}=\frac{k}{2(k-\nu+1)},\qquad
p_\nu(k)\leq\frac1{2\sqrt{3\nu-2}}\leq\frac1{2\sqrt\nu}.
\tag{11}
\]

**Proof.** Cancellation of factorials in (3) gives the ratio. It is greater than one for \(k<2\nu-2\), equal to one for \(k=2\nu-2\), and less than one thereafter. For \(\nu\geq2\), the maximum is therefore attained at \(2\nu-2\) and \(2\nu-1\), and equals
\[
\frac12\frac{\binom{2\nu-2}{\nu-1}}{4^{\nu-1}}.
\]
For \(\nu=1\), the maximum is \(p_1(1)=1/2\).

Set \(c_m=\binom{2m}{m}/4^m\). We prove \(c_m\leq(3m+1)^{-1/2}\) by induction. The case \(m=0\) is equality. Also
\[
\frac{c_{m+1}}{c_m}=\frac{2m+1}{2m+2},\qquad
(2m+2)^2(3m+1)-(2m+1)^2(3m+4)=m\geq0.
\]
All factors are positive, so squaring shows that the ratio is at most \(\sqrt{(3m+1)/(3m+4)}\). Induction proves the claim. Substitute \(m=\nu-1\); the last inequality in (11) follows from \(3\nu-2\geq\nu\). ∎

The two equal maxima are a useful reminder that a one-level shift need not strictly decrease a probability. For example, \(p_3(4)=p_3(5)=3/16\), whereas \(p_3(7)/p_3(6)=3/4\).

## Only a few terms cross a tube boundary

The next result isolates the comparison needed in (7) and (8). It is stated for an arbitrary slope \(\lambda\in(1,2)\), not only the logarithmic slope in (4). Set \(\Delta=2-\lambda\in(0,1)\). Assume every \(\nu\in I\) is at least an integer \(n\geq1\), and
\[
1\leq W\leq n/8.
\tag{12}
\]
Define \(L_\nu,q_{r,\nu},Z_r\) as before, with this slope, and put
\[
\mathcal D=\sum_{\nu\in I}|q_{1,\nu}-q_{0,\nu}|,
\qquad K=\lceil1/\Delta\rceil.
\]

**Theorem 2 (Neighboring profiles).** With these definitions,
\[
\mathcal D\leq
\frac{W+2}{2(n-W+1)}Z_0+
\frac{K}{\sqrt{3n-2}}
\leq\frac{2W}{n}Z_0+\frac{K}{\sqrt{3n-2}}.
\tag{13}
\]
In particular \(|Z_1-Z_0|\leq\mathcal D\). For \(\lambda=\log_2 3\), one has \(K=3\).

**Proof.** Write \(d_\nu=L_\nu-2\nu\). Since \(2\nu\) is integral,
\[
d_\nu=\lfloor A-\Delta\nu\rfloor+1.
\tag{14}
\]
On the common support of the two tube indicators, \(|d_\nu|<W\), and \(L_\nu\geq\nu\) by (12). The exact ratio in Lemma 1 gives
\[
\left|\frac{p_\nu(L_\nu+1)}{p_\nu(L_\nu)}-1\right|
=\frac{|d_\nu+2|}{2(\nu+d_\nu+1)}
\leq\frac{W+2}{2(n-W+1)}.
\tag{15}
\]
Its denominator is positive. Multiplying by \(q_{0,\nu}\) and summing pays at most the first term in (13).

It remains to count the times on just one support. Put \(R=\lceil W\rceil-1\). For an integer \(d\), \(|d|<W\) is equivalent to \(-R\leq d\leq R\). The base and shifted conditions on \(d_\nu\) are therefore
\[
-R\leq d_\nu\leq R,\qquad -R-1\leq d_\nu\leq R-1.
\tag{16}
\]
A lost term has \(d_\nu=R\); a gained term has \(d_\nu=-R-1\). For any fixed integer \(d\), (14) is equivalent to
\[
\frac{A-d}{\Delta}<\nu\leq\frac{A-d+1}{\Delta}.
\tag{17}
\]
This half-open interval has length \(1/\Delta\) and contains at most \(K\) integers. Indeed, if its integer points are \(v_1<\cdots<v_j\), then \(j-1\leq v_j-v_1<1/\Delta\), implying \(j\leq\lceil1/\Delta\rceil\). Restriction to the original finite set \(I\) only reduces this count.

There are consequently at most \(2K\) unmatched terms, each at most \(1/(2\sqrt{3n-2})\) by Lemma 1. Adding them proves the first inequality in (13). For the second, use \(W+2\leq3W\) and \(n-W+1\geq7n/8\) to obtain a coefficient at most \(12W/(7n)\leq2W/n\).

Finally \(9>8\) gives \(\lambda>3/2\), while \(27<32\) gives \(\lambda<5/3\). Hence \(1/3<\Delta<1/2\), so \(2<1/\Delta<3\) and \(K=3\). The mass difference is bounded by the triangle inequality. ∎

This proof exhibits the two costs separately. Interior terms change by a relative amount charged to \(Z_0\); at most six terms cross the boundary for the Collatz slope. The theorem applies on the actual finite time set \(I\), even if it is not an interval. It does not require extending a physical time window to a larger analytic one.

## Averaging while retaining both masses

We first give a theorem for arbitrary nonnegative weights \(q_{0,\nu},q_{1,\nu}\) on any finite set of phases \(x_\nu\in[0,1)\). They need not arise from (5). For \(r=0,1\), define the error in weighted interval counts by
\[
E_r=\sup_{0\leq t\leq1}
\left|\sum_\nu q_{r,\nu}\mathbf1_{x_\nu\leq t}-Z_rt\right|.
\tag{18}
\]
This is in mass units. It remains defined when \(Z_r=0\), and includes a possible atom at zero. The closed endpoint is intentional: subtraction from the total mass gives exactly
\[
\left|\sum_\nu q_{r,\nu}\mathbf1_{x_\nu>t}-Z_r(1-t)\right|\leq E_r.
\tag{19}
\]

**Theorem 3 (Two-mass averaging).** For (7) and (8),
\[
|\mathcal H-Z_0-(b-1)Z_1|\leq E_1,
\tag{20}
\]
\[
\left|\mathcal F-\frac{Z_0+(e^\beta-2)Z_1}{\ell}\right|
\leq E_0+(2e^\beta-2)E_1.
\tag{21}
\]

**Proof.** The integral of \(\chi\) on \([0,1]\) is \(1-\theta=b-1\). Apply (19) at \(\theta\) to prove (20). For the exponential terms set
\[
g_0(x)=2^{1-x},\qquad g_1(x)=2^{2-x}\mathbf1_{x>\theta}.
\]
The following identities retain the value at the strict jump:
\[
g_0(x)=2-\int_0^1\ell 2^{1-t}\mathbf1_{x>t}\,dt,
\tag{22}
\]
\[
g_1(x)=e^\beta\mathbf1_{x>\theta}
-\int_\theta^1\ell 2^{2-t}\mathbf1_{x>t}\,dt.
\tag{23}
\]
For (22), integrate up to \(x\). For (23), both sides vanish at and below \(\theta\); above it, integrate from \(\theta\) to \(x\), using \(2^{2-\theta}=e^\beta\).

Subtract each uniform integral, multiplied by the corresponding mass, from the weighted sum of (22) or (23). Finite summation commutes with integration. Equation (19) then bounds the first error by
\(E_0\int_0^1\ell2^{1-t}dt=E_0\), and the second by
\(E_1[e^\beta+\int_\theta^1\ell2^{2-t}dt]=(2e^\beta-2)E_1\).
The two means are
\[
\int_0^1g_0(x)\,dx=\frac1\ell,\qquad
\int_0^1g_1(x)\,dx=\frac{e^\beta-2}\ell.
\tag{24}
\]
Adding the estimates proves (21). ∎

No equality of \(Z_0\) and \(Z_1\) was used. Their separate means are sometimes the most useful answer, particularly when both weighted distributions are already understood.

## When one averaged profile is enough

If only the base profile is understood, Theorem 2 supplies a different route. Define \(\mathcal D=\sum|q_{1,\nu}-q_{0,\nu}|\) for the arbitrary finite weights of the preceding section.

**Corollary 4 (Base profile plus a controlled difference).**
\[
|\mathcal H-bZ_0|\leq E_0+\mathcal D,
\tag{25}
\]
\[
\left|\mathcal F-\frac{e^\beta-1}{\ell}Z_0\right|
\leq(2e^\beta-1)E_0+e^\beta\mathcal D.
\tag{26}
\]

**Proof.** The exact decompositions are
\[
\mathcal H=\sum q_{0,\nu}(1+\chi(x_\nu))
+\sum(q_{1,\nu}-q_{0,\nu})\chi(x_\nu),
\]
\[
\mathcal F=\sum q_{0,\nu}(g_0+g_1)(x_\nu)
+\sum(q_{1,\nu}-q_{0,\nu})g_1(x_\nu).
\]
Apply Theorem 3 with the same base weights in both positions to the first sums. Their means are \(bZ_0\) and \((e^\beta-1)Z_0/\ell\). The other sums have absolute values at most \(\mathcal D\) and \(e^\beta\mathcal D\), because \(0\leq\chi\leq1\) and \(0\leq g_1\leq e^\beta\). This proves both claims. ∎

Combining (13) with (25) and (26) gives an explicit finite comparison of the actual two geometric profiles. This is the neighboring-profile mechanism in Mazur's reciprocal and uniform comparisons. It does not assert that the two masses are equal: it proves the price of replacing one profile by the other. The preceding two-mass theorem remains available when that replacement is less useful.

Here is how to supply \(E_0\) from rotation estimates. On an integer interval \(m\leq\nu\leq N\), extend the chosen nonnegative weights by zero at unused indices, and write them as \(w_\nu\). Suppose the unweighted prefix discrepancies satisfy
\[
\left|C_j(t)\right|\leq B,\qquad
C_j(t)=\sum_{\nu=m}^j(\mathbf1_{x_\nu\leq t}-t),
\quad m\leq j\leq N,\quad0\leq t\leq1.
\]
Finite summation by parts gives, exactly,
\[
\sum_{\nu=m}^Nw_\nu(\mathbf1_{x_\nu\leq t}-t)
=w_NC_N(t)+\sum_{j=m}^{N-1}(w_j-w_{j+1})C_j(t).
\]
Thus
\[
E_0\leq B\left(w_N+\sum_{j=m}^{N-1}|w_j-w_{j+1}|\right).
\tag{27}
\]
The identity follows by substituting \(C_j-C_{j-1}\) for each summand, with \(C_{m-1}=0\), and collecting coefficients. Taking absolute values proves (27). The rational-grid and arithmetic estimates in [the rotation lesson](NT-COLLATZ-20.md#choosing-blocks-by-the-pigeonhole-principle) provide such prefix bounds. Closed-interval counts follow from their half-open counterparts by letting the upper endpoint decrease to the desired endpoint from above; for a finite sample the point count stabilizes and the interval length converges. Consequently the same bound retains equality cases at a jump. Controlling the variation of the particular weights remains a genuine mathematical input, not a consequence of equidistribution alone.

## Absorbing an error against the actual mass

A comparison often first yields a term proportional to the reference mass. That estimate is useful only if it can be combined with the mass one actually knows. The following elementary lemma makes the conversion exact.

**Theorem 5 (Proportional error).** For a finite index set let \(Y_i,R_i,e_i\geq0\) and \(0\leq a_i\leq a<1\). If
\[
|Y_i-R_i|\leq e_i+a_iR_i\quad\text{for every }i,
\]
then
\[
\sum_i|Y_i-R_i|
\leq\sum_i\frac{e_i+a_iY_i}{1-a_i}
\leq\frac{\sum_i e_i+a\sum_iY_i}{1-a}.
\tag{28}
\]
The last coefficients are sharp under these hypotheses.

**Proof.** Put \(d_i=|Y_i-R_i|\). Since \(R_i\leq Y_i+d_i\), the hypothesis gives
\((1-a_i)d_i\leq e_i+a_iY_i\). Division and summation prove the first inequality. Nonnegativity and \(a_i\leq a<1\) give the second. For one index choose any \(Y,e\geq0\) and \(R=(Y+e)/(1-a)\), with \(a_i=a\). Then \(R\geq Y\) and \(R-Y=e+aR\); equality holds throughout. Taking \(e=0\) or \(Y=0\) proves that neither coefficient can be reduced. ∎

The bound also controls \(|\sum_i h_i(Y_i-R_i)|\) for arbitrary complex \(|h_i|\leq1\), by the triangle inequality. In particular it controls every subcollection, not only the total sum. If \(e_i=q_i\varepsilon\) with \(q_i\geq0\) and \(\sum_iq_i\leq1\), while \(\sum_iY_i\leq1\), the final error is at most
\[
\frac{\varepsilon+a}{1-a}.
\tag{29}
\]
It is not multiplied by the number of indices. In a family indexed by both time and total, the geometric probabilities sum to at most one **at each fixed time**. Summing over \(J\) times may therefore cost \(\#J\,\varepsilon\); it does not cost the number of all time-total cells. A separate disjointness argument is needed if the actual \(Y_i\) are to have total mass at most one. These are precisely the roles of the exact probability formula (3) and the terminal injectivity proved in the preceding lesson.

Together, the comparisons separate integer geometry, probability mass, phase averaging and proportional error. This separation makes them composable: the exact endpoint convention survives the arithmetic reindexing; the neighboring-profile estimate pays for a legitimate change of weights; discrepancy controls the remaining average; and absorption charges the resulting error to the measured event. Each step is useful independently of a final orbit theorem.

## Exercises with solutions

### 1. A strict endpoint is not a rounding convention

Take \(b=3/2\). List the integers in \((s,s+b)\) for \(s=-2,-7/4,-3/2,-5/4\). For any real \(T\geq3\), show that \(T/\lfloor T\rfloor\) lies in \([1,4/3)\). Explain why this last fact alone does not specify a dyadic band width.

**Solution.** The four intervals admit respectively \(\{-1\},\{-1\},\{-1\},\{-1,0\}\). The phases are \(0,1/4,1/2,3/4\). At phase \(1/2\), zero is the excluded upper endpoint; at integral phase the first level is still \(\lfloor s\rfloor+1\). Writing \(k=\lfloor T\rfloor\geq3\) gives \(1\leq T/k<1+1/k\leq4/3\). This ratio is a width in the coordinate in which \(T\) was measured. A logarithmic width \(\beta\) becomes \(b=\beta/\log2\) in dyadic level coordinates; the division by \(\log2\) must be retained.

### 2. A shift has two boundary fibres

Let \(\Delta=2/5\), \(A=20\), \(W=2\), and \(I=\{40,41,\ldots,65\}\). Find the base and shifted supports of (5). Verify the number of lost and gained terms, and bound \(\mathcal D\) in terms of \(Z_0\).

**Solution.** Here \(d_\nu=\lfloor20-2\nu/5\rfloor+1\). The base tube requires \(d_\nu\in\{-1,0,1\}\), hence \(95/2<\nu\leq55\): its support is \(\{48,\ldots,55\}\). The shifted tube requires \(d_\nu\in\{-2,-1,0\}\), hence \(50<\nu\leq115/2\): its support is \(\{51,\ldots,57\}\). The lost terms are \(48,49,50\), the gained ones \(56,57\). All weights vanish below \(48\), so apply Theorem 2 on \(I\cap[48,\infty)\) with \(n=48\) and \(K=3\). It gives
\[
\mathcal D\leq\frac2{47}Z_0+\frac3{\sqrt{142}}.
\]
Using the actual five boundary terms in its proof improves the last numerator to \(5/2\). Both bounds keep the unaltered base mass \(Z_0\).

### 3. The two masses really can differ

For \(b=3/2\), take phases \(x=(0,1/2,3/4)\) and weights \(q_0=(1/4,1/4,0)\), \(q_1=(0,1/8,3/8)\). Compute \(\mathcal H,\mathcal F,Z_0,Z_1,\mathcal D\). Then add a weight \(1/8\) to the first component of \(q_1\), and determine which of these quantities change.

**Solution.** Initially \(Z_0=Z_1=1/2\),
\[
\mathcal H=\frac78,\qquad
\mathcal F=\frac12+\frac{\sqrt2}{4}+\frac38\,2^{5/4},
\qquad \mathcal D=\frac34.
\]
Only the third successor is admitted. In particular the weight at \(x=1/2=\theta\) contributes nothing to the successor term. Adding \(1/8\) at phase zero changes \(Z_1\) to \(5/8\) and \(\mathcal D\) to \(5/8\), while \(Z_0,\mathcal H,\mathcal F\) remain unchanged. The two-mass average and its discrepancy bound must account for that change; the exact sums are controlled by the actual locations of the weights, not their totals alone.

### 4. Why summing the error first matters

Let \(q_1=1/3,q_2=2/3\), \(a=1/4\), and \(\varepsilon=1/10\). Set \(Y_i=q_i\), \(e_i=\varepsilon q_i\), \(R_i=(Y_i+e_i)/(1-a)\). Compute the total comparison error. What changes if either index is split into a hundred identical smaller cells?

**Solution.** We have \(R_i=22q_i/15\), hence \(|Y_i-R_i|=7q_i/15\). Also
\(e_i+aR_i=q_i/10+11q_i/30=7q_i/15\), so the premise and conclusion of Theorem 5 are equalities. The total error is \(7/15=(1/10+1/4)/(3/4)\). Splitting a cell divides all its masses and errors into a hundred parts; their sum and the exact bound remain unchanged. A bound proportional to the number of cells would change under this irrelevant refinement of the description.

## References

- Lech Mazur, [*Natural-Density Almost-Bounded Collatz Orbits in Logarithmic Time*](https://www.proofatlas.ai/formalizations/natural-density-log-time-collatz/), version 2, 21 July 2026, Appendix C. The accompanying mathematical source supplies the strict two-level decomposition, the neighboring-profile comparison and the reciprocal and uniform profile applications. The finite estimates and proof presentation here retain the original masses and also give the explicit ratio and central-binomial constants in (11)–(13).
- Terence Tao, [*Almost all orbits of the Collatz map attain almost bounded values*](https://arxiv.org/abs/1909.03562v7), Sections 4 and 5. Valuation words, their geometric model, exact affine coordinates and harmonic passage weights.
- L. Kuipers and H. Niederreiter, *Uniform Distribution of Sequences*, Wiley, 1974, Chapter 2. Discrepancy and integration of functions of bounded variation; the necessary weighted identities are proved here and in the linked rotation lesson.

The [reproducible checks](../build/check_strict_profiles.py) test strict endpoints, binomial identities, support fibres, weighted finite sums and proportional-error equalities. Numerical exponential averages are recorded separately from exact rational checks; neither replaces the general proofs.
