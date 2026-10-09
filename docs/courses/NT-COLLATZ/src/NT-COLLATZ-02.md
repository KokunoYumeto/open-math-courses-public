# Symbolic itineraries and affine composition

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, proofs and exercises: CC0 1.0.*

A rule with several branches has two records: the states it visits and the branches it uses. A **symbolic itinerary** records the second. Such a record is useful only when we know which itineraries can occur and how much of the original trajectory they determine.

This lesson develops a concrete answer for affine branches. We first compose the branches exactly. We then impose the integer restrictions that turn a formal word into an actual orbit. For the shortcut Collatz map, a word of length \(k\) specifies exactly one residue class modulo \(2^k\). This connects symbolic dynamics with congruence arithmetic and, at the end, with a finite probability experiment.

We use integer arithmetic, induction, and the definitions of iteration from [Return maps and exact changes of clock](NT-COLLATZ-01.md). Congruence means that the difference of two integers is a multiple of the modulus. The division algorithm and the basic rules for fractions are assumed. No measure theory or conjecture about eventual convergence is needed. Terras and Everett are historical sources for finite parity coding. Laarhoven and de Weger discuss its graph-theoretic form; Inselmann uses the affine and concatenation identities in quantitative orbit estimates. Full references appear below.

## A word is not yet an orbit

Let a set \(X\) be partitioned into disjoint sets \(X_b\), indexed by symbols \(b\). Suppose a map \(F:X\to X\) uses the rule \(f_b\) on \(X_b\). The itinerary of a point \(x\) begins with \(b_0,\ldots,b_{k-1}\) precisely when

\[
F^i(x)\in X_{b_i}\qquad(0\leq i<k).
\]

The set of these starting points is the **cylinder** of the word. On this set, induction gives

\[
F^k(x)=f_{b_{k-1}}\circ\cdots\circ f_{b_0}(x).
\]

The order matters: the earliest rule is on the right. The composition may make sense on a larger space, but it describes \(F^k\) only on its cylinder. In particular, algebraically composing branches does not prove that the word is realizable.

Our running example is

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\qquad n\in\mathbb N_+.
\]

The branches extend to affine maps on the rational numbers:

\[
f_b(x)=\frac{3^b x+b}{2},\qquad b\in\{0,1\}.
\]

For a binary word \(w=(b_0,\ldots,b_{k-1})\), let \(\Phi_w=f_{b_{k-1}}\circ\cdots\circ f_{b_0}\), with the empty word giving the identity. The cylinder \(C_w\subseteq\mathbb N_+\) consists of the starts whose first \(k\) parities are \(w\).

## Keeping the additive term

Put \(s_i=b_0+\cdots+b_{i-1}\), with \(s_0=0\), and define

\[
A_w=\sum_{i=0}^{k-1} b_i2^i3^{s_k-s_{i+1}}.
\]

Every exponent is nonnegative, and \(A_w\) is a nonnegative integer. An empty sum is zero.

**Theorem 1 (Affine formula).** For every binary word of length \(k\) and every \(x\in\mathbb Q\),

\[
\Phi_w(x)=\frac{3^{s_k}x+A_w}{2^k}.
\]

In particular, this equals \(T^k(n)\) when \(n\in C_w\).

**Proof.** For the empty word the numerator is \(x\). Appending a bit \(b\) to a length-\(k\) word changes the affine expression to

\[
f_b(\Phi_w(x))
=\frac{3^{s_k+b}x+3^b A_w+b2^k}{2^{k+1}}.
\]

In the proposed sum for the new numerator, each old term acquires a factor \(3^b\), and the new last term is \(b2^k\). This proves the formula by induction. The cylinder identity from the preceding section gives its application to \(T\). ∎

The coefficient of \(x\) alone is not the iterate. The term \(A_w\) records every addition along the way. For instance, repeated use of \(f_1\) gives

\[
\Phi_{(1,\ldots,1)}(x)=\frac{3^k x+(3^k-2^k)}{2^k}.
\]

Indeed, the recurrence in the proof gives \(A_{k+1}=3A_k+2^k\), and substitution verifies \(A_k=3^k-2^k\), starting from zero. Both terms matter even before any question of asymptotic estimates arises.

## Joining two blocks

Let \(u\) and \(v\) have lengths \(a\) and \(b\), and let \(s(u)\) and \(s(v)\) denote their numbers of ones. Write \(uv\) for chronological concatenation: first follow \(u\), then \(v\).

**Proposition 2 (Composition coordinates).**

\[
\begin{aligned}
s(uv)&=s(u)+s(v),\\
A_{uv}&=3^{s(v)}A_u+2^a A_v,\\
\Phi_{uv}&=\Phi_v\circ\Phi_u.
\end{aligned}
\]

The realized cylinders satisfy

\[
C_{uv}=\{n\in C_u:T^a(n)\in C_v\}.
\]

**Proof.** Counts add. Substituting the affine formula for \(u\) into the one for \(v\) gives

\[
\Phi_v(\Phi_u(x))
=\frac{3^{s(u)+s(v)}x+3^{s(v)}A_u+2^a A_v}{2^{a+b}}.
\]

The cylinder statement follows by separating the parity tests before and after time \(a\). This also proves that the algebraic composition acts on exactly the required starts when it is used as an orbit formula. ∎

One can store these coordinates in an integer matrix:

\[
M_w=\begin{pmatrix}3^{s(w)}&A_w\\0&2^{|w|}\end{pmatrix},
\qquad M_{uv}=M_v M_u.
\]

To read the associated rational map, apply the matrix to \((x,1)\) and divide the first coordinate by the second. Its denominator is positive. Matrix multiplication explains the composition law; the cylinder still supplies its integer domain.

Another exact coordinate is \(r_w=A_w/(2^{|w|}3^{s(w)})\). Retaining the length and count makes this a reversible change of coordinates: \(A_w=2^{|w|}3^{s(w)}r_w\). Dividing the numerator formula by \(2^{a+b}3^{s(u)+s(v)}\) gives

\[
r_{uv}=2^{-b}r_u+3^{-s(u)}r_v.
\]

Neither term may be dropped. This identity describes the same composition using rational rather than integer coordinates.

## The arithmetic domain of a word

We now prove that every finite binary word occurs, and identify all its starting integers. For this proof only, extend \(T\) to nonnegative integers by \(T(0)=0\). This lets us use the representative 0 of a residue class without changing any positive orbit.

**Lemma 3 (Lifting a finite itinerary).** If nonnegative integers \(m,n\) satisfy \(n-m=2^k t\) for an integer \(t\), their first \(k\) parities agree. If that common word has prefix counts \(s_i\), then

\[
T^i(n)-T^i(m)=3^{s_i}2^{k-i}t\qquad(0\leq i\leq k).
\]

**Proof.** At \(i=0\) the difference is the assumed multiple of \(2^k\). Suppose the formula holds at an index \(i<k\). The difference is even, so the two current states have the same parity \(b_i\). Subtracting their branch formulas cancels the additive term and divides their difference by 2 after multiplication by \(3^{b_i}\). This proves the next formula and the next shared parity test. Induction completes the proof. ∎

**Theorem 4 (Words and residue classes).** For each length-\(k\) binary word \(w\), there is a unique \(c_w\) with \(0\leq c_w<2^k\) such that

\[
C_w=\{n\in\mathbb N_+:n\equiv c_w\pmod{2^k}\}.
\]

Below we write \(r=c_w\) when a single cylinder is fixed.

**Proof.** The empty word corresponds to the only class modulo 1. Suppose the length-\(k\) words correspond bijectively to the classes modulo \(2^k\). A class represented by \(r\) has exactly two lifts modulo \(2^{k+1}\), represented by \(r\) and \(r+2^k\). Lemma 3 says that both have the same first \(k\) bits. Their states at time \(k\) differ by \(3^{s_k}\), which is odd. Exactly one therefore has next bit 0, and exactly one has next bit 1. This proves existence and uniqueness for each extended word. Lemma 3 also shows that every integer in a chosen lifted class has that itinerary. Conversely, an integer with the extended itinerary must be in its prefix class and then in the uniquely specified lift. The induction proves the statement. Every class has a positive representative, including the class represented by zero. ∎

For a fixed word, write \(r\) for its representative, \(s=s(w)\), and \(A=A_w\). On its cylinder, \(T^k\) is an injective map onto the arithmetic progression

\[
\left\{\frac{3^s r+A}{2^k}+3^s t:
t\in\mathbb Z,\ r+2^k t>0\right\}.
\]

Its inverse on that image is \(y\mapsto(2^k y-A)/3^s\). The formula follows by substituting \(n=r+2^k t\) into Theorem 1. It proves both directions: every allowed \(t\) gives a cylinder point and its image, and the displayed inverse returns that point. Thus a word does not identify a single positive start. It identifies a congruence class; the additional integer \(t\) locates the start within that class.

## An actual concatenation

Consider the shortcut trajectory

\[
37\to56\to28\to14\to7\to11\to17\to26\to13.
\]

The first block has word \(u=(1,0,0,0,1)\), length 5 and two odd steps. The next has \(v=(1,1,0)\), length 3 and two odd steps. Directly from the sum in Theorem 1,

\[
A_u=3+16=19,\qquad A_v=3+2=5.
\]

Consequently

\[
A_{uv}=9\cdot19+32\cdot5=331,
\]

and

\[
\frac{9\cdot37+19}{32}=11,
\qquad \frac{9\cdot11+5}{8}=13,
\qquad \frac{81\cdot37+331}{256}=13.
\]

Here \(C_u\) is the class 5 modulo 32, \(C_v\) the class 3 modulo 8, and \(C_{uv}\) the class 37 modulo 256. This last description follows from Theorem 4 because the displayed trajectory realizes that word. The two separate congruence tests are compatible only after the second is imposed on the landing value 11, not on the original start 37.

There is also a time coordinate. One shortcut step uses one ordinary step at an even state and two at an odd state. Hence a block of length \(k\) with \(s\) ones consumes \(k+s\) ordinary steps. This follows by adding the costs at each step. For the example, the first block costs 7 ordinary steps, the second costs 5, and the combined block costs 12. The identity \((a+s(u))+(b+s(v))=(a+b)+s(uv)\) expresses the compatibility of time with concatenation.

## A finite probability law from an exact bijection

Choose a starting integer uniformly from any \(2^k\) consecutive positive integers. Each residue class modulo \(2^k\) occurs once, so Theorem 4 implies that each length-\(k\) word has probability \(2^{-k}\). In particular, specifying any \(j\) of the bits leaves exactly \(2^{k-j}\) words, so that specification has probability \(2^{-j}\). This proves that the first \(k\) bits in this experiment are independent fair bits.

The probability of exactly \(h\) odd steps is therefore

\[
2^{-k}\binom{k}{h}\qquad(0\leq h\leq k),
\]

because choosing the \(h\) positions of the ones specifies the word. This is an exact counting theorem for the stated finite experiment.

For a uniform start in \(\{1,\ldots,X\}\), where \(X\) is any positive integer, each word count differs from \(X/2^k\) by at most 1: divide the interval into complete blocks of length \(2^k\) and one incomplete block. Consequently

\[
\sum_{w\in\{0,1\}^k}
\left|\mathbb P(\text{word}=w)-2^{-k}\right|
\leq\frac{2^k}{X}.
\]

The dependence on \(k\) is essential. This bound tends to zero for fixed \(k\) as \(X\) grows, and more generally whenever \(2^k/X\to0\). It does not provide a small error for an arbitrarily long itinerary at a fixed cutoff. The next lesson studies explicitly how sampling measures enter such statements.

## Exercises with solutions

**Exercise 1.** Find the cylinder and affine formula for \(w=(1,0,1)\).

**Solution.** The prefix counts are \(0,1,1,2\), so \(A_w=3+4=7\), and \(\Phi_w(x)=(9x+7)/8\). The start 1 has trajectory \(1,2,1,2\), hence realizes the word. Theorem 4 gives \(C_w=\{1+8t:t\geq0\}\). The landing points are \(2+9t\), and the inverse there is \((8y-7)/9\).

**Exercise 2.** Reverse the two blocks in the worked example. Compute the formal composition and decide whether 37 realizes the reversed word.

**Solution.** Reversal gives \(A_{vu}=9\cdot5+8\cdot19=197\), so \(\Phi_{vu}(x)=(81x+197)/256\). The word begins with \(1,1,0\), whereas 37 begins with \(1,0,0\); thus 37 is not in its cylinder. Applying the rational formula at 37 is not computing its eighth iterate. The different numerators also show directly that the two affine block maps do not commute.

**Exercise 3.** A length-\(k\) word with \(s\) ones contains a periodic point \(n\), returning after these \(k\) shortcut steps. Derive its value. Is the resulting rational number automatically a positive periodic point?

**Solution.** The equation \(T^k(n)=n\) gives \((2^k-3^s)n=A_w\). For \(k\geq1\), the coefficient cannot vanish: when \(s=0\), \(3^s=1<2^k\); when \(s\geq1\), \(3^s\) is odd and \(2^k\) is even. Thus the only candidate is \(n=A_w/(2^k-3^s)\). It must still be a positive integer in \(C_w\). These checks are sufficient as well, because Theorem 1 then computes the actual iterate. The word \((0)\) gives only 0, outside the positive domain. The word \((1,0)\) gives 1 and realizes its two-step shortcut cycle. No assertion of least period follows without checking earlier returns.

**Exercise 4.** For a uniform start among 32 consecutive positive integers, what is the probability that the first five bits have exactly two ones? What if the start is uniform in \(\{1,\ldots,1000\}\)?

**Solution.** The first probability is \(\binom52/32=5/16\). For the second experiment, each of the ten words in question has count within 1 of \(1000/32\). Summing those ten count errors gives a probability within \(10/1000\) of \(5/16\). This follows from the cylinder counts without assuming an infinite random orbit.

## What carries forward

The composition of branches belongs to elementary algebra. The cylinder calculation belongs to arithmetic. The probability law comes from counting those cylinders under a specified distribution of starts. These are three connected arguments, not three interchangeable descriptions. Keeping them separate lets us ask the right question when we change the map or the sampling rule: which compositions remain valid, which words are realized, and how much weight does each cylinder carry?

Continue with [Pushforward measures and logarithmic sampling](NT-COLLATZ-03.md). The exact coordinates developed here will remain useful whenever successive orbit segments are joined.

## References

Thijs Laarhoven and Benne de Weger, *The Collatz conjecture and De Bruijn graphs*, [arXiv:1209.3495v1](https://arxiv.org/abs/1209.3495v1), §2. Finite parity encoding and the corresponding modular graphs.

Manuel Inselmann, *An Approximation of the Collatz Map and a Lower Bound for its Average Total Stopping Time*, [arXiv:2402.03276v3](https://arxiv.org/abs/2402.03276v3), §§1.2 and 2. Parity counts, affine remainder and concatenation in orbit estimates.

Riho Terras, *A stopping time problem on the positive integers*, Acta Arithmetica **30** (1976), 241–252. [DOI: 10.4064/aa-30-3-241-252](https://doi.org/10.4064/aa-30-3-241-252).

C. J. Everett, *Iteration of the number-theoretic function f(2n)=n, f(2n+1)=3n+2*, Advances in Mathematics **25** (1977), 42–45. [DOI: 10.1016/0001-8708(77)90087-1](https://doi.org/10.1016/0001-8708(77)90087-1).
