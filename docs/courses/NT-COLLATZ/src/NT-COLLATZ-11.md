# Weighted renewal estimates and Fourier decay

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, proofs and exercises: CC0 1.0.*

A random path may visit many positions at which an average loses a fixed fraction of its size. To obtain a decay estimate in the size of the problem, however, we must compare those losses with the distance travelled. A long journey to the first useful position can consume most of the available distance. The estimate must account for both effects on the same path.

We prove a weighted renewal theorem that makes this comparison. If the noncancelling regions are the separated triangles studied previously, the expected multiplicative weight is bounded by every negative power of the remaining horizontal width. The proof uses an increasing family of suprema: once the width is sufficiently large, adding one more starting column cannot increase the weighted supremum. This gives a uniform bound without assuming that any supremum is attained.

The arithmetic application is Tao's Fourier estimate for random Syracuse offsets. Every prescribed power of the length is available, uniformly over characters of full order. The order of a character matters: lower-order characters retain information about smaller quotients, and some of those coefficients do not tend to zero. This explains why a later mixing argument needs both Fourier cancellation and a dispersed arithmetic prefix.

The prerequisites are [the exact stopped-word identity](NT-COLLATZ-08.md#restarting-after-a-random-crossing), [the first-crossing tails](NT-COLLATZ-08.md#the-overshoot-and-the-transverse-displacement), [the uniform cancelling-exit estimate](NT-COLLATZ-10.md#a-cancelling-landing-above-a-triangle), and [the finite-horizon encounter theorem](NT-COLLATZ-10.md#many-cancelling-visits-within-a-fixed-further-horizon). The final application uses [conditional Fourier cancellation](NT-COLLATZ-09.md#a-phase-that-measures-the-cancellation) and the exact marked-block clock. Basic references are Terence Tao's *Almost all orbits of the Collatz map attain almost bounded values*, Section 7, and Robert Gallager's *Discrete Stochastic Processes*, Chapter 4. The weighted renewal method is Tao's; its required estimates have complete proofs here or in the specified preceding lessons.

## A multiplicative weight on a finite strip

Fix an integer \(M\geq1\). Let \(H_i=(J_i,L_i)\) be independent copies of [the marked holding law](NT-COLLATZ-07.md#a-two-coordinate-holding-time-from-marked-waiting-times), in the geometric setting of the preceding lesson. In particular,

\[
J_i\geq1,\qquad J_i\leq L_i,\qquad
\mathbb E(J_i,L_i)=(4,16),\qquad
\mathbb E e^{\eta(J_i+L_i)}=M_\eta<\infty.
\tag{1}
\]

for \(\eta=\log(33/32)\). Write \((X_k,Y_k)=\sum_{i=1}^kH_i\). The noncancelling set \(B\) is a union of disjoint lattice triangles

\[
\Delta=\{(x,y)\in\mathbb Z^2:x\geq u_\Delta,\ y\leq t_\Delta,
a(x-u_\Delta)+b(t_\Delta-y)\leq S_\Delta\},
\tag{2}
\]

where \(a=\log9\), \(b=\log2\), the corners are integral, \(u_\Delta\geq1\), and \(S_\Delta\geq0\). Distinct triangles have Euclidean separation greater than \(R\), and
\(u_\Delta+S_\Delta/a\leq M-R\). Choose \(R>R_0\), where \(R_0\) is the fixed constant in the preceding cancelling-exit proposition. Let
\(W=(\{1,\ldots,M\}\times\mathbb Z)\setminus B\); its indicator is zero outside that strip.

For a fixed \(\lambda>0\), and a starting point \(z=(j,l)\) with integer \(j\geq1\), define

\[
Q(z)=\mathbb E\exp\left[-\lambda
\sum_{k\geq0}\mathbf1_W\bigl(z+(X_k,Y_k)\bigr)\right].
\tag{3}
\]

Every horizontal increment is at least one. Thus the sum contains at most \(\max(M-j+1,0)\) nonzero terms. In particular, \(0<Q(z)\leq1\), and \(Q(z)=1\) when \(j>M\). There is no infinite-product convergence issue in (3).

**Proposition 1 (Exact continuation after a stopping time).** One has

\[
Q(z)=e^{-\lambda\mathbf1_W(z)}\mathbb E Q(z+H_1).
\tag{4}
\]

More generally, let \(\sigma\) be a nonnegative integer stopping time, bounded by a deterministic integer, for the increments already read. With \(Z_k=z+(X_k,Y_k)\),

\[
Q(z)=\mathbb E\left[
e^{-\lambda\sum_{k=0}^{\sigma-1}\mathbf1_W(Z_k)}Q(Z_\sigma)
\right].
\tag{5}
\]

**Proof.** Split the count in (3) at time one. The unused increments have the original product law independently of \(H_1\), proving (4). For (5), prescribe each possible stopped prefix. Its probability is the product of its increment masses, and the future word has its original product law independently of that prefix, by the linked stopped-word proof. The count up to \(\sigma-1\) is fixed on the prefix. The conditional expectation of the remaining factor is exactly \(Q(Z_\sigma)\). Sum over the countably many stopped prefixes. All terms are nonnegative, and the stopping time is bounded, so this regrouping uses only the countable probability identities already proved. The position at time \(\sigma\) belongs to the second factor, not both. ∎

For example, if \(z\in\Delta\), put \(s=t_\Delta-l\) and
\(\tau_s=\min\{k\geq1:Y_k>s\}\). Since \(L_i\geq1\),
\(\tau_s\leq s+1\). Both \(\tau_s+1\) and \(\tau_s+P\), for a fixed integer \(P\), satisfy the boundedness required by (5).

## The cost of moving to a later column

Fix a desired power \(A>0\). The remaining-width weight is
\(d_M(j)=\max(M-j,1)\). Moving horizontally by \(r\geq0\) changes its negative power by the factor

\[
R_m(r)=\left(\frac{m}{\max(m-r,1)}\right)^A,
\qquad m\geq2.
\tag{6}
\]

This is an inflation factor, not a probability. It is bounded by \(m^A\), but that rough bound is too expensive on ordinary paths.

**Lemma 2 (An exponential bound for the weight ratio).** For real \(r\geq0\),

\[
R_m(r)\leq e^{t_mr},\qquad
t_m=\frac{A\log m}{m-1}\leq\frac{2A\log m}{m}.
\tag{7}
\]

**Proof.** On \([0,m-1]\), the function
\(g(r)=\log(m/(m-r))\) has second derivative \((m-r)^{-2}>0\). A convex function lies below the chord joining two points on its graph; here \(g(0)=0\) and \(g(m-1)=\log m\). Hence \(g(r)\leq r\log m/(m-1)\) on this interval. For \(r\geq m-1\), the logarithm of (6), divided by \(A\), equals \(\log m\), which satisfies the same bound. The final inequality follows from \(m-1\geq m/2\). ∎

We also need exponential moments close to one, uniformly at the crossing. For each integer \(s\geq0\), let \(O_s=Y_{\tau_s}-s\). All depth parameters below are integers. The preceding first-crossing tail theorem gives fixed \(C_o,\eta_o>0\) such that
\(\mathbb P(O_s\geq r)\leq C_o e^{-\eta_or}\), for all integers \(r\geq1\) and all \(s\geq0\).

**Lemma 3 (Small exponential parameters).** There are fixed constants \(\kappa,B_J,B_O>0\) such that, for \(0\leq t\leq\kappa\),

\[
\mathbb E e^{tJ_1}\leq1+B_Jt,\qquad
\sup_{s\geq0}\mathbb E e^{tO_s}\leq1+B_Ot.
\tag{8}
\]

For an independent next horizontal increment \(J'\), these imply

\[
\mathbb E e^{t(X_{\tau_s}+J')}
\leq \exp\bigl(t(s+B_O+B_J)\bigr).
\tag{9}
\]

**Proof.** Take \(\kappa=\tfrac12\min(\eta,\eta_o)\). For \(u\geq0\), integration of the derivative in \(t\) gives
\(e^{tu}-1\leq tu e^{\kappa u}\) on the specified interval. Also
\(u e^{-\eta u/2}\leq2/\eta\), for instance by differentiating the left side. Thus
\(\mathbb E[J_1e^{\kappa J_1}]\leq2M_\eta/\eta\); this is a permissible \(B_J\).

Since \(\mathbb P(O_s=r)\leq C_o e^{-\eta_or}\), we have uniformly in \(s\)

\[
\mathbb E[O_se^{\kappa O_s}]
\leq C_o\sum_{r\geq1}r e^{-\eta_or/2}
=C_o\frac{q}{(1-q)^2},\qquad q=e^{-\eta_o/2}.
\]

The series identity follows by multiplying two convergent geometric series, or differentiating one within its radius of convergence. This provides \(B_O\) and proves (8). Finally, \(X_{\tau_s}\leq Y_{\tau_s}=s+O_s\), since \(J_i\leq L_i\). The independent future increment and (8) give
\(e^{ts}(1+B_Ot)(1+B_Jt)\) as an upper bound. Apply \(1+u\leq e^u\) to obtain (9). ∎

In the shallow regime \(s\leq m/(\log m)^2\), equations (7)–(9) show

\[
\sup_{0\leq s\leq m/(\log m)^2}
\mathbb E e^{t_m(X_{\tau_s}+J')}
\leq \exp\left(
\frac{2A}{\log m}+\frac{2A(B_O+B_J)\log m}{m}\right).
\tag{10}
\]

For sufficiently large \(m\), \(t_m\leq\kappa\); the right side then tends to one. The error is uniform in the allowed depth. A bound by an unspecified fixed exponential moment would not give this near-one conclusion.

## A weighted supremum that eventually stops increasing

For integers \(0\leq m\leq M-1\), define

\[
\mathcal Q_m=\sup_{\substack{j\geq M-m\\l\in\mathbb Z}}
d_M(j)^A Q(j,l).
\tag{11}
\]

All horizontal coordinates here are positive. We have \(\mathcal Q_0=1\), because points strictly beyond the strip have \(Q=1\), and
\(\mathcal Q_m\leq\max(m,1)^A\). For \(m\geq1\),

\[
\mathcal Q_m=\max\left\{\mathcal Q_{m-1},
\sup_{l\in\mathbb Z}m^A Q(M-m,l)\right\}.
\tag{12}
\]

Thus only one new starting column must be controlled. No point realizing either supremum is needed.

**Theorem 4 (Decay in the remaining width).** For every \(A,\lambda>0\), there is a constant \(C_{A,\lambda}\) such that

\[
Q(j,l)\leq C_{A,\lambda}\max(M-j,1)^{-A}
\quad(j\geq1,\ l\in\mathbb Z).
\tag{13}
\]

The constant is uniform in \(M\), the triangle family and all starting positions satisfying the geometric hypotheses (2). It depends on the fixed holding law and geometry, but not on the separation parameter once \(R>R_0\).

*Reference:* Tao, Section 7, the weighted maximal-expression argument. We prove the comparison using three bounded stopping rules.

**Proof.** We show that there is an integer \(m_*\geq2\), depending only on \(A,\lambda\) and the fixed preceding estimates, for which

\[
m^A Q(j,l)\leq\mathcal Q_{m-1},\qquad j=M-m,
\tag{14}
\]

whenever \(m\geq m_*\). For any displacement \((D,E)\) with integer \(D\geq1\), (11) gives

\[
Q(j+D,l+E)\leq
\mathcal Q_{m-1}\max(m-D,1)^{-A}.
\tag{15}
\]

Every stopping rule below advances by at least one horizontal unit, so this bound is available without assuming (14).

The three rules retain different parts of the cancellation count:

| Starting position | Stop at | Cancelling positions retained in the estimate |
| --- | --- | --- |
| Already in \(W\) | one step | the starting position |
| In a shallow triangle | \(\tau_s+1\) | the exit position at \(\tau_s\) |
| In a deep triangle | \(\tau_s+P\) | all positions from \(\tau_s\) to \(\tau_s+P-1\) |

**A cancelling starting position.** Equations (4), (7), (8) and (15) give

\[
Q(z)\leq m^{-A}\mathcal Q_{m-1}
e^{-\lambda}(1+B_Jt_m).
\]

Choose \(m_*\) sufficiently large that \(t_m\leq\kappa\) and
\(1+B_Jt_m\leq e^{\lambda/2}\) for all \(m\geq m_*\). The last factor is then at most \(e^{-\lambda/2}<1\), proving (14) in this case.

**A shallow triangle.** Suppose \(z\in\Delta\) and
\(0\leq s=t_\Delta-l\leq m/(\log m)^2\).
Apply (5) with \(\sigma=\tau_s+1\). Discard all factors of size at most one except the factor at the exit position \(Z_{\tau_s}\). Put
\(I=\mathbf1_W(Z_{\tau_s})\) and \(D=X_{\tau_s}+J'\), where \(J'\) is the next horizontal increment. The stopped-word identity makes \(J'\) independent of the prefix. Equations (7) and (15) yield

\[
Q(z)\leq m^{-A}\mathcal Q_{m-1}
\mathbb E\bigl[e^{-\lambda I}e^{t_mD}\bigr].
\tag{16}
\]

We do not factor this expectation: the exit colour and displacement can be dependent. Instead, since \(e^{t_mD}\geq1\),

\[
\mathbb E[e^{-\lambda I}e^{t_mD}]
\leq \mathbb E e^{t_mD}-(1-e^{-\lambda})\mathbb P(I=1).
\tag{17}
\]

The cancelling-exit proposition gives \(\mathbb P(I=1)\geq1/2\).
Equation (10) lets us increase \(m_*\) so that its first term is at most
\(1+(1-e^{-\lambda})/4\), uniformly in the shallow depth. The result is at most
\(1-(1-e^{-\lambda})/4<1\). This proves (14). Stopping one step after the crossing puts the exit weight in the first factor of (5); no separate estimate on \(Q\) at a white exit is being assumed.

**A deep triangle.** Now suppose \(s>m/(\log m)^2\). From the triangle equation and its right margin,

\[
s\leq(a/b)m,\qquad
\gamma=1/4,\qquad c_*:=\gamma a/b<1.
\]

Fix
\(\rho=(1+c_*)/2\), \(\rho_0=(c_*+\rho)/2\), and
\(\Gamma=(1-\rho)^{-A}\).
Choose an integer \(K\geq\log(8\Gamma)/\lambda\), and set
\(\delta=1/(8\Gamma)\). The preceding finite-horizon theorem gives an integer \(P\geq1\) and a width threshold for which, with

\[
V=\exp\left[-\lambda\sum_{p=0}^{P-1}
\mathbf1_W(Z_{\tau_s+p})\right],
\]

one has

\[
\mathbb E V\leq\delta+e^{-\lambda K}
\leq\frac1{4\Gamma}.
\tag{18}
\]

These parameters are fixed before the final choice of \(m_*\).

Let \(D=X_{\tau_s+P}\). We claim that, for this fixed \(P\),

\[
\mathbb P(D>\rho m)
\leq C e^{-cm}+M_\eta^P e^{-\eta(\rho-\rho_0)m}.
\tag{19}
\]

Indeed, the first-crossing horizontal tail bounds
\(\mathbb P(X_{\tau_s}>\rho_0m)\) by \(Ce^{-cm}\). To check its exponent, its distance above \(\gamma s\) is at least \((\rho_0-c_*)m\), while \(1+s\leq1+(a/b)m\); both the quadratic and linear terms in the tail exponent are therefore at least a fixed positive multiple of \(m\), for \(m\geq1\). The sum of the \(P\) unused horizontal increments exceeds \((\rho-\rho_0)m\) with probability at most the second term in (19), by the exponential moment (1). Independence after \(\tau_s\) gives this ordinary \(P\)-step law. If neither event occurs, their sum is at most \(\rho m\), proving (19).

Apply (5) at \(\tau_s+P\), discard weights strictly before \(\tau_s\), and use (15). This gives

\[
Q(z)\leq m^{-A}\mathcal Q_{m-1}\mathbb E[V R_m(D)].
\tag{20}
\]

On \(D\leq\rho m\), (6) is at most \(\Gamma\). On the complementary event it is at most \(m^A\); also \(V\leq1\). Consequently

\[
\mathbb E[V R_m(D)]
\leq\Gamma\mathbb EV+m^A\mathbb P(D>\rho m)
\leq\frac14+m^A\mathbb P(D>\rho m).
\tag{21}
\]

For fixed \(A,P\), the last term tends to zero by (19). Explicitly, \(m^Ae^{-cm}\to0\) because its logarithm is \(A\log m-cm\to-\infty\); the other term has the same form with a fixed multiplier \(M_\eta^P\). Increase \(m_*\) to make the last term at most \(1/4\), as well as to satisfy the finite-horizon theorem's width threshold. Equation (21) is then at most \(1/2\), proving (14).

The three cases exhaust the strip. Equation (12) now gives
\(\mathcal Q_m\leq\mathcal Q_{m-1}\) for \(m\geq m_*\). For smaller \(m\), the elementary bound following (11) is at most \(m_*^A\). Induction therefore gives \(\mathcal Q_m\leq m_*^A\) throughout its range. This proves (13), with \(C_{A,\lambda}=m_*^A\). Points with \(j\geq M\), and strips narrower than \(m_*\), are already covered by the elementary bound. All thresholds were uniform in the family and its strip width. ∎

The theorem does not say that every path has many cancelling visits. It bounds their multiplicative average, including paths that jump past a large part of the strip. Such paths are allowed; their probability is paid for by the exponential tail in (19).

## Beginning the path at its first marked block

The arithmetic occupation count starts at the first holding increment, rather than at a prescribed positive column. Define

\[
N_M=\sum_{k\geq1}\mathbf1_W(X_k,Y_k).
\]

There are at most \(M\) nonzero terms. Conditioning on \(H_1\) and using independence of the unused holding increments gives the exact identity

\[
\mathbb E e^{-\lambda N_M}=\mathbb E Q(H_1).
\tag{22}
\]

**Corollary 5 (Uniform occupation decay).** For every \(A,\lambda>0\), there is a fixed \(C'_{A,\lambda}\) such that

\[
\mathbb E e^{-\lambda N_M}\leq C'_{A,\lambda}M^{-A}
\qquad(M\geq1).
\tag{23}
\]

**Proof.** For \(M\geq2\), split according to \(J_1\leq M/2\). On that event, Theorem 4 bounds \(Q(H_1)\) by \(C_{A,\lambda}(2/M)^A\). On the complement use \(Q\leq1\) and
\(\mathbb P(J_1>M/2)\leq M_\eta e^{-\eta M/2}\). Thus

\[
\mathbb E Q(H_1)\leq C_{A,\lambda}(2/M)^A
+M_\eta e^{-\eta M/2}.
\]

The exponential term is at most a constant times \(M^{-A}\). For instance differentiation gives
\(\sup_{x\geq0}x^Ae^{-\eta x/2}=(2A/(e\eta))^A\). Enlarge the resulting constant to at least one for \(M=1\). ∎

This final averaging is essential. A first increment can jump far into the strip or beyond it, and that event is not represented by replacing the first column with its mean.

## Fourier decay for random affine offsets

Let \(A_1,\ldots,A_n\) be independent with
\(\mathbb P(A_i=r)=2^{-r}\), \(r\geq1\), and let \(S_i=A_1+\cdots+A_i\). Define the dyadic rational

\[
T_n=\sum_{i=1}^n3^{i-1}2^{-S_i}.
\tag{24}
\]

As in the preceding phase lesson, reduction modulo \(3^n\) sends \(2^{-1}\) to its multiplicative inverse in \(\mathbb Z/3^n\mathbb Z\). For a residue \(\xi\), set

\[
\widehat\mu_n(\xi)=\mathbb E
\exp\left(-\frac{2\pi i\xi(T_n\bmod 3^n)}{3^n}\right).
\tag{25}
\]

**Theorem 6 (Arbitrary-power Fourier decay).** For every \(A>0\), there is a constant \(C_A\) such that, for all \(n\geq1\) and all \(\xi\) not divisible by three,

\[
|\widehat\mu_n(\xi)|\leq C_A n^{-A}.
\tag{26}
\]

*Reference:* Tao, the decay-of-characteristic-function proposition and the key Fourier estimate in Section 7.

**Proof.** Choose once and for all
\(0<\varepsilon\leq\exp[-10\max\{1,R_0+1\}]\), and put
\(\lambda=\varepsilon^3\). For \(n\geq2\), set \(M=\lfloor n/2\rfloor\). The [phase separation theorem](NT-COLLATZ-09.md#the-low-phase-set-consists-of-separated-triangles), with the precise [real right-margin calculation](NT-COLLATZ-10.md#the-path-and-the-regions-it-must-cross), supplies the geometric hypotheses (2), uniformly in \(n,\xi\). Its cancelling set is determined by the centred phase of the character in (25).

The [conditional pairing calculation](NT-COLLATZ-09.md#pairing-waiting-times-before-taking-absolute-values) and its [occupation bound](NT-COLLATZ-09.md#a-phase-that-measures-the-cancellation) give
\(|\widehat\mu_n(\xi)|\leq\mathbb E e^{-\lambda N_M}\).
Here [the exact marked-block clock](NT-COLLATZ-09.md#from-pair-indices-to-a-renewal-occupation-count) identifies the counted positions with the holding process in (22). These identities retain the final factor when \(n\) is odd; that factor has modulus at most one and is not assigned a false independence.

Corollary 5 bounds this expectation by \(C'_{A,\lambda}M^{-A}\). Since \(M\geq n/3\) for \(n\geq2\), the result is at most \(3^AC'_{A,\lambda}n^{-A}\). The chosen \(\lambda\) is fixed independently of \(n,\xi,A\). Enlarge \(C_A\) to cover \(n=1\) by the bound one. ∎

Thus the renewal calculation proves the Fourier estimate, rather than only an analogy with spectral cancellation. The estimate concerns the independent-word offset law. Comparing that law with values sampled from deterministic integer orbits is a separate step, treated through valuation-word sampling and first-passage transport.

## Character order and mixing inside observation classes

The character of \(\mathbb Z/3^n\mathbb Z\) indexed by a nonzero \(\xi\) has exact order \(3^k\), where \(\xi=3^{n-k}\eta\) and \(3\nmid\eta\). This expression is understood with \(1\leq k\leq n\) and \(\eta\) a unit modulo \(3^k\). Its kernel is the set of multiples of \(3^k\) modulo \(3^n\): this follows directly by asking when \(\xi x/3^n\) is an integer.

Reduction of (24) modulo \(3^k\) discards exactly the terms with \(i>k\), because each has numerator divisible by \(3^k\) and denominator invertible there. The first \(k\) terms retain their original independent law. Hence

\[
\widehat\mu_n(3^{n-k}\eta)=\widehat\mu_k(\eta),
\qquad
|\widehat\mu_n(3^{n-k}\eta)|\leq C_A k^{-A}.
\tag{27}
\]

At frequency zero the coefficient is one. Formula (27) is an exact map between character groups and random laws, not an estimate identifying all nonzero frequencies with full-order characters.

To see the consequence, \(T_n\bmod3=2^{-A_1}\bmod3\) for every \(n\). Odd \(A_1\) has probability \(2/3\), even \(A_1\) probability \(1/3\); their residues are two and one. Thus this smallest quotient is not uniform. The coefficient of order three has modulus \(1/\sqrt3\), independently of \(n\), as Exercise 4 computes.

The appropriate next question is uniformity *within* selected observation classes. The [Fourier and collision-mass theorem](NT-COLLATZ-05.md#an-energy-estimate-for-mixing-inside-fibres) proves, on a finite cyclic group of order \(N\), for a nonnegative subprobability mass function \(f\) and a probability mass function \(g\),

\[
\|f*g-P(f*g)\|_1
\leq \delta\left(N\sum_x f(x)^2\right)^{1/2},
\tag{28}
\]

where \(P\) uniformly averages within the specified quotient fibres and \(\delta\) bounds the Fourier coefficients of \(g\) at the discarded frequencies. The factor \(\sum f(x)^2\) records collisions of the prefix distribution. Applying a coefficient bound directly to exponentially many frequencies can lose more than a negative power of the length gains. Formula (28) explains the role of arithmetic prefix separation: it controls that collision factor, while Theorem 6 controls the tail's oscillation. Their exact combination, with event masses retained, is the next part of the probability argument.

## Exercises

### 1. Deterministic increments through an entirely cancelling strip

Replace the holding law by the deterministic increment \((1,3)\), and let every point of the strip be cancelling. Write \(w=e^{-\lambda}\). Calculate \(Q(j,l)\), and for \(m=M-j\geq1\) calculate the ratio between consecutive terms \(a_m=m^Aw^{m+1}\). Find a sufficient threshold after which these terms decrease.

**Solution.** There are exactly \(M-j+1\) visits in the strip when \(j\leq M\), and none otherwise. Thus
\(Q(j,l)=w^{\max(M-j+1,0)}\). For \(m\geq1\),
\(a_{m+1}/a_m=w(1+1/m)^A\). This is at most one whenever
\(m\geq(w^{-1/A}-1)^{-1}\). The example illustrates why a polynomially weighted supremum can stop increasing even though its set of starting points grows. This deterministic law is only an example of the recursion; it is not claimed to satisfy the two-dimensional local-probability hypotheses of the marked law.

### 2. Do not separate a reward from a correlated cost

Let \((I,Y)=(1,1)\) or \((0,4)\), each with probability \(1/2\), and let \(w=1/2\). Compare \(\mathbb E[w^IY]\) with \(\mathbb E[w^I]\mathbb EY\). Check the bound used in (17).

**Solution.** The joint expectation is \((1/2)(1/2)+(1/2)4=9/4\). The product of expectations is \((3/4)(5/2)=15/8\), which is smaller and therefore cannot replace it in an upper bound. The valid estimate is

\[
\begin{aligned}
\mathbb E[w^IY]&\leq\mathbb EY-(1-w)\mathbb P(I=1)\\
&=5/2-1/4=9/4.
\end{aligned}
\]

It follows from the pointwise identity \(w^IY=Y-(1-w)IY\) and \(Y\geq1\). Equality happens in this example because \(Y=1\) whenever \(I=1\).

### 3. Choosing the cancellation allowance before the width

In the deep-case estimate suppose \(\Gamma=16\) and \(\lambda=\log2\). Use the proof's parameter rule to select \(\delta,K\), bound \(\Gamma\mathbb EV\), and state how small the large-displacement term must then be.

**Solution.** Choose \(\delta=1/128\) and \(K=7\). Since \(e^{-\lambda K}=2^{-7}=1/128\), the encounter theorem gives \(\mathbb EV\leq1/64\). Multiplication by \(\Gamma\) gives at most \(1/4\). After fixing the resulting horizon \(P\), choose the width threshold so that \(m^A\mathbb P(D>\rho m)\leq1/4\), using (19). The full weighted expectation is at most \(1/2\). Choosing \(P\) after this last width threshold would not follow the proof's order of quantifiers.

### 4. The coefficient of order three

Calculate \(\widehat\mu_n(3^{n-1})\) exactly, for every \(n\geq1\), and explain why it is consistent with Theorem 6.

**Solution.** Reduction modulo three keeps only \(2^{-A_1}\). The geometric series give
\(\mathbb P(A_1\text{ odd})=\sum_{r\geq0}2^{-2r-1}=2/3\) and even probability \(1/3\). Therefore

\[
\widehat\mu_n(3^{n-1})
=\tfrac13e^{-2\pi i/3}+\tfrac23e^{-4\pi i/3}
=-\tfrac12+\frac{i\sqrt3}{6}.
\]

Its squared modulus is \(1/4+1/12=1/3\). For \(n>1\) the frequency is divisible by three, so it is not a full-order frequency covered by (26). Equation (27) covers it with \(k=1\), a fixed character order; no decay in \(n\) is asserted there.

## What the weighted estimate adds

The cancellation count and the distance travelled have been controlled together. At a white starting point, one step supplies a fixed gain. A shallow crossing costs a factor tending to one and offers a uniform chance of a cancelling exit. A deep crossing consumes a fixed fraction of the width on the likely event; the finite-horizon encounter theorem supplies as much cancellation as a prescribed polynomial weight requires. Rare larger displacements have exponentially small probability.

This proves the arbitrary-power Fourier estimate for the independent Syracuse offset model, with all renewal inputs supplied by preceding lessons. It does not replace the arithmetic task of separating prefixes or the dynamical task of transporting sampled orbit laws across scales. Those tasks have precise roles: prefix separation converts Fourier cancellation into fine-scale probability control, and transport converts the probability estimates into information about trajectories. The conjecture remains a motivating case study within these broader methods.

## References

- Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, [arXiv:1909.03562v7](https://arxiv.org/abs/1909.03562v7), the decay-of-characteristic-function proposition and Section 7, especially the recursively controlled maximal expression. The phase and renewal method is credited to Tao, including his acknowledgement of Marek Biskup's renewal-process suggestion. The lessons give an independently expressed proof of this established Fourier estimate, not a new strengthening of the orbit-minimum theorem.
- Robert G. Gallager, *Discrete Stochastic Processes*, [MIT OpenCourseWare, Chapter 4: Renewal Processes](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/931ffa0940899c27f34b71ad64fd2bb0_MIT6_262S11_chap04.pdf), Section 4.1 and Definition 4.5.1. The exact stopped-word identities used here are proved in the preceding renewal lesson.
