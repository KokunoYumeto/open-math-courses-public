# Geometric waiting times and controlled conditioning

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, proofs and exercises: CC0 1.0.*

An independent random model is useful only if we know when it describes the objects being studied and what happens when we restrict it to an event. Both questions arise when a long calculation is divided into a prefix and a tail. A restriction that looks innocuous can couple those two pieces and invalidate a product formula.

We begin with geometric waiting times, whose sums and conditional distributions can be counted exactly. We then prove concentration estimates, use residue classes to compare this model with finite Collatz valuation words, and explain how to stop a random word while keeping its unused tail independent. The resulting estimates quantify the errors in the prefix–tail decomposition of [Quotient distributions and Fourier mixing](NT-COLLATZ-05.md#why-random-affine-sums-lead-to-this-estimate).

We assume elementary differentiation and integration, geometric series, binomial coefficients, and countable probability. [Pushforward measures and logarithmic sampling](NT-COLLATZ-03.md#counting-entire-fibres), Proposition 1, supplies regrouping of nonnegative sums and contraction under a map. The arithmetic application uses [Symbolic itineraries and affine composition](NT-COLLATZ-02.md#the-arithmetic-domain-of-a-word), Theorem 4, which proves the correspondence between finite parity words and residue classes. Basic references are Scott Sheffield's lectures on moment generating functions, Kyle Siegrist's *Random Services* treatment of negative binomial waiting times, and Tao's *Almost all orbits of the Collatz map attain almost bounded values*, Sections 2, 4 and 6. The required concentration and conditioning arguments are proved here.

## Counting waiting-time words

Fix \(0<p<1\). A positive geometric variable \(A\) has law

\[
\mathbb P(A=b)=p(1-p)^{b-1},\qquad b=1,2,\ldots.
\]

One interpretation is the number of independent trials needed to obtain a first success, each trial having success probability \(p\): the first \(b-1\) trials fail and the next succeeds. The displayed probabilities sum to one. We will use finite independent lists \(A_1,\ldots,A_n\), and put

\[
S_0=0,\qquad S_j=A_1+\cdots+A_j.
\]

The law of the whole word is the product of its coordinate laws. In particular, a specified word \((a_1,\ldots,a_k)\) of total length \(s\) has probability \(p^k(1-p)^{s-k}\).

**Proposition 1 (Sums and conditioning on a sum).** For integers \(k\geq1\) and \(s\geq k\),

\[
\mathbb P(S_k=s)=\binom{s-1}{k-1}p^k(1-p)^{s-k}. \tag{1}
\]

Given \(S_k=s\), the word is uniform on all positive \(k\)-tuples with sum \(s\). This conditional law does not depend on \(p\).

**Proof.** Send a positive tuple to its first \(k-1\) partial sums:

\[
(a_1,\ldots,a_k)\longmapsto
\{a_1,a_1+a_2,\ldots,a_1+\cdots+a_{k-1}\}.
\]

This is a bijection onto the \((k-1)\)-element subsets of \(\{1,\ldots,s-1\}\). In increasing order, take successive differences, including the differences from zero and to \(s\), to recover the tuple. There are therefore \(\binom{s-1}{k-1}\) tuples. Each has the same probability \(p^k(1-p)^{s-k}\). Summing proves (1), and dividing each word probability by this positive sum proves the conditional statement. For \(k=1\), the subset is empty and the only tuple is \((s)\). ∎

The coordinates are generally no longer independent after the total is fixed. For example, given \(A_1+A_2=3\), the only words are \((1,2)\) and \((2,1)\), with equal probabilities. Each coordinate has probability \(1/2\) of being one, but they cannot both be one.

There is a different statement for **separate totals of disjoint blocks**. Partition the coordinate indices into finitely many disjoint blocks. For a block of length \(k_j\), prescribe total \(s_j\geq k_j\). Under this conditioning, the blocks remain independent, and each block is uniform on its positive compositions of \(s_j\). Indeed, the probability of a collection of specified block words is the product of their original probabilities. The probability of the conditioning event is the product of the block-total probabilities. Dividing cancels separately in each factor. Coordinates inside a block need not be independent.

In particular, for \(p=1/2\), let \(B_j=A_{2j-1}+A_{2j}\). Then

\[
\mathbb P(B_j=b)=(b-1)2^{-b},\qquad b\geq2,
\]

and, given the separate values of all the \(B_j\), the pairs are independent. Within a pair of total \(b\), the first coordinate is uniform on \(\{1,\ldots,b-1\}\), and the second is its complement to \(b\). This distinction is useful in Tao's Fourier argument: averaging over a finite set of possible splits gives cancellation, while separate pair totals still permit multiplication across pairs.

## An exponential estimate with explicit constants

For the rest of the concentration calculation, take \(p=1/2\), so \(\mathbb P(A=b)=2^{-b}\). Its mean is two. One way to see this without differentiating an infinite series is to write

\[
\mathbb E A=\sum_{j\geq1}\mathbb P(A\geq j)
=\sum_{j\geq1}2^{1-j}=2.
\]

The first equality follows by counting \(b\) as the sum of \(b\) ones and regrouping nonnegative terms.

The **moment generating function** at a real number \(\lambda\) is \(\mathbb E e^{\lambda A}\), when this sum is finite. A geometric-series calculation gives

\[
\mathbb E e^{\lambda A}
=\sum_{b\geq1}(e^\lambda/2)^b
=\frac{e^\lambda}{2-e^\lambda},\qquad \lambda<\log2.
\]

For the centred variable \(A-2\), write

\[
\psi(\lambda)=\log\mathbb E e^{\lambda(A-2)}
=-\lambda-\log(2-e^\lambda).
\]

Set \(\alpha=\log(4/3)>0\). Direct differentiation of this finite expression gives

\[
\psi(0)=\psi'(0)=0,\qquad
\psi''(\lambda)=\frac{2e^\lambda}{(2-e^\lambda)^2}\leq6
\quad (|\lambda|\leq\alpha).
\]

For the bound, use \(e^\lambda\leq4/3\) and \(2-e^\lambda\geq2/3\). Integrating the second derivative twice, or applying Taylor's integral formula on the segment from zero to \(\lambda\), therefore proves

\[
\psi(\lambda)\leq3\lambda^2\qquad(|\lambda|\leq\alpha). \tag{2}
\]

The integral formula is valid also for negative \(\lambda\): it can be written as \(\psi(\lambda)=\lambda^2\int_0^1(1-t)\psi''(t\lambda)\,dt\).

**Theorem 2 (Concentration for geometric sums).** For \(k\geq1\) and \(t\geq0\), put

\[
\Phi_k(t)=\min\left\{\frac{t^2}{12k},\frac{\alpha t}{2}\right\}.
\]

Then

\[
\begin{aligned}
\mathbb P(S_k-2k\geq t)&\leq e^{-\Phi_k(t)},\\
\mathbb P(S_k-2k\leq-t)&\leq e^{-\Phi_k(t)},\\
\mathbb P(|S_k-2k|\geq t)&\leq2e^{-\Phi_k(t)}.
\end{aligned} \tag{3}
\]

**Proof.** For \(\lambda>0\), on the event \(S_k-2k\geq t\) the nonnegative variable \(e^{\lambda(S_k-2k)}\) is at least \(e^{\lambda t}\). Thus

\[
\mathbb P(S_k-2k\geq t)
\leq e^{-\lambda t}\mathbb E e^{\lambda(S_k-2k)}.
\]

Independence factors the expectation into \(k\) identical factors. This follows directly by summing the nonnegative product over all coordinate tuples. For \(0<\lambda\leq\alpha\), (2) bounds the right side by \(\exp(-\lambda t+3k\lambda^2)\).

If \(0<t\leq6k\alpha\), choose \(\lambda=t/(6k)\). The exponent is \(-t^2/(12k)\). If \(t\geq6k\alpha\), choose \(\lambda=\alpha\); then \(3k\alpha^2\leq\alpha t/2\), and the exponent is at most \(-\alpha t/2\). These are exactly the two branches of \(-\Phi_k(t)\). At \(t=0\), the one-sided estimate simply says that a probability is at most one.

For the lower tail use \(e^{-\lambda(S_k-2k)}\) and apply (2) at \(-\lambda\), with the same choices of positive \(\lambda\). Finally, the two tail events cover \(\{|S_k-2k|\geq t\}\); adding their probabilities proves the last bound. ∎

The estimate has two regimes. Deviations up to size proportional to \(k\) have a quadratic exponent \(t^2/(12k)\). Larger deviations have a linear exponent \(\alpha t/2\). Keeping both is important because one unusually large waiting time can produce a very large deviation.

## Controlling every interval of a word

For \(0\leq i<j\leq n\), write \(S_j-S_i=A_{i+1}+\cdots+A_j\). This block has exactly \(j-i\) summands and mean \(2(j-i)\). For \(u>0\), define

\[
b_m(u)=\sqrt{12mu}+\frac{2u}{\alpha},\qquad m\geq1.
\]

Both terms in the minimum defining \(\Phi_m(b_m(u))\) are at least \(u\). Theorem 2 therefore bounds the failure probability for one block by \(2e^{-u}\).

**Corollary 3 (Simultaneous block control).** Let \(G_n(u)\) be the event that

\[
|S_j-S_i-2(j-i)|\leq b_{j-i}(u)
\quad\text{for every }0\leq i<j\leq n.
\]

Then

\[
\mathbb P(G_n(u)^c)\leq n(n+1)e^{-u}. \tag{4}
\]

**Proof.** There are \(n(n+1)/2\) intervals. For any finite list of events, the indicator of their union is at most the sum of their indicators. Taking expectations proves that the probability of their union is at most the sum of their probabilities. Apply this to the block failures. They do not have to be independent. ∎

For a desired error \(0<\varepsilon<1\), the choice

\[
u=\log\frac{n(n+1)}{\varepsilon}
\]

makes the right side \(\varepsilon\). This is the source of the frequently useful combination \(\sqrt{m\log n}+\log n\) when the desired error is a negative power of \(n\). The formula (4) specifies the constants and the number of intervals instead of hiding either in an asymptotic phrase.

## How much information a residue class provides

We now connect the model to arithmetic. Let \(m\) be a positive odd integer, and let

\[
S(m)=\frac{3m+1}{2^{\nu_2(3m+1)}}
\]

be the odd-return Collatz map. The notation \(S(m)\) denotes a map here, while the subscripted \(S_j\) above denotes a random partial sum. For \(k\geq1\), the **valuation word** of \(m\) is

\[
V_k(m)=(a_1,\ldots,a_k),\qquad
a_i=\nu_2(3S^{i-1}(m)+1).
\]

Fix a positive word \(\boldsymbol a=(a_1,\ldots,a_k)\), let \(s_i=a_1+\cdots+a_i\), \(s_0=0\), and \(s=s_k\). Define the integer

\[
C_{\boldsymbol a}=\sum_{i=1}^k3^{k-i}2^{s_{i-1}}.
\]

**Proposition 4 (The exact valuation cylinder).** The set of positive odd starts having valuation word \(\boldsymbol a\) is exactly one residue class modulo \(2^{s+1}\), namely

\[
m\equiv3^{-k}(2^s-C_{\boldsymbol a})\pmod {2^{s+1}}. \tag{5}
\]

Here \(3^{-k}\) is the multiplicative inverse of \(3^k\) in that residue ring. The represented class is odd.

**Proof.** Use the shortcut map \(T(m)=(3m+1)/2\) for odd \(m\) and \(T(m)=m/2\) for even \(m\). An odd-return step with valuation \(a_i\) follows the parity block consisting of one 1 and then \(a_i-1\) zeros. After \(k\) such blocks there have been \(s\) shortcut steps, and the next state must again be odd. Thus the valuation cylinder is exactly the cylinder of the length-\((s+1)\) parity word

\[
1\,0^{a_1-1}\,1\,0^{a_2-1}\,\cdots\,1\,0^{a_k-1}\,1.
\]

The final 1 is a parity test at time \(s\), not an additional completed odd-return step. The word/residue theorem in [Symbolic itineraries and affine composition](NT-COLLATZ-02.md#the-arithmetic-domain-of-a-word) gives exactly one class modulo \(2^{s+1}\), and every positive member of it has the required valuation word.

On this cylinder, iterating the affine branch equations gives

\[
S^k(m)=\frac{3^k m+C_{\boldsymbol a}}{2^s}.
\]

The formula is also equation (6) of [Quotient distributions and Fourier mixing](NT-COLLATZ-05.md#why-random-affine-sums-lead-to-this-estimate) after multiplying through by \(2^s\). The output is odd, so its numerator is congruent to \(2^s\) modulo \(2^{s+1}\). There is exactly one solution for \(m\) because \(3^k\) is invertible modulo that power of two. It must therefore be the already established cylinder class. Finally, \(C_{\boldsymbol a}\) is odd: its first term is odd and every later term is even. Since \(s\geq1\), (5) is odd. ∎

The extra bit in the modulus matters. Divisibility by \(2^s\) alone would not ensure that the endpoint is odd and that the last removed exponent is exactly the prescribed one.

**Theorem 5 (A finite sampling comparison).** Let \(M_0\) be any random positive odd integer. For an integer \(q\geq1\), let \(\nu\) be its law modulo \(2^q\), and let \(u_q\) be uniform on the \(2^{q-1}\) odd classes. Put

\[
\eta=\sum_{r\text{ odd}\bmod 2^q}|\nu(r)-u_q(r)|.
\]

Let \(\gamma_k\) be the law of \(k\) independent positive geometric variables of parameter \(1/2\). Then

\[
\|\mathcal L(V_k(M_0))-\gamma_k\|_1
\leq\eta+2\,\mathbb P(S_k\geq q). \tag{6}
\]

In particular, when \(q\geq2k\),

\[
\|\mathcal L(V_k(M_0))-\gamma_k\|_1
\leq\eta+2e^{-\Phi_k(q-2k)}. \tag{7}
\]

**Proof.** Call a word short if its total \(s\) is less than \(q\). For such a word, Proposition 4 determines its cylinder from the class modulo \(2^q\). There are \(2^{q-s-1}\) odd classes in that cylinder, so its \(u_q\)-probability is exactly

\[
\frac{2^{q-s-1}}{2^{q-1}}=2^{-s},
\]

the same as its \(\gamma_k\)-probability. Distinct short words give disjoint cylinders. The remaining odd classes form a single residual cell. This partitions the finite set of odd classes into short-word cells and one residual cell; if there are no short words, the partition has only the residual cell.

Replace every non-short word by a symbol \(*\). Under \(u_q\), the resulting distribution agrees exactly with the similarly collapsed geometric law. Under \(\nu\), it agrees with the collapsed law of \(V_k(M_0)\). Pushforward contraction therefore gives

\[
\sum_{\boldsymbol a\text{ short}}|p_{\boldsymbol a}-g_{\boldsymbol a}|
+|p_*-g_*|\leq\eta.
\]

Here \(p\) and \(g\) denote the actual and geometric word laws, and \(g_*=\mathbb P(S_k\geq q)\). Without collapsing, the contribution from the remaining words is at most \(p_*+g_*\). Since \(p_*+g_*\leq|p_*-g_*|+2g_*\), (6) follows. Apply the upper-tail part of Theorem 2 to obtain (7). ∎

For example, choose \(M_0\) uniformly among the first \(B\) positive odd integers. In the index of that list, reduction modulo \(2^q\) cycles through \(K=2^{q-1}\) classes. Each class appears either \(\lfloor B/K\rfloor\) or \(\lceil B/K\rceil\) times. Each probability differs from \(1/K\) by at most \(1/B\), and hence \(\eta\leq K/B\). Taking \(q=3k\) in (7) gives the completely explicit estimate

\[
\|\mathcal L(V_k(M_0))-\gamma_k\|_1
\leq\frac{2^{3k-1}}{B}+2e^{-k/12}. \tag{8}
\]

In deriving the exponent, \(\alpha=\log(4/3)=\int_1^{4/3}dt/t\geq1/4\), so \(\Phi_k(k)=k/12\). If the displayed right side exceeds two it is simply a weak bound; the distance between two probability laws is at most two. For \(k\) tending to infinity slowly enough that \(2^{3k}/B\to0\), both error terms tend to zero. This is a statement about a specified finite sampling experiment, not independence along every infinite integer orbit.

## Changing an event without losing its mass

Let \(Z\) be a random variable in a countable set, and let \(E,F\) be events. Define subprobability mass functions

\[
\mu_E(z)=\mathbb P(Z=z,E),\qquad
\mu_F(z)=\mathbb P(Z=z,F).
\]

**Lemma 6 (Event replacement).**

\[
\|\mu_E-\mu_F\|_1\leq\mathbb P(E\mathbin\triangle F), \tag{9}
\]

where \(E\mathbin\triangle F\) consists of outcomes in exactly one of the events. If \(Z\) takes values in \(G_N\) and \(P\) is the fibre-averaging operator of the preceding lesson, then

\[
\left|\|\mu_E-P\mu_E\|_1-\|\mu_F-P\mu_F\|_1\right|
\leq2\mathbb P(E\mathbin\triangle F). \tag{10}
\]

**Proof.** At each \(z\), cancel the shared contribution from \(E\cap F\). The absolute remaining difference is at most the sum of the masses at \(z\) coming from \(E\setminus F\) and \(F\setminus E\). Summing proves (9). For (10), the reverse triangle inequality bounds the left side by

\[
\|(I-P)(\mu_E-\mu_F)\|_1
\leq\|\mu_E-\mu_F\|_1+\|P(\mu_E-\mu_F)\|_1
\leq2\|\mu_E-\mu_F\|_1.
\]

The last step uses the contraction proved in Proposition 1 of the preceding lesson. ∎

These are estimates for masses before dividing by an event probability. If \(a=\mathbb P(E)>0\) and \(b=\mathbb P(F)>0\), the conditional laws satisfy, for example,

\[
\left\|\frac{\mu_E}{a}-\frac{\mu_F}{b}\right\|_1
\leq\frac{2\mathbb P(E\mathbin\triangle F)}{a}.
\]

Indeed, insert \(\mu_F/a\). The two differences have total norm at most \(\|\mu_E-\mu_F\|_1/a+|a-b|/a\), and \(|a-b|\leq\mathbb P(E\mathbin\triangle F)\). Interchanging the events gives the corresponding bound with denominator \(b\). A small absolute error can become substantial after conditioning on a rare event. Retaining subprobability masses, as in Lemma 6 and the convolution estimate, avoids paying that division prematurely.

## Where to stop so that the tail remains independent

Consider a word \(A_1,\ldots,A_n\) with independent positive geometric entries of parameter \(1/2\), and fix \(h\geq0\). Define the first strict crossing

\[
\tau=\min\{j\in\{1,\ldots,n\}:S_j>h\},
\]

with \(\tau=\infty\) if there is no crossing. Since all entries are positive,

\[
\{\tau=j\}=\{S_{j-1}\leq h<S_j\}.
\]

This event is determined by the first \(j\) entries. It does not inspect \(A_{j+1},\ldots,A_n\). The entries after \(j\) therefore retain their product law after conditioning on any positive-probability event involving just that prefix. For specified tail values, factor their probability from the prefix-event probability and then divide by the latter. This proves the assertion directly; no stopping-time theorem is needed.

By contrast, fixing the number of entries *before* the crossing to be \(k\) inspects \(A_{k+1}\), because its defining inequality is \(S_k\leq h<S_{k+1}\). In that description, the independent unused tail starts at \(k+2\), not at \(k+1\). The distinction is one coordinate, but it determines which Fourier factorization is valid.

Let \(G_n(u)\) be the simultaneous-control event above. It examines the entire word. For \(j\leq n\), let \(G_j(u)\) impose the same inequalities only on intervals within the first \(j\) entries. Then \(G_n(u)\subseteq G_j(u)\), and \(G_j(u)\) is a prefix event. Define disjoint cells

\[
E_{j,l}=\{\tau=j,\ S_j=l\}\cap G_j(u),
\qquad 1\leq j\leq n,\quad l\in\mathbb N_+.
\]

They are disjoint because the first crossing and its total are uniquely specified. They are also finitely many nonempty cells: on \(G_j(u)\), \(S_j\leq2j+b_j(u)\leq2n+b_n(u)\). Put \(D=\bigcup_{j,l}E_{j,l}\).

**Proposition 7 (A prefix-measurable decomposition).**

\[
G_n(u)\cap\{\tau\leq n\}\subseteq D,
\qquad
\mathbb P(D^c)\leq n(n+1)e^{-u}+\mathbb P(S_n\leq h). \tag{11}
\]

For any countable-valued random variable \(Z\), its law has the exact decomposition

\[
\mathcal L(Z)=\mu_{D^c}+\sum_{j,l}\mu_{E_{j,l}}.
\]

Each event \(E_{j,l}\) depends only on the first \(j\) entries and fixes their sum. Thus for the affine random sum of the preceding lesson, each cell with \(j<n\) has the convolution representation of its Proposition 6, with an independent tail beginning at \(j+1\). For \(j=n\), the tail is empty and contributes unit mass at zero.

**Proof.** If all interval bounds hold and a crossing occurs, the unique pair \((\tau,S_\tau)\) places the word in one of the cells. Therefore \(D^c\) is contained in \(G_n(u)^c\cup\{\tau=\infty\}\). Positivity of the entries gives \(\{\tau=\infty\}=\{S_n\leq h\}\). Apply Corollary 3 and the union bound to obtain (11). The cells and their complement partition the probability space, proving the law decomposition. Prefix dependence and the fixed sum allow the independent-tail calculation already proved in the preceding lesson. ∎

If \(h<2n\), Theorem 2 gives the further explicit bound

\[
\mathbb P(D^c)\leq n(n+1)e^{-u}+e^{-\Phi_n(2n-h)}.
\]

There is no need to multiply the first error by the number of cells. All cells are disjoint, and every lost outcome lies in the same event \(G_n(u)^c\) or fails to cross. Likewise, replacing \(G_n(u)\) by \(G_j(u)\) on the cell with crossing \(j\) adds a set contained in \(G_n(u)^c\); the sum of those added masses is at most \(\mathbb P(G_n(u)^c)\).

This provides the probabilistic part of a mixing argument: a finite sum of genuine convolutions and an explicitly bounded residual mass. The arithmetic separation and tail Fourier bounds still enter through the estimates proved in [Quotient distributions and Fourier mixing](NT-COLLATZ-05.md#an-energy-estimate-for-mixing-inside-fibres). A concentration estimate controls which words are used; it does not itself estimate their oscillatory phases.

## Exercises

### 1. A total shared by three waiting times

List the positive triples of sum five. Given \(S_3=5\), find the distribution and mean of \(A_1\), and demonstrate that \(A_1\) and \(A_2\) are dependent. Does any answer depend on \(p\)?

**Solution.** The six triples are

\[
(1,1,3),(1,2,2),(1,3,1),(2,1,2),(2,2,1),(3,1,1).
\]

Proposition 1 assigns conditional probability \(1/6\) to each. The probabilities for \(A_1=1,2,3\) are \(1/2,1/3,1/6\), and its mean is \(1/2+2/3+3/6=5/3\). Each of \(A_1,A_2\) has conditional probability \(1/6\) of being three, but they cannot both be three because the total is five. Thus their joint law is not the product of their marginal laws. All these answers are independent of \(p\), as the proposition predicts.

### 2. A finite estimate, not an orbit heuristic

Take \(k=2\), \(q=6\), and let \(M_0\) be uniform on the 32 odd integers from 1 to 63. Calculate \(\mathbb P(S_2\geq6)\) exactly and use (6). Separately, use Theorem 2 to bound \(\mathbb P(S_{240}\geq600)\).

**Solution.** For parameter \(1/2\), (1) gives \(\mathbb P(S_2=s)=(s-1)2^{-s}\). Hence

\[
\mathbb P(S_2\geq6)
=1-\left(\frac14+\frac28+\frac3{16}+\frac4{32}\right)
=\frac3{16}.
\]

The starting sample contains every odd class modulo 64 exactly once, so \(\eta=0\). Equation (6) bounds the full \(\ell^1\) difference of the two word laws by \(3/8\), and their event distance by \(3/16\). The assertion concerns the first two valuations under this sample law.

For the second question, \(2k=480\) and \(t=120\). The quadratic term is \(120^2/(12\cdot240)=5\); the linear term is \(60\alpha\geq15\). Thus the upper-tail bound is \(e^{-5}\). This is a bound for the independent geometric experiment, not an assertion about every Collatz orbit.

### 3. The last parity test

Find all positive starts with valuation word \((2,1)\). Check the first two odd-return steps for the least positive representative. Explain why retaining only the class modulo eight cannot distinguish this word from every other word beginning with valuation two.

**Solution.** Here \(s=3\), \(C=3+4=7\), and the inverse of nine modulo sixteen is nine. Formula (5) gives \(m\equiv9(8-7)=9\pmod{16}\). At \(m=9\), the steps are

\[
9\longmapsto\frac{28}{4}=7\longmapsto\frac{22}{2}=11,
\]

so the word is indeed \((2,1)\). All and only the positive integers \(9+16t\), with integer \(t\geq0\), give that word. Modulo eight the representative nine agrees with one, but the odd-return orbit of one has \(3\cdot1+1=4\) at every step and begins with \((2,2)\). The missing bit is precisely the test that the state at shortcut time three is odd.

### 4. Rare conditioning and the unused tail

First take a probability space with three points \(x,y,z\), of masses \(d,d,1-2d\), where \(0<d<1/2\). Let \(Z(x)=0\), \(Z(y)=1\), and choose any value for \(Z(z)\). Compare the subprobability laws on \(E=\{x\}\), \(F=\{y\}\) with their conditional laws. Then, for independent geometric \(A_1,\ldots,A_4\), stop on first crossing of \(h=4\). On the event \(\{\tau=3,S_3=6\}\), which unused coordinates remain independent of the prefix? What changes if one also prescribes \(S_4=7\)?

**Solution.** The two subprobability laws are \(d\delta_0\) and \(d\delta_1\), whose full mass difference is \(2d=\mathbb P(E\mathbin\triangle F)\). Their conditional laws are \(\delta_0\) and \(\delta_1\), whose difference is two regardless of how small \(d\) is. Thus a small discarded mass alone does not imply a small conditional-law error.

The crossing event is \(\{S_2\leq4<S_3=6\}\), determined by the first three entries. It has positive probability; the prefix \((1,3,2)\) is one possible word. Consequently \(A_4\) retains its geometric law and is independent of the prefix under this conditioning. Adding \(S_4=7\) forces \(A_4=1\), so its geometric law is no longer retained. This additional event inspected the proposed unused coordinate. It cannot be ignored when forming the tail factor.

## What carries forward

Three distinct facts now work together. Residue cylinders turn finite arithmetic sampling into a quantitative comparison with geometric words. Exponential moments control unlikely word sums, including all subintervals at once. Prefix-measurable restrictions leave a genuinely independent unused tail, with the full event masses retained.

The next analytic steps need both probabilities of events and probabilities of individual lattice points. The concentration bounds here supply the first kind. They do not include the local \(k^{-d/2}\) factors for \(d\)-dimensional sums in Tao's Section 2, or the quantitative Fourier cancellation for the two-dimensional renewal process in Section 7. Those require their own proofs. The estimates already established here isolate the exact inputs those further arguments will use rather than replacing them by an assumption of randomness along an infinite integer orbit.

## References

- Scott Sheffield, *18.600: Moment generating functions and characteristic functions*, [MIT lecture notes](https://math.mit.edu/~sheffield/2019600fall/Lecture26.pdf), the sections “Moment generating functions” and “Moment generating functions for independent sums.” These explain the exponential-moment method. The two-sided geometric bound and constants above are derived explicitly.
- Kyle Siegrist, *Random Services: The Negative Binomial Distribution*, [online probability text](https://www.randomservices.org/random/bernoulli/NegativeBinomial.html), “The Probability Density Function” and “Times Between Successes.” The positive-waiting-time convention agrees with (1); the composition argument and conditional calculations here are independently expressed.
- Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, [arXiv:1909.03562v7](https://arxiv.org/abs/1909.03562v7), Section 2 (valuation description and Chernoff-type estimates), Section 4 (distribution of valuation words), and Section 6 (prefix restrictions and partial convolution). These supply the research application; the finite sampling estimate is an exposition of its cylinder-and-tail mechanism, not a claim to solve the conjecture.
