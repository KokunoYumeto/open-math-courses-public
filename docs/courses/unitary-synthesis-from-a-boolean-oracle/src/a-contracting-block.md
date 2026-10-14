# A contracting block

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The reduction of the next lessons removes a small group of coordinates from the synthesis problem. Its geometric series converge fast only if the corresponding diagonal block of the unitary has norm bounded away from one. This lesson obtains such a block with permutations, diagonal signs and Walsh–Hadamard transforms, all of which take few slots. Random signs make the block small: a moment estimate for sums of matrices with random signs (Lemma 1.2) bounds its norm on average, so some choice of signs works (Proposition 2.1). The removed block is large enough that fewer than \(8M(n+1)\) reductions reach dimension one (Lemma 2.2).

- Gaussian integration by parts and a matrix sign estimate (Lemmas 1.1 and 1.2).
- A block of small norm (Proposition 2.1) and the number of reductions (Lemma 2.2).

The lesson follows [OpenAI-US, Section 3]. It uses the slots of [Programmable slots](programmable-slots.md) and the spectral theorem of [Oracle circuits and the synthesis theorem](oracle-circuits-and-the-synthesis-theorem.md), Lemma 3.1.

## 1. A matrix sign estimate

A *Rademacher variable* takes the values \(1\) and \(-1\) with probability \(1/2\) each. A *standard Gaussian* has the density \(e^{-x^2/2}/\sqrt{2\pi}\) on \(\mathbb R\).

**Lemma 1.1** (Gaussian integration by parts). Let \(g_1,\dots,g_q\) be independent standard Gaussians and \(P\) a polynomial in \(q\) variables. Then
\[
\mathbb E[g_iP(g)]=\mathbb E[\partial_iP(g)] .
\]

*Proof.* By independence and Fubini's theorem it suffices to treat one variable. Integration by parts, with \(xe^{-x^2/2}=-\frac{d}{dx}e^{-x^2/2}\) and boundary terms that vanish because \(P\) grows polynomially, gives
\[
\int_{\mathbb R}xP(x)e^{-x^2/2}dx=\int_{\mathbb R}P'(x)e^{-x^2/2}dx .
\]
\(\blacksquare\)

**Lemma 1.2** (a matrix sign estimate; [OpenAI-US, Lemma 3.1]). Let \(L_1,\dots,L_q\) be Hermitian \(h\times h\) matrices, \(\varepsilon_1,\dots,\varepsilon_q\) independent Rademacher variables, and
\[
v=\Bigl\|\sum_iL_i^2\Bigr\| .
\]
For every integer \(a\ge1\),
\[
\mathbb E\Bigl\|\sum_i\varepsilon_iL_i\Bigr\|\le2h^{1/(2a)}\sqrt{(2a-1)v} .
\]

*Proof.* *Gaussian coefficients.* Let \(g_i\) be independent standard Gaussians and \(X=\sum_ig_iL_i\). Write the first factor of \(X^{2a}\) as \(\sum_ig_iL_i\); by Lemma 1.1, applied to the polynomial \(\operatorname{Tr}(L_iX^{2a-1})\), and the product rule for \(\partial_iX^{2a-1}\) with \(\partial_iX=L_i\),
\[
\begin{aligned}
&\mathbb E\operatorname{Tr}X^{2a}\\
&\quad=\sum_{i=1}^q\sum_{l=0}^{2a-2}\mathbb E\operatorname{Tr}\bigl(L_iX^lL_iX^{m-l}\bigr),
\end{aligned}
\]
where \(m=2a-2\). Fix \(X\) and diagonalize it with real eigenvalues \(\lambda_j\) (Lemma 3.1 of the first lesson). In this basis, as \(L_i\) is Hermitian,
\[
\begin{aligned}
&\operatorname{Tr}\bigl(L_iX^lL_iX^{m-l}\bigr)\\
&\quad=\sum_{j,k}|(L_i)_{jk}|^2\lambda_k^l\lambda_j^{m-l}.
\end{aligned}
\]
For \(m>0\), the weighted inequality of arithmetic and geometric means gives
\[
\bigl|\lambda_k^l\lambda_j^{m-l}\bigr|\le\tfrac lm|\lambda_k|^m+\tfrac{m-l}m|\lambda_j|^m ,
\]
and since \(\sum_j|(L_i)_{jk}|^2=(L_i^2)_{kk}\) and \(m\) is even, the sum is at most \(\operatorname{Tr}(L_i^2X^m)\); for \(m=0\) it equals it. As \(X^m\) is positive semidefinite and \(\sum_iL_i^2\le vI\),
\[
\mathbb E\operatorname{Tr}X^{2a}\le(2a-1)v\,\mathbb E\operatorname{Tr}X^{2a-2} .
\]
Iterating down to \(\operatorname{Tr}I=h\),
\[
\begin{aligned}
&\mathbb E\operatorname{Tr}X^{2a}\\
&\quad\le h(2a-1)(2a-3)\cdots1\cdot v^a\\
&\quad\le h(2a-1)^av^a .
\end{aligned}
\]
Since \(\|X\|^{2a}\) is the largest eigenvalue of \(X^{2a}\), it is at most \(\operatorname{Tr}X^{2a}\), and Jensen's inequality for \(y\mapsto y^{2a}\) gives
\[
\begin{aligned}
\mathbb E\|X\|&\le\bigl(\mathbb E\operatorname{Tr}X^{2a}\bigr)^{1/(2a)}\\
&\le h^{1/(2a)}\sqrt{(2a-1)v} .
\end{aligned}
\]

*Back to signs.* Write \(g_i=\varepsilon_it_i\) with \(t_i=|g_i|\). By the symmetry of the Gaussian density, the signs \(\varepsilon_i\) are independent Rademacher variables, independent of the \(t_i\), and \(\mathbb Et_i=\mu=\sqrt{2/\pi}\). For fixed signs, the norm of an average is at most the average of the norms:
\[
\mu\Bigl\|\sum_i\varepsilon_iL_i\Bigr\|\le\mathbb E_t\Bigl\|\sum_i\varepsilon_it_iL_i\Bigr\| .
\]
Averaging over the signs, \(\mu\,\mathbb E\|\sum_i\varepsilon_iL_i\|\le\mathbb E\|X\|\), and \(\mu^{-1}=\sqrt{\pi/2}<2\). \(\blacksquare\)

This is a finite-dimensional form of the noncommutative Khintchine inequality, with the constants used below.

## 2. A block of small norm

Fix
\[
M=4096(n+1)^2,\qquad r=\frac34 .
\]
For an integer \(2\le d\le2^n\), let \(q\) be the largest power of two with \(q\le d\), and put
\[
s=\max\{1,\lfloor q/M\rfloor\},\qquad k=d-s .
\]
The first \(k\) coordinates of \(\mathbb C^d\) are the *ports* and the last \(s\) the *internal* coordinates; both groups are nonempty.

**Proposition 2.1** (a block of small norm; [OpenAI-US, Proposition 3.2]). For every unitary \(U\) on \(\mathbb C^d\) there are unitaries \(P_{\mathrm L}\) and \(P_{\mathrm R}\) on \(\mathbb C^d\) with
\[
V=P_{\mathrm L}UP_{\mathrm R}=\begin{pmatrix}A&B\\C&D\end{pmatrix},\qquad\|D\|\le r,
\]
where \(D\) is \(s\times s\). The maps \(P_{\mathrm L}\), \(P_{\mathrm R}\) and their inverses are implemented exactly by \(O(n)\) slots with \(O(n)\) workspace qubits, on a skeleton determined by \(n\) and \(d\); the same skeleton serves every family \(U_\lambda\), with the labels among the controls.

*Proof.* *The case \(s=1\).* The last column of \(U\) is a unit vector in \(\mathbb C^d\), so one of its entries has modulus at most \(1/\sqrt d\). A permutation of the rows moves this entry to the last position, and then \(\|D\|\le1/\sqrt d\le1/\sqrt2<3/4\). Take this permutation as \(P_{\mathrm L}\) and \(P_{\mathrm R}=I\); Lemma 2.2 of [Programmable slots](programmable-slots.md) implements it with \(5n\) slots and \(n\) workspace qubits.

*The case \(s>1\).* Then \(q\ge2M\). Let \(M_0\) be the \(q\times q\) block of \(U\) in its last \(q\) rows and columns; it is a contraction. Let \(H_q=H^{\otimes\log_2q}\), a real orthogonal symmetric matrix with entries \(\pm1/\sqrt q\), and \(W\) its last \(s\) columns, which are orthonormal. For diagonal sign matrices \(E_1\), \(E_2\) on \(\mathbb C^q\), let \(P_{\mathrm L}\) act as \(H_qE_1\) and \(P_{\mathrm R}\) as \(E_2H_q\) on the last \(q\) coordinates, and as the identity on the first \(d-q\). The last \(s\) rows of \(H_qE_1\) form \(W^*E_1\), so
\[
D=W^*E_1C',\qquad C'=M_0E_2W .
\]
We choose \(E_2\) to make the entries of \(C'\) small, and then \(E_1\) to make \(\|D\|\) small.

*The entries of \(C'\).* With independent random signs on the diagonal of \(E_2\), each entry of \(C'\) is a sum \(S=\sum_j\varepsilon_j\alpha_j\) with \(\sum_j|\alpha_j|^2\le1/q\), because the rows of \(M_0\) have norm at most \(1\) and the entries of \(W\) have modulus \(1/\sqrt q\). For real coefficients \(a_j\) with \(\sum_ja_j^2\le1/q\) and \(t>0\), since \(\cosh x\le e^{x^2/2}\),
\[
\begin{aligned}
\mathbb E\exp\Bigl(t\sum_j\varepsilon_ja_j\Bigr)&=\prod_j\cosh(ta_j)\\
&\le e^{t^2/(2q)},
\end{aligned}
\]
and Markov's inequality with \(t=qu\) bounds the probability that \(|\sum_j\varepsilon_ja_j|\ge u\) by \(2e^{-qu^2/2}\). Applied to the real and the imaginary parts of \(S\), each at least \(u/\sqrt2\) in modulus when \(|S|\ge u\),
\[
\Pr\bigl(|S|\ge u\bigr)\le4e^{-qu^2/4}.
\]
There are \(qs\le4^n\) entries. For \(u=4\sqrt{(n+1)/q}\) the probability that some entry is at least \(u\) is at most
\[
4^{n+1}e^{-4(n+1)}<1 .
\]
Fix such an \(E_2\): every entry of \(C'\) has modulus at most \(4\sqrt{(n+1)/q}\), and \(\|C'\|\le1\).

*The norm of \(D\).* Let \(h_i\) and \(c_i\) be the \(i\)-th rows of \(W\) and \(C'\), as row vectors. Then \(\|h_i\|^2=s/q\) and
\[
\|c_i\|^2\le v:=\frac{16s(n+1)}q .
\]
With independent random signs \(\varepsilon_i\) on the diagonal of \(E_1\),
\[
\begin{gathered}
D=\sum_i\varepsilon_ih_i^*c_i ,\\
L_i=\begin{pmatrix}0&h_i^*c_i\\c_i^*h_i&0\end{pmatrix}.
\end{gathered}
\]
The Hermitian matrices \(L_i\) have size \(2s\), and \(\|\sum_i\varepsilon_iL_i\|=\|D\|\). The two diagonal blocks of \(\sum_iL_i^2\) are
\[
\sum_i\|c_i\|^2h_i^*h_i\le v\,W^*W=vI_s
\]
and
\[
\sum_i\|h_i\|^2c_i^*c_i=\tfrac sqC'^*C'\le\tfrac sqI_s\le vI_s .
\]
Lemma 1.2 with \(h=2s\) and \(a=n+1\), and \((2s)^{1/(2n+2)}\le\sqrt2\) because \(2s\le2^{n+1}\), give
\[
\begin{aligned}
\mathbb E\|D\|&\le2\sqrt2\sqrt{2(n+1)v}\\
&=16(n+1)\sqrt{s/q}\le\tfrac14 ,
\end{aligned}
\]
the last step because \(s\le q/M\). Some choice of \(E_1\) has \(\|D\|\le1/4\le r\).

*Slots.* A permutation of the \(n\)-bit index register moves the last \(q\) valid indices to the first \(q\) indices, an aligned block whose higher \(n-\log_2q\) bits are zero (Lemma 2.2 of [Programmable slots](programmable-slots.md), with \(5n\) slots and \(n\) workspace qubits). On that block, \(H_q\) is \(\log_2q\le n\) Hadamard slots controlled by the higher bits, with the table \(H\) when they are zero and \(I\) otherwise; each sign matrix is one diagonal slot. Then the permutation is undone. These operations preserve the valid subspace \(\mathcal H_d\) and act unitarily on the unused basis states. A family \(U_\lambda\) changes only the tables of the row permutation or of the signs, which depend on the label through the controls. \(\blacksquare\)

The random signs only prove that suitable tables exist; each label may use its own choice, and the circuit itself is deterministic.

**Lemma 2.2** (the number of reductions; [OpenAI-US, Lemma 3.3]). With these parameters, \(s\ge d/(4M)\). Starting at any \(d\le2^n\) and replacing \(d\ge2\) by \(d-s\) repeatedly, one reaches \(d=1\) in fewer than
\[
J=8M(n+1)
\]
steps.

*Proof.* If \(q/M\ge2\), then \(s=\lfloor q/M\rfloor\ge q/(2M)>d/(4M)\), because \(d<2q\). If \(q/M<2\), then \(s=1\) and \(d<2q<4M\), so again \(s>d/(4M)\). So every step multiplies the order by at most \(1-1/(4M)\). After \(J\) steps the order would be at most
\[
2^n\Bigl(1-\frac1{4M}\Bigr)^J\le2^ne^{-2(n+1)}<1,
\]
which is impossible for a positive integer. \(\blacksquare\)

## 3. Exercises

**3.1.** Show that \(\cosh x\le e^{x^2/2}\) by comparing the Taylor series term by term.

**3.2.** Check Lemma 1.1 for \(P(x)=x^3\): compute \(\mathbb E g^4\) in two ways.

**3.3.** Show that the norm of the Hermitian matrix \(\left(\begin{smallmatrix}0&D\\D^*&0\end{smallmatrix}\right)\) is \(\|D\|\).

**3.4.** For \(n=1\) and \(d=2\), find \(q\), \(s\), \(k\), and the block \(D\) of Proposition 2.1 for \(U=H\).

**3.5.** Why does the proof of Proposition 2.1 choose \(E_2\) before \(E_1\)?

## 4. Solutions

**3.1.** \(\cosh x=\sum_kx^{2k}/(2k)!\) and \(e^{x^2/2}=\sum_kx^{2k}/(2^kk!)\), and \((2k)!\ge2^kk!\) because \((2k)!/k!=(k+1)(k+2)\cdots(2k)\ge2^k\).

**3.2.** \(\mathbb E[g\cdot g^3]=\mathbb E[3g^2]=3\), and directly \(\mathbb Eg^4=3\).

**3.3.** Its square is \(\operatorname{diag}(DD^*,D^*D)\), of norm \(\|D\|^2\), and the norm of a Hermitian matrix is the square root of the norm of its square.

**3.4.** \(q=2\), \(M=16384>q\), so \(s=1\) and \(k=1\). The last column of \(H\) has entries \(\pm1/\sqrt2\); with \(P_{\mathrm L}=P_{\mathrm R}=I\), \(D=-1/\sqrt2\) and \(\|D\|<3/4\).

**3.5.** The bound on \(\|c_i\|\) needed for \(v\) uses the entries of \(C'=M_0E_2W\), which depend on \(E_2\) only; once \(E_2\) is fixed, \(D\) is a sum of fixed matrices with the random signs of \(E_1\).

## References

- [OpenAI-US] OpenAI, *Polynomial-Time Unitary Synthesis from a Boolean Oracle*, OpenAI Math Release preprint, 5 October 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026
