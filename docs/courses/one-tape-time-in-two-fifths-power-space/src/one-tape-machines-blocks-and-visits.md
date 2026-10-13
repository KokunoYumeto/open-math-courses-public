# One-tape machines, blocks and visits

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

How much working storage is needed to find out what a machine does in \(T\) steps, if the simulation may take as long as it likes? For a machine with one tape, a classical argument needs about \(\sqrt T\) cells. [OpenAI-S] shows that \(T^{2/5}\) bits, up to powers of \(\log T\), suffice. This course gives the proof.

This first lesson states the theorem and proves the combinatorial part of the argument. The tape is cut into blocks of width \(b\). The computation is a sequence of *visits*, each inside one block. Between two visits only a short record, the *controller*, is handed over. If someone proposes the list of all controllers, the proposal can be checked block by block, each block on its own. This is the fact on which the whole proof rests.

- The machine, the cap, and the theorem (Section 1).
- Controllers (Section 2), blocks and visits, and an offset with few visits (Lemma 3.1).
- The maps \(\operatorname{sel}\) and \(\operatorname{Visit}\) on raw data (Lemma 4.1).
- The reference evolution and local replay (Lemma 5.2).

The lesson follows [OpenAI-S, Sections 1 and 3.1]. It needs the notion of a Turing machine ([core course *Mathematical Logic, Set Theory, and Computability*](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C80)) and nothing else.

## 1. The machine and the theorem

**The machine.** Fix a deterministic machine \(M\) with a finite set of states, some of them *halting*, and a finite alphabet. It has

- one *writable tape*, whose cells are indexed by the integers, with one head, which starts at the cell \(0\);
- a fixed number \(\rho\ge0\) of *read-only heads* on read-only tapes, each starting at a fixed origin.

In one step the machine reads the cell under the writable head and the cells under the read-only heads; depending on these symbols and on its state it writes a symbol to the writable cell, moves every head by \(-1\), \(0\) or \(1\), and changes its state. In a halting state nothing changes any more.

**The input.** The machine works on a *public input* \(x\), a finite string. For the writable tape and for every read-only head there is a *symbol function*: \(\sigma_h(x,q)\) is the symbol that the tape of the head \(h\) contains initially at the displacement \(q\) from the origin of \(h\). An *accessor* is a fixed algorithm \(\mathsf{Sym}\) that computes \(\sigma_h(x,q)\) from \(x\), \(h\), a number \(T\) and \(q\). The *access condition holds for \((x,T)\)* if for every \(h\) and every \(q\) with \(|q|\le T\) the accessor finds \(\sigma_h(x,q)\) with at most \(C_0\log^{C_1}(T+2)\) bits of working storage, for fixed constants \(C_0,C_1\).

In the usual case the input stands on a tape and the other cells are blank. Then \(\sigma_h(x,q)\) is found by counting along the input, and the access condition holds for all \(T\) at least the length of \(x\).

**Space.** An *algorithm* in this course is a deterministic procedure that could be programmed on a Turing machine with a read-only input tape. Its *space* is the number of bits of working storage that it uses: counters, buffers, and the stack of its recursion. The input is not counted. The running time is not bounded and plays no role. Storage that a finished subroutine has used can be used again. The lessons describe algorithms in words and count their storage; they do not write out machines.

We write \(\widetilde O(f(T))\) for \(O(f(T)\log^C(T+2))\) with a fixed constant \(C\), and \(\operatorname{polylog}T\) for a bound \(O(\log^C(T+2))\). The constants may depend on the machine \(M\) and on the accessor, not on \(x\) and \(T\).

**The outcome.** Let \(T\ge2\). The *capped computation* runs \(M\) on \(x\) for at most \(T\) steps. Its *outcome* is the state after these steps together with the information whether the machine has halted.

**Theorem 1.1** ([OpenAI-S]). Let \(M\) be a machine as above with a fixed accessor. There is an algorithm that, for every input \(x\) and every number \(T\ge2\), given in binary, for which the access condition holds, computes the outcome of the capped computation in space
\[
\widetilde O\bigl(T^{2/5}\bigr).
\]
If the access condition holds for \((x,T)\) for every \(T\ge2\) and \(M\) halts on \(x\) after \(t\) steps, the outcome can be computed without a given cap in space \(\widetilde O((t+2)^{2/5})\).

The theorem is proved in the fourth lesson, [Histories, checkpoints and the theorem](histories-checkpoints-and-the-theorem.md). It is a statement about machines with one writable head. For machines with several writable tapes the method gives the exponent \(\tfrac12\) and no more.

From here on \(M\), \(x\) and \(T\ge2\) are fixed, and the access condition holds for \((x,T)\).

## 2. Controllers

**Definition.** A *controller* consists of

- a state of \(M\);
- two flags, *halt* and *timeout*; the controller is *terminal* if one of them is set;
- an elapsed time \(\tau\) with \(0\le\tau\le T\);
- a displacement for every head, the writable one and the \(\rho\) read-only ones, each an integer \(q\) with \(|q|\le\tau\).

The controller *of the computation at the time \(\tau\)* has the state and the head positions at that time (the positions as displacements from the origins); its halt flag is set if the state is halting, and its timeout flag if \(\tau=T\) and the state is not halting. A head moves by at most one cell per step, so \(|q|\le\tau\) holds.

A controller is written with a fixed number of bits,
\[
c=c_0+(\rho+2)\,\lceil\log_2(2T+3)\rceil ,
\]
where \(c_0\) depends only on \(M\): the time and the displacements are numbers between \(-T-1\) and \(T+1\). So \(c=O(\log(T+2))\). A string of \(c\) bits is a *raw controller*. It is *accepted* if it is the code of a controller, and *rejected* otherwise. All maps below are defined on all raw controllers, because the later lessons apply them to arbitrary strings.

A controller does not contain the tape. It is all that the computation needs to remember when the writable head passes from one part of the tape to another, apart from the tape contents themselves.

## 3. Blocks and visits

Let \(b\ge1\) be an integer, the *width*, and \(a\in\{0,\dots,b-1\}\) an *offset*. For an integer \(v\), the *block* with the index \(v\) is the set of the \(b\) cells from \(a+vb\) to \(a+(v+1)b-1\).
The blocks cut the writable tape into pieces. Let \(I_T\) be the set of the cells \(q\) with \(|q|\le T\); the writable head stays in \(I_T\) during the capped computation. The blocks that meet \(I_T\) have the indices from \(v_-=\lfloor(-T-a)/b\rfloor\) to \(v_+=\lfloor(T-a)/b\rfloor\). Call them \(C_1,\dots,C_N\) from left to right, so that
\[
N=v_+-v_-+1\le2+\frac{2T}b .
\]
The first and the last block may contain cells outside \(I_T\).

A *visit* is a part of the computation: it starts at some time with the writable head in a block \(C_i\), and it lasts until the head leaves \(C_i\), or the machine halts, or the time \(T\) is reached. The step in which the head leaves belongs to the visit: it writes to a cell of \(C_i\) and then moves. So a visit reads and writes only cells of one block. The capped computation is a sequence of visits; once it has halted or reached the time \(T\), we let it continue with *stationary* visits that change nothing.

**Lemma 3.1.** For some offset \(a\), the capped computation has at most \(T/b\) steps in which the writable head moves from one block to another. For this offset, the controller after
\[
R=\lceil1+T/b\rceil
\]
visits is terminal.

**Proof.** A step that moves the head from the cell \(q\) to \(q+1\) passes from one block to another exactly if \(q+1-a\) is divisible by \(b\). This holds for exactly one of the \(b\) offsets. The same is true for a step from \(q+1\) to \(q\), and a step without a move passes no boundary. So the numbers of the passing steps, added over the \(b\) offsets, give at most \(T\), and one of them is at most \(T/b\). Every visit that does not end the computation ends with a passing step. So with at most \(T/b\) passing steps, the visit number \(\lfloor T/b\rfloor+1\le R\) at the latest ends with a halt or at the time \(T\). \(\blacksquare\)

The algorithm of the theorem does not know which offset is good. It tries all \(b\) offsets, one after the other, in the same storage. An offset for which the controller after \(R\) visits is not terminal is given up. Every offset follows the same capped computation, so every offset that finishes gives the same outcome.

## 4. Visits as maps on raw data

Fix \(b\) and \(a\). Let \(\ell\ge1\) be a number of bits that suffices to write one symbol of the writable tape, with a fixed code for every symbol, and let \(s_{\mathrm{fill}}\) be a fixed symbol, the *filler*. A *raw block* is a string of \(b\ell\) bits, read as \(b\) entries of \(\ell\) bits.

For a tape content \(\Gamma\) and a label \(i\), the *represented block* \(\operatorname{rep}_i(\Gamma)\) is the raw block whose entry for the cell \(q\in C_i\) is the code of \(\Gamma(q)\) if \(q\in I_T\), and the code of the filler if \(q\notin I_T\).

**Definition** (\(\operatorname{sel}\) and \(\operatorname{Visit}\)). For a raw controller \(z\):

- \(\operatorname{sel}(z)\in\{1,\dots,N\}\) is the label of the block that contains the writable displacement of \(z\), if \(z\) is accepted; it is the label of the block that contains the cell \(0\), if \(z\) is rejected.

For a raw controller \(z\) and a raw block \(B\), the pair \(\operatorname{Visit}(z,B)=(z',B')\) of a raw controller and a raw block is defined as follows.

- If \(z\) is rejected: \(B'=B\), and \(z'\) is the code of a fixed terminal controller \(z_{\mathrm{dummy}}\) with the elapsed time \(0\) and all displacements \(0\).
- If \(z\) is accepted and terminal: \(z'=z\) and \(B'=B\).
- Otherwise: read \(B\) as the content of the block \(C_i\), \(i=\operatorname{sel}(z)\), and run \(M\) from the controller \(z\). An entry of the buffer is decoded when the writable head reads its cell, with a fixed symbol for every string that is not a code; a written symbol is stored as its code. The symbols under the read-only heads are found with the accessor. The run stops when the writable head has left \(C_i\), or the state is halting, or the elapsed time is \(T\); no step is made at the elapsed time \(T\). Then \(z'\) is the code of the controller reached, with the halt flag for a halting state and otherwise the timeout flag at the time \(T\), and \(B'\) is the buffer.

**Lemma 4.1.** (1) \(\operatorname{sel}\) and \(\operatorname{Visit}\) are defined for all raw arguments, and \(\operatorname{Visit}(z,B)\) is computed from \(z\) and \(B\) in space \(O((b+1)\operatorname{polylog}T)\).

(2) (Confinement.) In the run for an accepted \(z\), every cell of the writable tape that is read or written lies in \(C_i\cap I_T\), and the accessor is asked only for displacements \(q\) with \(|q|\le T\). The entries of \(B\) for the cells outside \(I_T\) are not changed.

(3) (Agreement.) Let \(z\) be the controller of the capped computation at the start of a visit, \(\Gamma\) the content of the writable tape at that time, and \(i=\operatorname{sel}(z)\). Then
\[
\operatorname{Visit}\bigl(z,\operatorname{rep}_i(\Gamma)\bigr)=\bigl(z',\operatorname{rep}_i(\Gamma')\bigr),
\]
where \(z'\) and \(\Gamma'\) are the controller and the tape content at the end of the visit. The blocks other than \(C_i\) are the same in \(\Gamma\) and \(\Gamma'\).

**Proof.** (1) Whether a string is the code of a controller is decided by reading its fields. The run keeps the buffer of \(b\ell\) bits, the current controller, and the storage of the accessor. It makes at most \(T\) steps, so it ends.

(2) An accepted \(z\) has the elapsed time \(\tau\le T\) and displacements with \(|q|\le\tau\). After \(s\) further steps, where \(s\le T-\tau\) because no step is made at the time \(T\), every head has a displacement of absolute value at most
\[
|q|+s\le\tau+s\le T .
\]
A cell is read or written only while the writable head is in \(C_i\). So these cells lie in \(C_i\cap I_T\), and the questions to the accessor are within the range of the access condition.

(3) By (2), the run reads the same symbols as the capped computation: the entries of \(\operatorname{rep}_i(\Gamma)\) for the cells of \(C_i\cap I_T\) are the codes of the symbols of \(\Gamma\), and the accessor gives the true symbols of the read-only tapes. By induction on the steps, the run makes the same steps as the capped computation until the visit ends, and the buffer is the represented block of the current tape content. A visit does not write outside \(C_i\). \(\blacksquare\)

The lemma holds for accepted controllers that never occur in the computation as well: (1) and (2) need only that \(z\) is accepted. This matters, because the later lessons apply \(\operatorname{Visit}\) to proposals that turn out to be wrong.

## 5. The reference evolution and local replay

**Definition.** Let \(z_0\) be a raw controller and \(B_1,\dots,B_N\) raw blocks. The *reference evolution* from these data is the sequence of steps of the following kind: with the current raw controller \(z\) and the current blocks, let \(i=\operatorname{sel}(z)\), replace \((z,B_i)\) by \(\operatorname{Visit}(z,B_i)\), and leave the other blocks unchanged. After \(m\) steps this gives raw controllers \(z_0,z_1,\dots,z_m\), the *reference list*, and raw blocks \(B_1^{(m)},\dots,B_N^{(m)}\).

The reference evolution is a notion of the proof. The algorithm of the theorem never holds all \(N\) blocks in its storage.

**Lemma 5.1.** Let \(z_0\) be the controller of the computation at the time \(0\) and \(B_i=\operatorname{rep}_i(\Gamma_0)\) for the initial tape content \(\Gamma_0\). Then for every \(m\) the raw controller \(z_m\) of the reference evolution is the controller of the capped computation after \(m\) visits, and \(B_i^{(m)}=\operatorname{rep}_i(\Gamma)\) for the tape content \(\Gamma\) at that time. In particular, for an offset as in Lemma 3.1, \(z_R\) is terminal and contains the outcome of the capped computation.

**Proof.** By induction on \(m\) with Lemma 4.1(3). After the computation has halted or reached the time \(T\), the controller is terminal and \(\operatorname{Visit}\) changes nothing, as the stationary visits. \(\blacksquare\)

**Definition** (replay). Let \(Z=(z_0,\dots,z_m)\) be a list of raw controllers, \(i\) a label and \(B\) a raw block. The *replay* \(\operatorname{Replay}_i(Z,B)\) is computed as follows. Start with a buffer equal to \(B\) and a flag equal to \(1\). For \(t=1,\dots,m\) in turn: if \(\operatorname{sel}(z_{t-1})=i\), compute \(\operatorname{Visit}(z_{t-1},\text{buffer})=(z',B')\), put the buffer equal to \(B'\), and put the flag equal to \(0\) if \(z'\ne z_t\) as strings of bits. If \(\operatorname{sel}(z_{t-1})\ne i\), do nothing. The scan continues after a failed comparison. The result is the pair of the final buffer and the final flag.

So the replay for the block \(i\) looks only at the visits that the list assigns to this block, and it believes the list about all the rest.

**Lemma 5.2** (local replay). Let \(z_0\) be a raw controller, \(B_1,\dots,B_N\) raw blocks, and \(Z=(z_0,z_1,\dots,z_m)\) a list of raw controllers that begins with \(z_0\).

1. The flags of \(\operatorname{Replay}_i(Z,B_i)\) are \(1\) for all \(i=1,\dots,N\) if and only if \(Z\) is the reference list from \(z_0,B_1,\dots,B_N\).
2. If they are all \(1\), the buffer of \(\operatorname{Replay}_i(Z,B_i)\) is the block \(B_i^{(m)}\) of the reference evolution, for every \(i\).
3. \(\operatorname{Replay}_i(Z,B)\) is defined for all raw arguments and is computed from \(Z\) and \(B\) in space \(O((b+(m+1)c+1)\operatorname{polylog}T)\).

**Proof.** (3) The scan makes \(m\) rounds, each with at most one call of \(\operatorname{Visit}\), and keeps one buffer, the list and counters.

(1), (2) Suppose that \(Z\) is the reference list. In the reference evolution the block \(i\) changes exactly at the steps \(t\) with \(\operatorname{sel}(z_{t-1})=i\), by \(\operatorname{Visit}\) applied to \(z_{t-1}\) and the current block. The replay for \(i\) does the same with its buffer. So the buffer is at every time the block of the reference evolution, all comparisons succeed, and the final buffer is \(B_i^{(m)}\).

Conversely, suppose that all flags are \(1\), and let \(z_0,\hat z_1,\dots,\hat z_m\) be the reference list. We show by induction on \(t\) that \(z_s=\hat z_s\) for \(s\le t\), and that for every \(i\) the buffer of the replay for \(i\) after its first \(t\) rounds is the block \(i\) of the reference evolution after \(t\) steps. For \(t=0\) this holds. Let it hold for \(t-1\), and let \(i=\operatorname{sel}(z_{t-1})=\operatorname{sel}(\hat z_{t-1})\). In the round \(t\), only the replay for \(i\) acts. Its buffer is the reference block, so \(\operatorname{Visit}\) gives \(\hat z_t\) and the new reference block. Its flag is \(1\), so the comparison succeeded: \(z_t=\hat z_t\). The buffers of the other replays and the other reference blocks do not change in this round. \(\blacksquare\)

The lemma is used in this way. The true list of the controllers of an epoch of the computation is not known. But a proposed list can be tested by \(N\) replays, and each replay needs one block and the list. Exactly one proposal passes all \(N\) tests. In the algebraic form of the third lesson, "all tests pass" is a product of \(N\) factors, one for each block.

## 6. Exercises

**6.1.** Let \(T=10\), \(b=4\), \(a=1\). Find \(v_-\), \(v_+\), \(N\) and the blocks \(C_1\) and \(C_N\). Which of their cells lie outside \(I_T\)?

**6.2.** A machine moves its writable head one cell to the right in every step. How many steps pass from one block to another during \(T\) steps, for the offset \(a\)? Compare with Lemma 3.1.

**6.3.** Show that the bound \(|q|\le\tau\) in the definition of a controller cannot be left out in Lemma 4.1(2): describe a string that would be the code of a "controller" without this bound and for which a run would ask the accessor for a displacement larger than \(T\).

**6.4.** Let \(Z=(z_0,\dots,z_m)\) pass all replays, as in Lemma 5.2. Let \(Z'\) be \(Z\) with the last controller \(z_m\) changed. Which replays fail for \(Z'\)?

**6.5.** Suppose the machine had two writable tapes, cut into blocks in the same way, and a visit ended when one of the two heads leaves its block. A visit would then read two blocks, one of each tape. Explain why the proof of Lemma 5.2 does not go through if every replay is to use one block only.

## 7. Solutions

**6.1.** \(v_-=\lfloor-11/4\rfloor=-3\) and \(v_+=\lfloor9/4\rfloor=2\), so \(N=6\le2+20/4\). \(C_1\) is the block with the index \(-3\): the cells \(-11,-10,-9,-8\), of which \(-11\) lies outside \(I_T\). \(C_6\) has the index \(2\): the cells \(9,10,11,12\), of which \(11\) and \(12\) lie outside \(I_T\).

**6.2.** The step from \(q\) to \(q+1\), for \(q=0,\dots,T-1\), passes a boundary if \(q+1-a\) is divisible by \(b\). Among the numbers \(1,\dots,T\) there are \(\lfloor(T-a)/b\rfloor\) or one more with this property, depending on \(a\). The sum over the offsets is exactly \(T\), and the smallest of them is \(\lfloor T/b\rfloor\). So Lemma 3.1 cannot be improved for this machine.

**6.3.** Take the elapsed time \(\tau=0\) and a read-only displacement \(q=T\). If the machine moves this head to the right in its first step, the next question to the accessor is for the displacement \(T+1\), outside the range of the access condition; after more steps the displacement can grow up to \(2T\).

**6.4.** Only the replay for the block \(i=\operatorname{sel}(z_{m-1})\) compares anything with the last controller, in its round \(m\). Its earlier comparisons are unchanged and succeed, and its last one fails. All other replays succeed. So exactly one flag is \(0\).

**6.5.** The induction in the proof uses that the visit at the round \(t\) is computed from the controller \(z_{t-1}\) and ONE buffer, which the replay for that block has kept up to date. With two tapes the visit needs the current contents of a block of the first tape and of a block of the second tape. A replay that holds only one of them cannot compute the visit, and so cannot compare its result with \(z_t\). The outgoing controller depends on both blocks together, in a way that is not a combination of a condition on the first and a condition on the second. The last lesson of the course comes back to this.

## References

- [OpenAI-S] OpenAI, *Simulating One-Tape Time in Two-Fifths-Power Space*, OpenAI Math Release preprint, 25 September 2026, Sections 1 and 3.1. https://github.com/openai/math/tree/main/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026
