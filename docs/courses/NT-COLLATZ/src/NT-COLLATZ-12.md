# Arithmetic separation and fine-scale mixing

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, proofs and exercises: CC0 1.0.*

Small Fourier coefficients describe cancellation, but a probability law on a large group has many coefficients. An estimate for each one need not survive summation over the whole group. A useful way forward is to divide a random sum into two parts. The first part must distribute its mass among many distinct values. The second must cancel at the frequencies that distinguish nearby states. Their convolution then combines arithmetic separation with harmonic analysis.

We carry this out for random affine offsets associated with the odd-return Collatz map. Averaging uniformly within each residue class modulo a smaller power of three changes the full probability law by less than every prescribed negative power of that smaller exponent. This controls conditional discrepancies averaged with their actual class probabilities; it does not give the same bound separately in every class. The classes themselves need not have equal mass. In particular, the result is consistent with the nonuniform distribution modulo three found in the preceding lesson.

The proof has two mathematical parts. First, a dyadic rational offset determines its entire finite word, and a height bound preserves that injectivity after reduction modulo a power of three. Second, we stop a random word when its accumulated exponent reaches a suitable threshold. On each retained prefix event, the unused tail remains independent. Exact event masses, rather than conditional laws with mass one, connect the two parts without losing their probability weights.

The prerequisites are [the Fourier and collision-mass estimate](NT-COLLATZ-05.md#an-energy-estimate-for-mixing-inside-fibres), [concentration for geometric sums](NT-COLLATZ-06.md#an-exponential-estimate-with-explicit-constants), and [the full-order Fourier estimate and character-order reduction](NT-COLLATZ-11.md#fourier-decay-for-random-affine-offsets). Basic references are Terence Tao's *Almost all orbits of the Collatz map attain almost bounded values*, Section 6, and Keith Conrad's *Characters of finite abelian groups*, Section 4. The mixing theorem and its prefix–tail mechanism are Tao's. All additional arguments needed here are proved below; the preceding lessons supply the stated analytic inputs.

## Mixing while preserving a coarse observation

Let \(A_1,A_2,\ldots\) be independent positive integers with
\(\mathbb P(A_i=a)=2^{-a}\). Put \(S_0=0\), \(S_j=A_1+\cdots+A_j\), and

\[
T_n=\sum_{j=1}^n3^{j-1}2^{-S_j}\in\mathbb Z[1/2].
\]

Let \(G_n=\mathbb Z/3^n\mathbb Z\), and let \(\mu_n\) be the mass function of \(T_n\bmod3^n\). Reduction sends the denominator two to its multiplicative inverse modulo \(3^n\), as proved in [Characters on dyadic fractions](NT-COLLATZ-09.md#characters-on-fractions-with-powers-of-two-as-denominators). It is not the ordinary real fractional-part operation.

For \(1\leq m\leq n\), define reduction of mass and uniform lifting by

\[
\begin{aligned}
(R_{m,n}f)(a)&=\sum_{x\equiv a\ (3^m)} f(x),\\
(U_{m,n}h)(x)&=3^{m-n}h(x\bmod3^m),\\
P_{m,n}&=U_{m,n}R_{m,n}.
\end{aligned}
\tag{1}
\]

Here \(f:G_n\to\mathbb C\), \(h:G_m\to\mathbb C\), and \(a\in G_m\). The reduction has kernel the mass functions summing to zero on each fibre. Its specified right inverse \(U_{m,n}\) assigns equal mass to the \(3^{n-m}\) positions in a fibre. The [reduction-and-lifting proposition](NT-COLLATZ-05.md#what-a-quotient-observation-forgets) proves

\[
\begin{gathered}
\|R_{m,n}f\|_1\leq\|f\|_1,\qquad \|U_{m,n}h\|_1=\|h\|_1,\\
P_{m,n}^2=P_{m,n}.
\end{gathered}
\tag{2}
\]

The norms are sums of absolute masses, with no factor of \(1/2\). For two probability laws, the largest discrepancy on an event is half their \(\ell^1\) distance.

For \(j>m\), the \(j\)-th term of \(T_n\) vanishes modulo \(3^m\). The first \(m\) variables retain their original law. Thus

\[
R_{m,n}\mu_n=\mu_m,
\qquad P_{m,n}\mu_n=U_{m,n}\mu_m.
\tag{3}
\]

**Theorem 1 (Fine-scale mixing).** For every real \(p>0\), there is a constant \(K_p\), independent of \(m,n\), such that

\[
\begin{gathered}
\|\mu_n-U_{m,n}\mu_m\|_1\leq K_p m^{-p},\\
1\leq m\leq n.
\end{gathered}
\tag{4}
\]

*Reference:* Tao, the fine-scale mixing proposition and Section 6.

Here is an exact conditional interpretation. Let \(F_a\) be the fibre over \(a\in G_m\), let \(u_a\) be its uniform probability law, and, when \(\mu_m(a)>0\), let \(\nu_a(x)=\mu_n(x)/\mu_m(a)\) on \(F_a\). Then

\[
\|\mu_n-U_{m,n}\mu_m\|_1
=\sum_{a:\,\mu_m(a)>0}\mu_m(a)\|\nu_a-u_a\|_1.
\]

Indeed, on each such fibre the difference of masses is \(\mu_m(a)(\nu_a-u_a)\). A zero-mass fibre has all its masses zero and contributes nothing. Summing absolute values proves the identity. It explains both what is controlled and why a rare class can have a larger conditional discrepancy.

This is a statement about the independent-word offset law. The proof below first treats \(9n/10\leq m\leq n\), then joins those comparisons through exact lifts. Translating this probability model into a statement about sampled integer trajectories also requires the valuation-word and first-passage arguments.

## Recovering a word from its rational offset

For a deterministic word \(a=(a_1,\ldots,a_r)\) of positive integers, write \(s_j=a_1+\cdots+a_j\), \(L=s_r\), and

\[
\begin{aligned}
T_r(a)&=\sum_{j=1}^r3^{j-1}2^{-s_j},\\
Z_r(a)&=2^L T_r(a)=\sum_{j=1}^r3^{j-1}2^{L-s_j}.
\end{aligned}
\tag{5}
\]

The cleared quantity \(Z_r(a)\) is a positive integer. Its last summand is \(3^{r-1}\), which is odd. Every preceding summand is even, because \(s_j<L\) for \(j<r\). Hence \(Z_r(a)\) is odd.

**Lemma 2 (Exact word recovery).** For each fixed \(r\geq1\), the map
\(T_r:\mathbb Z_{>0}^r\to\mathbb Z[1/2]\) is injective. Its inverse on its image is obtained by successively recovering the reduced dyadic denominator and removing the last summand.

**Proof.** Since \(Z_r(a)\) is odd, the reduced denominator of \(T_r(a)\) is exactly \(2^L\). Thus the value of \(T_r(a)\) determines \(L\). Subtract
\(3^{r-1}2^{-L}\). The result is exactly \(T_{r-1}(a_1,\ldots,a_{r-1})\). For \(r>1\), its reduced denominator determines \(s_{r-1}\), by the same parity argument. Continue until \(T_1=2^{-a_1}\). This recovers all the partial sums, and then \(a_j=s_j-s_{j-1}\), with \(s_0=0\). At \(r=1\) the first denominator already recovers the word. These operations undo (5) on its image, proving injectivity. ∎

For example,
\(T_3(2,1,3)=49/64\). The denominator first gives \(L=6\). Subtracting \(9/64\) leaves \(5/8\), whose denominator gives \(s_2=3\). Subtracting \(3/8\) leaves \(1/4\), giving \(s_1=2\). The successive differences are \(2,1,3\).

**Corollary 3 (Separation below a modulus).** Fix \(r,L,n\). On any set of length-\(r\) words of total \(L\) for which
\(0<Z_r(a)<3^n\), the map \(a\mapsto T_r(a)\bmod3^n\) is injective.

**Proof.** Equal residues of \(T_r\) give equal residues of the integer \(Z_r=2^LT_r\), since the multiplier is the same for both words. Two integers strictly between zero and \(3^n\) that are congruent modulo \(3^n\) are equal: their difference is a multiple of \(3^n\) of absolute value less than \(3^n\). Dividing by \(2^L\) gives equal rational offsets, so Lemma 2 gives equal words. ∎

Both the common denominator and the height bound have a role. Rational injectivity alone does not prevent collisions after modular reduction. The next estimate supplies a height bound on a large part of the random-word law.

## A quantitative bound for the cleared numerator

All logarithms below are natural unless a base is shown. Set

\[
\begin{gathered}
b=\log2,\qquad d=\log(4/3),\\
D=10C^2,\qquad t=n\log_2 3-D\log n,
\end{gathered}
\tag{6}
\]

where \(C\geq2\) is fixed. We take \(n\geq3\). The threshold lies a logarithmic distance below the exponent at which \(2^t\) would equal \(3^n\).

**Lemma 4 (Height bound).** Suppose a positive word satisfies, for every \(1\leq j\leq r\),

\[
\begin{gathered}
s_j\geq2j-C\bigl(\sqrt{j\log n}+\log n\bigr),\\
t<L\leq t+3C\log n.
\end{gathered}
\tag{7}
\]

Then, with \(K_0=1/[3(e^{d/2}-1)]\),

\[
0<Z_r(a)\leq K_0\,3^n n^{-C^2}.
\tag{8}
\]

In particular, once \(n^{C^2}>K_0\), Corollary 3 applies to every fixed-total family satisfying (7).

**Proof.** The lower bounds for the partial sums give

\[
T_r(a)\leq\frac13 n^{Cb}
\sum_{j=1}^r\exp\bigl(-dj+bC\sqrt{j\log n}\bigr).
\]

Completing a square, or applying \(2uv\leq u^2+v^2\), gives

\[
bC\sqrt{j\log n}
\leq\frac d2j+\frac{b^2C^2}{2d}\log n.
\]

The remaining sum is at most
\(\sum_{j\geq1}e^{-dj/2}=1/(e^{d/2}-1)\). Also
\(2^L\leq3^n n^{-Db+3Cb}\), by the upper bound for \(L\). Multiplying proves

\[
\begin{gathered}
Z_r(a)\leq K_0\,3^n n^{-\Lambda},\\
\Lambda=Db-4Cb-\frac{b^2C^2}{2d}.
\end{gathered}
\tag{9}
\]

We check the sign with explicit inequalities. Integrating \(1/x\) on \([1,2]\) gives \(1/2<b<1\), and integrating on \([1,4/3]\) gives \(d>1/4\). Therefore
\(Db>5C^2\), \(4Cb<4C\), and \(b^2C^2/(2d)<2C^2\). It follows that

\[
\Lambda>3C^2-4C\geq C^2,
\]

since \(C\geq2\). This proves (8). Positivity follows directly from (5). ∎

The constants are not optimized. The important comparison is between a quadratic allowance in \(C\) at the stopping threshold and the quadratic loss in the partial-sum bound. The displayed inequalities show that the allowance wins, uniformly in the word length.

## Stopping on events that depend only on the prefix

Fix the desired power \(p>0\), put \(B=p+2\), and choose

\[
C\geq\max\left\{2,\sqrt{12(B+3)},\frac{2(B+3)}d\right\}.
\tag{10}
\]

Use this \(C\) in (6). For \(1\leq r\leq n\), let \(E_r\) be the event that

\[
\begin{gathered}
|S_j-S_i-2(j-i)|\\
\leq C\bigl(\sqrt{(j-i)\log n}+\log n\bigr),\\
0\leq i<j\leq r.
\end{gathered}
\tag{11}
\]

The logarithm in this event is always \(\log n\), including when \(r<n\). This gives nested events \(E_n\subseteq E_r\).

**Lemma 5 (A disjoint family of good prefixes).** For all sufficiently large \(n\), depending only on \(p\), there is a finite disjoint family of events \(H_{r,L}\), each determined by \(A_1,\ldots,A_r\), with the following properties:

\[
\begin{gathered}
1\leq r\leq\lfloor17n/20\rfloor,\qquad
t<L\leq t+3C\log n,\\
\mathbb P\left(\bigcup_{r,L}H_{r,L}\right)
\geq1-2n^{-B-1}.
\end{gathered}
\tag{12}
\]

On \(H_{r,L}\), the prefix satisfies (7) and has total \(S_r=L\). There are at most \((3C+2)n^2\) possible pairs \((r,L)\).

**Proof.** An interval of length \(h\) has the geometric-sum law in the preceding concentration theorem. At the deviation
\(u=C(\sqrt{h\log n}+\log n)\), its two exponent bounds obey

\[
\frac{u^2}{12h}\geq\frac{C^2}{12}\log n,
\qquad \frac{du}{2}\geq\frac{dC}{2}\log n.
\]

By (10), both are at least \((B+3)\log n\). The failure probability for one interval is at most \(2n^{-B-3}\). There are \(n(n+1)/2\leq n^2\) nonempty intervals, so

\[
\mathbb P(E_n^c)\leq2n^{-B-1}.
\tag{13}
\]

For large enough \(n\), \(t>0\). Set \(R_n=\lfloor17n/20\rfloor\). On \(E_n\),

\[
S_{R_n}\geq2R_n-C\bigl(\sqrt{R_n\log n}+\log n\bigr)>t.
\tag{14}
\]

for sufficiently large \(n\). To justify the last strict inequality, divide by \(n\): the lower expression tends to \(17/10\), while \(t/n\) tends to \(\log_2 3<17/10\). The latter comparison is exact because \(3^{10}=59049<131072=2^{17}\). The error terms tend to zero since \(\log n/n\to0\). Thus a fixed threshold in \(n\) makes (14) hold for every later \(n\).

For \(1\leq r\leq R_n\) and an integer \(L\), define

\[
H_{r,L}=\{S_{r-1}\leq t<S_r,\ S_r=L\}\cap E_r.
\tag{15}
\]

All increments are positive, so there can be only one crossing index \(r\) and one total \(L\) on a word. These events are disjoint. They depend only on the stated prefix. By (14), every word in \(E_n\) belongs to one of them.

The one-entry case of (11) bounds the last increment by

\[
A_r\leq2+C(\sqrt{\log n}+\log n)\leq3C\log n,
\]

because \(\log n\geq1\) and \(C\geq2\). At a crossing, \(S_{r-1}\leq t\), so this proves the range for \(L\) in (12). The cases \(i=0,j\leq r\) of (11) give the partial-sum bounds (7). There are at most \(3C\log n+2\) integers in the indicated interval for \(L\), and at most \(n\) choices of \(r\). Since \(\log n\leq n\), their product is at most \((3C+2)n^2\). Finally, (13) gives the probability assertion. ∎

The distinction between \(E_r\) and \(E_n\) is important. The full event \(E_n\) controls the probability of the discarded part, but the retained pieces use only \(E_r\). Imposing \(E_n\) on each piece would also restrict its future coordinates and would not justify an independent tail. The union in (12) may be larger than \(E_n\); that is harmless because every retained piece has precisely the properties needed for the next calculation.

## Exact prefix mass and the independent tail

Write \(q_{r,L}=\mathbb P(H_{r,L})\), and define a subprobability mass function on \(G_n\) by

\[
f_{r,L}(y)=\mathbb P(T_r\equiv y\pmod{3^n},\ H_{r,L}).
\tag{16}
\]

For large enough \(n\), Lemma 4 and Corollary 3 show that at most one allowed length-\(r\) word of total \(L\) maps to each \(y\). The probability of that word is exactly
\(\prod_{i=1}^r2^{-a_i}=2^{-L}\). Thus

\[
\begin{gathered}
f_{r,L}(y)\in\{0,2^{-L}\},\\
\sum_y f_{r,L}(y)^2=2^{-L}q_{r,L}.
\end{gathered}
\tag{17}
\]

This equality retains the mass of the event. There is no division by \(q_{r,L}\), so it remains valid even when that mass is zero.

On \(S_r=L\), direct splitting of the offset sum gives

\[
T_n=T_r+3^r2^{-L}T'_{n-r},
\tag{18}
\]

where \(T'_{n-r}\) is formed in the same way from \(A_{r+1},\ldots,A_n\). For each fixed \(r,L\), these future variables are independent of the entire prefix and of \(H_{r,L}\). This is ordinary independence of disjoint coordinate sets; after fixing a prefix word, summing over future words gives the original product law, with total mass one.

Define

\[
\begin{gathered}
\phi_{r,L}:G_{n-r}\longrightarrow G_n,\\
\phi_{r,L}(x)=3^r2^{-L}x\pmod{3^n}.
\end{gathered}
\tag{19}
\]

This map is well defined because adding \(3^{n-r}\) to \(x\) changes its image by a multiple of \(3^n\). It is an additive injection: an element maps to zero exactly when its representative is divisible by \(3^{n-r}\). Its image is the subgroup of multiples of \(3^r\). The inverse on that subgroup divides an integer representative by \(3^r\) and multiplies by \(2^L\), modulo \(3^{n-r}\); different representatives give the same result.

Let \(g_{r,L}=(\phi_{r,L})_*\mu_{n-r}\), a probability law on \(G_n\). Equations (16)–(19) imply the exact decomposition

\[
\begin{gathered}
\mu_n=e+\sum_{r,L}f_{r,L}*g_{r,L},\\
\|e\|_1\leq2n^{-B-1},\qquad e\geq0.
\end{gathered}
\tag{20}
\]

Here \(e\) is the offset law restricted to the complement of the disjoint union in (12). To check (20) at a state \(y\), sum over its possible prefix value \(z\). The probability of the prefix event and value is \(f_{r,L}(z)\); the probability that its independent tail image equals \(y-z\) is \(g_{r,L}(y-z)\). Their product, summed over \(z\), is exactly the convolution.

The second factor is a probability law on a subgroup, not a uniform law. Its usefulness comes from its Fourier coefficients at the particular frequencies left after a quotient observation.

## Which characters the tail must cancel

Assume for now that \(9n/10\leq m<n\). The frequencies discarded by \(P_{m,n}\) are

\[
\mathcal D_{m,n}=\{\xi\in G_n:3^{n-m}\nmid\xi\},
\tag{21}
\]

by [the exact quotient-frequency calculation](NT-COLLATZ-05.md#frequencies-that-distinguish-the-missing-information). Such a frequency is nonzero. Write \(\xi=3^j\eta\), where \(0\leq j<n-m\) and \(3\nmid\eta\). Pulling its character back along (19) gives

\[
\widehat g_{r,L}(\xi)
=\widehat\mu_{n-r}(\xi2^{-L}\bmod3^{n-r}).
\tag{22}
\]

The power of two is invertible and therefore does not change the power of three dividing the frequency. Moreover,

\[
k:=n-r-j>m-r\geq n/20,
\tag{23}
\]

since \(r\leq17n/20\). In particular \(j<n-r\), so the pulled-back character is nontrivial and has exact order \(3^k\). Its coefficient reduces to a full-order coefficient of \(\mu_k\), by [the character-order identity](NT-COLLATZ-11.md#character-order-and-mixing-inside-observation-classes). Consequently, for every fixed \(\beta>0\),

\[
\delta_{r,L}:=\max_{\xi\in\mathcal D_{m,n}}
|\widehat g_{r,L}(\xi)|
\leq C_\beta20^\beta n^{-\beta}.
\tag{24}
\]

The constant is independent of the chosen prefix. This is exactly where a sufficiently long unused tail matters. The ambient group has \(3^n\) states, but the relevant decay parameter is the surviving character order \(k\), which (23) keeps proportional to \(n\).

## Combining collision mass with cancellation

**Proposition 6 (Mixing between comparable scales).** For each \(p>0\), there is a constant \(K'_p\) such that

\[
\begin{gathered}
\|\mu_n-P_{m,n}\mu_n\|_1\leq K'_p n^{-p},\\
9n/10\leq m\leq n.
\end{gathered}
\tag{25}
\]

**Proof.** The case \(m=n\) has zero left side. For \(m<n\), take \(n\) large enough for all preceding estimates, and apply the [several-piece collision estimate](NT-COLLATZ-05.md#an-energy-estimate-for-mixing-inside-fibres) to (20). It gives

\[
\begin{aligned}
\|\mu_n-P_{m,n}\mu_n\|_1
\leq{}&4n^{-B-1}\\
&+\sum_{r,L}\delta_{r,L}
\left(3^n\sum_y f_{r,L}(y)^2\right)^{1/2}.
\end{aligned}
\tag{26}
\]

Since \(L>t\), equations (6) and (17) give

\[
3^n\sum_y f_{r,L}(y)^2
=3^n2^{-L}q_{r,L}\leq n^{Db}q_{r,L}.
\tag{27}
\]

The events are disjoint, so \(\sum q_{r,L}\leq1\). Cauchy–Schwarz and the bound on the number of pairs give

\[
\sum_{r,L}\sqrt{q_{r,L}}
\leq\sqrt{(3C+2)n^2}\sqrt{\sum_{r,L}q_{r,L}}
\leq\sqrt{3C+2}\,n.
\tag{28}
\]

Combining (24), (26)–(28) yields

\[
\begin{aligned}
\|\mu_n-P_{m,n}\mu_n\|_1
\leq{}&4n^{-B-1}\\
&+C_\beta20^\beta\sqrt{3C+2}\,n^{-\beta+Db/2+1}.
\end{aligned}
\tag{29}
\]

Choose \(\beta=p+Db/2+2\). Recall that \(B=p+2\) and that \(C,D\) were already fixed in terms of \(p\). The first power on the right is \(-p-3\), and the second is \(-p-1\). Thus (25) follows for large \(n\), with a constant depending only on \(p\). If the argument requires \(n\geq n_0(p)\), enlarge the constant to at least \(2n_0(p)^p\). For the remaining positive integers \(n<n_0(p)\), the elementary bound \(\|\mu_n-P_{m,n}\mu_n\|_1\leq2\) then proves (25). ∎

The two inputs have different jobs. The Fourier bound supplies any chosen negative power of \(n\). Integer separation ensures that the collision factor loses only a fixed positive power of \(n\), rather than a factor exponential in \(n\). Choosing \(\beta\) after that loss has been calculated closes the estimate. This is why counting distinct prefix values is analytically useful.

## Passing from nearby scales to arbitrary scales

For \(a\leq b\leq n\), uniform lifts compose exactly:

\[
U_{b,n}U_{a,b}=U_{a,n}.
\tag{30}
\]

Indeed, the two factors multiplying a mass at a residue are \(3^{b-n}\) and \(3^{a-b}\), whose product is \(3^{a-n}\); reduction of a residue first modulo \(3^b\) and then modulo \(3^a\) equals direct reduction modulo \(3^a\). Also set \(U_{n,n}=I\).

**Proof of Theorem 1.** If \(m=n\), the discrepancy is zero. If \(18\leq m<n\), start with \(n_0=m\) and define

\[
n_{i+1}=\min\{n,\lfloor10n_i/9\rfloor\}
\]

until \(n_s=n\). This occurs after finitely many steps because \(\lfloor10h/9\rfloor>h\) for every integer \(h\geq18\). Each successive pair satisfies
\(n_i\geq9n_{i+1}/10\). Before the final step,

\[
n_{i+1}=\lfloor10n_i/9\rfloor
\geq10n_i/9-1\geq19n_i/18.
\tag{31}
\]

Consequently \(n_i\geq(19/18)^i m\) for every index \(i<s\); no growth estimate for the truncated final endpoint is required.

By (30),

\[
\mu_n-U_{m,n}\mu_m
=\sum_{i=0}^{s-1}U_{n_{i+1},n}
\left(\mu_{n_{i+1}}-U_{n_i,n_{i+1}}\mu_{n_i}\right).
\tag{32}
\]

Each positive term in the sum cancels the next negative one after lifting. Use the isometry (2), compatibility (3), and Proposition 6. The norm of the \(i\)-th summand is at most
\(K'_p n_{i+1}^{-p}\leq K'_p n_i^{-p}\). Therefore

\[
\|\mu_n-U_{m,n}\mu_m\|_1
\leq K'_p\sum_{i=0}^{s-1}n_i^{-p}
\leq\frac{K'_p}{1-(18/19)^p}\,m^{-p}.
\tag{33}
\]

For \(1\leq m<18\), the left side is at most two. Taking
\(K_p\) at least \(2\cdot18^p\), as well as the constant in (33), proves (4) for every pair of positive integers \(m\leq n\). ∎

The number of intermediate scales is not the error bound. Their sizes grow geometrically, so their errors form a summable geometric series. This is the probability-law analogue of the summable-scale reasoning in [First passage and transport across scales](NT-COLLATZ-04.md#geometrically-separated-logarithmic-scales).

## Exercises

### 1. Recovering all partial sums

Starting only from the length three and the rational value \(97/128\), apply Lemma 2 to recover the word. Why can no cancellation hide the total exponent in its reduced denominator?

**Solution.** The reduced denominator gives \(s_3=7\). Remove \(3^2/2^7=9/128\), obtaining \(88/128=11/16\); hence \(s_2=4\). Remove \(3/2^4=3/16\), obtaining \(8/16=1/2\); hence \(s_1=1\). Taking differences gives \((1,3,3)\). At each nonempty stage, the cleared numerator is odd: the final term is an odd power of three, and all previous terms contain a positive power of two. An odd numerator cannot cancel a factor of two from its denominator.

### 2. What a small modulus can forget

For all positive words of length two and total five, compute the cleared numerator \(Z_2\) and its residues modulo three and nine. Explain which conclusion of Corollary 3 holds modulo 27, and why its height hypothesis is sufficient rather than necessary.

**Solution.** Equation (5) gives \(Z_2=2^{5-a_1}+3\). The complete list is

| Word | Cleared numerator | Residue modulo three | Residue modulo nine |
| --- | ---: | ---: | ---: |
| \((1,4)\) | 19 | 1 | 1 |
| \((2,3)\) | 11 | 2 | 2 |
| \((3,2)\) | 7 | 1 | 7 |
| \((4,1)\) | 5 | 2 | 5 |

Modulo three there are two pairs of collisions. Multiplication by the common invertible denominator \(2^{-5}\) does not remove those collisions. Modulo 27 all four positive numerators are less than the modulus, so Corollary 3 proves injectivity of the offsets. The residues modulo nine happen to be distinct as well, although two numerators exceed nine. Thus the height hypothesis guarantees injectivity but is not a necessary condition for every finite family.

### 3. Collision mass before and after conditioning

In Exercise 2 let the entries be independent with masses \(2^{-a}\), and retain the event that the two entries sum to five. Work modulo nine. Compute its mass \(q\), the collision sum of its restricted offset law \(f\), and the collision sum after conditioning on the event.

**Solution.** Each of the four words has probability \(2^{-5}=1/32\), so \(q=1/8\). Their offset residues are distinct, since their numerator residues are distinct and multiplication by \(2^{-5}\) is a bijection modulo nine. Thus

\[
\sum_y f(y)^2=4(1/32)^2=1/256=2^{-5}q.
\]

The conditional law gives mass \(1/4\) to each residue and has collision sum \(4(1/4)^2=1/4\). To use that conditional law in the original mixture, its probability weight \(q\) must also be retained. Omitting the weight replaces the restricted law by a different law and loses the factor \(q^2\) in the collision sum.

### 4. A bound independent of the number of scales

Verify (32) for three successive comparisons \(a<b<c<n\). If every successive-scale discrepancy is at most \(K h^{-2}\), where \(h\) is its lower exponent, and the lower exponents grow by at least \(19/18\), give the resulting bound in terms of the first exponent \(a\).

**Solution.** The proposed decomposition is

\[
\begin{aligned}
\mu_n-U_{a,n}\mu_a
={}&U_{b,n}(\mu_b-U_{a,b}\mu_a)\\
&+U_{c,n}(\mu_c-U_{b,c}\mu_b)\\
&+(\mu_n-U_{c,n}\mu_c).
\end{aligned}
\]

Expansion and (30) cancel the lifted \(\mu_b\) and \(\mu_c\) terms, leaving the left side. Isometry and the triangle inequality bound a chain of any finite length by

\[
K a^{-2}\sum_{i\geq0}(18/19)^{2i}
=\frac{361K}{37}\,a^{-2}.
\]

The last equality uses \(1-324/361=37/361\). There is no multiplicative factor equal to the number of comparisons.

## From random offsets to orbit estimates

The theorem keeps the coarse distribution exactly and averages only within its fibres. Its proof identifies the work done by each ingredient: denominator recovery gives rational injectivity; a height estimate turns this into modular separation; prefix-only events preserve a genuinely independent tail; and the collision estimate combines that tail's cancellation with the spread of the prefix. Compatible lifts then extend the estimate to every pair of scales.

These methods belong to arithmetic probability and harmonic analysis, not only to the Collatz problem. For the Collatz application, another transition remains: an independent geometric word must be compared with valuation words of sampled integer orbits, and the resulting estimates must be transported through first-passage locations. [Geometric waiting times and controlled conditioning](NT-COLLATZ-06.md#how-much-information-a-residue-class-provides) supplies the finite-residue comparison; [First passage and transport across scales](NT-COLLATZ-04.md) explains the relevant transport mechanism. The fine-scale theorem supplies one precise distributional input, not a conclusion about the convergence of every integer orbit.

## References

- Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, [arXiv:1909.03562v7](https://arxiv.org/abs/1909.03562v7), the fine-scale mixing proposition and Section 6, including injectivity and separation of offsets. The theorem above is this established mixing result, proved here from the preceding Fourier estimate with independently expressed prefix selection, explicit maps and probability weights.
- Keith Conrad, *Characters of finite abelian groups (short version)*, [Section 4](https://kconrad.math.uconn.edu/blurbs/grouptheory/charthyshort.pdf). The exact Fourier identities and quotient-energy estimate used here have complete proofs in the preceding finite-group probability lesson.
