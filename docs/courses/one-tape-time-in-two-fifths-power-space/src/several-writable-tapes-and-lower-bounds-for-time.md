# Several writable tapes, and lower bounds for time

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The theorem of this course is about machines with one writable tape. This lesson looks at its two sides. First, the proof does not extend to two writable tapes, and the lesson shows where it stops and what remains: space \(\widetilde O(\sqrt T)\), the exponent that was known. Second, a simulation in small space gives a lower bound for time: by the space hierarchy theorem, there are problems that can be solved in space \(s\) and that no machine with one writable tape solves in time \(s^{5/2-\epsilon}\).

- A test that is not a product (Proposition 1.1).
- Machines with several writable tapes in space \(\widetilde O(\sqrt T)\) (Proposition 2.3).
- A lower bound for time from the space hierarchy theorem, which is a named hypothesis (Corollary 3.1).

The lesson follows [OpenAI-S, Sections 4 and 5]. It uses the first lesson, [One-tape machines, blocks and visits](one-tape-machines-blocks-and-visits.md), the evaluator of [An evaluator with one pool of registers](an-evaluator-with-one-pool-of-registers.md) for ordinary rules only, and the theorem of [Histories, checkpoints and the theorem](histories-checkpoints-and-the-theorem.md).

## 1. A test that is not a product

In the proof of the theorem, a guess for the next controllers is tested against every block separately, and the guess is right if all tests are passed. This has the form of a product, \(\prod_iP_{Y,i}(H,A_i)\), and the evaluator needs this form: it brings the words \(A_i\) into one register one after the other.

With two writable tapes, one step reads a cell of each tape, so a visit reads two blocks, and the controller after the visit depends on both.

**Proposition 1.1.** There are no functions \(P_1,P_2\) from bits to a field such that \(P_1(x)P_2(y)\) is \(1\) if \(x=y\) and \(0\) if \(x\ne y\), for all bits \(x,y\).

**Proof.** From \(P_1(0)P_2(0)=1\) and \(P_1(1)P_2(1)=1\), all four values are different from \(0\). Then \(P_1(0)P_2(1)\ne0\). \(\blacksquare\)

So consider a machine that, in its first step, reads one bit on each of two tapes and goes to one state if they are equal and to another if not. Whether the guess "the next state is the first one" is right is the condition \(x=y\) on the two bits. By the proposition it is not a product of a test of the first tape and a test of the second, and it is not so even when everything that happened before is known. The proof of the theorem stops here. This is a statement about this proof, not about what is possible for machines with two tapes.

## 2. Several writable tapes

**The machine.** Let \(M\) be a deterministic machine with \(w\ge1\) writable tapes, each with one head, and \(\rho\ge0\) read-only heads. In one step it reads the cells under all heads, writes to the cells under the writable heads, moves every head by \(-1\), \(0\) or \(1\) and changes its state. Symbol functions, the accessor and the access condition are as in the first lesson, with one symbol function for each writable tape and each read-only head. A *controller* consists of a state, the two flags, the elapsed time \(\tau\le T\) and the displacements of all \(w+\rho\) heads, each of absolute value at most \(\tau\); it has \(c=O(\log(T+2))\) bits.

**Blocks and joint visits.** Cut every writable tape into blocks of the width \(b\) with the same offset \(a\), and label the blocks that meet \(I_T\) by \(1,\dots,N\) on each tape. A *joint visit* lasts until one of the writable heads leaves its block, or the machine halts, or the time \(T\) is reached. It reads and writes \(w\) blocks, one of each tape.

**Lemma 2.1.** For some offset, the controller after \(R=\lceil1+wT/b\rceil\) joint visits is terminal.

**Proof.** A step in which a given head moves by one cell passes from a block to another for exactly one offset. So the number of the pairs of a step and a head that passes a boundary in it, added over the \(b\) offsets, is at most \(wT\). For some offset, at most \(wT/b\) steps have a head that passes a boundary. Every joint visit that does not end the computation ends with such a step. \(\blacksquare\)

For a raw controller \(z\) let \(\operatorname{sel}_h(z)\) be the label of the block of the tape \(h\) that contains the displacement of its head, or the block of the cell \(0\) if \(z\) is rejected. For raw blocks \(B_1,\dots,B_w\) let
\[
\begin{aligned}
&\operatorname{JVisit}(z;B_1,\dots,B_w)\\
&\quad=(z';B_1',\dots,B_w')
\end{aligned}
\]
be defined as \(\operatorname{Visit}\) in the first lesson: a rejected \(z\) gives the dummy controller and unchanged blocks, a terminal one gives no change, and otherwise the machine is run from \(z\) with \(B_h\) as the block \(\operatorname{sel}_h(z)\) of the tape \(h\), until the joint visit ends. Lemma 4.1 of the first lesson holds with the same proof: \(\operatorname{JVisit}\) is defined for all raw arguments and computed in space \(O((wb+1)\operatorname{polylog}T)\); the run stays in the cells of \(I_T\) and asks the accessor only within the range of the access condition; and on the controller and the represented blocks of the capped computation it gives the controller and the represented blocks after the joint visit.

**The system of a list.** Let \(Z=(z_0,z_1,\dots,z_R)\) be a list of raw controllers in which \(z_0\) is the code of the controller at the time \(0\). For \(1\le t\le R\) and a tape \(h\), let \(i_{t,h}=\operatorname{sel}_h(z_{t-1})\), and let \(\operatorname{pre}(t,h)\) be the largest \(s<t\) with \(i_{s,h}=i_{t,h}\), or \(0\) if there is none. Consider the following system of words of the width \(d=b\ell\), where \(\ell\) is the number of bits of a symbol.

- Base vertices \(I_{h,i}\): the represented block \(i\) of the initial content of the tape \(h\).
- For \(1\le t\le R\), the *incoming* vertices of \(t\) are, for each tape \(h\): the vertex \(Q_{\operatorname{pre}(t,h),h}\) if \(\operatorname{pre}(t,h)\ge1\), and \(I_{h,i_{t,h}}\) otherwise.
- \(Q_{t,h}\), for \(1\le t\le R\) and each tape \(h\), is an ordinary vertex whose dependencies are the \(w\) incoming vertices of \(t\). Its function is the block \(B_h'\) of \(\operatorname{JVisit}(z_{t-1};\cdot)\) applied to these \(w\) words.
- \(X_t\), for \(1\le t\le R\), is an ordinary vertex with the same dependencies. Its function has the value \(10\cdots0\) if the raw controller \(z'\) of \(\operatorname{JVisit}(z_{t-1};\cdot)\) is equal to \(z_t\), and \(00\cdots0\) otherwise.

The values of the vertices are defined by the rules; this is possible for every list \(Z\), because all dependencies of a vertex with the index \(t\) have smaller indices. The list \(Z\) is data that stay fixed while the system is evaluated.

**Lemma 2.2.** The words \(X_1,\dots,X_R\) all begin with \(1\) if and only if \(Z\) is the list of the controllers of the reference evolution, the serial application of \(\operatorname{JVisit}\) from \(z_0\) and the initial represented blocks.

**Proof.** We show by induction on \(t\): if \(X_1,\dots,X_t\) begin with \(1\), then \(z_0,\dots,z_t\) are the first controllers of the reference evolution, and for \(s\le t\) the word \(Q_{s,h}\) is the block \(i_{s,h}\) of the tape \(h\) after \(s\) steps of the reference evolution. Let this hold for \(t-1\). Up to the step \(t-1\) the reference evolution selects the blocks that the list selects. The block \(i_{t,h}\) of the tape \(h\) was last selected at the step \(\operatorname{pre}(t,h)\), or never, and has not changed since. So the incoming words of \(t\) are the contents, after \(t-1\) steps, of the blocks that \(z_{t-1}\) selects, and the functions of \(Q_{t,h}\) and \(X_t\) compute the step \(t\) of the reference evolution. Since \(X_t\) begins with \(1\), \(z_t\) is the reference controller, and \(Q_{t,h}\) is the new content. The same induction shows that all \(X_t\) begin with \(1\) if \(Z\) is the reference list. \(\blacksquare\)

**Proposition 2.3** ([OpenAI-S]). Let \(M\) be a machine with a fixed number of writable tapes and read-only heads and a fixed accessor. There is an algorithm that, for every input \(x\) and every \(T\ge2\) for which the access condition holds, computes the outcome of the capped computation in space \(\widetilde O(\sqrt T)\).

**Proof.** If there is no writable tape, the algorithm runs the machine, keeping the controller: space \(\operatorname{polylog}T\). Let \(w\ge1\), and put \(b=\lceil\sqrt T\rceil\) and \(R=\lceil1+wT/b\rceil\).

*The algorithm.* For every offset \(a\) and every list \(Z=(z_0,\dots,z_R)\) of raw controllers with the given \(z_0\): keep \(Z\) in a buffer of \((R+1)c\) bits; compute the words \(X_1,\dots,X_R\) one after the other with the evaluator (Theorem 2.1 of the third lesson); if all begin with \(1\) and \(z_R\) is terminal, give out the state and the halt flag of \(z_R\) and stop.

*It is right.* If all \(X_t\) begin with \(1\), then by Lemma 2.2 and the agreement of \(\operatorname{JVisit}\) with the capped computation, \(z_R\) is the controller of the capped computation after \(R\) joint visits; if it is terminal, it gives the outcome. For an offset as in Lemma 2.1, the reference list passes and ends with a terminal controller. So the algorithm stops, and with the right outcome.

*The space.* The system has ordinary and base vertices only, at most \(w\) dependencies per vertex, and polynomially many vertices. The dependencies of a vertex are found from its name by scanning the buffer of \(Z\). Every step of a path lowers the index \(t\), so \(W\le R\). By Theorem 2.1 of the third lesson, with the buffer added once, the space is
\[
\begin{aligned}
&O\bigl((d+R+1)\operatorname{polylog}T\bigr)+(R+1)c\\
&\quad=\widetilde O(b+T/b)=\widetilde O(\sqrt T).
\end{aligned}
\]
\(\blacksquare\)

Compare with the proof of the theorem. Here the whole list of the controllers is guessed at once and kept in storage: about \(T/b\) controllers. For one writable tape, the guesses are made round by round and the earlier rounds are recomputed when they are needed; this is what the factored test allows. A machine with several tapes can be simulated by a machine with one tape in about \(T^2\) steps, by the usual construction; the theorem for one tape then gives space \(\widetilde O(T^{4/5})\), which is worse than \(\sqrt T\). So the theorem gives nothing new for several tapes.

For several tapes, R. Williams proved the bound \(O(\sqrt{T\log T})\), with a better power of the logarithm than Proposition 2.3; see [OpenAI-S, Section 1] for the reference.

## 3. A lower bound for time

A *language* is a set of strings. An algorithm *decides* it if, for every string, it stops and says correctly whether the string belongs to the language. A language is *decided in space \(O(s(n))\)* if some algorithm decides it with space at most \(Cs(n)+C\) on all strings of the length \(n\). It is *decided in space \(o(s(n))\)* if some algorithm decides it in a space \(r(n)\) with \(r(n)/s(n)\to0\).

A function \(s\) from the natural numbers to the natural numbers is *space-constructible* if some algorithm computes the number \(s(n)\) from every string of the length \(n\) in space \(O(s(n))\).

**Hypothesis (SH), the space hierarchy theorem.** For every space-constructible function \(s\) with \(s(n)\ge\log_2(n+2)\) there is a language that is decided in space \(O(s(n))\) and not in space \(o(s(n))\).

This is a theorem of R. Stearns, J. Hartmanis and P. Lewis. It is proved by a diagonal argument and is not proved in this course. The notion of space of this course, the number of bits of working storage, agrees up to constant factors with the number of cells of the work tapes of a Turing machine with a read-only input tape, for which the theorem is usually stated.

A language is *decided by a machine with one writable tape in time \(O(t(n))\)* if a machine as in Theorem 1.1 of the first lesson, with the input written on one of its tapes in the usual way, halts on every string of the length \(n\) after at most \(Ct(n)+C\) steps, in a state that says whether the string belongs to the language.

**Corollary 3.1** ([OpenAI-S]). Assume (SH). Let \(s\) be a space-constructible function with \(s(n)\ge n\), and \(0<\epsilon<\tfrac52\). Then there is a language that is decided in space \(O(s(n))\), and that no machine with one writable tape decides in time \(O(s(n)^{5/2-\epsilon})\).

**Proof.** Let \(\alpha=\tfrac52-\epsilon\), and let \(M\) be a machine with one writable tape that decides a language in time \(t(n)\le Cs(n)^\alpha+C\). We show that the language is decided in space \(o(s(n))\); the corollary then follows from (SH).

On a string \(x\) of the length \(n\), the algorithm counts \(n\) and applies the second part of the theorem (Theorem 4.1 of the fourth lesson), starting with the cap \(\max\{2,n\}\) and doubling it. For a cap \(T\ge n\), a symbol of the input at a displacement of at most \(T\) is found by counting along the input, in \(O(\log(T+2))\) bits; so the access condition holds for every cap that is used. The machine halts after \(t(n)\) steps, so the last cap is at most \(2\max\{2,n,t(n)\}\), and the space is
\[
\widetilde O\bigl((n+t(n)+2)^{2/5}\bigr).
\]
Since \(n\le s(n)\) and \(t(n)\le Cs(n)^\alpha+C\), we have \(n+t(n)+2=O(s(n)^{\max\{1,\alpha\}})\). Put
\[
\begin{aligned}
\beta&=\tfrac25\max\{1,\alpha\}\\
&=\max\bigl\{\tfrac25,\ 1-\tfrac{2\epsilon}5\bigr\}<1 .
\end{aligned}
\]
The space is \(O(s(n)^\beta\log^{C'}(s(n)+2))\), and this is \(o(s(n))\) because \(\beta<1\) and \(s(n)\ge n\) tends to infinity. \(\blacksquare\)

**Example 3.2.** For \(s(n)=n\): assuming (SH), there is a language that is decided in linear space and that no machine with one writable tape decides in time \(O(n^{2.49})\). The classical simulation with the exponent \(\tfrac12\) gives, by the same proof, the time bound \(n^{2-\epsilon}\) only.

[OpenAI-S, Section 5] also gives a particular language with this property: the set of the triples of a machine, an input and a number \(k\) in unary such that the machine halts on the input within \(k\) cells. That statement, and the proof that this language is complete for linear space, are not in this course.

Corollary 3.1 is a statement about machines with one writable head. It gives no bound for machines with several writable tapes or with random access.

## 4. Exercises

**4.1.** Show that equality of two bits is a sum of two products: give functions \(P_1,P_2,P_1',P_2'\) from bits to bits such that \(P_1(x)P_2(y)+P_1'(x)P_2'(y)\) is \(1\) for \(x=y\) and \(0\) for \(x\ne y\). Why does this not rescue the proof of the theorem for two writable tapes?

**4.2.** In the system of Section 2, let \(w=2\), and let the list \(Z\) select the blocks \((1,1)\), \((2,1)\), \((2,2)\), \((1,2)\) of the two tapes at the steps \(t=1,2,3,4\). Give the incoming vertices of \(t=4\).

**4.3.** Why can the algorithm of Proposition 2.3 not keep the list \(Z\) on the stack of the evaluator, as a guess of a history vertex?

**4.4.** Compute \(\beta\) in the proof of Corollary 3.1 for \(\alpha=2\) and for \(\alpha=\tfrac12\). Where does the proof use \(s(n)\ge n\)?

**4.5.** Let \(s(n)=n^2\). What does Corollary 3.1 say? What would the classical exponent \(\tfrac12\) give?

## 5. Solutions

**4.1.** Take \(P_1(x)=x\), \(P_2(y)=y\), \(P_1'(x)=1-x\), \(P_2'(y)=1-y\). Then \(xy+(1-x)(1-y)\) is \(1\) for \(x=y\) and \(0\) for \(x\ne y\). In the same way, a condition on two blocks is a sum, over all contents \(u\) of the first block, of the product of the test "the first block is \(u\)" and a test of the second block that depends on \(u\). This has the form (1.1) of the third lesson, with the content \(u\) as a part of the guess. But then the guess has as many bits as a block, and a guess is kept on the stack whenever one of the words \(A_i\) is called for. In the proof of the theorem a guess has \(kc\) bits, about the square root of the size of a block, and this is what the bound needs.

**4.2.** At \(t=4\) the list selects the block \(1\) of the first tape and the block \(2\) of the second. The block \(1\) of the first tape was last selected at \(t=1\): the incoming vertex is \(Q_{1,1}\). The block \(2\) of the second tape was last selected at \(t=3\): the incoming vertex is \(Q_{3,2}\).

**4.3.** A guess of a history vertex is tested by factors, each of which contains one of the words \(A_i\). The test of the list for several tapes at the step \(t\) contains \(w\) blocks at once, and by Proposition 1.1 it is not a product of tests of the single blocks. Apart from this, the list has \((R+1)c\) bits; a guess of this size, kept on the stack along a path with several steps to blocks, would cost more than the one buffer of the algorithm.

**4.4.** For \(\alpha=2\): \(\beta=\tfrac45\). For \(\alpha=\tfrac12\): \(\beta=\tfrac25\), because of the term \(n\) in \(n+t(n)\): the simulation must at least be able to address the input. The assumption \(s(n)\ge n\) is used for \(n=O(s(n))\) in the bound of the space, and for \(s(n)\to\infty\).

**4.5.** Assuming (SH), there is a language that is decided in space \(O(n^2)\) and that no machine with one writable tape decides in time \(O(n^{5-2\epsilon})\), for example not in time \(O(n^{4.9})\). With the exponent \(\tfrac12\) the same proof gives \(\beta=\tfrac12\max\{1,\alpha\}<1\) for \(\alpha<2\): no machine decides it in time \(O(s(n)^{2-\epsilon})=O(n^{4-2\epsilon})\).

## References

- [OpenAI-S] OpenAI, *Simulating One-Tape Time in Two-Fifths-Power Space*, OpenAI Math Release preprint, 25 September 2026, Sections 1, 4 and 5. https://github.com/openai/math/tree/main/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026
