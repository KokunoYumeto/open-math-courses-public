# Return maps and exact changes of clock

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, exercises and diagram: CC0 1.0.*

When studying an iterated rule, we need not record every step. We can record successive visits to a chosen set, keeping the times between visits. This produces a **return map**. The central questions are what the shorter record preserves, how to recover the original clock, and what is lost if the waiting times are discarded.

We will prove the general return-clock formula, then work it out completely for a map on positive integers. The Collatz rule halves an even number and replaces an odd number by three times that number plus one. Starting with 3 gives

\[
3\longrightarrow10\longrightarrow5\longrightarrow16
\longrightarrow8\longrightarrow4\longrightarrow2\longrightarrow1.
\]

There are good reasons to record fewer of these steps. One can combine an odd step with the division by two that necessarily follows it. One can also record only the odd numbers. These choices produce different maps and different notions of elapsed time. They do not change the least value attained along the orbit.

This example makes the general distinction visible: counting returns is not the same as counting individual steps. We will identify the corresponding times, reconstruct every omitted state, and determine why the least value survives this particular change of record. The last property depends on the values inside the omitted blocks; it is not automatic for return maps.

We assume induction, arithmetic of positive integers and the well-ordering principle: every nonempty set of positive integers has a least member. The divisibility facts needed below are proved here. No probability or assumption that Collatz orbits reach 1 is needed. Tao's *Almost all orbits of the Collatz map attain almost bounded values*, §1.2, is a reference for the three maps and the orbit-minimum identity. Terras's *A stopping time problem on the positive integers* is an earlier reference for the shortened iteration. The arguments below give the clock conversion in full, independently of any density theorem.

## Recording visits instead of steps

Let \(X\) be a set, let \(F:X\to X\), and choose a subset \(A\subseteq X\). Define \(F^0(x)=x\) and \(F^{j+1}(x)=F(F^j(x))\). For \(a\in A\), its **first positive return time** is

\[
\tau(a)=\min\{r\geq1:F^r(a)\in A\},
\]

when that set is nonempty. Suppose for this section that it is nonempty for every \(a\in A\). The **induced map** is then the well-defined map

\[
R:A\longrightarrow A,\qquad R(a)=F^{\tau(a)}(a).
\]

Fix \(a\in A\) and set

\[
\Theta_0=0,\qquad
\Theta_j=\sum_{i=0}^{j-1}\tau(R^i(a)).
\]

**Theorem A (Return-clock formula).** For every \(j\geq0\),

\[
F^{\Theta_j}(a)=R^j(a).
\]

The map \(j\mapsto\Theta_j\) is a strictly increasing bijection from the nonnegative integers onto the times \(t\) for which \(F^t(a)\in A\). Its inverse counts the earlier visits to \(A\). Every time \(t\geq0\) has a unique representation

\[
t=\Theta_j+r,\qquad 0\leq r<\tau(R^j(a)),
\]

and at that time \(F^t(a)=F^r(R^j(a))\).

**Proof.** The formula at \(j=0\) is the identity. If it holds at \(j\), then applying \(F^{\tau(R^j(a))}\) proves it at \(j+1\). The definition of first return excludes visits strictly between these two times. All return times are positive integers, so \(\Theta_j\geq j\). Thus the listed times increase without bound, and their half-open intervening intervals partition the nonnegative integers. This proves the claimed description of every visit, the unique representation of \(t\), and the state formula. Exactly \(j\) earlier visits precede \(\Theta_j\), giving the inverse. ∎

This reconstruction uses the original rule \(F\). The abstract data \(R\) and \(\tau\) alone do not specify the intermediate states of a different, otherwise unknown system. Likewise, the assumption that every point of \(A\) returns must be justified in an application. It is not an assumption that every trajectory eventually enters any smaller target set.

For a first example, let \(X=\{0,1,2,3,4,5\}\) and let \(F\) add 1 modulo 6. Choose \(A=\{0,2,5\}\). The induced orbit is \(0\to2\to5\to0\), and the return times at those points are \(2,3,1\). Its accumulated times are \(0,2,5,6,8,11,\ldots\), not \(0,1,2,3,\ldots\). Theorem A recovers the six-step original cycle from the three-return cycle.

Even a minimum can be lost by recording visits. For the cycle \(4\to1\to7\to4\), recording only \(A=\{4,7\}\) changes the least recorded value from 1 to 4. Below we will prove that the even blocks in the Collatz example have a special property that prevents this loss.

## Odd parts and powers of two

Write \(\mathbb N_+=\{1,2,3,\ldots\}\), \(\mathbb N_0=\{0,1,2,\ldots\}\), and \(\mathcal O=\{1,3,5,\ldots\}\). An integer is odd when it is not divisible by 2.

**Lemma 1.** Each \(n\in\mathbb N_+\) has a unique expression

\[
n=2^a m,\qquad a\in\mathbb N_0,\quad m\in\mathcal O.
\]

**Proof.** If \(n\) is even, divide it by 2 and repeat while the quotient is even. Every division strictly decreases a positive integer, so the procedure must terminate. Equivalently, infinitely many divisions would give an infinite strictly decreasing sequence of positive integers; its set of values would have a least element, followed by a smaller one, contradicting well-ordering. At termination the quotient \(m\) is odd. If there were two expressions \(2^a m=2^b u\) with \(m,u\) odd and \(a<b\), cancellation would give \(m=2^{b-a}u\), which is even. Interchanging the expressions rules out \(b<a\). Thus \(a=b\) and \(m=u\). ∎

The exponent \(a\) is called the **2-adic valuation** of \(n\), denoted \(\nu_2(n)\). The word “2-adic” here needs no additional number system: it just counts the factors of 2. The **odd part** is

\[
\pi(n)=\frac{n}{2^{\nu_2(n)}}.
\]

For instance, \(40=2^3\cdot5\), so \(\nu_2(40)=3\) and \(\pi(40)=5\). Lemma 1 gives inverse bijections

\[
\begin{aligned}
\mathbb N_0\times\mathcal O&\longrightarrow\mathbb N_+,
&(a,m)&\longmapsto2^a m,\\
\mathbb N_+&\longrightarrow\mathbb N_0\times\mathcal O,
&n&\longmapsto(\nu_2(n),\pi(n)).
\end{aligned}
\]

In particular, retaining both coordinates loses no information. Retaining only \(\pi(n)\) forgets the exponent: the fibre over an odd number \(m\) is exactly \(\{m,2m,4m,8m,\ldots\}\).

## The three rules

The **ordinary Collatz map** \(C:\mathbb N_+\to\mathbb N_+\) is

\[
C(n)=\begin{cases}3n+1,&n\text{ odd},\\n/2,&n\text{ even}.
\end{cases}
\]

The **shortcut map** \(T:\mathbb N_+\to\mathbb N_+\) includes one division by 2 in every step:

\[
T(n)=\begin{cases}(3n+1)/2,&n\text{ odd},\\n/2,&n\text{ even}.
\end{cases}
\]

If \(n=2u+1\), then \(3n+1=6u+4\) is even. Thus the shortcut rule always produces a positive integer. At an odd state it performs two ordinary steps; at an even state it performs one.

The **Syracuse map** \(S:\mathcal O\to\mathcal O\) removes all factors of 2 after the odd step:

\[
S(m)=\frac{3m+1}{2^{\nu_2(3m+1)}}.
\]

Lemma 1 proves that this quotient is a positive odd integer. For odd \(m\), the exponent \(\nu_2(3m+1)\) is at least 1. Thus every Syracuse step includes one multiplication by 3, the addition of 1, and a positive number of divisions by 2.

For a map \(F\), the notation \(F^0(n)=n\) and \(F^{k+1}(n)=F(F^k(n))\) denotes iteration. The orbit is the indexed sequence of these values. Keeping the indices matters: \(S(1)=1\), but the successive occurrences of 1 are distinct visits.

Starting at 3 illustrates all three rules:

| Map | Successive states through the first occurrence of 1 |
| :--- | :--- |
| Ordinary \(C\) | \(3,10,5,16,8,4,2,1\) |
| Shortcut \(T\) | \(3,5,8,4,2,1\) |
| Syracuse \(S\) | \(3,5,1\) |

The different sequence lengths are not an approximation error. Each row uses its own exact clock.

## One odd return at a time

**Lemma 2.** Let \(m\) be odd, put \(q=\nu_2(3m+1)\), and put \(u=S(m)\). Then \(3m+1=2^q u\), and

\[
C^r(m)=2^{q+1-r}u\qquad(1\leq r\leq q+1),
\]

whereas

\[
T^r(m)=2^{q-r}u\qquad(1\leq r\leq q).
\]

The first odd state after \(m\) is \(u\). It occurs after exactly \(q+1\) ordinary steps or \(q\) shortcut steps.

**Proof.** The ordinary first step produces \(2^q u\). Until the exponent becomes zero the number is even, so the rule divides it by 2. This proves the first formula successively for every displayed \(r\). It also proves that the intermediate states are even and the final one is odd. The shortcut first step produces \(2^{q-1}u\); the same argument proves the second formula. If \(q=1\), the shortcut map reaches \(u\) immediately, so there are no intermediate even shortcut states. ∎

Here the subset in Theorem A is \(\mathcal O\). Lemma 2 proves existence and gives the precise first-return time for every odd starting point: \(q+1\) for \(C\), and \(q\) for \(T\). Consequently \(S\) is the induced map of either rule on \(\mathcal O\). We have verified the return hypothesis directly, without making any assertion about reaching 1.

## Exact conversion between the clocks

Fix a positive integer \(N=2^a m\) with \(m\) odd. Define

\[
m_j=S^j(m),\qquad q_j=\nu_2(3m_j+1),
\]

and define the accumulated number of halvings by

\[
Q_0=0,\qquad Q_j=\sum_{i=0}^{j-1}q_i\quad(j\geq1).
\]

There are initially \(a\) halvings to reach \(m\). Each subsequent odd return contributes \(q_j\) shortcut steps, but \(q_j+1\) ordinary steps. This gives the following exact statement.

**Theorem 3.** For every \(j\in\mathbb N_0\),

\[
T^{a+Q_j}(N)=m_j=C^{a+j+Q_j}(N).
\]

Moreover, the maps

\[
\begin{aligned}
\theta_T:\mathbb N_0&\longrightarrow\{t\geq0:T^t(N)\text{ is odd}\},
&j&\longmapsto a+Q_j,\\
\theta_C:\mathbb N_0&\longrightarrow\{t\geq0:C^t(N)\text{ is odd}\},
&j&\longmapsto a+j+Q_j
\end{aligned}
\]

are strictly increasing bijections. For \(F=C\) or \(F=T\), the inverse on its indicated domain is

\[
\theta_F^{-1}(t)=
\#\{h:0\leq h<t,\ F^h(N)\text{ is odd}\}.
\]

Thus the inverse counts earlier odd visits, not distinct odd values.

**Proof.** For \(0\leq t\leq a\), both trajectories are \(2^{a-t}m\). Their first odd visit is at \(t=a\), which proves the formulas for \(j=0\). Suppose an odd visit to \(m_j\) has been located. Lemma 2 places the next odd visit to \(m_{j+1}\) exactly \(q_j\) shortcut steps or \(q_j+1\) ordinary steps later, with no odd visit in between. Since \(Q_{j+1}=Q_j+q_j\), induction gives the stated times.

Every \(q_j\geq1\). Hence \(Q_j\geq j\), so both time sequences are strictly increasing and unbounded. The initial segment and the intervals between successive listed times therefore cover every nonnegative integer time. The initial segment before \(a\) has no odd states, and Lemma 2 excludes any extra odd states between consecutive listed visits. This proves surjectivity onto precisely the two sets of odd-visit times; strict increase proves injectivity. At the \(j\)-th listed visit there are exactly \(j\) earlier odd visits, proving the inverse formula. ∎

For \(N=3\), the odd states are \(3,5,1,1,\ldots\). The relevant factorizations are

\[
3\cdot3+1=2\cdot5,\qquad
3\cdot5+1=2^4\cdot1,\qquad
3\cdot1+1=2^2\cdot1.
\]

Thus \(q_0=1\), \(q_1=4\), and \(q_j=2\) for \(j\geq2\).

| Odd-visit index \(j\) | State \(m_j\) | \(Q_j\) | Shortcut time \(Q_j\) | Ordinary time \(j+Q_j\) |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 3 | 0 | 0 | 0 |
| 1 | 5 | 1 | 1 | 2 |
| 2 | 1 | 5 | 5 | 7 |
| 3 | 1 | 7 | 7 | 10 |

![Three timelines for the orbit beginning at 3. The ordinary row is 3, 10, 5, 16, 8, 4, 2, 1 at times 0 through 7. The shortcut row is 3, 5, 8, 4, 2, 1 at times 0 through 5. The odd-return row is 3, 5, 1 at times 0 through 2. Each row has a separate time scale.](../figures/three-clocks.svg)

*Figure 1. Each dot is an actual state, not an interpolated value. The labels beneath it give the time in that row's own clock. The highlighted odd states correspond under Theorem 3.*

The repeated state 1 explains why a bijection between visit times is the right formulation. At ordinary times 7 and 10 the value is the same, but the inverse map returns indices 2 and 3 respectively. Indeed, the ordinary orbit continues \(1,4,2,1,4,2,\ldots\), whereas the odd-return orbit stays at 1.

## Reconstructing every omitted state

Theorem 3 is not merely a way to extract a shorter list. It has an exact reconstruction procedure.

**Proposition 4.** The initial exponent \(a\) and the indexed odd orbit \((m_j)_{j\geq0}\) determine the entire ordinary and shortcut trajectories uniquely.

**Proof.** Each \(q_j\) is determined by \(m_j\), so all \(Q_j\) and visit times are known. For \(0\leq t<a\), set both trajectories equal to \(2^{a-t}m_0\). After that, the increasing unbounded visit times determine a unique block containing any given time.

For the shortcut clock, write uniquely

\[
t=a+Q_j+r,\qquad 0\leq r<q_j.
\]

The state is \(m_j\) for \(r=0\), and \(2^{q_j-r}m_{j+1}\) for \(1\leq r<q_j\). At the next block's first time it is \(m_{j+1}\).

For the ordinary clock, write uniquely

\[
t=a+j+Q_j+r,\qquad 0\leq r<q_j+1.
\]

The state is \(m_j\) for \(r=0\), and \(2^{q_j+1-r}m_{j+1}\) for \(1\leq r\leq q_j\). Again the next block starts at \(m_{j+1}\). Lemma 2 verifies the rule at every transition, including the block boundaries. Hence these formulas recover the actual trajectories and leave no state unspecified. ∎

The exponent \(a\) is essential if the starting integer was not retained. The starts 3 and 24 have the same odd-return sequence, but 24 first takes the three steps \(24\to12\to6\to3\). Knowing \(a=3\) restores that prefix.

There is also an important distinction between deleting an initial even prefix and deleting every even portion of an orbit. The projection \(\pi\) alone does not intertwine a single ordinary step with a single Syracuse step. For example,

\[
\pi(C(6))=3,\qquad S(\pi(6))=S(3)=5.
\]

This does not make the maps unrelated. Their precise relation is the induced-map identity of Lemma 2 and the time bijections of Theorem 3. A single ordinary step can remain inside a block; one Syracuse step crosses the whole block.

## The least value attained does not depend on the clock

For a map \(F\) on positive integers and an allowed starting point \(n\), define

\[
F_{\min}(n)=\min\{F^k(n):k\in\mathbb N_0\}.
\]

The set is nonempty because it contains \(n\), and well-ordering supplies a minimum. This definition does not require the orbit to be bounded, periodic, or known to terminate.

**Theorem 5.** For every \(a\in\mathbb N_0\) and \(m\in\mathcal O\),

\[
C_{\min}(2^a m)=T_{\min}(2^a m)=S_{\min}(m).
\]

**Proof.** Put \(b=S_{\min}(m)\). Every odd state \(m_j\) occurs in both other trajectories by Theorem 3. In particular, the value \(b\) occurs, so the minima of those trajectories are at most \(b\).

Conversely, each state in the initial halving segment is at least \(m\), hence at least \(b\). Each later odd state is some \(m_j\geq b\). Each intervening even state, by Lemma 2, is a positive power of 2 times the following odd state \(m_{j+1}\), so it too is at least \(b\). Every state in either trajectory is therefore at least \(b\). The two opposite inequalities prove the result. ∎

The same reasoning yields a useful finite statement. Through the \(j\)-th odd visit, including its endpoint, the minima are exactly

\[
\min_{0\leq t\leq a+Q_j}T^t(N)
=\min_{0\leq i\leq j}m_i
=\min_{0\leq t\leq a+j+Q_j}C^t(N).
\]

Every omitted even state in these prefixes is followed by an odd state that still lies in the prefix, so the proof of Theorem 5 applies word for word with a finite range. Matching endpoints is necessary. For the start 3 and a horizon of five steps in each clock, the shortcut prefix has reached 1, but the ordinary prefix ends at 4 and has minimum 3.

As an immediate consequence, the assertion that every positive ordinary Collatz orbit reaches 1 is equivalent to the assertion that every positive odd Syracuse orbit reaches 1. In one direction restrict to odd starts and use Theorem 5. In the other, factor an arbitrary start as \(2^a m\) and apply the same theorem. A minimum of 1 is attained by definition. This proves equivalence of the formulations, not either conjecture.

## Exercises with solutions

**Exercise 1.** Starting at 40, find the first odd state, its two following odd returns, and their times for \(C\) and \(T\). Give both trajectories through the first occurrence of 1.

**Solution.** The factorization \(40=2^3\cdot5\) gives \(a=3\) and \(m_0=5\). The next states are \(m_1=1\) and \(m_2=1\); the valuations are \(q_0=4\) and \(q_1=2\). Thus \(Q_0=0\), \(Q_1=4\), and \(Q_2=6\). The shortcut visit times are \(3,7,9\), and the ordinary visit times are \(3,8,11\). Through the first 1, the trajectories are

\[
\begin{aligned}
C:&\quad40,20,10,5,16,8,4,2,1,\\
T:&\quad40,20,10,5,8,4,2,1.
\end{aligned}
\]

The second odd return is a later visit to 1, not a new odd value.

**Exercise 2.** In the orbit beginning at 7, compute the first three odd returns and verify both clock formulas. Do these three returns prove that the orbit eventually reaches 1?

**Solution.** The identities

\[
22=2\cdot11,\qquad34=2\cdot17,\qquad52=2^2\cdot13
\]

give the odd states \(7,11,17,13\) and valuations \(1,1,2\). Hence \(Q_j\), for \(j=0,1,2,3\), is \(0,1,2,4\). The shortcut states are \(7,11,17,26,13\); the ordinary states are \(7,22,11,34,17,52,26,13\). Their odd-visit times are respectively \(0,1,2,4\) and \(0,2,4,7\), as asserted. These calculations describe finite prefixes only. The clock theorem would convert a later verified visit to 1 into the other clocks, but does not assert that such a visit must occur.

**Exercise 3.** Suppose an odd orbit returns to its starting value after \(h\geq1\) Syracuse steps. Put \(Q=\sum_{j=0}^{h-1}q_j\). Prove that the ordinary and shortcut orbits return to that same starting value after \(h+Q\) and \(Q\) steps respectively. If \(h\) is the least positive Syracuse return time, prove that these are also the least positive return times for the other two maps.

**Solution.** Theorem 3 with \(a=0\) gives the two returns. Any return to the starting value must occur at an odd-visit time, since the starting value is odd. The inverse bijection assigns an index \(j\geq1\) to such a return. If its time were smaller than the listed one, strict increase of \(\theta_F\) would imply \(j<h\), contrary to the minimality of \(h\). For \(m=1\), this recovers periods 1 for \(S\), 2 for \(T\), and 3 for \(C\).

**Exercise 4.** An odd-return calculation gives \(S^j(m)<m\). What exactly follows about the other clocks, and what follows if only \(j\) is known but the valuations are not?

**Solution.** Theorem 3 proves \(T^{Q_j}(m)<m\) and \(C^{j+Q_j}(m)<m\). Thus both orbits have fallen below their start by the displayed times. These need not be their first such times, since an intervening even state might already lie below \(m\). Knowing only \(j\) gives \(Q_j\geq j\), not the actual elapsed times or an upper bound for them from this inequality. The missing clock information is the sum of the valuations. The orbit-minimum conclusion \(C_{\min}(m)=T_{\min}(m)<m\) does not require those times to be evaluated.

## What carries forward

Theorem A applies to any discrete system with the stated return property. The Collatz calculation supplies explicit formulas for its return times and intervening states. Its preservation of minima comes from a further inequality: each omitted even state is at least the following odd state. Separating these two arguments tells us what can be reused in a different system and what needs to be checked afresh.

There are two different coordinate choices here. The factorization \(N=2^a m\) separates the initial halving prefix from the odd start. The sequence \((q_j)\) then records the durations between odd visits. Together with the odd states, these data reconstruct every step. For questions about the least value ever attained, the durations can be discarded; for questions about time they cannot.

A further distinction will matter when starting integers are chosen at random. The projection \(\pi\) has infinitely many points in each fibre. The orbit identities proved here therefore do not, by themselves, identify the distribution of projected starting points. To transfer statements about “most” starting integers, one must also calculate the weight carried by those fibres. This is the reason to develop sampling alongside dynamics rather than treating a change of clock as an automatic change of probability law.

Continue with [Symbolic itineraries and affine composition](NT-COLLATZ-02.md) to describe whole blocks of an orbit algebraically. [Pushforward measures and logarithmic sampling](NT-COLLATZ-03.md) instead follows the question of how changing coordinates changes a distribution.

## References

Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, [arXiv:1909.03562v7](https://arxiv.org/abs/1909.03562v7), especially §1.2 and equations (1.1)–(1.2). The journal article appeared in *Forum of Mathematics, Pi* **10** (2022), e12. The elementary clock and minimum identities used here belong to that established formulation; no stronger orbit-minimum theorem is asserted here.

Riho Terras, *A stopping time problem on the positive integers*, *Acta Arithmetica* **30** (1976), no. 3, 241–252. [DOI: 10.4064/aa-30-3-241-252](https://doi.org/10.4064/aa-30-3-241-252).
