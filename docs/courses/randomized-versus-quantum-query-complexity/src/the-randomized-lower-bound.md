# The randomized lower bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves that a randomized algorithm for the function \(F_{k,m}\) needs more than \(\lfloor mL/100\rfloor\) queries, where \(L\) is about \(m^{1-1/k}\) and is a lower bound for the Forrelation function. The proof compares two random inputs. In the first, every column has exactly one zero in its string, and all cells are blank; the value of \(F_{k,m}\) is \(0\). In the second, a random column is turned into a winner by two changes: its zero is removed, and one cell is filled. An algorithm that does not meet one of the two changed places cannot tell the inputs apart. It meets the removed zero with small probability, and it cannot find the filled cell without knowing the address of the column, which would cost more than \(L\) queries, or guessing it.

- A distribution on which the Forrelation function is hard, from (BS) and the minimax theorem (Lemma 1.1).
- Guessing the answers of several independent inputs (Lemma 2.1).
- The dummy input and the planted input (Section 3).
- The lower bound (Proposition 4.1).

The lesson follows [OpenAI-Q, Section 4]. It uses the function \(F_{k,m}\), decision trees and the hypothesis (BS) from [Query complexity and a function with outward pointers](query-complexity-and-a-function-with-outward-pointers.md), and the minimax theorem from [Alignment of lists: patterns, minimax and Ramsey's theorem](course:large-independent-sets-in-three-colorable-graphs/alignment-of-lists-patterns-minimax-and-ramseys-theorem) (course *Large independent sets in three-colorable graphs*). No quantum algorithm occurs in this lesson.

## 1. A hard distribution

Fix \(k\ge2\). As in the first lesson, \(P=P_{k,m}\) is the Forrelation function on \(km\) bits, with the domain \(\mathcal D\), and
\[
L=\Bigl\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\Bigr\rfloor .
\]

**Lemma 1.1.** Assume (BS). For all large powers of four \(m\) we have \(1\le L\le m\), and there is a probability distribution \(\mu\) on \(\mathcal D\) such that for every decision tree \(A\) of depth at most \(L\) with outputs in \(\{0,1\}\),
\[
\Pr_{z\sim\mu}\bigl(A(z)=P(z)\bigr)\le\frac23 .
\]

**Proof.** By (BS), \(R(P)\ge c_k(m/\log_2(km))^{1-1/k}\) for large \(m\). This is larger than \(m^{1-1/k}/(\log_2m)^2\) as soon as \(c_k(\log_2m)^2>(\log_2(km))^{1-1/k}\), which holds for large \(m\). So \(L<R(P)\), and \(1\le L\le m\) for large \(m\).

Let \(\mathcal A\) be the set of the decision trees of depth at most \(L\) on \(km\) bits with outputs in \(\{0,1\}\); it is finite. For \(z\in\mathcal D\) and \(A\in\mathcal A\) let \(b(z,A)=1\) if \(A(z)=P(z)\), and \(b(z,A)=0\) otherwise. By the minimax theorem (Theorem 3.2 of the lesson named above), with the probability distributions \(\nu\) on \(\mathcal D\) and \(\rho\) on \(\mathcal A\),
\[
\begin{aligned}
&\min_\nu\max_A\sum_z\nu_z\,b(z,A)\\
&\qquad=\max_\rho\min_z\sum_Ab(z,A)\,\rho_A .
\end{aligned}
\]
A distribution \(\rho\) is a randomized algorithm of cost at most \(L\), and \(\sum_Ab(z,A)\rho_A\) is the probability that it outputs \(P(z)\) on the input \(z\). Since \(L<R(P)\), no such algorithm has this probability \(\ge\tfrac23\) for all \(z\in\mathcal D\). So the right side is smaller than \(\tfrac23\). Let \(\mu\) be a distribution \(\nu\) for which the minimum on the left side is attained. \(\blacksquare\)

So the hardness of \(P\) for randomized algorithms, which is a statement about the worst input for each algorithm, becomes a statement about one distribution of inputs and all algorithms.

## 2. Guessing several answers

Let \(\mathcal D\subseteq\{0,1\}^{n_0}\) be a set, \(P:\mathcal D\to\{0,1\}\) a function and \(\mu\) a probability distribution on \(\mathcal D\). For a probability distribution \(\nu\) on \(\mathcal D\) and an integer \(j\ge0\) let
\[
\operatorname{val}(\nu,j)=\max_A\ \Pr_{z\sim\nu}\bigl(A(z)=P(z)\bigr),
\]
the maximum over the decision trees \(A\) of depth at most \(j\) with outputs in \(\{0,1\}\). Two properties follow from the definition.

First, \(\operatorname{val}(\nu,0)=\max_{b}\nu(P=b)\), and \(\operatorname{val}(\nu,j)\ge\operatorname{val}(\nu,0)\).

Second, let \(j\ge1\) and let \(i\) be a position. Let \(\nu^a\) be the distribution \(\nu\) conditioned on \(z_i=a\), for the \(a\in\{0,1\}\) with \(\nu(z_i=a)>0\). Then
\[
\sum_a\nu(z_i=a)\,\operatorname{val}(\nu^a,j-1)\le\operatorname{val}(\nu,j).
\]
We refer to this inequality as (2.1). Indeed, the tree that reads the position \(i\) and continues, after the answer \(a\), with a best tree of depth \(j-1\) for \(\nu^a\), has the depth at most \(j\) and the success probability on the left.

**Lemma 2.1** ([OpenAI-Q]; the argument goes back to Shaltiel and Drucker). Let \(L\ge0\) and \(\beta=\operatorname{val}(\mu,L)\). Let \(U_1,\dots,U_r\) be independent, each with the distribution \(\mu\). Let \(A\) be a decision tree on the input \((U_1,\dots,U_r)\in\{0,1\}^{rn_0}\) with outputs in \(\{0,1\}^r\) that on every path makes at most \(L\) queries to each \(U_h\). Call its output *correct* if it is \((P(U_1),\dots,P(U_r))\). Then
\[
\Pr(\text{the output of }A\text{ is correct})\le\beta^r .
\]
The same holds if \(A\) is chosen at random, and if \(A\) may also read, without any limit, a further input that is independent of \((U_1,\dots,U_r)\).

**Proof.** *Product form.* Let \(\tau\) be a vertex of the tree. The inputs that reach \(\tau\) are those that have the answers of the path to \(\tau\) at the positions of the path. This is a condition on \(U_1\), a condition on \(U_2\), and so on, separately. So, given that \(\tau\) is reached (if this has positive probability), \(U_1,\dots,U_r\) are independent, and \(U_h\) has the distribution \(\mu\) conditioned on the answers of the path at the positions in \(U_h\); call it \(\mu^h_\tau\).

*A potential.* Let \(q_h(\tau)\le L\) be the number of the queries to \(U_h\) on the path to \(\tau\), and
\[
\begin{gathered}
V_h(\tau)=\operatorname{val}\bigl(\mu^h_\tau,\ L-q_h(\tau)\bigr),\\
\Psi(\tau)=\prod_{h=1}^rV_h(\tau).
\end{gathered}
\]
At the root, \(\Psi=\beta^r\).

*One query.* Let \(\tau\) be an inner vertex that reads a position of \(U_h\), with the children \(\tau_0,\tau_1\) for the two answers. The conditional probability of the answer \(a\), given \(\tau\), is \(\mu^h_\tau(z_i=a)\); the distribution of \(U_h\) at \(\tau_a\) is \(\mu^h_\tau\) conditioned on this answer, and \(q_h(\tau_a)=q_h(\tau)+1\le L\). For the other inputs nothing changes. By (2.1) with \(j=L-q_h(\tau)\ge1\),
\[
\sum_a\Pr(\tau_a\mid\tau)\,\Psi(\tau_a)\le\Psi(\tau).
\]
By induction from the root, the sum of \(\Pr(\lambda)\Psi(\lambda)\) over the leaves \(\lambda\) is at most \(\beta^r\).

*The leaves.* At a leaf \(\lambda\) with the output \((b_1,\dots,b_r)\), by the product form,
\[
\begin{aligned}
&\Pr(\text{the output is correct}\mid\lambda)\\
&\quad=\prod_h\mu^h_\lambda(P=b_h)\\
&\quad\le\prod_h\operatorname{val}(\mu^h_\lambda,0)\le\Psi(\lambda).
\end{aligned}
\]
Summing over the leaves gives the lemma.

*Random choices and further input.* For every value of the random choices and of the further input, the algorithm is a decision tree on \((U_1,\dots,U_r)\) of the kind above, and the distribution of \((U_1,\dots,U_r)\) is not changed by conditioning on this value. \(\blacksquare\)

The bound \(\beta^r\) would be obvious if the algorithm treated the \(r\) inputs one after the other. The lemma allows it to jump between them, and to let its queries to one input depend on what it has seen in the others. The limit of \(L\) queries holds for each input separately; with a common limit of \(rL\) queries for all inputs the statement is false (Exercise 5.2).

## 3. The dummy input and the planted input

Let \(m\) be a large power of four and \(\mu\) the distribution of Lemma 1.1. We define two random inputs of \(F_{k,m}\) on one probability space.

**The dummy input \(Y^{(0)}\).** For every column \(i\) choose a position \(J_i\in\{1,\dots,m\}\) uniformly; the string \(X_i\) has a zero at the position \(J_i\) and ones elsewhere. Choose all strings \(A_{i,h}\) with the distribution \(\mu\). All these choices are independent. Every cell \(B_{i,s}\) consists of zeros only.

Every column has a zero in its string, so there is no winner: \(F_{k,m}(Y^{(0)})=0\).

**The planted input \(Y^{(1)}\).** Choose a column \(I\) uniformly, independently of the dummy input. \(Y^{(1)}\) is \(Y^{(0)}\) with two changes: the string \(X_I\) consists of ones only; and the cell \(B_{I,s_I}\) of the true address \(s_I\) of the column \(I\) contains the correct transcripts for \(A_{I,1},\dots,A_{I,r}\) and the pointers \(p_{I,s_I,j}=J_j\) for \(j\ne I\).

The strings \(A_{I,h}\) lie in the domain of \(P\), so the true address is defined. The pointers show the zeros of the other columns. So \(I\) is a winner: \(F_{k,m}(Y^{(1)})=1\).

The two inputs differ only at the bit \(X_I[J_I]\) and inside the cell \(B_{I,s_I}\).

## 4. The lower bound

**Proposition 4.1** ([OpenAI-Q]). Assume (BS). Let \(k\ge2\). For all large powers of four \(m\),
\[
R(F_{k,m})>G,\qquad G=\Bigl\lfloor\frac{mL}{100}\Bigr\rfloor .
\]

**Proof.** Let \(A\) be a decision tree of depth at most \(G\) on the inputs of \(F_{k,m}\), with outputs in \(\{0,1\}\), and
\[
\begin{aligned}
\Delta(A)={}&\Pr\bigl(A(Y^{(1)})=1\bigr)\\
&-\Pr\bigl(A(Y^{(0)})=1\bigr).
\end{aligned}
\]
We show
\[
\Delta(A)\le\frac{4G}{m^2}+\frac G{mL}+G\Bigl(\frac23\Bigr)^r .
\]
We refer to this inequality as (4.1).

*The coupling.* Consider the run of \(A\) on \(Y^{(0)}\), the *dummy run*. As long as it has not read the bit \(X_I[J_I]\) or a bit of the cell \(B_{I,s_I}\), the run on \(Y^{(1)}\) receives the same answers and reads the same positions. So \(\Delta(A)\) is at most the probability that the dummy run reads \(X_I[J_I]\) or a bit of \(B_{I,s_I}\). The dummy run does not depend on \(I\).

*The removed zero.* Say that the dummy run *finds the zero of the column \(i\)* if it reads the bit \(X_i[J_i]\), and let \(Z\) be the number of the columns whose zero it finds. Call a query an *early hit* if it reads \(X_i[J_i]\) for a column \(i\) in which, before this query, fewer than \(m/2\) positions of \(X_i\) were read. Consider a query to a position of \(X_i\) that was not read before, at a moment when the zero of \(i\) is not yet found and fewer than \(m/2\) positions of \(X_i\) were read. Given everything that the run has seen so far, \(J_i\) is uniformly distributed among the positions of \(X_i\) that were not read: the answers so far say about \(J_i\) only that it is none of the positions read, and all other parts of the input are independent of \(J_i\). So the query is an early hit with a conditional probability of at most \(\tfrac2m\). There are at most \(G\) queries, so the mean number of early hits is at most \(\tfrac{2G}m\). If the zero of a column is found, but not by an early hit, at least \(m/2\) positions of its string were read; there are at most \(\tfrac{2G}m\) such columns. Hence the mean of \(Z\) is at most \(\tfrac{4G}m\). Since \(I\) is uniform and independent of the dummy run,
\[
\begin{aligned}
&\Pr\bigl(\text{the dummy run reads }X_I[J_I]\bigr)\\
&\qquad=\frac{\mathbb E\,Z}m\le\frac{4G}{m^2}.
\end{aligned}
\]

*Heavy columns.* Call a column *heavy* if the dummy run makes more than \(L\) queries to its strings \(A_{i,1},\dots,A_{i,r}\) together. There are at most \(G/L\) heavy columns, so
\[
\Pr(I\text{ is heavy})\le\frac G{mL}.
\]

*Guessing the address.* Fix a column \(i\) and a number \(t\in\{1,\dots,G\}\). Consider the following algorithm \(A'\). Its inputs are \(U_h=A_{i,h}\), \(h=1,\dots,r\); the rest of the dummy input is its further input, which is independent of them. It carries out the dummy run up to the query number \(t\), which it does not make. If the run wants to make more than \(L\) queries to the strings \(U_1,\dots,U_r\) together, \(A'\) stops and outputs \(0\dots0\). If the run arrives at the query number \(t\) and this query reads a bit of a cell \(B_{i,s}\) of the column \(i\), \(A'\) outputs \(s\). Otherwise it outputs \(0\dots0\).

\(A'\) makes at most \(L\) queries to each \(U_h\). By Lemma 1.1, \(\operatorname{val}(\mu,L)\le\tfrac23\). By Lemma 2.1, \(A'\) outputs the true address \(s_i=(P(U_1),\dots,P(U_r))\) with a probability of at most \((2/3)^r\). Let \(E_{i,t}\) be the event that the column \(i\) is not heavy and the query number \(t\) of the dummy run reads a bit of \(B_{i,s_i}\). If it occurs, \(A'\) does not stop early and outputs \(s_i\). So
\[
\Pr(E_{i,t})\le\Bigl(\frac23\Bigr)^r .
\]
Adding over \(t\), and averaging over the column \(I\),
\[
\begin{aligned}
&\Pr\bigl(\text{the dummy run reads a bit of }B_{I,s_I}\bigr)\\
&\qquad\le\frac G{mL}+G\Bigl(\frac23\Bigr)^r .
\end{aligned}
\]
This proves (4.1).

*The numbers.* For large \(m\) we have \(1\le L\le m\) and \(G\le\tfrac{mL}{100}\). So \(\tfrac{4G}{m^2}\le\tfrac4{100}\) and \(\tfrac G{mL}\le\tfrac1{100}\). With \(r\ge20\log_2m\) and \(G\le m^2\),
\[
G\Bigl(\frac23\Bigr)^r\le m^{2-20\log_2(3/2)}\le m^{-9}.
\]
So the right side of (4.1) is at most \(\tfrac6{100}\).

*Randomized algorithms.* Let a randomized algorithm of cost at most \(G\) be given, a distribution on such trees \(A\). Averaging (4.1), the probabilities of the output \(1\) on \(Y^{(1)}\) and on \(Y^{(0)}\) differ by at most \(\tfrac6{100}\). If the algorithm computed \(F_{k,m}\) with error at most \(\tfrac13\), the first probability would be at least \(\tfrac23\) and the second at most \(\tfrac13\), because \(F_{k,m}(Y^{(1)})=1\) and \(F_{k,m}(Y^{(0)})=0\) always. So no such algorithm exists. \(\blacksquare\)

This is Part 2 of Theorem 2.2 of the first lesson. For large \(m\), \(G\ge\tfrac1{400}\,m^{2-1/k}/(\log_2m)^2\).

**The roles of the parts of the construction.** A randomized algorithm has three ways to find out that a column is a winner. It can look for zeros: this costs about \(m\) queries in a column, and \(m^2\) for all columns. It can compute the address of a column: this costs more than \(L\) queries in a column, by (BS), and \(mL\) for all columns; this is the cheapest way, and it gives the bound. Or it can guess the address: the \(r\) bits of the address are answers to independent hard questions, and Lemma 2.1 shows that a guess is right with a probability of at most \((2/3)^r\le m^{-11}\), too small even for \(m^2\) guesses. The cells of different columns are separate, so what an algorithm learns in one column does not help in another.

**What is assumed.** The proposition uses the hypothesis (BS) through Lemma 1.1 only: it needs a distribution on the domain of \(P\) on which every decision tree of depth at most \(L\) errs with a probability of at least \(\tfrac13\). All other steps are proved in this course.

## 5. Exercises

**5.1.** Show that \(\operatorname{val}(\nu,j)\) does not decrease in \(j\), and that \(\operatorname{val}(\nu,n_0)=1\).

**5.2.** Let \(n_0=2\), \(P(z)=z_1\oplus z_2\), \(\mu\) uniform, \(L=1\), \(r=2\). Find \(\beta\). Give a decision tree on \((U_1,U_2)\) with two queries in all that outputs \((P(U_1),P(U_2))\) with a probability larger than \(\beta^2\). Why is this no contradiction to Lemma 2.1?

**5.3.** In the proof of Proposition 4.1, why is the dummy run considered, and not the run on the planted input?

**5.4.** The address has \(r=\lceil20\log_2m\rceil\) bits. Which condition on the number \(20\) does the proof need?

**5.5.** Show \(D(F_{k,m})\le m^2+rkm+(m-1)\ell+rS\). Compare with Proposition 4.1 and with the quantum bound \(Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^4\).

## 6. Solutions

**5.1.** A tree of depth at most \(j\) is a tree of depth at most \(j+1\). A tree of depth \(n_0\) can read all of \(z\) and output \(P(z)\).

**5.2.** A tree with one query sees one bit of \(z\), and \(z_1\oplus z_2\) is uniform given this bit; so \(\beta=\tfrac12\) and \(\beta^2=\tfrac14\). The tree that reads both bits of \(U_1\) and outputs \((P(U_1),0)\) is right with the probability \(\tfrac12\). It makes two queries to \(U_1\), more than \(L=1\); the lemma limits the queries to each input separately.

**5.3.** The dummy run is independent of the column \(I\). So the probability that it meets the column \(I\) at a certain place is an average over all columns, and counting arguments apply: few columns are heavy, few zeros are found. The run on the planted input depends on \(I\) as soon as it meets a changed place; up to that moment it is the dummy run.

**5.4.** \(G(2/3)^r\) must be small, with \(G\le m^2\): this needs \(20\log_2(3/2)>2\), that is a number larger than \(2/\log_2(3/2)\approx3.42\) in place of \(20\).

**5.5.** Read all strings \(X_i\): \(m^2\) queries. A winner has a string of ones, and all other columns have a zero. So if the number of the columns whose string consists of ones only is not exactly one, the value is \(0\). Otherwise let \(i\) be this column. Read its strings \(A_{i,h}\): \(rkm\) queries. If some \(P(A_{i,h})\) is not defined, the value is \(0\). Otherwise read the cell of the true address, \((m-1)\ell+rS\) queries, and check the conditions 3 and 4 of a winner; the strings of the other columns are known. For large \(m\) this is at most \(2m^2\). With Proposition 4.1, \(R(F_{k,m})\) and \(D(F_{k,m})\) lie between \(\tfrac1{400}m^{2-1/k}/(\log_2m)^2\) and \(2m^2\), while \(Q(F_{k,m})\) is about \(\sqrt m\): the deterministic number is about the fourth power of the quantum number.

## References

- [OpenAI-Q] OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, OpenAI Math Release preprint, 5 October 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026
- [BS] N. Bansal and M. Sinha, *k-Forrelation optimally separates quantum and classical query complexity*, arXiv:2008.07003, version 3, Corollary 1.4. https://arxiv.org/abs/2008.07003
