# Oracle circuits and the synthesis theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A unitary on \(n\) qubits is a \(2^n\times2^n\) matrix, so a classical description of it is exponentially long. Aaronson and Kuperberg asked whether every such unitary can nevertheless be performed in quantum polynomial time when a suitable classical description is available through coherent queries to a Boolean function [AK, Section 7, Problem (4)]. This course proves the theorem of [OpenAI-US]: in the constant-error form, the answer is yes. One circuit, generated in polynomial time from \(n\) alone, with polynomially many qubits, gates and oracle calls of polynomial length, approximates every \(n\)-qubit unitary within diamond-norm distance \(1/2\) once a suitable Boolean oracle is chosen. The oracle depends on the unitary, and the theorem does not say how to compute it.

This lesson fixes the model, states the theorem, and proves the facts about norms used at the end of the course.

- Qubits, gates and oracle circuits (Section 1).
- The theorem (Theorem 2.1).
- Hermitian matrices and the trace norm (Lemmas 3.1 and 3.2).
- Clean-workspace errors (Definition 4.1, Proposition 4.2).
- The plan of the course (Section 5).

The course follows [OpenAI-US].

## 1. Qubits, gates and oracle circuits

A *register* of \(N\) qubits is the Hilbert space \((\mathbb C^2)^{\otimes N}=\mathbb C^{2^N}\) with its *computational basis* \(|x\rangle=|x_1\rangle\otimes\cdots\otimes|x_N\rangle\), \(x\in\{0,1\}^N\). We also read \(x\) as the integer with binary digits \(x_1\dots x_N\), the first being the most significant, and write
\[
\mathcal H_d=\operatorname{span}\{|0\rangle,\dots,|d-1\rangle\}
\]
for \(1\le d\le2^N\). Vector norms are Euclidean, \(\|A\|\) is the operator norm of a linear map, and \(A^*\) is its adjoint. A scalar phase is never divided out: \(U\) and \(e^{i\varphi}U\) are different maps.

The *elementary gates* are
\[
\begin{gathered}
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\\
T=\begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix},
\end{gathered}
\]
\(T^*\), and \(\mathrm{CNOT}\), which maps \(|a,b\rangle\) to \(|a,a\oplus b\rangle\). A gate applied to some qubits of a register acts as the tensor product of the gate with the identity on the other qubits. A *Boolean oracle* \(f\colon\{0,1\}^m\to\{0,1\}\) supplies the gate
\[
O_f|x,b\rangle=|x,b\oplus f(x)\rangle
\]
on \(m+1\) qubits, a permutation of the computational basis that is its own inverse.

A *quantum oracle circuit* consists of a register of \(N\) qubits, of which \(n\) are designated *input qubits* and the others are *workspace*, and a finite sequence of elementary gates and oracle calls on chosen qubits. For an oracle \(f\) it defines a unitary \(C^f\) on the register. Its *output channel* is
\[
\Phi(\rho)=\operatorname{Tr}_W\bigl[C^f(\rho\otimes|0\rangle\langle0|_W)(C^f)^*\bigr],
\]
for operators \(\rho\) on the input qubits, where \(W\) is the workspace, initialized to zero, and the input qubits are read out at the end. Here the *partial trace* \(\operatorname{Tr}_W\) of an operator \(X\) on \(V\otimes W\) is the operator on \(V\) characterized by
\[
\operatorname{Tr}\bigl(M\operatorname{Tr}_WX\bigr)=\operatorname{Tr}\bigl((M\otimes I_W)X\bigr)
\]
for all operators \(M\) on \(V\); it maps \(A\otimes B\) to \((\operatorname{Tr}B)A\), and positive semidefinite operators to positive semidefinite ones.

The *trace norm* of a matrix is \(\|X\|_1=\operatorname{Tr}\sqrt{X^*X}\). For a unitary \(U\) on \(n\) qubits write \(\mathcal U(\rho)=U\rho U^*\). The distance of channels \(\Phi\) and \(\Psi\) on \(n\) qubits is measured in the *diamond norm*
\[
\begin{aligned}
&\|\Phi-\Psi\|_\diamond\\
&\quad=\sup_\rho\bigl\|\bigl((\Phi-\Psi)\otimes\mathrm{id}_R\bigr)(\rho)\bigr\|_1 ,
\end{aligned}
\]
where \(R\) is a reference register of \(n\) qubits and \(\rho\) runs over the density operators on the input qubits and \(R\). This norm has no factor \(1/2\); the distance of two channels is at most \(2\).

## 2. The theorem

**Theorem 2.1** (polynomial-time unitary synthesis; [OpenAI-US, Theorem 1.1]). There are a polynomial \(p\) and a deterministic classical algorithm which, on input \(1^n\) for an integer \(n\ge1\), outputs in time at most \(p(n)\) a quantum oracle circuit \(A_n\) with the following properties. It uses the gates \(H\), \(T\), \(T^*\), \(\mathrm{CNOT}\) and one Boolean oracle of input length \(m(n)\le p(n)\), and its numbers of qubits, elementary gates and oracle calls are each at most \(p(n)\). For every unitary \(U\in U(2^n)\) there is a function \(f\colon\{0,1\}^{m(n)}\to\{0,1\}\) for which the output channel \(\Phi_{n,f}\) of \(A_n^{f}\) satisfies
\[
\|\Phi_{n,f}-\mathcal U\|_\diamond\le\frac12 .
\]

The order of the quantifiers matters. The circuit and its resources depend on \(n\) only; the oracle depends on \(U\). Nothing is required of \(f\) beyond its existence: its truth table may be arbitrary, and no efficient procedure to compute it from a description of \(U\) is claimed. The error bound holds for all inputs, including inputs entangled with a reference system.

The theorem is proved in the last lesson, [Compilation into one Boolean oracle](compilation-into-one-boolean-oracle.md), Theorem 4.2.

## 3. Hermitian matrices and the trace norm

**Lemma 3.1** (spectral theorem). Every Hermitian matrix \(A\) on \(\mathbb C^d\) has an orthonormal basis of eigenvectors, with real eigenvalues.

*Proof.* By induction on \(d\); the case \(d=0\) is empty. The function \(x\mapsto\langle x,Ax\rangle\) is real and continuous on the compact unit sphere; let \(x\) be a point where it is largest. For \(y\perp x\) and real \(t\), the quotient
\[
g(t)=\frac{\langle x+ty,A(x+ty)\rangle}{1+t^2\|y\|^2}
\]
is largest at \(t=0\), and its derivative there is \(2\operatorname{Re}\langle y,Ax\rangle\). So \(\operatorname{Re}\langle y,Ax\rangle=0\) for every \(y\perp x\), and replacing \(y\) by \(iy\) gives \(\langle y,Ax\rangle=0\). Hence \(Ax=\lambda x\) with \(\lambda=\langle x,Ax\rangle\) real. The orthogonal complement of \(x\) is invariant, since \(\langle x,Ay\rangle=\langle Ax,y\rangle=\lambda\langle x,y\rangle\), and \(A\) restricted to it is Hermitian; apply the induction hypothesis. \(\blacksquare\)

For a Hermitian matrix \(X=\sum_i\lambda_iv_iv_i^*\) in such a basis, \(\sqrt{X^*X}=\sum_i|\lambda_i|v_iv_i^*\), so \(\|X\|_1=\sum_i|\lambda_i|\). With
\[
X_\pm=\sum_{\pm\lambda_i>0}\pm\lambda_iv_iv_i^*
\]
we have \(X=X_+-X_-\), both positive semidefinite, and \(\|X\|_1=\operatorname{Tr}X_++\operatorname{Tr}X_-\). For Hermitian \(M\), \(-I\le M\le I\) means \(|\langle v,Mv\rangle|\le\|v\|^2\) for all \(v\).

**Lemma 3.2** (the trace norm of Hermitian matrices). Let \(X\) and \(Y\) be Hermitian.

1. \(\|X\|_1\) is the largest value of \(\operatorname{Tr}(MX)\) over Hermitian \(M\) with \(-I\le M\le I\).
2. \(\|X+Y\|_1\le\|X\|_1+\|Y\|_1\).
3. If \(X\) acts on \(V\otimes W\), then \(\|\operatorname{Tr}_WX\|_1\le\|X\|_1\).
4. For unit vectors \(a\) and \(b\),
\[
\begin{aligned}
\|aa^*-bb^*\|_1&=2\sqrt{1-|\langle a,b\rangle|^2}\\
&\le2\|a-b\| .
\end{aligned}
\]

*Proof.* (1) The matrix \(M=\sum_i\operatorname{sign}(\lambda_i)v_iv_i^*\) satisfies \(-I\le M\le I\) and \(\operatorname{Tr}(MX)=\sum_i|\lambda_i|\). Conversely, write \(X_+=\sum_k\mu_kw_kw_k^*\) with \(\mu_k\ge0\); then \(\operatorname{Tr}(MX_+)=\sum_k\mu_k\langle w_k,Mw_k\rangle\), which is at most \(\operatorname{Tr}X_+\), likewise \(-\operatorname{Tr}(MX_-)\le\operatorname{Tr}X_-\), and so \(\operatorname{Tr}(MX)\le\|X\|_1\).

(2) follows from (1), since \(\operatorname{Tr}(M(X+Y))=\operatorname{Tr}(MX)+\operatorname{Tr}(MY)\).

(3) \(\operatorname{Tr}_WX\) is Hermitian, and \(\operatorname{Tr}(M\operatorname{Tr}_WX)=\operatorname{Tr}((M\otimes I_W)X)\), where \(-I\le M\otimes I_W\le I\) whenever \(-I\le M\le I\). Apply (1) twice.

(4) The matrix \(Z=aa^*-bb^*\) is Hermitian of rank at most \(2\) and trace \(0\), so its nonzero eigenvalues are \(\pm\lambda\) for some \(\lambda\ge0\), and
\[
2\lambda^2=\operatorname{Tr}Z^2=2-2|\langle a,b\rangle|^2 .
\]
So \(\|Z\|_1=2\lambda=2\sqrt{1-|\langle a,b\rangle|^2}\). With \(c=|\langle a,b\rangle|\le1\),
\[
\begin{aligned}
1-c^2&=(1-c)(1+c)\le2(1-c)\\
&\le2-2\operatorname{Re}\langle a,b\rangle=\|a-b\|^2 .
\end{aligned}
\]
\(\blacksquare\)

## 4. Clean-workspace errors

The circuits of this course are compared with their targets on inputs whose workspace is zero, and they must return the workspace to zero.

**Definition 4.1.** Let \(\mathcal V\) be a subspace of a register and \(w\ge0\). Write \(\iota\colon\mathcal V\to\mathcal V\otimes(\mathbb C^2)^{\otimes w}\) for the map \(v\mapsto v\otimes|0^w\rangle\) appending \(w\) workspace qubits in the zero state. A unitary \(C\) on the enlarged register *implements* a linear map \(\mathcal U\colon\mathcal V\to\mathcal V\) with *clean-workspace error* \(\delta\) if
\[
\|C\iota-\iota\,\mathcal U\|\le\delta .
\]

The estimate includes the return of the workspace to zero. It is unchanged when both sides are tensored with the identity of a further register: for an operator \(A\) and an orthonormal basis \(e_r\) of that register, a vector \(v=\sum_rv_r\otimes e_r\) has \(\|(A\otimes I)v\|^2=\sum_r\|Av_r\|^2\le\|A\|^2\|v\|^2\), with equality approached on product vectors.

**Proposition 4.2.** Let a quantum oracle circuit with \(n\) input qubits and \(w\) workspace qubits have the unitary \(C\), and let \(U\) be a unitary on the input qubits with \(\|C\iota-\iota U\|\le\delta\). Then the output channel satisfies \(\|\Phi-\mathcal U\|_\diamond\le2\delta\).

*Proof.* Let \(\psi\) be a unit vector of the input qubits and \(R\), and put
\[
a=(C\iota\otimes I_R)\psi,\qquad b=(\iota U\otimes I_R)\psi .
\]
Both are unit vectors, and \(\|a-b\|\le\delta\) by the remark above. The vector \(b\) is \((U\otimes I_R)\psi\) followed by \(|0^w\rangle\), so the partial trace over the workspace of \(bb^*\) is \((\mathcal U\otimes\mathrm{id}_R)(\psi\psi^*)\), while that of \(aa^*\) is \((\Phi\otimes\mathrm{id}_R)(\psi\psi^*)\). By Lemma 3.2, parts 3 and 4,
\[
\bigl\|\bigl((\Phi-\mathcal U)\otimes\mathrm{id}_R\bigr)(\psi\psi^*)\bigr\|_1\le2\delta .
\]
A density operator is \(\rho=\sum_kp_k\psi_k\psi_k^*\) with \(p_k\ge0\), \(\sum_kp_k=1\) (Lemma 3.1), and part 2 of Lemma 3.2 gives the same bound for \(\rho\). \(\blacksquare\)

## 5. The plan of the course

The construction replaces the synthesis of a unitary of order \(d\) by the synthesis of one smaller, coherently controlled unitary, removing at each step a fraction at least \(1/\operatorname{poly}(n)\) of the dimension, and using the smaller circuit exactly once.

1. [Programmable slots](programmable-slots.md): circuits whose one-qubit gates are read from arbitrary tables, controlled by other qubits; state preparation, permutations of the basis and Fourier transforms take few slots.
2. [A contracting block](a-contracting-block.md): after permutations, diagonal signs and Walsh–Hadamard transforms, a unitary has the block form \(\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\) with \(\|D\|\le3/4\) and \(D\) not too small, by a moment estimate for random signs.
3. [Fourier fields for a smaller unitary](fourier-fields-for-a-smaller-unitary.md): feeding the lower output back through a diagonal phase \(Z\) gives the unitary \(F=A+BZ(I-DZ)^{-1}C\); truncated series give two nearly isometric maps intertwining \(V\) with \(F\), with few nonzero entries in each row of their Fourier coefficients.
4. [Encoders and the recursion](encoders-and-the-recursion.md): a reflection argument implements such maps; one call of the smaller circuit between two encoders synthesizes \(V\), and the recursion gives a programmable circuit of polynomial size with error below \(1/100\).
5. [Compilation into one Boolean oracle](compilation-into-one-boolean-oracle.md): every slot is replaced by words in \(H\), \(T\), \(T^*\) read from one oracle, with the phases kept; this proves Theorem 2.1.

## 6. Exercises

**6.1.** Show that \(O_f\) is a permutation matrix and its own inverse, and compute \(O_f\) for the constant function \(f=1\) with \(m=1\).

**6.2.** Let \(U\) be a unitary on one qubit and \(\varphi\) real. Show that \(\mathcal U\) and the channel of \(e^{i\varphi}U\) are equal, but the controlled unitaries \(|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes U\) and \(|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes e^{i\varphi}U\) differ unless \(e^{i\varphi}=1\).

**6.3.** Compute \(\|aa^*-bb^*\|_1\) for \(a=|0\rangle\) and \(b=\cos t\,|0\rangle+\sin t\,|1\rangle\), and compare with \(2\|a-b\|\).

**6.4.** Show that \(\|\Phi-\Psi\|_\diamond\le2\) for any two channels, that is, linear maps sending density operators of the input qubits and \(R\), after tensoring with \(\mathrm{id}_R\), to density operators.

**6.5.** Show that \(\|\operatorname{Tr}_WX\|_1\le\|X\|_1\) can be strict: take \(X=|00\rangle\langle00|-|01\rangle\langle01|\) on two qubits and trace out the second.

## 7. Solutions

**6.1.** \(O_f\) maps the basis vector \(|x,b\rangle\) to the basis vector \(|x,b\oplus f(x)\rangle\), and \((b\oplus f(x))\oplus f(x)=b\). For \(f=1\) and \(m=1\), \(O_f=I\otimes X_p\), where \(X_p\) exchanges \(|0\rangle\) and \(|1\rangle\).

**6.2.** \(e^{i\varphi}U\rho\,(e^{i\varphi}U)^*=U\rho U^*\). The controlled unitaries differ by the block \(|1\rangle\langle1|\otimes(e^{i\varphi}-1)U\), which is zero only when \(e^{i\varphi}=1\).

**6.3.** \(\langle a,b\rangle=\cos t\), so \(\|aa^*-bb^*\|_1=2|\sin t|\), while \(2\|a-b\|=2\sqrt{2-2\cos t}=4|\sin(t/2)|\), which is at least \(2|\sin t|\).

**6.4.** For a density operator \(\rho\), both images are density operators, of trace norm \(1\), and Lemma 3.2(2) gives at most \(2\) for their difference.

**6.5.** The eigenvalues of \(X\) are \(1\), \(-1\), \(0\), \(0\), so \(\|X\|_1=2\), while \(\operatorname{Tr}_WX=|0\rangle\langle0|-|0\rangle\langle0|=0\).

## References

- [OpenAI-US] OpenAI, *Polynomial-Time Unitary Synthesis from a Boolean Oracle*, OpenAI Math Release preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026
- [AK] S. Aaronson and G. Kuperberg, *Quantum versus classical proofs and advice*, Theory of Computing 3 (2007), 129–157; arXiv:quant-ph/0604056, Section 7, Problem (4). https://arxiv.org/abs/quant-ph/0604056
