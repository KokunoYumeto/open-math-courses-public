# Compatible entrance laws and weighted orbit minima

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, proofs and exercises: CC0 1.0.*

A small error at one scale does not automatically remain small through arbitrarily many scales. The useful distinction is between an error that is merely small and a family of errors whose sum is finite. When the errors are summable, approximate agreement can produce an exactly compatible limiting family of probability laws.

We develop that principle for first entrance into nested targets. The same sequence of starting distributions will supply a limit at every threshold. Observing several thresholds together costs no more than observing the largest one, because the smaller entrance locations are determined by the largest. A second application controls orbit minima under logarithmic sampling. It yields Tao's fixed-threshold estimate and his theorem for every prescribed bound tending to infinity, including bounds that increase arbitrarily slowly or are not monotone.

The general mathematical subjects are probability transport, compatible distributions, tightness, and weighted counting. Collatz supplies the concrete system for which the preceding lessons have proved the analytic estimates. The prerequisites are [pushforward contraction and harmonic weights](NT-COLLATZ-03.md), [nested first passage and summable transport](NT-COLLATZ-04.md), and [logarithmic first-passage stabilization](NT-COLLATZ-13.md#the-entrance-law-and-the-sampling-experiment). We also use [the exact equality of orbit minima under changes of clock](NT-COLLATZ-01.md#the-least-value-attained-does-not-depend-on-the-clock). The main research reference is Tao's *Almost all orbits of the Collatz map attain almost bounded values*, Remark 1.4 and Section 3. The compatible-family and joint-entrance statements are derived below from the first-passage estimate. All further proofs are supplied here.

## Tightness under weighted counting

Let \(D\subseteq\mathbb N_+\) be infinite. Assign each \(n\in D\) a positive real weight \(w(n)\), and suppose

\[
W(X)=\sum_{\substack{n\in D\\n\leq X}}w(n)\longrightarrow\infty.
\]

For a nonempty prefix, let \(\rho_X(n)=w(n)/W(X)\) on \(D\cap[1,X]\), and zero elsewhere. Take a finite-valued function \(g:D\to[0,\infty)\). It need not be bounded as a function of \(n\). Its distributions under the different \(\rho_X\) are **uniformly tight** if

\[
\lim_{K\to\infty}\sup_X\rho_X(g>K)=0.
\tag{1}
\]

Thus one finite interval contains almost all the probability, uniformly over all the input cutoffs. The supremum is over nonempty prefixes.

**Theorem 1 (A weighted tightness criterion).** The following three statements are equivalent:

1. For every real-valued function \(f:D\to\mathbb R\) with \(f(n)\to\infty\), one has \(\rho_X(g\geq f)\to0\) as \(X\to\infty\).
2. \(\lim_{K\to\infty}\limsup_{X\to\infty}\rho_X(g>K)=0\).
3. The family is uniformly tight, as in (1).

The limit of \(f\) is taken along \(D\). Its speed of growth and its monotonicity play no role.

**Proof.** First assume statement 2. Fix a finite \(K\). Since \(f(n)\to\infty\), choose \(Y_K\) such that \(f(n)>K\) for \(n>Y_K\). Then

\[
\{g\geq f\}\subseteq(D\cap[1,Y_K])\cup\{g>K\}.
\]

The first set has probability at most \(W(Y_K)/W(X)\), tending to zero. Taking the limsup as \(X\to\infty\) at this fixed \(K\), and then letting \(K\to\infty\), proves statement 1.

For the converse, suppose statement 2 fails. Because its inner limsup decreases as \(K\) increases, there is an \(\varepsilon>0\) such that, for every integer \(j\geq1\), arbitrarily large integer cutoffs satisfy \(\rho_X(g>j)\geq\varepsilon\). Start with an integer \(X_0\geq\min D\). Choose recursively \(X_j>X_{j-1}\) with that property and with

\[
\frac{W(X_{j-1})}{W(X_j)}\leq\frac\varepsilon2.
\tag{2}
\]

Such a choice is possible because the suitable cutoffs are unbounded and \(W(X)\to\infty\). Define \(f(n)=j\) for \(X_{j-1}<n\leq X_j\), and choose any finite value on the initial prefix. The strictly increasing integer sequence \(X_j\) tends to infinity, so this defines \(f\) on all of \(D\) and gives \(f(n)\to\infty\). At cutoff \(X_j\), remove the earlier prefix from the event \(\{g>j\}\). By (2), probability at least \(\varepsilon/2\) remains. On it, \(g>j=f\), contradicting statement 1.

Next assume statement 2 and fix \(\varepsilon>0\). Choose \(K_0\) such that the limsup in that statement is less than \(\varepsilon/2\). There is \(X_0\) after which all the probabilities \(\rho_X(g>K_0)\) are at most \(\varepsilon\). Increase \(K_0\) to exceed the finitely many values of \(g\) on \(D\cap[1,X_0]\). Every earlier tail is now empty, and increasing the threshold cannot enlarge a later tail. This proves statement 3. Finally, statement 3 implies statement 2 because a limsup is bounded by the corresponding supremum. ∎

The finite-valued hypothesis is used when the initial prefix is removed. The divergence of \(W\) ensures that a fixed prefix becomes negligible. The theorem is independent of any dynamical interpretation of \(g\).

## First-passage operators at nested thresholds

Return to the odd-return map \(S\) on \(\mathbb O=\{1,3,5,\ldots\}\). Let \(p_x\) record its first entrance at most \(x\), with failure recorded by \(\dagger\), as in the preceding lesson. Extend \(p_x(\dagger)=\dagger\), and write

\[
E_x=(\mathbb O\cap[1,x])\cup\{\dagger\},
\qquad K_x\lambda=(p_x)_*\lambda.
\tag{3}
\]

The operator acts on summable signed mass functions on \(\mathbb O\cup\{\dagger\}\). The [nested-passage theorem and operator description](NT-COLLATZ-04.md#nested-targets-compose-exactly) prove

\[
\begin{gathered}
p_xp_y=p_x=p_yp_x\quad(x\leq y),\\
K_xK_y=K_x=K_yK_x,\qquad
\|K_x\lambda\|_1\leq\|\lambda\|_1.
\end{gathered}
\tag{4}
\]

The norm is the unhalved sum of absolute masses. The image of \(K_x\) consists exactly of the signed laws supported on \(E_x\); these laws are fixed by \(K_x\). Its kernel consists of masses whose sum on every fibre of \(p_x\) is zero. These facts identify what is forgotten and what is retained when a distribution is transported to a smaller target.

Fix the same \(\alpha=1001/1000\) as before. Let \(\mu_s\) be the logarithmic law on \(\mathbb O\cap[s,s^\alpha]\). For all sufficiently large \(s\), these sets are nonempty. Define

\[
\begin{aligned}
\nu_s&=K_s\mu_{s^\alpha},\\
d(s)&=\nu_s(\dagger),\\
e(s)&=\|\nu_s-K_s\nu_{s^\alpha}\|_1.
\end{aligned}
\tag{5}
\]

The two laws in \(e(s)\) land at the same threshold \(s\). By (4), its second law is also \(K_s\mu_{s^{\alpha^2}}\). Therefore [Theorem 1 of Logarithmic sampling and first-passage distributions](NT-COLLATZ-13.md#the-entrance-law-and-the-sampling-experiment) supplies constants \(C,s_*\), with \(s_*\geq2\), for which

\[
\begin{aligned}
d(s)&\leq Cs^{-\beta},& \beta&=1/20000,\\
e(s)&\leq C(\log s)^{-\gamma},& \gamma&=1/5.
\end{aligned}
\tag{6}
\]

Both bounds hold for \(s\geq s_*\). These are proved estimates for the specified integer sampling laws. In particular, (6) is not an assumption that the landing distribution becomes uniform.

## One input sequence for all thresholds

Choose a base \(b\geq s_*\) once, and put

\[
\begin{aligned}
t_j&=b^{\alpha^j},\\
\lambda_{x,j}^{(b)}&=K_x\mu_{t_{j+1}}.
\end{aligned}
\tag{7}
\]

Here \(j\geq0\) and \(x\geq1\). The same input \(\mu_{t_{j+1}}\) is used at every threshold \(x\). This common choice is essential for comparing the resulting limits. Set

\[
D_\gamma=\frac{C}{1-\alpha^{-\gamma}}.
\]

**Theorem 2 (Compatible limiting entrance laws).** For every \(x\geq1\), the laws in (7) converge in \(\ell^1(E_x)\) to a probability law \(\lambda_x^{\infty,(b)}\). Whenever \(x\leq t_j\),

\[
\|\lambda_{x,j}^{(b)}-\lambda_x^{\infty,(b)}\|_1
\leq D_\gamma(\log t_j)^{-\gamma}.
\tag{8}
\]

For every pair of real thresholds \(1\leq x\leq y\), the limits satisfy the exact identity

\[
K_x\lambda_y^{\infty,(b)}=\lambda_x^{\infty,(b)}.
\tag{9}
\]

Their failure mass, for \(x\geq b\), satisfies

\[
\lambda_x^{\infty,(b)}(\dagger)
\leq Cx^{-\beta/\alpha}
     +D_\gamma\alpha^\gamma(\log x)^{-\gamma}.
\tag{10}
\]

**Proof.** If \(x\leq t_j\), use (4) to write

\[
\begin{aligned}
\lambda_{x,j}^{(b)}&=K_x\nu_{t_j},\\
\lambda_{x,j+1}^{(b)}&=K_xK_{t_j}\nu_{t_{j+1}}.
\end{aligned}
\]

Contraction and (6) give

\[
\|\lambda_{x,j+1}^{(b)}-\lambda_{x,j}^{(b)}\|_1
\leq C(\alpha^j\log b)^{-\gamma}.
\tag{11}
\]

For any fixed \(x\), the condition \(x\leq t_j\) holds eventually. The sum of the bounds in (11) is a geometric series. Each coordinate is therefore a real Cauchy sequence, with a limit by completeness of \(\mathbb R\). There are only finitely many coordinates in \(E_x\); their limits are nonnegative and their sum remains one. Summing the tail from \(j\) proves (8), since

\[
\sum_{h=j}^\infty C(\log t_h)^{-\gamma}
=D_\gamma(\log t_j)^{-\gamma}.
\]

For \(x\leq y\), nested passage gives \(K_x\lambda_{y,j}^{(b)}=\lambda_{x,j}^{(b)}\) at every finite index. Contraction allows passage to the limits: the distance between \(K_x\lambda_y^{\infty,(b)}\) and \(\lambda_x^{\infty,(b)}\) is at most the sum of the two finite-index convergence errors, which tends to zero. This proves (9). The thresholds need not be members of \((t_j)\).

To prove (10), choose the unique \(k\geq0\) with \(r=t_k\leq x<t_{k+1}=r^\alpha\). At threshold \(r\) and index \(k\), (7) is \(\nu_r\). Equations (6) and (8) imply

\[
\lambda_r^{\infty,(b)}(\dagger)
\leq Cr^{-\beta}+D_\gamma(\log r)^{-\gamma}.
\]

By (9), \(\lambda_r^{\infty,(b)}=K_r\lambda_x^{\infty,(b)}\). The symbol \(\dagger\) is fixed by \(p_r\); other states may also be sent to it. Nonnegativity gives
\(\lambda_x^{\infty,(b)}(\dagger)\leq\lambda_r^{\infty,(b)}(\dagger)\).
Finally, \(r>x^{1/\alpha}\) and \(\log r>(\log x)/\alpha\). Substitution proves (10). ∎

The finite comparisons were approximate; the compatibility of the limiting laws is exact. This does not make them invariant under one application of \(S\): the maps in (9) are first-passage maps, not a single fixed-time iterate.

The base remains part of the notation for a reason. Replacing \(b\) by \(b^{\alpha^k}\), for a nonnegative integer \(k\), removes the first \(k\) inputs from the same sequence and gives the same limiting family. The estimates above do not compare two arbitrarily chosen bases. Equality between their limits would require a comparison between their input sequences, not just the adjacent-scale estimate already used.

## Observing several entrance levels together

Fix \(1\leq x_1\leq\cdots\leq x_r\). A tuple of possible entrance values is compatible when

\[
\begin{gathered}
(z_1,\ldots,z_r)\in\mathcal C,\\
\mathcal C=\left\{(z_i)\in\prod_iE_{x_i}:
p_{x_i}(z_{i+1})=z_i\ (i<r)\right\}.
\end{gathered}
\tag{12}
\]

**Proposition 3 (Joint laws without an error for each coordinate).** If \(N_j\) has law \(\mu_{t_{j+1}}\), then the joint law of
\((p_{x_1}(N_j),\ldots,p_{x_r}(N_j))\) converges to a probability law \(\Lambda_{x_1,\ldots,x_r}^{(b)}\) on \(\mathcal C\). For \(x_r\leq t_j\), its \(\ell^1\) convergence error is at most \(D_\gamma(\log t_j)^{-\gamma}\), with no factor depending on \(r\). Its marginal at \(x_i\) is \(\lambda_{x_i}^{\infty,(b)}\).

**Proof.** Define

\[
\begin{aligned}
J:E_{x_r}&\longrightarrow\mathcal C,\\
z&\longmapsto(p_{x_1}(z),\ldots,p_{x_r}(z)).
\end{aligned}
\tag{13}
\]

Equation (4) proves that the image lies in \(\mathcal C\). Its last coordinate is \(z\), so \(J\) is injective. Conversely, repeated use of (12) and nested passage gives \(z_i=p_{x_i}(z_r)\). Thus projection to the last coordinate is its inverse. Every fibre is a singleton, and the tuple retains exactly the information in its last coordinate.

For a signed mass \(\eta\) on \(E_{x_r}\), injectivity gives \(\|J_*\eta\|_1=\|\eta\|_1\): no two atoms are combined. The finite joint law is exactly \(J_*\lambda_{x_r,j}^{(b)}\). Define its limit as \(J_*\lambda_{x_r}^{\infty,(b)}\), and apply this isometry to (8). The marginal identity follows by projecting the tuple and applying (9). ∎

For example, the largest entrance value can contain information not recoverable from a smaller one, because several values may have the same subsequent entrance. Recording the entire compatible tuple adds no information beyond the largest value. This is why summing a separate error for every coordinate would be unnecessary.

## A uniform estimate for a fixed orbit bound

For an odd start, write \(S_{\min}(m)=\min_{j\geq0}S^j(m)\). This minimum exists by well-ordering, even if the orbit is unbounded. For the ordinary Collatz map

\[
C(n)=\begin{cases}n/2,&n\text{ even},\\3n+1,&n\text{ odd},\end{cases}
\]

write \(C_{\min}(n)=\min_{j\geq0}C^j(n)\).

**Theorem 4 (Tao's fixed-threshold estimate).** There is an absolute constant \(A\) such that, for all real \(K,X\geq2\),

\[
\begin{aligned}
\sum_{\substack{m\leq X,\ m\in\mathbb O\\S_{\min}(m)>K}}\frac1m
&\leq\frac{A\log X}{(\log K)^{1/5}},\\
\sum_{\substack{n\leq X\\C_{\min}(n)>K}}\frac1n
&\leq\frac{A\log X}{(\log K)^{1/5}}.
\end{aligned}
\tag{14}
\]

*Reference:* Tao, Theorem 3.1 and Section 3. The argument below uses the first-passage estimate now proved in the preceding lesson.

**Proof.** First take sufficiently large \(K\). The [summable-transport theorem and its explicit power-error estimate](NT-COLLATZ-04.md#two-explicit-summable-error-estimates), applied to (6), give for every defined block law

\[
\begin{aligned}
\mu_s(S_{\min}>K)
&\leq CK^{-\beta/\alpha^3}
 +\frac{C\alpha^{3\gamma}}{1-\alpha^{-\gamma}}(\log K)^{-\gamma}\\
&\leq A_0(\log K)^{-\gamma},\qquad \gamma=1/5.
\end{aligned}
\tag{15}
\]

Its range is initially \(K\geq s_*^{\alpha^3}\). The power term is absorbed because \(t^\gamma e^{-\beta t/\alpha^3}\) is bounded for \(t=\log K\geq\log2\); differentiating it shows its maximum is finite. Increasing \(A_0\) includes the bounded range \(2\leq K<s_*^{\alpha^3}\), since probabilities are at most one.

Let \(h_s=\sum_{m\in\mathbb O\cap[s,s^\alpha]}1/m\). For \(s\geq2\), the reciprocal progression estimate of the preceding lesson gives
\(h_s\leq((\alpha-1)/2)\log s+1/s\leq A_1\log s\).
When \(1<s<2\), this interval contains no odd integer: \(s^\alpha<2^\alpha<3\). The block at \(s=1\) contains only one, whose minimum is one. Thus for all blocks relevant to a bad event at \(K\geq2\), (15) gives

\[
\sum_{\substack{m\in\mathbb O\cap[s,s^\alpha]\\S_{\min}(m)>K}}\frac1m
\leq A_2(\log s)(\log K)^{-\gamma}.
\tag{16}
\]

If \(X\leq K\), the bad sum is zero because the starting value is part of the orbit. Otherwise put \(z_i=X^{\alpha^{-i}}\), and choose \(J\geq1\) least such that \(z_J\leq K\). The blocks \([z_i,z_i^\alpha]\), \(1\leq i\leq J\), cover \([z_J,X]\). Every bad start exceeds \(K\); no bad start is lost below this union. A duplicated endpoint can only increase the upper bound. Furthermore,

\[
\sum_{i=1}^J\log z_i
\leq\log X\sum_{i=1}^\infty\alpha^{-i}
=\frac{\log X}{\alpha-1}.
\tag{17}
\]

Summing (16) proves the odd estimate in (14).

Every positive integer has a unique expression \(n=2^am\), with \(m\) odd. The [orbit-minimum theorem](NT-COLLATZ-01.md#the-least-value-attained-does-not-depend-on-the-clock) proves \(C_{\min}(2^am)=S_{\min}(m)\): all the intervening even states are at least the following odd state. Therefore there is an exact finite weighted identity

\[
\sum_{\substack{n\leq X\\C_{\min}(n)>K}}\frac1n
=\sum_{a\geq0}2^{-a}
 \sum_{\substack{m\leq X/2^a,\ m\in\mathbb O\\S_{\min}(m)>K}}\frac1m.
\tag{18}
\]

The inner bad sum is zero when \(X/2^a<2\). For every other term use the odd bound, and then

\[
\sum_{a:X/2^a\geq2}2^{-a}\log(X/2^a)
\leq2\log X.
\]

This proves the ordinary-map bound after enlarging \(A\). ∎

No approximate uniformity of odd parts was used in this transfer. Equation (18) retains each finite-cutoff fibre and its exact weight.

## Every prescribed diverging bound

Let \(H(X)=\sum_{n\leq X}1/n\). The [harmonic-sum estimates](NT-COLLATZ-03.md#logarithmic-weights) prove \(H(X)=\log X+O(1)\). A set \(B\subseteq\mathbb N_+\) has logarithmic density zero when
\(H(X)^{-1}\sum_{n\leq X,\,n\in B}1/n\to0\).

**Corollary 5 (Tao's almost-bounded theorem).** For every \(f:\mathbb N_+\to\mathbb R\) tending to infinity,

\[
\lim_{X\to\infty}\frac1{H(X)}
 \sum_{\substack{n\leq X\\C_{\min}(n)\geq f(n)}}\frac1n=0.
\tag{19}
\]

Equivalently, \(C_{\min}(n)<f(n)\) on a set of logarithmic density one. The odd version holds with \(S_{\min}\) and \(H_o(X)=\sum_{m\leq X,\,m\text{ odd}}1/m\).

**Proof.** Fix an integer \(K\geq2\). Choose \(Y_K\) such that \(f(n)>K\) for \(n>Y_K\). Then the bad event in (19) is contained in the union of the finite prefix and \(\{C_{\min}>K\}\). By (14), its normalized weight has limsup at most \(A(\log K)^{-1/5}\) as \(X\to\infty\). The finite prefix has vanished because \(H(X)\to\infty\). Let \(K\to\infty\). This proves (19), including equality in its bad event. For the odd case, use the first estimate in (14) and \(H_o(X)=\tfrac12\log X+O(1)\). ∎

The order of limits is important. A bound for a tail of \(f\) cannot be substituted as a lower bound for all its earlier values. Fixing \(K\) first and removing the finite prefix avoids that problem. It also shows that the qualitative conclusion is exactly the weighted tightness property of Theorem 1, with \(w(n)=1/n\) and \(g=C_{\min}\).

The theorem allows a different exceptional set for each prescribed \(f\). It does not supply a single finite bound reached by every orbit, and it is not a bound on the number of ordinary iterations. The clock identities explain why an orbit minimum and an elapsed-time estimate require different information.

## The mathematical route through the case study

The endpoint is an arithmetic density theorem, but the proof brings together several subjects. Return maps identify the same minimum in different orbit records. Symbolic coding gives exact arithmetic domains for affine branches. Geometric concentration controls sampled finite words. Finite Fourier analysis and renewal estimates give mixing of affine offsets. Exact inverse branches and harmonic weights turn this into a comparison of entrance laws. Summable transport then yields compatible limits and tight orbit minima.

These ingredients have different roles. The maps between clocks preserve individual orbit information. Pushforwards can discard information within their fibres. Fourier estimates control distributions, not each orbit separately. The compatible joint observation in Proposition 3, by contrast, is an exact bijection and loses no information. Keeping those distinctions visible makes the methods reusable in other discrete systems, where the maps and the analytic hypotheses can be checked on their own terms.

## Exercises with solutions

### 1 Changing the base along the same sequence

Let \(b'=b^{\alpha^k}\) for an integer \(k\geq0\). Prove directly, at finite indices, the identity between the entrance laws for bases \(b,b'\), and deduce equality of their limiting families. Does this prove equality for every pair of bases?

**Solution.** The new sequence is \(t'_j=(b')^{\alpha^j}=t_{j+k}\). Thus \(\lambda_{x,j}^{(b')}=K_x\mu_{t_{j+k+1}}=\lambda_{x,j+k}^{(b)}\). A sequence and any of its tails have the same limit, proving equality. Arbitrary bases need not be related by an integer shift of this form; the displayed identity then gives no comparison. This is a statement about what the proof establishes, not a proof that other bases yield different limits.

### 2 Joint observations in a finite system

On \(D=\{1,2,3,4,5,6\}\), define

\[
\begin{aligned}
F(1)&=1,&F(2)&=1,&F(3)&=2,\\
F(4)&=3,&F(5)&=6,&F(6)&=5.
\end{aligned}
\]

Use thresholds \(2,4,6\) and input laws
\(\eta_j=(1-2^{-j})\delta_6+2^{-j}\delta_4\), \(j\geq0\).
Compute the limiting joint law and its exact \(\ell^1\) error. Verify that the sum of adjacent-law errors equals that error.

**Solution.** The compatible tuples for the two possible starts are \((\dagger,\dagger,6)\) and \((2,4,4)\), respectively. The joint law has the same two weights as \(\eta_j\). Its limit is unit mass at \((\dagger,\dagger,6)\), and the error is \(2\cdot2^{-j}=2^{1-j}\). Adjacent laws have distance \(2(2^{-j}-2^{-j-1})=2^{-j}\). Their tail sum from \(j\) is \(\sum_{h=j}^\infty2^{-h}=2^{1-j}\), exactly the same quantity. Three coordinates have introduced no factor of three.

### 3 An unbounded function with tight weighted distributions

Under weights \(w(n)=1/n\), define \(g(2^k)=k\) for integers \(k\geq0\), and \(g(n)=0\) for other positive integers. Prove that its distributions over all nonempty prefixes are uniformly tight, although \(g\) is unbounded.

**Solution.** For \(K\geq0\), the unnormalized weight of \(\{g>K\}\) is at most
\(\sum_{k> K}2^{-k}=2^{-\lfloor K\rfloor}\). Since \(H(X)\geq1\), the same upper bound holds for every normalized prefix. It tends to zero. The values \(g(2^k)=k\) show unboundedness. Theorem 1 therefore applies to every diverging \(f\), despite the infinitely many large values of \(g\).

### 4 Why the finite prefix cannot be ignored at the start

Suppose a nonnegative finite-valued \(g\) satisfies
\(\sum_{n\leq X,\,g(n)>K}1/n\leq A\log X/(\log K)^c\) for \(K,X\geq2\). Let \(f(n)\to\infty\), without assuming monotonicity. Give a bound for the harmonic mass of \(\{g\geq f\}\) that keeps the finite prefix, and specify the order of limits proving density zero.

**Solution.** For each fixed \(K\geq2\), choose \(Y_K\) with \(f(n)>K\) beyond it. The mass up to \(X\) is at most
\(H(Y_K)+A\log X/(\log K)^c\). Divide by \(H(X)\), and first let \(X\to\infty\) with \(K\) fixed. The prefix term vanishes and the limsup is at most \(A/(\log K)^c\). Only then let \(K\to\infty\). A threshold defined using only values of \(f\) after \(X\) would not control the values being summed before \(X\).

## References

- Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12; [arXiv:1909.03562, version 7](https://arxiv.org/abs/1909.03562v7). Remark 1.4 discusses tightness; Proposition 1.11 supplies the entrance estimate; Section 3 derives the orbit-minimum conclusions. The complete analytic input is proved in the preceding lessons.
- [First passage and transport across scales](NT-COLLATZ-04.md), for nested passage, finite-chain contraction and the complete summable-scale proof used in (15).
- [Logarithmic sampling and first-passage distributions](NT-COLLATZ-13.md), for the proved bounds in (6).
