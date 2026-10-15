# Exact circuits and dyadic probabilities

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Shor's quantum algorithm factors an integer \(N\) in time polynomial in its bit length, with a probability of success bounded away from zero [Shor 1997]. A proposed factorization can be checked, so repetition makes failure unlikely; but a procedure that repeats until it succeeds has no polynomial bound on its worst-case running time, and the probabilities in the algorithm involve rotations by angles that a fixed finite set of gates can only approximate. This course presents OpenAI's construction of a polynomial-time uniform family of quantum circuits over one fixed finite gate set that outputs the complete prime factorization of every \(N\ge2\) with probability one [OpenAI-EQF]. Earlier exact quantum algorithms used gates whose parameters are computed during the computation, as in the exact Fourier transforms and discrete-logarithm algorithms of Mosca and Zalka [Mosca–Zalka 2004], or an exact order-finding algorithm that receives a multiple of the unknown order [Imran 2022]; Brassard and Høyer gave an exact algorithm for Simon's problem [Brassard–Høyer 1997].

This lesson fixes the model of computation and proves its general tools.

- Qubits, the gate set and uniform circuit families (Section 1).
- Reversible classical computation (Section 2).
- Exact dyadic sampling and retained records (Section 3).
- Exact amplification from probability one quarter (Section 4).
- The theorem, and the plan of the course (Section 5).

We use the linear algebra of finite-dimensional complex inner product spaces: unitary maps, orthogonal projections and tensor products.

## 1. Qubits, gates and uniform circuits

A *register* of \(k\) qubits is the space \((\mathbb C^2)^{\otimes k}=\mathbb C^{2^k}\) with its *computational basis* \(|x\rangle\), \(x\in\{0,1\}^k\). A gate applied to some qubits of a register acts as its tensor product with the identity on the other qubits.

The gate set \(\mathcal G\) of this course consists of

- NOT, \(|b\rangle\mapsto|1-b\rangle\); CNOT, \(|a,b\rangle\mapsto|a,a\oplus b\rangle\); and Toffoli, \(|a,b,c\rangle\mapsto|a,b,c\oplus ab\rangle\);
- the Hadamard gate \(H\) and the phase gate \(S\),
\[
\begin{gathered}H=\frac1{\sqrt2}\begin{pmatrix}1&1\\ 1&-1\end{pmatrix},\\ S=\begin{pmatrix}1&0\\ 0&i\end{pmatrix};\end{gathered}
\]
- the inverses of these gates, and their singly controlled versions: for a gate \(G\) on \(j\) qubits, the controlled gate on \(j+1\) qubits acts as \(G\) on the last \(j\) qubits when the first qubit is \(1\), and as the identity when it is \(0\).

All gates except \(S\) are their own inverses, so \(\mathcal G\) is a fixed finite set of gates on at most four qubits, closed under inverses.

A *circuit* on \(k\) qubits is a finite sequence of gates of \(\mathcal G\), each applied to chosen qubits; its unitary is the product of the gates in order. Its *size* is the number of qubits plus the number of gates. A circuit receives an input \(x\) as the basis state \(|x\rangle\) on designated input qubits, all other qubits being \(|0\rangle\), and at the end designated output qubits are measured in the computational basis: the outcome \(y\) has probability \(\|\Pi_yU|x,0\rangle\|^2\), where \(U\) is the unitary and \(\Pi_y\) the projection onto the basis states whose output bits are \(y\). A family of circuits \((C_\ell)_{\ell\ge1}\), one for each input bit length \(\ell\), is *polynomial-time uniform* if a deterministic classical algorithm outputs \(C_\ell\) on input \(\ell\) in time polynomial in \(\ell\).

## 2. Reversible classical computation

**Lemma 2.1** (reversible evaluation). Let \(f\colon\{0,1\}^m\to\{0,1\}^k\) be computed by a Boolean circuit with \(s\) gates, each of which computes the conjunction of two earlier values or the negation of one earlier value, the earlier values being input bits or outputs of earlier gates. Then a circuit of at most \(4s+k\) gates from NOT, CNOT and Toffoli on \(m+s+k\) qubits maps
\[
\begin{gathered}|x,0^s,z\rangle\longmapsto|x,0^s,z\oplus f(x)\rangle\\ \bigl(x\in\{0,1\}^m,\ z\in\{0,1\}^k\bigr).\end{gathered}
\]

*Proof.* Give each gate of the Boolean circuit its own scratch qubit, initially \(0\). In the order of the Boolean circuit, compute each gate into its scratch qubit: a conjunction of the values held by qubits \(a,b\) by a Toffoli gate with controls \(a,b\); a negation of the value held by qubit \(a\) by a CNOT from \(a\) followed by a NOT. Then CNOT each output value onto the corresponding qubit of \(z\). Finally apply the gates of the first stage in reverse order. Each of them is its own inverse and none of them acts on \(z\), so they return the scratch qubits to \(0\) and leave \(z\oplus f(x)\) in place. The three stages have at most \(2s\), \(k\) and \(2s\) gates. \(\square\)

Classical algorithms are Turing machines. A *Turing machine* has finite sets of states and of tape symbols, the symbols including \(0\), \(1\) and a blank; a tape with cells \(0,1,2,\ldots\); and a transition function that assigns to a state and a symbol read a new state, a symbol to write and a head move in \(\{-1,0,1\}\), where a move to the left from cell \(0\) leaves the head on cell \(0\). Some states are halting states, in which the transition function changes nothing. On input \(x\in\{0,1\}^m\) the machine starts in its initial state, with \(x\) in cells \(0,\ldots,m-1\), blanks in the other cells and the head on cell \(0\). It *computes* \(f\colon\{0,1\}^m\to\{0,1\}^k\) *within \(T\) steps* if on every input \(x\) it is in a halting state after \(T\) steps, with \(f(x)\) in cells \(0,\ldots,k-1\). A *polynomial-time algorithm* does this on every input length \(m\) within a number of steps bounded by a polynomial in \(m\).

**Lemma 2.2** (unrolling a computation). Let a Turing machine compute \(f\colon\{0,1\}^m\to\{0,1\}^k\) within \(T\) steps, where \(m\ge1\) and \(T\ge k\). Then \(f\) is computed by a Boolean circuit as in Lemma 2.1 with at most \(c(T+1)^2\) gates, where \(c\) depends only on the machine, and this circuit is written down from \(m\) and \(T\) in time polynomial in \(m+T\).

*Proof.* In \(t\le T\) steps the head visits only the cells \(0,\ldots,T\). Describe the configuration after \(t\) steps by the values \(v_{t,i}\), \(0\le i\le T\), where \(v_{t,i}\) is the pair formed by the symbol in cell \(i\) and the current state if the head is on cell \(i\), or a mark \(\ast\) otherwise. The symbol in cell \(i\) changes only when the head is on cell \(i\), and the head arrives at cell \(i\) only from the cells \(i-1\), \(i\) and \(i+1\). Hence \(v_{t+1,i}=F(v_{t,i-1},v_{t,i},v_{t,i+1})\) for \(0<i<T\), with one function \(F\) given by the transition function, and \(v_{t+1,0}=F_0(v_{t,0},v_{t,1})\) and \(v_{t+1,T}=F_T(v_{t,T-1},v_{t,T})\) with two further such functions. Encode the finitely many possible values by bit strings of one fixed length. Every Boolean function of finitely many bits is computed by a circuit of conjunctions and negations, for instance as the disjunction of the conjunctions of literals that describe the points where it equals \(1\), with \(u\vee w=\neg(\neg u\wedge\neg w)\). So \(F\), \(F_0\) and \(F_T\) are computed by fixed circuits. The values \(v_{0,i}\) are given by the input bits and by constants, which are obtained as \(0=x_1\wedge\neg x_1\) and \(1=\neg0\). Composing \(T\) layers of \(T+1\) copies of these circuits, and reading the symbols of \(v_{T,0},\ldots,v_{T,k-1}\) with fixed circuits, gives a circuit for \(f\) with at most \(c(T+1)^2\) gates. Two nested loops over \(t\) and \(i\) write it down. \(\square\)

By Lemmas 2.1 and 2.2, every function computed by a polynomial-time algorithm has polynomial-size uniform circuits over NOT, CNOT and Toffoli that compute its value into fresh qubits and return all scratch qubits to zero. This applies to integer arithmetic, Euclid's algorithm, modular powering with exponents of polynomial bit length and comparisons, which run in polynomial time by the school methods. This is the reversible simulation method of Bennett; explicit arithmetic networks of this kind are given by Vedral, Barenco and Ekert [VBE 1996].

**Lemma 2.3.** Let \(t(x)\in\{0,1\}\) be computed from a basis label \(x\) in polynomial time.

1. The map \(|x\rangle\mapsto(-1)^{t(x)}|x\rangle\), together with zero scratch qubits that are returned to zero, is a polynomial-size circuit over \(\mathcal G\).
2. For a gate \(G\in\mathcal G\) and qubits \(c_1,\ldots,c_j\), the gate \(G\) controlled by the conjunction of \(c_1,\ldots,c_j\) is a circuit over \(\mathcal G\) of size linear in \(j\).
3. Let \(\pi\) be a permutation of \(\{0,1\}^k\) such that \(\pi\) and \(\pi^{-1}\) are computed in polynomial time. Then \(|y\rangle\mapsto|\pi(y)\rangle\), together with zero scratch qubits that are returned to zero, is a polynomial-size circuit over NOT, CNOT and Toffoli.

*Proof.* (1) Compute \(t(x)\) into a scratch qubit, apply \(S^2=\operatorname{diag}(1,-1)\) to that qubit, and uncompute \(t(x)\). (2) Compute the conjunction of the controls into a scratch qubit with \(j-1\) Toffoli gates and further scratch qubits, apply the singly controlled \(G\) with that qubit as control, and undo the Toffoli gates. (3) With a second register of \(k\) zero qubits, Lemma 2.1 gives \(|y,0\rangle\mapsto|y,\pi(y)\rangle\). Lemma 2.1 for \(\pi^{-1}\), with the roles of the two registers exchanged, then gives \(|y\oplus\pi^{-1}(\pi(y)),\pi(y)\rangle=|0,\pi(y)\rangle\). Finally three CNOT gates exchange each pair of corresponding qubits of the two registers. \(\square\)

## 3. Exact dyadic sampling and retained records

A *dyadic rational* is a number \(A/2^T\) with \(A\in\mathbb Z\) and an integer \(T\ge0\). It has *polynomial bit length* if \(T\) and the bit length of \(|A|\) are bounded by a polynomial in the input length.

**Lemma 3.1** (exact dyadic sampling; [OpenAI-EQF, Lemma 2.1]). Suppose that from a classical basis label \(\lambda\) one computes in polynomial time integers \(A(\lambda)\ge0\) and \(T(\lambda)\le T_0\), where \(T_0\) is a polynomial bound, with \(q(\lambda)=A(\lambda)/2^{T(\lambda)}\le1\). A polynomial-size circuit over \(\mathcal G\) appends to \(|\lambda\rangle\) a flag qubit that is \(1\) with probability exactly \(q(\lambda)\), and leaves \(\lambda\) unchanged.

*Proof.* Put \(A'=A(\lambda)\,2^{T_0-T(\lambda)}\), so that \(q(\lambda)=A'/2^{T_0}\). Hadamard gates on \(T_0\) fresh zero qubits give the uniform superposition of the labels \(u\in\{0,\ldots,2^{T_0}-1\}\), each with amplitude \(2^{-T_0/2}\). Compute the flag \([u<A']\) reversibly from \(\lambda\) and \(u\) into a fresh qubit, keeping \(u\). Exactly \(A'\) labels set the flag, so it is \(1\) with probability \(A'/2^{T_0}=q(\lambda)\). \(\square\)

When a procedure *retains* an event with probability \(q\), it appends such a flag and requires it for its final success. The other branches are not discarded and nothing is renormalized: every flag that is required contributes its actual probability to the probability of success.

The procedures of this course measure registers and use the outcomes to choose later operations. The next lemma turns such a procedure into a single circuit.

**Lemma 3.2** (retained records; [OpenAI-EQF, Lemma 2.2]). Consider a procedure with polynomially many steps on polynomially many qubits and classical bits, where each step is one of the following: a gate of \(\mathcal G\) applied to qubits, both the gate and the qubits being chosen by classical data held at that moment; a measurement of a qubit in the computational basis, whose outcome becomes a classical bit; a deterministic polynomial-time computation on classical data. Then there is a polynomial-size uniform circuit over \(\mathcal G\) such that a final measurement of its record qubits gives exactly the joint distribution of the classical data of the procedure. Its inverse is again a circuit over \(\mathcal G\).

*Proof.* Represent the classical data by *record* qubits. Replace a measurement of a qubit \(q\) by a CNOT from \(q\) onto a fresh record qubit. Replace a classical computation by its reversible circuit (Section 2), computed into fresh record qubits. Replace a gate chosen by the data by the following: for each of the polynomially many possible choices of a gate of \(\mathcal G\) and of the qubits it acts on, apply that gate to those qubits controlled by the test, computed from the record qubits into a scratch qubit and uncomputed afterwards, that the data select this choice (Lemma 2.3(2)).

For a record value \(o\), let \(\psi_o\) be the unnormalized state of the quantum registers of the procedure on the event that its data so far equal \(o\); thus \(\|\psi_o\|^2\) is the probability of that event, where \(o\) runs over the possible values of the data. We show by induction on the steps that the circuit is in the state \(\sum_o\psi_o\otimes|o\rangle\). A measurement of \(q\) splits \(\psi_o\) into the two components \(\Pi_b\psi_o\), \(b\in\{0,1\}\), and the CNOT copies \(b\) into the record: \(\sum_o\sum_b\Pi_b\psi_o\otimes|o,b\rangle\). A classical computation appends a function of \(o\) to the record. A gate chosen by the data acts on the branch with record \(o\) as the gate selected by \(o\). The records are orthogonal basis states, so a final measurement of the record qubits returns \(o\) with probability \(\|\psi_o\|^2\).

Each gate of \(\mathcal G\) has its inverse in \(\mathcal G\), so reversing the list of gates and inverting each gives the inverse circuit. \(\square\)

**Lemma 3.3** (fresh registers). In the circuit of Lemma 3.2, let a step apply to fresh zero qubits a unitary \(W_o\) that depends only on the record \(o\), and leave all older qubits alone. Then, on the event of record \(o\), the outcome probabilities of a measurement of the new qubits are those of \(W_o|0\rangle\), whatever the state of the older qubits.

*Proof.* The state \(\psi_o\otimes|o\rangle\otimes|0\rangle\) becomes \(\psi_o\otimes|o\rangle\otimes W_o|0\rangle\), and for a projection \(\Pi\) on the new qubits
\[
\begin{aligned}&\|(I\otimes\Pi)(\psi_o\otimes|o\rangle\otimes W_o|0\rangle)\|^2\\&\quad=\|\psi_o\|^2\,\|\Pi W_o|0\rangle\|^2 .\qquad\square\end{aligned}
\]

So conditional probabilities along recorded classical histories can be computed step by step, even though old quantum registers may remain entangled with each other.

## 4. Exact amplification from probability one quarter

**Lemma 4.1** (one step of amplification; [OpenAI-EQF, proof of Theorem 1.1]; [BHMT 2002, Section 2]). Let \(V\) be a unitary on a register, \(\psi=V|0\rangle\), and let \(\Pi\) be an orthogonal projection with \(\|\Pi\psi\|^2=\frac14\). Then
\[
\bigl(2|\psi\rangle\langle\psi|-I\bigr)(I-2\Pi)\psi=2\Pi\psi ,
\]
a unit vector in the range of \(\Pi\). Moreover \(2|\psi\rangle\langle\psi|-I=V(2|0\rangle\langle0|-I)V^{-1}\).

*Proof.* Put \(g=\Pi\psi\). Then \((I-2\Pi)\psi=\psi-2g\) and \(\langle\psi,\psi-2g\rangle=1-2\langle\psi,\Pi\psi\rangle\), where \(\langle\psi,\Pi\psi\rangle=\|g\|^2=\frac14\); so \(\langle\psi,\psi-2g\rangle=\frac12\). Hence
\[
\begin{aligned}&\bigl(2|\psi\rangle\langle\psi|-I\bigr)(\psi-2g)\\&\quad=2\cdot\tfrac12\,\psi-\psi+2g=2g,\end{aligned}
\]
and \(\|2g\|=1\). The last identity holds because \(V\) is unitary and \(V|0\rangle=\psi\). \(\square\)

If \(\Pi\) is the projection onto the states whose flag qubit is \(1\), then \(I-2\Pi\) is the sign of a bit test, and \(I-2|0\rangle\langle0|\) is the sign of the test "all qubits are zero"; both are circuits over \(\mathcal G\) by Lemma 2.3(1). The reflection \(2|0\rangle\langle0|-I=-(I-2|0\rangle\langle0|)\) differs from such a sign by the global factor \(-1\), which changes no measurement probability. The probability \(\frac14\) is special: one step of amplitude amplification turns it into certainty, without any rotation by a computed angle [BHMT 2002, Section 2].

## 5. The theorem, and the plan of the course

**Theorem 5.1** ([OpenAI-EQF, Theorem 1.1]). There is a polynomial-time uniform family of polynomial-size circuits over \(\mathcal G\) that outputs the complete prime factorization of every input integer \(N\ge2\) with probability one. The numbers of gates and of qubits are bounded by a fixed polynomial in the bit length of \(N\).

The output is the nondecreasing list of the primes whose product is \(N\), with multiplicities. The theorem is proved in [Certain output from deferred filters](certain-output-from-deferred-filters.md). The construction separates two tasks: making the probability of a useful event an exactly computable dyadic number, and recovering, from data that the run itself generates and verifies, the information needed to evaluate that number.

- [A transform with a piecewise-linear phase](a-transform-with-a-piecewise-linear-phase.md) replaces the Fourier transform of order finding by a transform built from the gates of \(\mathcal G\), whose output probabilities are exact dyadic numbers.
- [An order trial with prescribed probability](an-order-trial-with-prescribed-probability.md) corrects these probabilities with classical coins, so that the probability of returning the multiplicative order \(r\) of a unit is the explicit number \(\varphi(r)\,2^{-\lceil\log_2r\rceil-10}\), while every returned candidate is a multiple of \(r\).
- [A deterministic primality test](a-deterministic-primality-test.md) proves a classical polynomial-time primality test, a variant of the test of Agrawal, Kayal and Saxena, which the verification of the data below uses.
- [Factoring with verifiable auxiliary data](factoring-with-verifiable-auxiliary-data.md) builds a factoring process whose successful runs also produce the factorizations of \(p-1\) for the primes \(p\) involved, recursively; these data determine the exact probabilities of all the steps.
- [Certain output from deferred filters](certain-output-from-deferred-filters.md) equalizes the probabilities of the steps after the data are verified, arranges a total success probability of exactly \(\frac14\), and applies Lemma 4.1.

## 6. Exercises

**6.1.** Show that every outcome probability of a circuit over \(\mathcal G\) applied to a basis state is a dyadic rational. Deduce that no such circuit prepares, from a basis state, a state in which some outcome has probability \(\frac13\).

**6.2.** Give a circuit over NOT, CNOT and Toffoli that maps \(|x,y,0\rangle\) to \(|x,y,x\vee y\rangle\).

**6.3.** Let \(\|\Pi\psi\|^2=\sin^2\theta\) with \(0<\theta\le\pi/2\). Show that \(\|\Pi(2|\psi\rangle\langle\psi|-I)(I-2\Pi)\psi\|^2=\sin^2(3\theta)\), and that this equals one only for \(\theta=\pi/6\) and \(\theta=\pi/2\).

**6.4.** Show that replacing a computational-basis measurement of a qubit by a CNOT onto a fresh qubit, followed by a measurement of the fresh qubit, does not change the probabilities of the outcomes.

**6.5.** In Lemma 3.1, let \(q=5/8\) and \(T_0=4\). Which labels \(u\) set the flag?

## 7. Solutions

**6.1.** Every gate of \(\mathcal G\) has matrix entries in \(\{0,\pm1,\pm i,\pm1/\sqrt2\}\), and only the Hadamard gates and their controlled versions contribute the factor \(1/\sqrt2\). So each amplitude after a circuit with \(h\) such gates is \(2^{-h/2}(a+bi)\) with integers \(a,b\), and each outcome probability, a sum of squared moduli of amplitudes, is \(2^{-h}\) times an integer. The number \(\frac13\) is not dyadic.

**6.2.** Since \(x\vee y=1\oplus\bigl((1\oplus x)(1\oplus y)\bigr)\): apply NOT to the first two qubits, a Toffoli gate onto the third, NOT to the third, and NOT to the first two qubits again.

**6.3.** Write \(\psi=\sin\theta\,e_1+\cos\theta\,e_0\) with unit vectors \(e_1\in\operatorname{range}\Pi\), \(e_0\perp\operatorname{range}\Pi\). In the plane of \(e_0,e_1\), \(I-2\Pi\) is the reflection in the \(e_0\)-axis and \(2|\psi\rangle\langle\psi|-I\) is the reflection in the line of \(\psi\); their product is the rotation by \(2\theta\), so the result is \(\sin3\theta\,e_1+\cos3\theta\,e_0\). For \(0<\theta\le\pi/2\), \(\sin^23\theta=1\) exactly when \(3\theta\in\{\pi/2,3\pi/2\}\).

**6.4.** If the qubit is in the state \(\alpha|0\rangle\otimes\phi_0+\beta|1\rangle\otimes\phi_1\) with unit vectors \(\phi_b\) on the other qubits, the CNOT gives \(\alpha|0,0\rangle\otimes\phi_0+\beta|1,1\rangle\otimes\phi_1\), and the fresh qubit reads \(b\) with probability \(|\alpha|^2\) or \(|\beta|^2\), as the original measurement does.

**6.5.** Here \(A'=5\cdot2^{4-3}=10\), so the labels \(u=0,\ldots,9\) among \(0,\ldots,15\) set the flag, with probability \(10/16=5/8\).

## References

- [OpenAI-EQF] OpenAI, *Exact quantum factoring over a fixed finite gate set*, OpenAI Math Release preprint, 25 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026
- [Shor 1997] P. W. Shor, *Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer*, SIAM J. Comput. 26 (1997), no. 5, 1484–1509. https://arxiv.org/abs/quant-ph/9508027
- [Mosca–Zalka 2004] M. Mosca, C. Zalka, *Exact quantum Fourier transforms and discrete logarithm algorithms*, Int. J. Quantum Inf. 2 (2004), no. 1, 91–100. https://arxiv.org/abs/quant-ph/0301093
- [Imran 2022] M. Imran, *An exact quantum order finding algorithm and its applications*, preprint, 2022. https://arxiv.org/abs/2205.04240
- [Brassard–Høyer 1997] G. Brassard, P. Høyer, *An exact quantum polynomial-time algorithm for Simon's problem*, Proc. Fifth Israeli Symposium on Theory of Computing and Systems (1997), 12–23. https://arxiv.org/abs/quant-ph/9704027
- [BHMT 2002] G. Brassard, P. Høyer, M. Mosca, A. Tapp, *Quantum amplitude amplification and estimation*, Contemp. Math. 305 (2002), 53–74. https://arxiv.org/abs/quant-ph/0005055
- [VBE 1996] V. Vedral, A. Barenco, A. Ekert, *Quantum networks for elementary arithmetic operations*, Phys. Rev. A 54 (1996), no. 1, 147–153. https://arxiv.org/abs/quant-ph/9511018
