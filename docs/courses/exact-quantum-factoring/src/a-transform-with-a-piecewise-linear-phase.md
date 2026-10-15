# A transform with a piecewise-linear phase

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Order finding in Shor's algorithm prepares the superposition \(\sum_x|x\rangle|a^x\bmod m\rangle\) and applies the quantum Fourier transform modulo a power of two \(Q\), whose matrix entries \(Q^{-1/2}e^{-2\pi ikx/Q}\) involve phases that the gate set \(\mathcal G\) of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md) cannot produce exactly [Shor 1997]. This lesson replaces the exponential by its piecewise-linear interpolation \(g\) at the quarter-integers. A circuit over \(\mathcal G\) realizes the matrix \(Q^{-1/2}g(kx/Q)\) on a designated success outcome, by controlled shifts of an auxiliary register in the manner of the phase kickback of Cleve, Ekert, Macchiavello and Mosca [CEMM 1998]; the auxiliary register is not an eigenvector of the shifts, and the success test is part of the probability. The outputs are then decoded into fractions by continued fractions, and the probabilities of order sampling become explicit sums [OpenAI-EQF, Section 3].

- The interpolated exponential and the phase register (Sections 1 and 2).
- The transform (Section 3).
- Continued fractions and the recovery of fractions (Section 4).
- Order sampling with the transform (Section 5).

Throughout, \(n\ge128\) is an integer, \(B=2^n\), and
\[
Q=B^{16}=2^b,\qquad b=16n .
\]

## 1. The interpolated exponential

Let \(g\colon\mathbb R\to\mathbb C\) be the continuous function of period one obtained by linear interpolation of \(e^{-2\pi iz}\) at the quarter-integers: for \(q\in\mathbb Z\) and \(0\le t\le1\),
\[
\begin{aligned}g\Bigl(\frac{q+t}4\Bigr)&=(1-t)(-i)^q\\&\quad+t(-i)^{q+1}.\end{aligned}\tag{1.1}
\]
The two descriptions of a quarter-integer \((q+1)/4\) give the same value, so \(g\) is well defined, and \(g(q/4)=(-i)^q=e^{-2\pi iq/4}\).

**Lemma 1.1.** \(|g(z)|\le1\) and \(g(z+\frac12)=-g(z)\) for every real \(z\).

*Proof.* By (1.1), \(g(z)\) is a convex combination of two numbers of modulus one. Adding \(\frac12\) to \(z\) adds \(2\) to \(q\) in (1.1), and \((-i)^{q+2}=-(-i)^q\). \(\square\)

## 2. The phase register

Let a register of \(b\) qubits hold \(y\in\{0,\ldots,Q-1\}\), with \(y_{b-1}\) the most significant bit, and put
\[
|\chi\rangle=Q^{-1/2}\sum_{y=0}^{Q-1}i^{\lfloor4y/Q\rfloor}|y\rangle .
\]
Since \(\lfloor4y/Q\rfloor=2y_{b-1}+y_{b-2}\), this state is prepared from \(|0\rangle\) by Hadamard gates on all \(b\) qubits, followed by \(S^2\) on the most significant qubit and \(S\) on the next one. For \(D\in\mathbb Z\) let \(T_D\) be the shift \(|y\rangle\mapsto|y+D\bmod Q\rangle\).

**Lemma 2.1** ([OpenAI-EQF, Lemma 3.2]). For every integer \(D\), \(\langle\chi|T_D|\chi\rangle=g(D/Q)\).

*Proof.* Write \(D\equiv qQ/4+s\pmod Q\) with \(0\le q<4\) and \(0\le s<Q/4\), and \(y=cQ/4+u\) with \(0\le c<4\) and \(0\le u<Q/4\). The coefficient of \(|y\rangle\) in \(T_D|\chi\rangle\) is the coefficient of \(|y-D\bmod Q\rangle\) in \(|\chi\rangle\). Equivalently,
\[
\begin{aligned}&\langle\chi|T_D|\chi\rangle\\&\quad=\frac1Q\sum_{y}i^{\lfloor4y/Q\rfloor-\lfloor4((y+D)\bmod Q)/Q\rfloor}.\end{aligned}
\]
The point \(y+D\) lies \(q\) quarter-bins after \(y\) when \(u+s<Q/4\), and \(q+1\) bins after it otherwise; for each \(c\) the second case occurs for exactly \(s\) values of \(u\). So a fraction \(1-4s/Q\) of the terms equals \(i^{-q}=(-i)^q\) and a fraction \(4s/Q\) equals \((-i)^{q+1}\). By (1.1) with \(t=4s/Q\), the average is \(g\bigl((q+4s/Q)/4\bigr)=g(D/Q)\), using the periodicity of \(g\). \(\square\)

For instance, a shift by \(Q/4\) has overlap \(g(\tfrac14)=-i\).

## 3. The transform

Write the input and the output of a \(b\)-qubit data register in binary, from the units bit: \(x=\sum_{i=0}^{b-1}2^ix_i\) and \(k=\sum_{j=0}^{b-1}2^jk_j\).

**Lemma 3.1** (the transform; [OpenAI-EQF, Lemma 3.2]). There is a circuit over \(\mathcal G\), of size polynomial in \(b\), acting on the data register and on auxiliary qubits initially zero, with a designated success outcome of the auxiliary qubits, whose matrix on that outcome is
\[
\begin{gathered}A_{k,x}=Q^{-1/2}\,g(kx/Q)\\ (0\le x,k<Q).\end{gathered}
\]

*Proof.* Prepare the phase register in \(|\chi\rangle\). For \(j=0,1,\ldots,b-1\) in turn: apply a Hadamard gate to the qubit that holds \(x_{b-1-j}\), and call its new value \(k_j\); then, for every \(i<b-1-j\), apply the shift \(T_{2^{i+j}}\) to the phase register, controlled by the two qubits holding \(x_i\) and \(k_j\). The qubit of \(x_i\) has not yet been transformed, because its Hadamard gate comes at the later step \(b-1-i>j\). Finally undo the preparation of \(|\chi\rangle\), and designate the all-zero outcome of the phase register as success. The output bits \(k_j\) stand in reversed order on the qubits; relabeling the wires puts them in order.

Fix a basis input \(x\) and an output \(k\). Each data qubit has a definite value before and after its single Hadamard gate, and the product of the Hadamard matrix entries is \(Q^{-1/2}(-1)^h\), where
\[
\begin{gathered}h=\sum_{i+j=b-1}x_ik_j,\\ D=\sum_{i+j<b-1}2^{i+j}x_ik_j .\end{gathered}
\]
On this branch the controlled shifts compose to \(T_D\), since all shifts commute. By linearity the amplitude of output \(k\) and success is \(Q^{-1/2}(-1)^h\langle\chi|T_D|\chi\rangle\), which equals \(Q^{-1/2}(-1)^hg(D/Q)\) by Lemma 2.1. In the product \(xk=\sum_{i,j}2^{i+j}x_ik_j\), the terms with \(i+j\ge b\) are multiples of \(Q\), and those with \(i+j=b-1\) give \(2^{b-1}h=(Q/2)h\). So \(xk\equiv D+(Q/2)h\pmod Q\), and Lemma 1.1 gives \(g(xk/Q)=(-1)^hg(D/Q)\).

There are \(O(b^2)\) controlled shifts, each a reversible addition of a constant modulo \(Q\) controlled by two qubits, of size polynomial in \(b\) (Lemma 2.3(2) and (3) of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md)). \(\square\)

The success outcome is a test of the auxiliary register, not an instruction to force it: the circuit is unitary, and the probability of success, with any output, is the squared norm of the corresponding part of the state. Since \(|g|\le1\), every column of \(A\) has squared norm at most one.

## 4. Continued fractions and the recovery of fractions

Let \(0\le\alpha<1\) be rational. Its *continued fraction* is computed by \(\alpha_0=\alpha\) and \(c_i=\lfloor\alpha_i\rfloor\), with \(\alpha_{i+1}=1/(\alpha_i-c_i)\) as long as \(\alpha_i\ne c_i\). The denominators of the \(\alpha_i\) decrease strictly, so the process stops at some \(\alpha_\ell=c_\ell\); and \(c_0=0\), \(c_i\ge1\) for \(i\ge1\). The *convergents* \(p_i/v_i\) are given by
\[
\begin{gathered}(p_{-1},v_{-1})=(1,0),\quad(p_0,v_0)=(c_0,1),\\ p_i=c_ip_{i-1}+p_{i-2},\\ v_i=c_iv_{i-1}+v_{i-2}.\end{gathered}
\]

**Lemma 4.1.** For \(0\le i\le\ell\):

1. \(p_iv_{i-1}-p_{i-1}v_i=(-1)^{i-1}\); in particular \(p_i/v_i\) is in lowest terms.
2. \(1=v_0\le v_1<v_2<\cdots<v_\ell\).
3. If \(i<\ell\), then \(\alpha=\frac{p_i\alpha_{i+1}+p_{i-1}}{v_i\alpha_{i+1}+v_{i-1}}\) and
\[
\begin{aligned}\Bigl|\alpha-\frac{p_i}{v_i}\Bigr|&=\frac1{v_i\,(v_i\alpha_{i+1}+v_{i-1})}\\&\le\frac1{v_iv_{i+1}} ;\end{aligned}
\]
and \(\alpha=p_\ell/v_\ell\).

*Proof.* (1) For \(i=0\) the expression is \(c_0\cdot0-1\cdot1=-1\); the recurrences show that \(p_iv_{i-1}-p_{i-1}v_i\) is \(-(p_{i-1}v_{i-2}-p_{i-2}v_{i-1})\). (2) \(v_1=c_1\ge1\), and \(v_i=c_iv_{i-1}+v_{i-2}>v_{i-1}\) for \(i\ge2\). (3) Put \(F_i(\theta)=(p_i\theta+p_{i-1})/(v_i\theta+v_{i-1})\) for \(\theta>0\). Then \(F_0(\theta)=c_0+1/\theta\), and the recurrences give \(F_i(\theta)=F_{i-1}(c_i+1/\theta)\) for \(i\ge1\). As \(\alpha_0=c_0+1/\alpha_1\) and \(\alpha_i=c_i+1/\alpha_{i+1}\), induction on \(i\) gives \(\alpha=F_i(\alpha_{i+1})\) for \(i<\ell\). Subtracting \(p_i/v_i\) and using (1) gives the error, and \(v_i\alpha_{i+1}+v_{i-1}\ge v_ic_{i+1}+v_{i-1}=v_{i+1}\). Finally \(\alpha=F_{\ell-1}(\alpha_\ell)=F_{\ell-1}(c_\ell)=p_\ell/v_\ell\) when \(\ell\ge1\), and \(\alpha=c_0=p_0/v_0\) when \(\ell=0\). \(\square\)

For every reduced fraction \(j/d\) with \(0\le j<d<B\), define its *bin*
\[
\begin{gathered}k(d,j)=\Bigl\lfloor\frac{jQ}d+\frac12\Bigr\rfloor,\\ \eta=k(d,j)-\frac{jQ}d ,\end{gathered}\tag{4.1}
\]
so that \(|\eta|\le\frac12\) and \(0\le k(d,j)<Q\). We call \((d,j)\) the *label* of the bin.

**Lemma 4.2** (recovering labels; [OpenAI-EQF, Lemma 3.3]). Given \(0\le k<Q\), one decides in time polynomial in \(n\) whether \(k=k(d,j)\) for a reduced fraction \(0\le j<d<B\), and finds \((d,j)\) when it exists. Such a label is unique.

*Proof.* Compute the continued fraction of \(k/Q\), and let \(p/v\) be its last convergent with \(v<B\); it exists because \(v_0=1\). Then
\[
\Bigl|\frac kQ-\frac pv\Bigr|\le\frac1{vB} :
\]
if \(p/v\) is the last convergent, the difference is zero; otherwise the next denominator is at least \(B\), and Lemma 4.1(3) applies. Suppose that \(k=k(d,j)\) for a reduced \(j/d\) with \(d<B\), but \(j/d\ne p/v\). Then \(|jv-pd|\ge1\), so
\[
\begin{aligned}\Bigl|\frac jd-\frac pv\Bigr|&\ge\frac1{dv}\ge\frac1{(B-1)v}\\&>\frac1{vB}+\frac1{2Q},\end{aligned}
\]
where the last step amounts to \(2Q>vB(B-1)\), true because \(v<B\) and \(Q=B^{16}\). On the other hand \(|k/Q-j/d|\le1/(2Q)\) by (4.1), and the triangle inequality gives \(|j/d-p/v|\le1/(2Q)+1/(vB)\), a contradiction. Hence \(j/d=p/v\), and as both are in lowest terms, \((d,j)=(v,p)\). The algorithm checks \(0\le p<v<B\) and \(k=k(v,p)\); it accepts exactly the valid labels, and the argument proves their uniqueness. For \(k=0\) the expansion stops at once with the convergent \(0/1\), which covers \(d=1\). The Euclidean algorithm and the checks use integers of \(O(n)\) bits. \(\square\)

## 5. Order sampling with the transform

Let \(2\le m<B\) and let \(a\) be a unit modulo \(m\) of multiplicative order \(r\), the least \(r\ge1\) with \(a^r\equiv1\pmod m\). Hadamard gates on the \(b\) data qubits and reversible modular powering prepare
\[
Q^{-1/2}\sum_{x=0}^{Q-1}|x\rangle\,|a^x\bmod m\rangle ,
\]
with the work of the powering returned to zero. Apply the transform of Lemma 3.1 to the data register. For a reduced label \((d,j)\) and \(0\le t<d\), let \(X_t\) be the set of \(0\le x<Q\) with \(x\equiv t\pmod d\), and define, with \(k=k(d,j)\),
\[
\begin{aligned}&P(d,j,t)\\&\quad=\Bigl|\frac1Q\sum_{x\in X_t}g(kx/Q)\Bigr|^2 .\end{aligned}\tag{5.1}
\]

**Proposition 5.1** ([OpenAI-EQF, Section 3]). For every reduced label \((r,j)\) with denominator the order \(r\),
\[
\begin{aligned}&\Pr\bigl(\text{success and output }k=k(r,j)\bigr)\\&\quad=\sum_{t=0}^{r-1}P(r,j,t).\end{aligned}
\]

*Proof.* On success with output \(k\), the second register is in the unnormalized state
\[
\frac1Q\sum_{x=0}^{Q-1}g(kx/Q)\,|a^x\bmod m\rangle .
\]
The value \(a^x\bmod m\) depends only on \(x\bmod r\), and different residues modulo \(r\) give different values, hence orthogonal basis states. The squared norm is therefore \(\sum_{t<r}\bigl|Q^{-1}\sum_{x\equiv t}g(kx/Q)\bigr|^2\), which for \(k=k(r,j)\) is the stated sum. \(\square\)

The quantity \(P(d,j,t)\) in (5.1) is defined for every reduced label, but only at \(d=r\) is it related to a probability. The next lesson computes these quantities exactly and corrects them with classical coins, without knowing \(r\).

## 6. Exercises

**6.1.** Compute \(g(\frac18)\) and compare it with \(e^{-2\pi i/8}\).

**6.2.** Verify that the preparation described in Section 2 produces \(|\chi\rangle\), and compute \(\langle\chi|T_{Q/2}|\chi\rangle\) directly.

**6.3.** Compute the continued fraction and the convergents of \(\frac7{16}\).

**6.4.** Show that \(\sum_kQ^{-1}|g(kx/Q)|^2\le1\) for every \(x\), and explain why the transform of Lemma 3.1 is not unitary on the data register.

**6.5.** Let \(B=8\) and \(Q=2^{12}\) (a smaller value than in the lesson, for computation by hand). Find the bin of \(\frac35\), and check that the continued fraction of \(k/Q\) recovers \(\frac35\).

## 7. Solutions

**6.1.** With \(q=0\) and \(t=\frac12\) in (1.1), \(g(\frac18)=\frac12(1-i)\), of modulus \(1/\sqrt2\), whereas \(e^{-2\pi i/8}=(1-i)/\sqrt2\) has modulus one.

**6.2.** After the Hadamard gates every \(|y\rangle\) has amplitude \(Q^{-1/2}\); \(S^2\) multiplies it by \((-1)^{y_{b-1}}=i^{2y_{b-1}}\) and \(S\) by \(i^{y_{b-2}}\). The shift by \(Q/2\) moves every \(y\) two bins on, so each term of the sum in the proof of Lemma 2.1 is \(i^{-2}=-1\), and the overlap is \(-1=g(\frac12)\).

**6.3.** \(\alpha_0=\frac7{16}\), \(c_0=0\); \(\alpha_1=\frac{16}7\), \(c_1=2\); \(\alpha_2=\frac72\), \(c_2=3\); \(\alpha_3=2=c_3\). The convergents are \(\frac01,\frac12,\frac37,\frac7{16}\).

**6.4.** Each term is at most \(Q^{-1}\), and there are \(Q\) values of \(k\). The columns of \(A\) are not unit vectors (for \(x\) with \(kx/Q\) away from the quarter-integers, \(|g|<1\)), so \(A\) is not unitary; it is the part of a unitary circuit on the success outcome.

**6.5.** \(jQ/d=3\cdot4096/5=2457.6\), so \(k=\lfloor2458.1\rfloor=2458\). The fraction \(\frac{2458}{4096}=\frac{1229}{2048}\) has the partial quotients \(0,1,1,1,1,409\) and the convergents \(\frac01,\frac11,\frac12,\frac23,\frac35,\frac{1229}{2048}\). The last convergent with denominator less than \(8\) is \(\frac35\), and \(k(5,3)=2458\) passes the check.

## References

- [OpenAI-EQF] OpenAI, *Exact quantum factoring over a fixed finite gate set*, OpenAI Math Release preprint, 25 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026
- [Shor 1997] P. W. Shor, *Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer*, SIAM J. Comput. 26 (1997), no. 5, 1484–1509. https://arxiv.org/abs/quant-ph/9508027
- [CEMM 1998] R. Cleve, A. Ekert, C. Macchiavello, M. Mosca, *Quantum algorithms revisited*, Proc. R. Soc. Lond. A 454 (1998), no. 1969, 339–354. https://arxiv.org/abs/quant-ph/9708016
