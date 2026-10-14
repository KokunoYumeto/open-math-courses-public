# Programmable slots

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The synthesis circuit of this course is built in two stages. First its one-qubit gates may be read from arbitrary tables, indexed by the values of other qubits: such a gate is a *programmable slot*. The geometry of the circuit, its registers and the positions of its slots, depends only on the sizes, while everything that depends on the target unitary sits in the tables. The last lesson stores finite approximations of these tables in one Boolean oracle. This lesson defines slots and builds three tools from few of them: state preparation (Lemma 2.1), permutations of the computational basis (Lemma 2.2) and Fourier transforms (Lemma 2.3).

- Controlled tasks and slots (Section 1).
- State preparation, permutations and Fourier transforms (Section 2).

The lesson follows [OpenAI-US, Section 2]. It uses the clean-workspace errors of [Oracle circuits and the synthesis theorem](oracle-circuits-and-the-synthesis-theorem.md), Definition 4.1.

## 1. Controlled tasks and slots

The recursion of the course synthesizes many unitaries at once, coherently. Let a *label register* of \(t\) qubits have the basis \(|\lambda\rangle\), \(\lambda\in\{0,1\}^t\), let \(1\le d\le2^n\), and let \(U_\lambda\) be unitaries on \(\mathcal H_d\subseteq(\mathbb C^2)^{\otimes n}\). The *controlled task* of this family is the unitary
\[
\mathcal U=\sum_\lambda|\lambda\rangle\langle\lambda|\otimes U_\lambda
\]
on \(\mathcal V=\operatorname{span}\{|\lambda\rangle\}\otimes\mathcal H_d\). A circuit *solves* it with error \(\delta\) if it implements \(\mathcal U\) on \(\mathcal V\) with clean-workspace error \(\delta\). Nothing is prescribed outside \(\mathcal V\). Since all maps involved are block diagonal in the labels, and the norm of a block diagonal operator is the largest norm of its blocks, the estimate holds for every superposition of labels as soon as it holds for each label.

**Definition 1.1.** A *programmable slot* on a register consists of a *target* qubit and an ordered list of \(c\) other qubits, its *controls*. Given a *table* of matrices \(W_y\in U(2)\), \(y\in\{0,1\}^c\), it acts on the controls and the target as
\[
\sum_{y\in\{0,1\}^c}|y\rangle\langle y|\otimes W_y ,
\]
and as the identity on the other qubits. A *skeleton* consists of registers and a finite sequence of slots with their targets and control lists, without tables. *Reversing* a skeleton reverses the order of its slots and replaces every table by the table of adjoints; for every choice of tables it gives the inverse unitary.

Fixed gates are slots with fixed tables: \(H\) is a slot without controls, and \(\mathrm{CNOT}\) is a slot with one control and the table \((I,X_p)\), where \(X_p\) exchanges \(|0\rangle\) and \(|1\rangle\). Tables may depend on the target family, and so on the labels: a label qubit can be a control.

*Diagonal unitaries.* A diagonal unitary on \(u\ge1\) qubits is one slot: choose one of the qubits as target, the others as controls, and put the two diagonal entries belonging to each value of the controls into a diagonal table entry. Label qubits may be added to the controls, so a family of diagonal unitaries indexed by labels is one slot. In particular, the reflection \(I-2P\) in the span of chosen computational basis vectors, with \(P\) the orthogonal projection onto it, is one slot, and a phase \(e^{i\varphi_\lambda}\) depending only on the label is one slot: a diagonal table on a target qubit that is in the zero state, or a scalar table on any target.

## 2. State preparation, permutations and Fourier transforms

**Lemma 2.1** (state preparation; [OpenAI-US, Lemma 2.1]). For \(u\ge1\) there is a skeleton of \(u+1\) slots on a label register and \(u\) further qubits, depending only on the sizes, such that for every family of unit vectors \(a_\lambda\in\mathbb C^{2^u}\) some choice of tables maps \(|\lambda\rangle|0^u\rangle\) to \(|\lambda\rangle|a_\lambda\rangle\) for every \(\lambda\).

*Proof.* Fix a label and write \(a=\sum_xa_x|x\rangle\). For a binary prefix \(p\) of length at most \(u\), let \(P(p)\) be the sum of \(|a_x|^2\) over the \(x\) beginning with \(p\); so \(P(\text{empty})=1\) and \(P(p)=P(p0)+P(p1)\). For \(j=1,\dots,u\), the \(j\)-th slot has the \(j\)-th qubit as target and the labels and the first \(j-1\) qubits as controls. For the control value \(p\) with \(P(p)>0\), its table entry is the real rotation
\[
\frac1{\sqrt{P(p)}}\begin{pmatrix}\sqrt{P(p0)}&-\sqrt{P(p1)}\\ \sqrt{P(p1)}&\sqrt{P(p0)}\end{pmatrix},
\]
and any unitary when \(P(p)=0\). By induction on \(j\), after \(j\) slots the state is
\[
\sum_{|p|=j}\sqrt{P(p)}\,|p\rangle|0^{u-j}\rangle ,
\]
because the \(j\)-th slot sends \(|p\rangle|0\rangle\) to \(|p\rangle\bigl(\sqrt{P(p0)}|0\rangle+\sqrt{P(p1)}|1\rangle\bigr)/\sqrt{P(p)}\), and terms with \(P(p)=0\) are absent. After \(u\) slots the amplitude at \(x\) is \(|a_x|\). The last slot is diagonal and multiplies \(|x\rangle\) by \(a_x/|a_x|\), with an arbitrary phase where \(a_x=0\). All tables are chosen for each label separately, at the same positions. \(\blacksquare\)

**Lemma 2.2** (basis permutations; [OpenAI-US, Lemma 2.2]). For \(u\ge1\) there is a skeleton of \(5u\) slots on a label register, \(u\) qubits and \(u\) temporary qubits, depending only on the sizes, such that for every family of permutations \(\pi_\lambda\) of \(\{0,1\}^u\) some choice of tables maps \(|\lambda\rangle|x\rangle|0^u\rangle\) to \(|\lambda\rangle|\pi_\lambda(x)\rangle|0^u\rangle\).

*Proof.* With \(u\) slots, the \(j\)-th having the \(j\)-th temporary qubit as target and the labels and the first register as controls, write \(\pi_\lambda(x)\) bitwise into the temporary register: the table entry is \(X_p\) when the \(j\)-th bit of \(\pi_\lambda(x)\) is \(1\), and \(I\) otherwise. This gives \(|\lambda\rangle|x\rangle|\pi_\lambda(x)\rangle\). With \(u\) more slots, controlled by the labels and the temporary register, add \(\pi_\lambda^{-1}(y)\) bitwise modulo \(2\) to the first register, where \(y\) is the content of the temporary register. As \(\pi_\lambda^{-1}(\pi_\lambda(x))=x\), this gives \(|\lambda\rangle|0^u\rangle|\pi_\lambda(x)\rangle\). Exchange the two registers, using three \(\mathrm{CNOT}\)s for each pair of corresponding qubits. \(\blacksquare\)

The *Fourier transform* on \(b\ge1\) qubits is the unitary
\[
F_b|x\rangle=2^{-b/2}\sum_{z=0}^{2^b-1}e^{2\pi ixz/2^b}|z\rangle .
\]

**Lemma 2.3** (Fourier transforms; [OpenAI-US, Lemma 2.3]). \(F_b\) is a fixed skeleton, with fixed tables, of \(2b+3\lfloor b/2\rfloor\) slots.

*Proof.* Write \(z=\sum_{j=0}^{b-1}z_j2^j\). Then \(e^{2\pi ixz/2^b}=\prod_j\bigl(e^{2\pi ix/2^{b-j}}\bigr)^{z_j}\), so
\[
F_b|x\rangle=\bigotimes_{j=b-1}^{0}\frac{|0\rangle+e^{2\pi ix/2^{b-j}}|1\rangle}{\sqrt2},
\]
the factor of \(z_j\) standing at the position of the bit of place value \(2^j\), the most significant first. The phase \(e^{2\pi ix/2^{b-j}}\) depends only on the residue of \(x\) modulo \(2^{b-j}\), that is, on the bits of \(x\) of place value below \(2^{b-j}\).

Write \(x=\sum_ix_i2^i\), the qubit of \(x_{b-1}\) first. For \(j=0,1,\dots,b-1\), treat the qubit of \(x_{b-1-j}\): apply \(H\), giving \(\bigl(|0\rangle+(-1)^{x_{b-1-j}}|1\rangle\bigr)/\sqrt2\), and then a diagonal slot with this qubit as target and the qubits of the lower bits \(x_{b-2-j},\dots,x_0\) as controls, which multiplies \(|1\rangle\) by \(e^{2\pi iL_j/2^{b-j}}\), where
\[
L_j=\sum_{i<b-1-j}x_i2^i .
\]
Since \(x_{b-1-j}2^{b-1-j}/2^{b-j}=x_{b-1-j}/2\), the qubit now holds the factor of \(z_j\); the lower bits are still untouched when they are used as controls, and the higher bits contribute integer multiples of \(2\pi\). After all \(b\) steps the factors stand in the reverse order, the factor of \(z_j\) at the position of \(x_{b-1-j}\). Reverse the order of the qubits with \(\lfloor b/2\rfloor\) exchanges of three \(\mathrm{CNOT}\)s each. The circuit maps every basis vector \(|x\rangle\) to \(F_b|x\rangle\), so by linearity it equals \(F_b\). \(\blacksquare\)

A product of Fourier transforms on several registers takes a number of slots linear in their total width.

These constructions keep the scalar phase of each label branch. For one isolated unitary a scalar phase is invisible, but for a family controlled by a label register the phases of different labels are relative phases, and the controlled task prescribes them.

## 3. Exercises

**3.1.** Show that reversing a skeleton, with adjoint tables, gives the inverse unitary for every choice of tables.

**3.2.** Give the tables of Lemma 2.1 for \(u=1\) and \(a=(|0\rangle+i|1\rangle)/\sqrt2\).

**3.3.** Check Lemma 2.3 for \(b=1\) and \(b=2\): show that \(F_1=H\), and write \(F_2\) as a matrix.

**3.4.** Show that the norm of a block diagonal operator \(\sum_\lambda|\lambda\rangle\langle\lambda|\otimes A_\lambda\) is the largest of the norms \(\|A_\lambda\|\).

**3.5.** Count the slots of Lemma 2.2 that depend on the permutations, and those that do not.

## 4. Solutions

**3.1.** A slot with table \(W_y\) is block diagonal in the controls, with inverse the slot with table \(W_y^*\). The inverse of a product is the product of the inverses in the reverse order.

**3.2.** \(P(0)=P(1)=1/2\), so the first slot is the rotation with first column \((1/\sqrt2,1/\sqrt2)\). The diagonal slot multiplies \(|0\rangle\) by \(1\) and \(|1\rangle\) by \(i\).

**3.3.** For \(b=1\), \(F_1|x\rangle=(|0\rangle+(-1)^x|1\rangle)/\sqrt2\), which is \(H\). For \(b=2\), \(F_2\) has the entries \(i^{xz}/2\) for \(x,z\in\{0,1,2,3\}\):
\[
F_2=\frac12\begin{pmatrix}1&1&1&1\\1&i&-1&-i\\1&-1&1&-1\\1&-i&-1&i\end{pmatrix}.
\]

**3.4.** For \(v=\sum_\lambda|\lambda\rangle\otimes v_\lambda\), the image has squared norm \(\sum_\lambda\|A_\lambda v_\lambda\|^2\le\max_\lambda\|A_\lambda\|^2\|v\|^2\), with equality approached by vectors with one label.

**3.5.** The \(2u\) slots writing \(\pi_\lambda(x)\) and erasing \(x\) depend on the permutations; the \(3u\) \(\mathrm{CNOT}\)s do not.

## References

- [OpenAI-US] OpenAI, *Polynomial-Time Unitary Synthesis from a Boolean Oracle*, OpenAI Math Release preprint, 5 October 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026
