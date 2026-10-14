# Compilation into one Boolean oracle

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The programmable circuit of [Encoders and the recursion](encoders-and-the-recursion.md), Proposition 4.1, has polynomially many slots, but each slot may have an exponentially large table of one-qubit unitaries. This lesson stores finite gate words approximating these tables in one Boolean function. Two points need care: the words must approximate the matrices together with their phases, since a slot controlled by other qubits turns scalar phases into relative phases; and the circuit must be generated without finding the words, which are stored in the oracle. The words come from the density of the determinant-one words in \(H\), \(T\), \(T^*\) (Proposition 1.4) and a commutator refinement in the style of Solovay and Kitaev (Lemma 2.1); a controlled application of each looked-up symbol is exact (Lemma 3.1). The compilation of slots (Proposition 4.1) then proves the theorem of the course.

- Density of determinant-one words (Lemmas 1.1 to 1.3, Proposition 1.4).
- Short words with the phase (Lemma 2.1).
- Exact controlled symbols (Lemma 3.1).
- Compilation of slots and the theorem (Proposition 4.1, Theorem 4.2).

The lesson follows [OpenAI-US, Section 7]. It uses [Oracle circuits and the synthesis theorem](oracle-circuits-and-the-synthesis-theorem.md) and the inverse function theorem of the core course Real Analysis II [Lebl, Theorem 8.5.1].

## 1. Density of determinant-one words

Write \(X_p,Y_p,Z_p\) for the Pauli matrices
\[
\begin{gathered}
X_p=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad Y_p=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\\
Z_p=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\end{gathered}
\]
and \(\mathbf m\cdot\boldsymbol\sigma=m_1X_p+m_2Y_p+m_3Z_p\) for \(\mathbf m\in\mathbb R^3\). Then
\[
\begin{aligned}
&(\mathbf n\cdot\boldsymbol\sigma)(\mathbf m\cdot\boldsymbol\sigma)\\
&\quad=(\mathbf n\cdot\mathbf m)I+i(\mathbf n\times\mathbf m)\cdot\boldsymbol\sigma .
\end{aligned}
\] The matrices \(x_0I+i\,\mathbf x\cdot\boldsymbol\sigma\) with \((x_0,\mathbf x)\) a unit vector of \(\mathbb R^4\) are exactly the elements of \(SU(2)\), which is therefore a sphere, compact and connected. For a unit vector \(\mathbf n\), \(\exp(it\,\mathbf n\cdot\boldsymbol\sigma)=\cos t\,I+i\sin t\,\mathbf n\cdot\boldsymbol\sigma\); these matrices form the *circle with axis* \(\mathbf n\). A direct computation with the product rule above shows that conjugation by \(\exp(i\varphi\,\mathbf n\cdot\boldsymbol\sigma)\) maps \(\mathbf m\cdot\boldsymbol\sigma\) to \(\mathbf m'\cdot\boldsymbol\sigma\), where \(\mathbf m'\) is \(\mathbf m\) rotated about \(\mathbf n\) by the angle \(-2\varphi\).

A *word* is a product of the letters \(H\), \(T\), \(T^*\); it is a *determinant-one word* if its determinant is \(1\). Products of determinant-one words are determinant-one words, and so are inverses: the inverse of a word is the reversed word with \(T\) and \(T^*\) exchanged, as \(H^*=H\).

**Lemma 1.1** (irrational rotations). If \(\theta/\pi\) is irrational, then the points \(e^{ik\theta}\), \(k\ge1\), are dense in the unit circle.

*Proof.* The points are pairwise distinct, since \(e^{ik\theta}=e^{il\theta}\) with \(k\ne l\) would make \(\theta/\pi\) rational. For an integer \(N\ge1\), two of the points \(e^{i\theta},\dots,e^{i(N+1)\theta}\) are at angular distance at most \(2\pi/N\), so some \(e^{im\theta}\ne1\), \(1\le m\le N\), is within angular distance \(2\pi/N\) of \(1\). Its powers \(e^{ikm\theta}\), \(k\ge1\), go around the circle in steps of less than \(2\pi/N\), so every point is within \(2\pi/N\) of one of them. \(\blacksquare\)

**Lemma 1.2.** The number \(c=1+\sqrt2/2\) is not a root of a monic polynomial with integer coefficients. If \(e^{i\theta}\) is a root of unity, then \(2\cos\theta\) is a root of such a polynomial.

*Proof.* Suppose \(g(c)=0\) with \(g\) monic of degree \(D\ge1\) with integer coefficients. Then \(f(x)=g(x+1)\) is of the same kind and \(f(1/\sqrt2)=0\): with \(f(x)=\sum_{k=0}^Da_kx^k\), \(a_D=1\),
\[
\sum_{k=0}^Da_k2^{(D-k)/2}=0 .
\]
The terms with \(D-k\) odd are integer multiples of \(\sqrt2\), those with \(D-k\) even are integers, and \(\sqrt2\) is irrational; so the integer terms add up to \(0\). Among them, the term \(k=D\) is \(1\) and all others are even, a contradiction.

For the second claim define \(P_0=2\), \(P_1=x\) and \(P_{m+1}=xP_m-P_{m-1}\). By induction \(P_m\) is monic of degree \(m\) with integer coefficients for \(m\ge1\), and \(P_m(2\cos\theta)=2\cos(m\theta)\), by the identity
\[
\begin{aligned}
&2\cos\theta\cdot2\cos(m\theta)\\
&\quad=2\cos((m+1)\theta)+2\cos((m-1)\theta).
\end{aligned}
\] If \(e^{iN\theta}=1\) with \(N\ge1\), then \(2\cos\theta\) is a root of \(P_N-2\). \(\blacksquare\)

**Lemma 1.3.** Let \(V=e^{-i(\pi/8)X_p}e^{-i(\pi/8)Z_p}\). Then \(W=(HTH)T=e^{i\pi/4}V\), the word \(W^4=-V^4\) has determinant one, and its powers are dense in the circle whose axis is the axis of \(V\), which is not parallel to the \(Z_p\)-axis.

*Proof.* \(T=e^{i\pi/8}e^{-i(\pi/8)Z_p}\) and \(HTH=e^{i\pi/8}e^{-i(\pi/8)X_p}\), as \(HZ_pH=X_p\). So \(W=e^{i\pi/4}V\) and \(W^4=e^{i\pi}V^4=-V^4\), of determinant one. With \(c_0=\cos(\pi/8)\), \(s_0=\sin(\pi/8)\) and \(X_pZ_p=-iY_p\),
\[
\begin{aligned}
V&=c_0^2I\\
&\quad+i\bigl(-c_0s_0X_p+s_0^2Y_p-c_0s_0Z_p\bigr),
\end{aligned}
\]
whose axis \(\mathbf n\) is the direction of \((-c_0s_0,s_0^2,-c_0s_0)\), not parallel to the \(Z_p\)-axis. So \(V=\cos\theta\,I+i\sin\theta\,\mathbf n\cdot\boldsymbol\sigma\), that is, \(V=\exp(i\theta\,\mathbf n\cdot\boldsymbol\sigma)\), with \(\cos\theta=c_0^2\) and \(0<\theta<\pi\); its eigenvalues are \(e^{\pm i\theta}\), and \(2\cos\theta=\operatorname{Tr}V=2c_0^2=1+\sqrt2/2\). By Lemma 1.2, \(e^{i\theta}\) is not a root of unity, so \(\theta/\pi\) is irrational. As \(-I=\exp(i\pi\,\mathbf n\cdot\boldsymbol\sigma)\),
\[
W^4=\exp\bigl(i(\pi+4\theta)\,\mathbf n\cdot\boldsymbol\sigma\bigr),
\]
and \((\pi+4\theta)/\pi\) is irrational. By Lemma 1.1 the powers of \(W^4\) are dense in the circle with axis \(\mathbf n\). \(\blacksquare\)

**Proposition 1.4** ([OpenAI-US, Lemma 7.1, first part]). The determinant-one words are dense in \(SU(2)\).

*Proof.* Let \(G\) be the closure of the group of determinant-one words; it is a closed subgroup of \(SU(2)\). By Lemma 1.3 it contains the circle with axis \(\mathbf n_1\), the axis of \(V\). Conjugation by \(T\), which is \(e^{-i(\pi/8)Z_p}\) up to a scalar, sends determinant-one words to determinant-one words and rotates axes about the \(Z_p\)-axis by \(\pi/4\); so \(G\) contains the circle whose axis \(\mathbf n_2\) is \(\mathbf n_1\) rotated by \(\pi/4\) about the \(Z_p\)-axis. As \(\mathbf n_1\) is not parallel to the \(Z_p\)-axis, \(\mathbf n_2\) is neither \(\mathbf n_1\) nor \(-\mathbf n_1\); write \(\mathbf n_2=\alpha\mathbf n_1+\beta\mathbf m\) with \(\mathbf m\perp\mathbf n_1\) a unit vector and \(\beta\ne0\). Conjugating by \(\exp(-i(\pi/4)\mathbf n_1\cdot\boldsymbol\sigma)\in G\) rotates \(\mathbf n_2\) about \(\mathbf n_1\) by \(\pi/2\), to \(\mathbf n_3=\alpha\mathbf n_1+\beta\,\mathbf n_1\times\mathbf m\), and \(G\) contains the circle with axis \(\mathbf n_3\). The vectors \(\mathbf n_1,\mathbf n_2,\mathbf n_3\) are linearly independent.

Consider the map
\[
\psi(t_1,t_2,t_3)=\prod_{j=1}^3\exp(it_j\,\mathbf n_j\cdot\boldsymbol\sigma)
\]
from \(\mathbb R^3\) to \(G\), followed by the coordinates \(x_0I+i\,\mathbf x\cdot\boldsymbol\sigma\mapsto\mathbf x\in\mathbb R^3\). This composite is continuously differentiable, sends \(0\) to \(0\), and its derivative at \(0\) is \((t_1,t_2,t_3)\mapsto\sum_jt_j\mathbf n_j\), which is invertible. By the inverse function theorem [Lebl, Theorem 8.5.1], it maps a neighbourhood of \(0\) onto a neighbourhood \(\Omega\) of \(0\in\mathbb R^3\); for small \(t\) the coordinate \(x_0\) of \(\psi(t)\) is positive, so \(G\) contains the matrices \(\sqrt{1-|\mathbf x|^2}\,I+i\,\mathbf x\cdot\boldsymbol\sigma\), \(\mathbf x\in\Omega\), a neighbourhood of \(I\) in \(SU(2)\). Then \(G\) contains a neighbourhood of each of its elements, so it is open; it is also closed, and \(SU(2)\) is connected, so \(G=SU(2)\). \(\blacksquare\)

## 2. Short words with the phase

**Lemma 2.1** ([OpenAI-US, Lemma 7.1]). There is a positive integer \(K_{\mathrm w}\) such that for every \(S\in SU(2)\) and \(0<\xi<1\) some determinant-one word of length at most \(K_{\mathrm w}\xi^{-3}\) is within \(\xi\) of \(S\) in operator norm.

*Proof.* *Two estimates.* For skew-Hermitian \(P\), \(Q\) with \(x=\|P\|+\|Q\|\le1\), expand the four exponential series in \(e^Pe^Qe^{-P}e^{-Q}\). The terms of degrees \(1\) cancel, those of degree \(2\) add up to \(PQ-QP\), and the terms of degree at least \(3\) have total norm at most \(\sum_{k\ge3}(2x)^k/k!\le10x^3\). So
\[
\|e^Pe^Qe^{-P}e^{-Q}-I-[P,Q]\|\le10x^3 .
\]
For \(U=\exp(i\mathbf a\cdot\boldsymbol\sigma)\) with \(|\mathbf a|\le1\), the eigenvalues of \(U\) are \(e^{\pm i|\mathbf a|}\), and
\[
\begin{aligned}
\|U-I-i\,\mathbf a\cdot\boldsymbol\sigma\|&=|e^{i|\mathbf a|}-1-i|\mathbf a||\\
&\le|\mathbf a|^2 .
\end{aligned}
\]
Also \(\|U-I\|=2\sin(|\mathbf a|/2)\ge2|\mathbf a|/\pi\) for \(|\mathbf a|\le\pi\).

*Refinement.* Suppose that the determinant-one words of length at most \(\ell\) form an \(\varepsilon\)-net of \(SU(2)\), with \(\varepsilon\le1/16\). Given \(S\), choose such a word \(W_0\) with \(\|S-W_0\|\le\varepsilon\). Then \(SW_0^*=\exp(i\mathbf a\cdot\boldsymbol\sigma)\) with \(|\mathbf a|\le(\pi/2)\varepsilon\le2\varepsilon\). Choose perpendicular vectors \(\mathbf u\), \(\mathbf v\) of length \(\sqrt{|\mathbf a|/2}\) with \(\mathbf u\times\mathbf v=-\mathbf a/2\), and put
\[
P=i\,\mathbf u\cdot\boldsymbol\sigma,\qquad Q=i\,\mathbf v\cdot\boldsymbol\sigma .
\]
By the product rule, \([P,Q]=-2i(\mathbf u\times\mathbf v)\cdot\boldsymbol\sigma=i\,\mathbf a\cdot\boldsymbol\sigma\), and \(\|P\|=\|Q\|=\sqrt{|\mathbf a|/2}\le\sqrt\varepsilon\). With \(A=e^P\), \(B=e^Q\), the two estimates give
\[
\begin{aligned}
\|ABA^*B^*-SW_0^*\|&\le80\varepsilon^{3/2}+4\varepsilon^2\\
&\le84\varepsilon^{3/2}.
\end{aligned}
\]
Choose words \(\widetilde A\), \(\widetilde B\) of length at most \(\ell\) within \(\varepsilon\) of \(A\), \(B\). Writing \(B=I+(B-I)\) and cancelling the identity terms,
\[
\|ABA^*B^*-\widetilde AB\widetilde A^*B^*\|\le2\varepsilon\|B-I\|,
\]
and in the same way
\[
\|\widetilde AB\widetilde A^*B^*-\widetilde A\widetilde B\widetilde A^*\widetilde B^*\|\le2\varepsilon\|\widetilde A-I\| .
\]
Here \(\|B-I\|\le2\|Q\|\le2\sqrt\varepsilon\) and \(\|\widetilde A-I\|\le2\sqrt\varepsilon+\varepsilon\le3\sqrt\varepsilon\). So the determinant-one word \(\widetilde A\widetilde B\widetilde A^*\widetilde B^*W_0\), of length at most \(5\ell\), is within \(94\varepsilon^{3/2}\) of \(S\).

*Iteration.* Fix \(\varepsilon_0\le1/16\) with \(94\sqrt{\varepsilon_0}\le1/2\). By Proposition 1.4 and the compactness of \(SU(2)\) there is a finite \(\varepsilon_0\)-net of determinant-one words, of lengths at most some \(\ell_0\). As \(94\varepsilon^{3/2}\le\varepsilon/2\) for \(\varepsilon\le\varepsilon_0\), \(j\) refinements give a \(2^{-j}\varepsilon_0\)-net of words of length at most \(5^j\ell_0\). For \(0<\xi<1\), let \(j\) be the least integer with \(2^{-j}\varepsilon_0\le\xi\); if \(j\ge1\), then \(2^j<2\varepsilon_0/\xi\), and as \(\log_25<3\),
\[
5^j=(2^j)^{\log_25}<(2\varepsilon_0/\xi)^{\log_25}<\xi^{-3},
\]
because \(2\varepsilon_0<1\) and \(\xi<1\). So \(K_{\mathrm w}=\ell_0\) works. \(\blacksquare\)

Only the existence of the integer \(K_{\mathrm w}\) is used below: a generator of circuits can contain it as a constant, without knowing the net or a procedure that selects words. The selected words are stored in the oracle.

## 3. Exact controlled symbols

**Lemma 3.1.** With clean scratch qubits, the following are exact circuits over \(H\), \(T\), \(T^*\), \(\mathrm{CNOT}\): the bit flip \(X_p\); the doubly controlled \(Z_p\) and the Toffoli gate; every reversible classical operation on bits, in particular equality tests and the preparation of addresses; and the singly controlled \(H\), \(T\) and \(T^*\).

*Proof.* \(T^4=Z_p\) and \(HZ_pH=X_p\). For bits \(a,b,c\),
\[
\begin{aligned}
4abc&=a+b+c-(a\oplus b)-(a\oplus c)\\
&\quad-(b\oplus c)+(a\oplus b\oplus c),
\end{aligned}
\]
as one checks on the eight cases. Compute each of the seven parities into a clean scratch qubit with \(\mathrm{CNOT}\)s, apply \(T\) to it for a plus sign and \(T^*\) for a minus sign, and uncompute it: the total phase is \(e^{i\pi abc}=(-1)^{abc}\), the doubly controlled \(Z_p\). Conjugating its target by \(H\) gives the Toffoli gate, and with \(X_p\), \(\mathrm{CNOT}\) and Toffoli gates on clean scratch every reversible classical operation is exact.

A controlled \(T\) is the phase \(e^{i\pi/4}\) on the basis vectors where control and target are both \(1\): compute the AND of control and target into a clean scratch qubit with a Toffoli gate, apply \(T\) there, and uncompute; likewise for \(T^*\). For \(H\), put \(D_0=(T^2H)T(T^2H)^*\). Since \((T^2H)Z_p(T^2H)^*=Y_p\), we have \(D_0=e^{i\pi/8}e^{-i(\pi/8)Y_p}\), and conjugation by \(e^{-i(\pi/8)Y_p}\) rotates the \(Z_p\)-axis by \(\pi/4\) about the \(Y_p\)-axis, towards the \(X_p\)-axis:
\[
D_0Z_pD_0^*=\frac{X_p+Z_p}{\sqrt2}=H .
\]
Apply \(D_0^*\) to the target, then a controlled \(Z_p\), which is a \(\mathrm{CNOT}\) conjugated by \(H\) on its target, then \(D_0\). When the control is \(0\) the two outer gates cancel; when it is \(1\) their product is exactly \(H\). \(\blacksquare\)

## 4. Compilation of slots and the theorem

**Proposition 4.1** (compilation of slots; [OpenAI-US, Proposition 7.2]). Let a skeleton have \(S\) slots on \(Q\) qubits, and let \(\eta=1/h\) for an integer \(h\ge2\). A deterministic procedure, running in time polynomial in \(Q\), \(S\), \(1/\eta\), produces a circuit over \(H\), \(T\), \(T^*\), \(\mathrm{CNOT}\) and one Boolean oracle, with polynomially many qubits, gates, oracle calls and address bits, such that for every choice of the slot tables some contents of the oracle make the circuit differ by at most \(S\eta\) from the skeleton with these tables, on inputs whose added scratch qubits are zero, the comparison map keeping the scratch at zero.

*Proof.* *One table entry.* Write \(W_y=e^{i\gamma_y}S_y\) with \(\gamma_y\) real and \(S_y\in SU(2)\). By Lemma 2.1 choose determinant-one words within \(\eta/2\) of \(S_y\) and of
\[
P_y=\operatorname{diag}(e^{i\gamma_y},e^{-i\gamma_y})\in SU(2),
\]
and pad all words with the identity symbol to the common length \(\ell=\lceil K_{\mathrm w}(2/\eta)^3\rceil\). Apply the first word to the target of the slot and the second to a scratch *phase qubit* in the state \(|0\rangle\). The ideal actions are \(S_y\) on the target and the factor \(e^{i\gamma_y}\) on \(|0\rangle\), so together \(W_y\), with the phase qubit returned to zero; the two errors add up to at most \(\eta\). Different control values \(y\) occupy orthogonal blocks, so the bound holds for the whole controlled slot, and \(e^{i\gamma_y}\) is kept as a relative phase between control values.

*The oracle.* Encode the symbols \(I,H,T,T^*\) by two bits. One Boolean function stores all symbol bits, at the addresses
\[
(\text{slot},\ y,\ \text{word},\ \text{position},\ \text{bit}),
\]
the field of \(y\) padded to \(Q\) bits; all addresses have the common length \(O(Q+\log(S+1)+\log(\ell+1))\). For each position of each word, copy the controls of the slot into an address register with \(\mathrm{CNOT}\)s, set the fixed address bits, query the two symbol bits into zero qubits, apply the symbol to the target or the phase qubit, controlled by the symbol bits (Lemma 3.1), erase the symbol bits by querying again, and undo the address preparation. The controls of the slot are not changed by any of these operations, so the erasure is exact also for superpositions of control values.

*Composition.* Let \(A_j\) be the implementation of slot \(j\) and \(V_j\) the ideal slot, acting as the identity on all added scratch. The phase qubit and the other scratch are reused; although after an actual slot they need not be exactly zero, the identity
\[
\begin{aligned}
&A_S\cdots A_1-V_S\cdots V_1\\
&\quad=\sum_{j=1}^SA_S\cdots A_{j+1}(A_j-V_j)V_{j-1}\cdots V_1
\end{aligned}
\]
uses \(A_j-V_j\) only after an ideal prefix, which keeps all added scratch at zero, where the bound for one slot applies; the unitary suffix keeps norms. So the error is at most \(S\eta\).

*Resources.* There are two words per slot, \(\ell\) positions per word and polynomially many elementary gates per lookup, so the numbers of qubits, gates, calls and address bits are polynomial in \(Q\), \(S\), \(1/\eta\). The circuit is generated from the skeleton, the constant \(K_{\mathrm w}\) and integer arithmetic; it never selects a word or computes a table entry. Each choice of tables determines a Boolean function storing the selected words. \(\blacksquare\)

**Theorem 4.2.** Theorem 2.1 of [Oracle circuits and the synthesis theorem](oracle-circuits-and-the-synthesis-theorem.md) holds: there are a polynomial \(p\) and a deterministic algorithm producing from \(1^n\), in time \(p(n)\), an oracle circuit \(A_n\) over \(H,T,T^*,\mathrm{CNOT}\), of polynomial size and oracle input length, such that for every \(U\in U(2^n)\) some oracle \(f\) gives \(\|\Phi_{n,f}-\mathcal U\|_\diamond\le1/2\).

*Proof.* Proposition 4.1 of [Encoders and the recursion](encoders-and-the-recursion.md), with \(d=2^n\) and no labels, gives a skeleton with polynomially many qubits and \(S\) slots, generated in polynomial time, whose tables can be chosen so that it implements \(U\) with clean-workspace error less than \(1/100\). Compile it by Proposition 4.1 with
\[
\eta=\frac1{100(S+1)} ,
\]
which adds an error less than \(1/100\) on inputs whose workspace and scratch are zero. So the whole circuit implements \(U\) with clean-workspace error less than \(1/50\), the designated qubits being the original index qubits. By Proposition 4.2 of [Oracle circuits and the synthesis theorem](oracle-circuits-and-the-synthesis-theorem.md), its output channel is within \(1/25<1/2\) of \(\mathcal U\) in the diamond norm. Its numbers of qubits, gates and calls, the length of its oracle addresses and the running time of the generator are polynomial in \(n\), and a single polynomial \(p\) bounds them all. \(\blacksquare\)

## 5. Exercises

**5.1.** Check the parity identity in the proof of Lemma 3.1 for \((a,b,c)=(1,1,0)\) and \((1,1,1)\).

**5.2.** Show that \(H\) and \(T\) have determinants \(-1\) and \(e^{i\pi/4}\), and that a word with \(a\) letters \(H\), \(b\) letters \(T\) and \(c\) letters \(T^*\) has determinant one exactly when \(4a+b-c\) is divisible by \(8\). Give a determinant-one word with an odd number of letters \(H\).

**5.3.** Why does a slot compiled with words for \(S_y\) only, without the phase qubit, fail to implement \(W_y\) under control?

**5.4.** Show that \(P_2=x^2-2\) and \(P_3=x^3-3x\), and check \(P_3(2\cos\theta)=2\cos3\theta\) at \(\theta=0\).

**5.5.** In the proof of Lemma 2.1, verify \([P,Q]=i\,\mathbf a\cdot\boldsymbol\sigma\) for \(\mathbf u=(\rho,0,0)\), \(\mathbf v=(0,\rho,0)\), and find \(\mathbf a\).

## 6. Solutions

**5.1.** For \((1,1,0)\): \(2-0-1-1+0=0\). For \((1,1,1)\): \(3-0-0-0+1=4\).

**5.2.** \(\det H=-1/2-1/2=-1\), \(\det T=e^{i\pi/4}\) and \(\det T^*=e^{-i\pi/4}\). The word has determinant \((-1)^ae^{i\pi(b-c)/4}=e^{i\pi(4a+b-c)/4}\), which is \(1\) exactly when \(8\) divides \(4a+b-c\). For example \(HT^4\) has determinant \((-1)\cdot e^{i\pi}=1\).

**5.3.** It applies \(S_y=e^{-i\gamma_y}W_y\) for the control value \(y\); different \(y\) get different phases \(e^{-i\gamma_y}\), which are relative phases of the controlled operation and change it, as in Exercise 6.2 of the first lesson.

**5.4.** \(P_2=x\cdot x-2\), \(P_3=x(x^2-2)-x=x^3-3x\); at \(\theta=0\), \(P_3(2)=8-6=2=2\cos0\).

**5.5.** By the product rule \((\mathbf u\cdot\boldsymbol\sigma)(\mathbf v\cdot\boldsymbol\sigma)=i(\mathbf u\times\mathbf v)\cdot\boldsymbol\sigma\) for perpendicular vectors, so \([P,Q]=i^2\cdot2i(\mathbf u\times\mathbf v)\cdot\boldsymbol\sigma=-2i\rho^2Z_p\), and \(\mathbf a=(0,0,-2\rho^2)\).

## References

- [OpenAI-US] OpenAI, *Polynomial-Time Unitary Synthesis from a Boolean Oracle*, OpenAI Math Release preprint, 5 October 2026, Section 7. https://github.com/openai/math/tree/main/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026
- [Lebl] J. Lebl, *Basic Analysis II*, version 6.3, Theorem 8.5.1 (inverse function theorem); core course Real Analysis II. https://www.jirka.org/ra/html/sec_svinvfuncthm.html#thm_inverse
