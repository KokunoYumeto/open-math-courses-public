# Histories, checkpoints and the theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the theorem of [OpenAI-S]: the outcome of \(T\) steps of a machine with one writable tape can be computed in space \(\widetilde O(T^{2/5})\). The computation is cut into *epochs* of \(b\) visits, and each epoch into *rounds* of \(k=\sqrt b\) visits. The list of the controllers of an epoch grows round by round, and the content of every block is recorded at the start of every epoch. These lists and blocks are the words of a system as in the previous lesson. A round is a history rule: the \(k\) new controllers are guessed, and the guess is tested against every block separately, by the replay of the first lesson. The evaluator then gives the space bound.

- The epochs, the rounds and the words (Section 1).
- The rules of the system, and the round as a history rule (Lemmas 2.1 and 2.2).
- The weight of a path (Lemma 3.1).
- Proof of the theorem (Section 4), and why the exponent is \(\tfrac25\) (Section 5).

The lesson follows [OpenAI-S, Sections 3.2 to 3.4]. It uses the visits, the reference evolution and the replay of [One-tape machines, blocks and visits](one-tape-machines-blocks-and-visits.md) and the evaluator of [An evaluator with one pool of registers](an-evaluator-with-one-pool-of-registers.md).

## 1. Epochs, rounds and words

The machine \(M\), the input \(x\) and the cap \(T\ge2\) are as in the first lesson, and the access condition holds for \((x,T)\). Put
\[
\begin{gathered}
k=\lceil T^{1/5}\rceil,\qquad b=k^2,\\
R=\lceil1+T/b\rceil,\qquad E=\lceil R/b\rceil .
\end{gathered}
\]
Fix an offset \(a\). The blocks \(C_1,\dots,C_N\) have the width \(b\), and \(N\le2+2T/b\). Let \(z_0,z_1,z_2,\dots\) and \(B_i^{(m)}\), for \(1\le i\le N\) and \(m\ge0\), be the reference list and the blocks of the reference evolution that starts from the controller of the computation at the time \(0\) and the represented blocks of the initial tape. By Lemma 5.1 of the first lesson, \(z_m\) is the controller of the capped computation after \(m\) visits, and \(B_i^{(m)}\) is the represented block \(i\) of the tape at that time.

The first \(Eb\) visits are divided into \(E\) *epochs* of \(b\) visits: the epoch \(e\), for \(0\le e<E\), consists of the visits number \(eb+1,\dots,eb+b\). An epoch is divided into \(k\) *rounds* of \(k\) visits. Since \(Eb\ge R\), the controller \(z_{Eb}\) is terminal if the offset is as in Lemma 3.1 of the first lesson.

**The width.** Let \(\ell\) be the number of bits of a symbol and \(c=O(\log(T+2))\) the number of bits of a raw controller, as in the first lesson. Put
\[
\begin{aligned}
d&=\max\{b\ell,\ (b+1)c\}\\
&=O\bigl(b\log(T+2)\bigr).
\end{aligned}
\]
A *word* is a string of \(d\) bits. A raw block is written as a word by adding zeros at the end, and so is a list of at most \(b+1\) raw controllers. When a word is read as a block or as a list, only the bits at the beginning that are needed are read.

**The words.** For \(0\le e<E\):

- \(A_{e,i}\), for \(1\le i\le N\), is the block \(B_i^{(eb)}\): the block \(i\) at the start of the epoch \(e\);
- \(H_{e,j}\), for \(0\le j\le k\), is the list \((z_{eb},z_{eb+1},\dots,z_{eb+jk})\): the controller at the start of the epoch \(e\) and the controllers after each of the visits of its first \(j\) rounds.

The word that is wanted is \(H_{E-1,k}\): its last controller is \(z_{Eb}\).

A list \(H_{e,j}\) has at most \(b+1\) controllers, about \(b\log T\) bits, like a block. The \(N\) blocks of one epoch together have about \(T\) bits. They are never in storage together.

## 2. The rules

The words are the values of a system in the sense of the previous lesson, with the following vertices and rules. The functions of the rules are defined for all words, not only for those that occur.

- **Base.** \(A_{0,i}\) and \(H_{0,0}\) are base vertices. The bits of \(A_{0,i}\) are found with the accessor for the cells of \(C_i\) in \(I_T\), and are the code of the filler for the other cells. \(H_{0,0}\) is the code of the controller at the time \(0\).
- **Extraction.** For \(e\ge1\), \(H_{e,0}\) is an ordinary vertex with the one dependency \(H_{e-1,k}\). Its function reads a word as a list of \(b+1\) raw controllers and returns the last one, as a list of length one.
- **Checkpoint.** For \(e\ge1\), \(A_{e,i}\) is an ordinary vertex with the two dependencies \(H_{e-1,k}\) and \(A_{e-1,i}\). Its function reads the first word as a list \(Z\) of \(b+1\) raw controllers and the second as a raw block \(B\), and returns the buffer of \(\operatorname{Replay}_i(Z,B)\).
- **Round.** For \(0\le j<k\), \(H_{e,j+1}\) is a history vertex with the dependency \(H=H_{e,j}\), the further dependencies \(A_{e,1},\dots,A_{e,N}\), and guesses of \(g=kc\) bits. Its functions are given in Lemma 2.2.

**Lemma 2.1.** The words \(H_{e,0}\) and \(A_{e,i}\), \(e\ge1\), are the values of the extraction and the checkpoint functions at the words of their dependencies.

**Proof.** For the extraction this is the definition of the words. For the checkpoint, consider the reference evolution that starts from the raw controller \(z_{(e-1)b}\) and the blocks \(B_i^{((e-1)b)}\). It is the part of the reference evolution of Section 1 from the step \((e-1)b\) on. So its reference list after \(b\) steps is the list of \(H_{e-1,k}\), and its blocks after \(b\) steps are the \(B_i^{(eb)}\). By Lemma 5.2 of the first lesson, the replay of this list on the block \(B_i^{((e-1)b)}\) has the flag \(1\) and the buffer \(B_i^{(eb)}\). \(\blacksquare\)

**Lemma 2.2** (a round is a history rule). Let \(0\le e<E\) and \(0\le j<k\). For a guess \(Y\), a string of \(kc\) bits read as \(k\) raw controllers \(y_1,\dots,y_k\), and for words \(H'\) and \(A'\), define:

- \(Z_Y(H')\) is the list of the first \(jk+1\) raw controllers of \(H'\), followed by \(y_1,\dots,y_k\);
- \(G_Y(H')\) is the list \(Z_Y(H')\), written as a word;
- \(P_{Y,i}(H',A')\) is the flag of \(\operatorname{Replay}_i(Z_Y(H'),B')\), where \(B'\) is the raw block at the beginning of \(A'\).

Then exactly one guess \(Y\) has \(P_{Y,i}(H_{e,j},A_{e,i})=1\) for all \(i\le N\), namely the guess formed by \(z_{eb+jk+1},\dots,z_{eb+(j+1)k}\), and for this guess \(G_Y(H_{e,j})=H_{e,j+1}\). So the identity (1.1) of the previous lesson holds:
\[
\begin{aligned}
\overline{H_{e,j+1}}=\sum_Y\ &\overline{G_Y(H_{e,j})}\\
&\cdot\prod_{i=1}^NP_{Y,i}(H_{e,j},A_{e,i}).
\end{aligned}
\]
The functions \(G_Y\) and \(P_{Y,i}\) are computed from their arguments in space \(O(d\operatorname{polylog}T)\).

**Proof.** The list \(Z_Y(H_{e,j})\) begins with \(z_{eb}\) and has \((j+1)k+1\) controllers. By Lemma 5.2 of the first lesson, applied to the reference evolution from \(z_{eb}\) and the blocks \(B_i^{(eb)}=A_{e,i}\), all its replay flags are \(1\) if and only if it is the reference list \((z_{eb},\dots,z_{eb+(j+1)k})\). Its first \(jk+1\) controllers are those of \(H_{e,j}\) and agree with this list. So the flags are all \(1\) exactly if \(y_1,\dots,y_k\) are the next \(k\) controllers. For this guess, \(G_Y(H_{e,j})\) is the list of \(H_{e,j+1}\). In the sum, the term of this guess is \(\overline{H_{e,j+1}}\) and all other terms are \(0\).

For the space: \(Z_Y(H')\) has at most \(b+1\) controllers because \((j+1)k\le b\), and the replay needs \(O((b+(b+1)c+1)\operatorname{polylog}T)\) bits by Lemma 5.2(3) of the first lesson. \(\blacksquare\)

The replay in \(P_{Y,i}\) starts at the beginning of the epoch, where the block \(A_{e,i}\) is known, and runs through the earlier rounds of the epoch again before it reaches the guessed part. The lemma is where the single writable tape is used: the test of a guess is a product of \(N\) tests, and each test looks at one block.

**The system.** The vertices are the \(E(N+k+1)\) pairs of a letter and two indices. The epoch \(e-1\) comes before the epoch \(e\), and inside an epoch the \(A_{e,i}\) come first and then \(H_{e,0},\dots,H_{e,k}\); every dependency comes earlier in this order. The assumptions of the previous lesson on size and uniformity hold: the number of the vertices is at most \(T^C\); a name consists of a letter and two numbers of \(O(\log(T+2))\) bits, and the dependencies are found from it by adding and subtracting \(1\); the ordinary rules have at most \(r=2\) dependencies; all functions are computed in space \(O(d\operatorname{polylog}T)\), by Lemma 2.2 and Lemmas 4.1 and 5.2 of the first lesson; and
\[
\Delta=(N+1)d
\]
is at most \(T^C\) and bounds \(d\) and the degree of every history vertex.

## 3. The weight of a path

In the system of Section 2, the steps of a path have the following weights: \(1\) from \(H_{e,j+1}\) to \(H_{e,j}\); \(kc+1\) from \(H_{e,j+1}\) to \(A_{e,i}\); and \(1\) from \(H_{e,0}\) to \(H_{e-1,k}\), from \(A_{e,i}\) to \(A_{e-1,i}\) and from \(A_{e,i}\) to \(H_{e-1,k}\).

**Lemma 3.1.** Every path that starts at a vertex of the epoch \(e\) has a weight of at most \((e+1)(k+kc+2)\). In particular
\[
\begin{aligned}
W(H_{E-1,k})&\le E\,(k+kc+2)\\
&=O\bigl(Ek\log(T+2)\bigr).
\end{aligned}
\]

**Proof.** Put \(q=k+kc+2\). Let \(\alpha_e\) be the largest weight of a path that starts at some \(A_{e,i}\), and \(\eta_e\) the largest weight of a path that starts at some \(H_{e,j}\). We show \(\alpha_e\le eq\) and \(\eta_e\le(e+1)q-1\) by induction on \(e\).

A path from \(H_{e,j}\) first goes down through \(H_{e,j-1},H_{e,j-2},\dots\) by steps of the weight \(1\). It leaves this chain either by a step of the weight \(kc+1\) to some \(A_{e,i}\), after at most \(k-1\) steps of the chain, or, for \(e\ge1\), by the step of the weight \(1\) from \(H_{e,0}\) to \(H_{e-1,k}\), after at most \(k\) steps of the chain; or it ends at the base vertex \(H_{0,0}\). So \(\eta_e\) is at most the larger of the two numbers
\[
\begin{gathered}
(k-1)+(kc+1)+\alpha_e=k+kc+\alpha_e,\\
k+1+\eta_{e-1},
\end{gathered}
\]
where the second number is present only for \(e\ge1\). A path from \(A_{e,i}\), \(e\ge1\), starts with a step of the weight \(1\) into the epoch \(e-1\): \(\alpha_e\le1+\max\{\alpha_{e-1},\eta_{e-1}\}\); and \(\alpha_0=0\).

For \(e=0\): \(\alpha_0=0\) and \(\eta_0\le k+kc=q-2\). For \(e\ge1\), by the induction hypothesis, \(\alpha_e\le1+(eq-1)=eq\), and
\[
\begin{aligned}
\eta_e&\le\max\{k+kc+eq,\ k+1+eq-1\}\\
&=eq+k+kc=(e+1)q-2 .
\end{aligned}
\]
\(\blacksquare\)

The point of the lemma: a step of the large weight \(kc+1\) leads to a block \(A_{e,i}\), and from there the path can only go on into the epoch before. So a path pays for at most one guess in each epoch, although an epoch has \(k\) rounds.

## 4. Proof of the theorem

**Theorem 4.1** ([OpenAI-S]). Let \(M\) be a machine with one writable tape and head and a fixed number of read-only heads, with a fixed accessor. There is an algorithm that, for every input \(x\) and every \(T\ge2\) for which the access condition holds, computes the outcome of the capped computation in space \(\widetilde O(T^{2/5})\). If the access condition holds for \((x,T)\) for all \(T\ge2\) and \(M\) halts on \(x\) after \(t\) steps, the outcome is computed without a given cap in space \(\widetilde O((t+2)^{2/5})\).

**Proof.** *The algorithm.* For each offset \(a=0,1,\dots,b-1\) in turn: compute the word \(H_{E-1,k}\) of the system of Section 2 with the evaluator (Theorem 2.1 of the previous lesson), and read its last controller. If it is terminal, give out its state and its halt flag, and stop. Otherwise go on with the next offset, in the same storage.

*It is right.* By Lemmas 2.1 and 2.2 the words of Section 1 are the values of the system, so the evaluator finds \(H_{E-1,k}\), whose last controller is \(z_{Eb}\), the controller of the capped computation after \(Eb\) visits (Lemma 5.1 of the first lesson). If it is terminal, the capped computation has ended, and its state and halt flag are the outcome; this holds for every offset. For an offset with at most \(T/b\) passing steps, which exists by Lemma 3.1 of the first lesson, it is terminal, because \(Eb\ge R\).

*The space.* By Theorem 2.1 of the previous lesson and Lemma 3.1 the space is
\[
\begin{aligned}
&O\bigl((d+W(H_{E-1,k})+1)\operatorname{polylog}T\bigr)\\
&\quad=\widetilde O(b+Ek).
\end{aligned}
\]
Here \(k\le T^{1/5}+1\), so \(b=k^2\le4T^{2/5}\). And \(b^2=k^4\ge T^{4/5}\), so \(T/b^2\le T^{1/5}\le k\) and
\[
E\le1+\frac Rb\le1+\frac{2+T/b}{b}\le3+k .
\]
Hence \(Ek\le3k+k^2=O(T^{2/5})\). The counters for the offsets and the storage of the accessor add \(\operatorname{polylog}T\).

*Without a cap.* Run the algorithm with the caps \(T=2,4,8,\dots\), each time in the same storage. If the outcome for a cap says that the machine has not halted, go on to the next cap; if it has halted, give out the state. If \(M\) halts after \(t\) steps, this happens at the latest for the first cap \(T\ge t\), and \(T\le2\max\{t,2\}\). \(\blacksquare\)

The algorithm never writes down the tape of the machine. Its storage is three registers of \(d+1\) field elements, a scratch area of the same order, and a stack of \(O(Ek\operatorname{polylog}T)\) bits.

**Remark** (one bit of an output). If the machine writes an output, symbol by symbol, on a further tape that it cannot read, one bit of the output at a given position can be found in the same space: the controller is extended by the position asked for, a counter of the symbols written so far, and the bit, once it has been written. This adds \(O(\log(T+2))\) bits to \(c\) and changes nothing else.

## 5. Why the exponent is two fifths

Let the block width be \(\mathsf B\), the number of the visits of an epoch \(\mathsf L\), and the number of the visits of a round \(\mathsf q\); in the proof \(\mathsf B=\mathsf L=b\) and \(\mathsf q=k\). Leave out logarithms and rounding.

- A word must hold a block or the list of an epoch: \(\mathsf B+\mathsf L\) bits.
- There are \(T/\mathsf B\) visits, so \(T/(\mathsf B\mathsf L)\) epochs, each with \(\mathsf L/\mathsf q\) rounds.
- A path pays \(\mathsf L/\mathsf q\) for the steps along the rounds of an epoch and \(\mathsf q\) for one guess, in every epoch:
\[
\frac{T}{\mathsf B\mathsf L}\Bigl(\frac{\mathsf L}{\mathsf q}+\mathsf q\Bigr).
\]

The bracket is smallest for \(\mathsf q=\sqrt{\mathsf L}\), where the stack is \(2T/(\mathsf B\sqrt{\mathsf L})\). If the storage is to be at most \(\mathsf S\), then \(\mathsf B,\mathsf L\le\mathsf S\), so the stack is at least \(2T/\mathsf S^{3/2}\), and \(\mathsf S\ge2T/\mathsf S^{3/2}\) gives \(\mathsf S\ge T^{2/5}\). So within this construction the three scales cannot be chosen better. This says nothing about other constructions.

Two special cases show what the rounds are for (Exercises 6.3 and 6.4). With one round per epoch (\(\mathsf q=\mathsf L\)) the whole list of an epoch is guessed at once, and with rounds of one visit (\(\mathsf q=1\)) a path has a step for every visit. Both give the exponent \(\tfrac12\).

## 6. Exercises

**6.1.** Compute \(k\), \(b\), \(R\), \(E\) and the bound for \(N\) for \(T=10^5\). How many vertices has the system?

**6.2.** The checkpoint rule replays \(b\) visits, and the round rule replays at most \(b\) visits for every guess. Why does a step to a dependency of a checkpoint have the weight \(1\), and a step from a round to a block the weight \(kc+1\)?

**6.3.** Suppose every epoch consisted of one round of \(b\) visits (guesses of \(bc\) bits). Find the bound for the weight of a path and the resulting space, as a function of \(b\), and the best \(b\).

**6.4.** The same for rounds of one visit (guesses of \(c\) bits, \(b\) rounds per epoch).

**6.5.** Show that the last controller of \(H_{E-1,k}\) is the same for every offset \(a\) for which it is terminal, although the words \(A_{e,i}\) and \(H_{e,j}\) depend on \(a\).

## 7. Solutions

**6.1.** \(k=\lceil10\rceil=10\), \(b=100\), \(R=\lceil1+1000\rceil=1001\), \(E=\lceil1001/100\rceil=11\), and \(N\le2+2000=2002\). The system has \(E(N+k+1)\le11\cdot2013=22{,}143\) vertices.

**6.2.** The weight counts what a call keeps on the stack while it waits. The replay itself is a local computation in the scratch area; it is finished before any call is made, whatever its length. A checkpoint calls for its two dependencies from the loops of an ordinary rule, where only a few field elements are kept. A round calls for a block \(A_{e,i}\) in the middle of the trial of a guess, and the \(kc\) bits of the guess stay on the stack.

**6.3.** In every epoch a path has one step of the weight \(bc+1\) to a block and a bounded number of steps of the weight \(1\). So the weight is about \(Ebc\), with \(E\) about \(T/b^2\): the space is \(\widetilde O(b+T/b)\), smallest for \(b=\sqrt T\), where it is \(\widetilde O(\sqrt T)\).

**6.4.** In every epoch a path has up to \(b\) steps of the weight \(1\) along the rounds and one step of the weight \(c+1\). So the weight is about \(E(b+c)\), again \(\widetilde O(T/b)\), and the space is \(\widetilde O(b+T/b)\), with the best value \(\widetilde O(\sqrt T)\) at \(b=\sqrt T\).

**6.5.** By Lemma 5.1 of the first lesson, \(z_{Eb}\) is, for every offset, the controller of the capped computation after \(Eb\) visits for this offset. If it is terminal, the capped computation has ended by then, and its state and halt flag are those at the end of the capped computation, which does not depend on the offset. The elapsed time and the displacements in it are those at the end as well.

## References

- [OpenAI-S] OpenAI, *Simulating One-Tape Time in Two-Fifths-Power Space*, OpenAI Math Release preprint, 25 September 2026, Sections 3.2 to 3.4. https://github.com/openai/math/tree/main/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026
