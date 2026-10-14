# Encoders and the recursion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A matrix with few nonzero entries in each row can be applied by slots: prepare each column while keeping its input index, then erase the index, conditionally on the output row, with an amplitude that depends only on the maximal row size, and amplify the result by reflections. When the matrix is nearly isometric, all its singular directions need nearly the same amplification angle (Lemma 1.1). Applied to the field maps of the previous lesson this gives two encoders (Proposition 2.1). One call of a circuit for the smaller unitaries \(F(z)\), between the two encoders, synthesizes \(V\) (Lemma 3.1), and the recursion over the dimension gives a programmable circuit of polynomial size for every family of unitaries, with error below \(1/100\) (Proposition 4.1).

- Row-sparse nearly isometric maps (Lemma 1.1).
- The field encoders (Proposition 2.1).
- One synthesis step (Lemma 3.1).
- The recursion (Proposition 4.1).

The lesson follows [OpenAI-US, Sections 5 and 6]. It uses [Programmable slots](programmable-slots.md), [A contracting block](a-contracting-block.md) and [Fourier fields for a smaller unitary](fourier-fields-for-a-smaller-unitary.md). The reflection argument is amplitude amplification [BHMT, Section 2].

## 1. Row-sparse nearly isometric maps

Let \(\mathcal R\) be a set of *rows*, encoded in a register of \(w\) qubits, and let \(T\colon\mathbb C^d\to\mathbb C^{\mathcal R}\), with \(d\le2^n\), have the entries \(a_{ui}\). Fix an integer \(L\ge1\), and suppose that every row has at most \(L\) nonzero entries and
\[
(1-\varepsilon)I_d\le T^*T\le I_d,\qquad0\le\varepsilon<1 .
\]
These data may depend on a label register, with the same sizes and bounds for every label.

*Layout.* Extend the \(n\)-qubit input index by \(h=\lceil\log_2(L+1)\rceil\) higher bits, and add the row register and two one-qubit *flags*. Let \(\iota\) embed \(\mathbb C^d\) as the valid input indices with all new qubits zero, and let \(\jmath\) embed \(\mathbb C^{\mathcal R}\) with the extended index zero, the row in the row register, and both flags equal to one. Put \(P_0=\iota\iota^*\) and \(Q=\jmath\jmath^*\); the range of \(Q\) is the *good subspace*.

**Lemma 1.1** ([OpenAI-US, Lemma 5.1]). There is a slot circuit \(\mathsf U_T\) with
\[
\|\mathsf U_T\iota-\jmath T\|\le5\varepsilon .
\]
It uses \(O(L(n+w+h))\) slots and \(w+h+2\) fresh qubits; its skeleton depends only on the sizes, \(d\) and \(L\), and it works coherently for families indexed by labels.

*Proof.* *A block encoding.* Put
\[
\theta=\frac\pi{4L+2},\qquad t_0=\sin\theta .
\]
We first build a unitary \(\mathsf B\) with
\[
\jmath^*\mathsf B\iota=t_0T .
\]
(i) For each valid input \(i\), the column \(Te_i\) has norm at most \(1\). Conditionally on \(i\), prepare in the row register and the first flag (Lemma 2.1 of [Programmable slots](programmable-slots.md)) a unit vector whose flag-one part is \(\sum_ua_{ui}|u\rangle|1\rangle\), the remaining norm lying in the flag-zero part; the input index is not changed. (ii) For each row \(u\), choose a list \(I_u\) of exactly \(L\) distinct extended indices containing every \(i\) with \(a_{ui}\ne0\); this is possible since there are \(2^{n+h}\ge2^n(L+1)>L\) extended indices, valid or not. Conditionally on the row, apply the inverse of a state preparation of \(L^{-1/2}\sum_{i\in I_u}|i\rangle\) on the extended index register; its matrix element from \(|i\rangle\), \(i\in I_u\), to \(|0\rangle\) is \(1/\sqrt L\). (iii) Rotate the second flag from \(|0\rangle\) to a unit vector with amplitude \(t_0\sqrt L\) at \(|1\rangle\); this is possible because
\[
t_0\sqrt L\le\theta\sqrt L\le\frac{\pi\sqrt L}{4L+2}<1 .
\]
Unitary extensions for invalid indices and rows are arbitrary. Projecting onto the extended index zero and both flags one multiplies each \(a_{ui}\) by \((1/\sqrt L)\,t_0\sqrt L=t_0\), which proves the block identity.

*Amplification.* Let
\[
\mathsf U_T=\bigl[(2\mathsf BP_0\mathsf B^*-I)(I-2Q)\bigr]^L\mathsf B .
\]
Here \(2\mathsf BP_0\mathsf B^*-I=\mathsf B(2P_0-I)\mathsf B^*\), and \(2P_0-I\) and \(I-2Q\) are reflections in spans of computational basis vectors, one slot each. By Lemma 3.1 of [Oracle circuits and the synthesis theorem](oracle-circuits-and-the-synthesis-theorem.md), applied to \(T^*T\), there is an orthonormal basis \(v_j\) of \(\mathbb C^d\) with \(T^*Tv_j=\sigma_j^2v_j\), where
\[
\sqrt{1-\varepsilon}\le\sigma_j\le1 ,
\]
and the vectors \(e_j=Tv_j/\sigma_j\) are orthonormal, since \(\langle Tv_j,Tv_k\rangle=\langle v_j,T^*Tv_k\rangle\). Identify \(\mathbb C^d\) and \(\mathbb C^{\mathcal R}\) with their images under \(\iota\) and \(\jmath\). As \(Q\mathsf Bv_j=\jmath t_0Tv_j=t_0\sigma_je_j\),
\[
\begin{gathered}
\mathsf Bv_j=\sin\beta_j\,e_j+\cos\beta_j\,e_j',\\
\beta_j=\arcsin(t_0\sigma_j),
\end{gathered}
\]
with a unit vector \(e_j'\) in the kernel of \(Q\); note \(\cos\beta_j>0\). The \(e_j'\) are orthonormal: for \(j\ne k\), \(0=\langle\mathsf Bv_j,\mathsf Bv_k\rangle=\cos\beta_j\cos\beta_k\langle e_j',e_k'\rangle\). And every \(e_j'\) is orthogonal to every \(e_k\). So the planes \(\Pi_j=\operatorname{span}\{e_j,e_j'\}\) are mutually orthogonal.

The first reflection is the reflection in the range of \(\mathsf BP_0\), which is spanned by the \(\mathsf Bv_k\). The vector \(\cos\beta_j\,e_j-\sin\beta_j\,e_j'\) of \(\Pi_j\) is orthogonal to all \(\mathsf Bv_k\), so on \(\Pi_j\) this reflection fixes \(\mathsf Bv_j\) and negates the orthogonal direction. The second changes the sign of \(e_j\) and fixes \(e_j'\). Writing \(\Pi_j\ni\sin\alpha\,e_j+\cos\alpha\,e_j'\) by its angle \(\alpha\), the second reflection sends \(\alpha\) to \(-\alpha\) and the first sends \(-\alpha\) to \(2\beta_j+\alpha\). So each round adds \(2\beta_j\), and
\[
\begin{gathered}
\mathsf U_Tv_j=\sin\varphi_j\,e_j+\cos\varphi_j\,e_j',\\
\varphi_j=(2L+1)\beta_j .
\end{gathered}
\]

*The error.* As \((2L+1)\theta=\pi/2\) and \(\varphi_j\le\pi/2\), the distance from \(\mathsf U_Tv_j\) to \(e_j\) is \(2\sin\bigl((\pi/2-\varphi_j)/2\bigr)\le(2L+1)(\theta-\beta_j)\), and so
\[
\begin{aligned}
\|\mathsf U_Tv_j-\sigma_je_j\|&\le(2L+1)(\theta-\beta_j)\\
&\quad+(1-\sigma_j).
\end{aligned}
\]
Since \(t_0\le\sin(\pi/6)=1/2\), the derivative of \(\arcsin\) is at most \(2\) on \([0,t_0]\), so \(\theta-\beta_j\le2t_0(1-\sigma_j)\le2\theta(1-\sigma_j)\), and \((2L+1)\,2\theta=\pi\). With \(1-\sigma_j\le1-\sqrt{1-\varepsilon}\le\varepsilon\),
\[
\|\mathsf U_Tv_j-\sigma_je_j\|\le(\pi+1)\varepsilon\le5\varepsilon .
\]
The error vectors \(\mathsf U_Tv_j-\sigma_je_j\) lie in the mutually orthogonal planes \(\Pi_j\), so for \(x=\sum_jc_jv_j\) the error has norm at most \(5\varepsilon\|x\|\).

*Resources.* Step (i) is a state preparation on \(w+1\) qubits and step (ii) one on \(n+h\) qubits, each with additional controls; so \(\mathsf B\) takes \(O(n+w+h)\) slots. The circuit has \(2L+1\) copies of \(\mathsf B\) or \(\mathsf B^*\) and \(2L\) reflections, and the fresh qubits are the \(h\) higher index bits, the \(w\) row qubits and the two flags. All tables can be chosen for each label separately at the same positions, the labels being added to the controls; the maps are block diagonal in the labels, so the bound holds for superpositions of labels. \(\blacksquare\)

## 2. The field encoders

Apply Lemma 1.1 to the field maps of [Fourier fields for a smaller unitary](fourier-fields-for-a-smaller-unitary.md), with the notation there. A row is a frequency \(w\in\mathcal G\) and a port. Put
\[
K=b(L+1),\qquad h=\lceil\log_2(L+1)\rceil ,
\]
encode the frequency in \(K\) qubits and the port in \(n\) qubits, using the first \(k\) port states. Both field maps have this row space, so they use the same output embedding \(\jmath\): extended input index zero, both flags one, a valid port. This shared layout allows the second encoding to be reversed after the recursive call.

**Proposition 2.1** ([OpenAI-US, Proposition 5.2]). There are slot circuits \(\mathsf U_E\) and \(\mathsf U_R\) with
\[
\begin{gathered}
\|\mathsf U_E\iota-\jmath\mathcal E_L\|\le5r^{2L},\\
\|\mathsf U_R\iota-\jmath\mathcal R_L\|\le5r^{2L}.
\end{gathered}
\]
Each uses \(O(L(K+n+h)+K)\) slots and \(K+n+h+2\) fresh qubits, with a skeleton independent of \(V\), and works coherently with any further label register.

*Proof.* Write either field map in the Fourier coordinates of Section 3 of the previous lesson: the coefficient map \(T\) has at most \(L\) nonzero entries in each row by Proposition 3.2 there, and \(T^*T\) is the Gram matrix of the field map, because the Fourier basis is orthonormal, so \((1-r^{2L})I\le T^*T\le I\) by Proposition 2.1 there. Lemma 1.1 with \(w=K+n\) and \(\varepsilon=r^{2L}\) gives a circuit with error at most \(5r^{2L}\) for \(T\). Then apply the Fourier transform \(F_b\) of [Programmable slots](programmable-slots.md), Lemma 2.3, to each of the \(L+1\) factors of the frequency register; it sends \(|w\rangle\) to \(|\mathcal G|^{-1/2}\sum_z\chi_w(z)|z\rangle=|\widehat w\rangle\), so the register now holds the phase label \(z\) instead of the frequency \(w\), and the coefficient map becomes the field map. These transforms take \(O(K)\) slots, preserve the good subspace, since every frequency is allowed there and the index, flags and port are unchanged, and are unitary, so the error bound is kept. \(\blacksquare\)

## 3. One synthesis step

**Lemma 3.1** (one synthesis step; [OpenAI-US, Lemma 6.1]). Let \(V\) be a unitary on \(\mathbb C^{k+s}\) in the block form above, with \(\|D\|\le r<1\), and use the fields and encoders with truncation length \(L\). Suppose that a slot circuit \(\mathsf C\) solves the controlled task of the family \(F(z)\) of \(k\)-dimensional unitaries, with the phase label \(z\) as label, with clean-workspace error \(\delta'\). Then \(\mathsf U_R^*\,\mathsf C\,\mathsf U_E\) implements \(V\) with clean-workspace error at most
\[
\delta'+\frac{2r^L}{1-r}+10r^{2L}.
\]
The same holds coherently for a family \(V_\lambda\), with \(\mathsf C\) controlled by \(\lambda\) and \(z\).

*Proof.* Let \(\iota\) embed the input space into the whole layout with all working qubits zero, including the fresh workspace of \(\mathsf C\), and let \(\jmath\) embed \(\mathbb C^{\mathcal G}\otimes\mathbb C^k\) into the good subspace, again with the workspace of \(\mathsf C\) zero. The circuit \(\mathsf C\) acts on the port register, the phase register and its own workspace, and as the identity elsewhere; in the good subspace the port is valid, so its guarantee gives
\[
\|\mathsf C\jmath-\jmath\widetilde F\|\le\delta' .
\]
Put \(\tau=r^L/(1-r)\). The field maps are contractions with \(\|\widetilde F\mathcal E_L-\mathcal R_LV\|\le2\tau\) (Proposition 2.1 of the previous lesson), and the encoders satisfy the bounds of Proposition 2.1. So
\[
\begin{aligned}
&\|\mathsf C\mathsf U_E\iota-\mathsf U_R\iota V\|\\
&\quad\le\|\mathsf C(\mathsf U_E\iota-\jmath\mathcal E_L)\|\\
&\qquad+\|(\mathsf C\jmath-\jmath\widetilde F)\mathcal E_L\|\\
&\qquad+\|\jmath(\widetilde F\mathcal E_L-\mathcal R_LV)\|\\
&\qquad+\|(\jmath\mathcal R_L-\mathsf U_R\iota)V\|\\
&\quad\le5r^{2L}+\delta'+2\tau+5r^{2L}.
\end{aligned}
\]
Multiplying by the unitary \(\mathsf U_R^*\) gives the claim. The guarantee of \(\mathsf C\) is used only on the ideal encoded state \(\jmath\mathcal E_Lx\), of norm at most \(\|x\|\); the part of the actual encoded state outside the good subspace is in the first error term and is not enlarged by the unitary \(\mathsf C\). For labels \(\lambda\), all maps are block diagonal in the label basis, and the bounds are uniform in \(\lambda\). \(\blacksquare\)

The amplification inside \(\mathsf U_E\) and \(\mathsf U_R\) repeats only their own state preparations, never \(\mathsf C\): the smaller circuit is called once.

## 4. The recursion

Keep \(M\), \(r=3/4\) and \(J=8M(n+1)\) from [A contracting block](a-contracting-block.md), and put
\[
\begin{gathered}
L=10000J,\qquad K=b(L+1),\\
b=nL+\lceil\log_2(L+1)\rceil .
\end{gathered}
\]

**Proposition 4.1** (uniform programmable synthesis; [OpenAI-US, Proposition 6.2]). Let \(n\ge1\), \(1\le d\le2^n\) and \(t\ge0\). There is a skeleton, determined by \(n\), \(d\) and \(t\), with the following property: for every family \((U_\lambda)_{\lambda\in\{0,1\}^t}\) of unitaries on \(\mathcal H_d\), some choice of tables solves its controlled task with clean-workspace error less than \(1/100\). The skeleton has \(t+O((n+1)^{10})\) qubits and \(O((n+1)^{13})\) slots, and it is generated, with the ordered control list of every slot, by a deterministic algorithm in time polynomial in \(n+t\).

*Proof.* *The construction*, by recursion on \(d\), with \(n\)-qubit index and port registers at every level. If \(d=1\), each \(U_\lambda\) is a scalar \(e^{i\varphi_\lambda}\) on \(\mathcal H_1=\operatorname{span}\{|0\rangle\}\), applied exactly by one slot with an index qubit as target, which is zero on the valid input, and the labels as controls. If \(d\ge2\), Proposition 2.1 of [A contracting block](a-contracting-block.md) gives \(V_\lambda=P_{\mathrm L,\lambda}U_\lambda P_{\mathrm R,\lambda}\) with internal order \(s\), port order \(k=d-s\) and \(\|D_\lambda\|\le r\). Apply Lemma 3.1, taking for \(\mathsf C\) the circuit of order \(k\) given by the recursion for the family \(F_\lambda(z)\), with the labels \((\lambda,z)\) and fresh workspace. To implement \(U_\lambda=P_{\mathrm L,\lambda}^*V_\lambda P_{\mathrm R,\lambda}^*\), apply \(P_{\mathrm R,\lambda}^*\) first and \(P_{\mathrm L,\lambda}^*\) last; they are exact slot circuits and add no error.

*The error.* At each level Lemma 3.1 adds at most
\[
\frac{2r^L}{1-r}+10r^{2L}=8r^L+10r^{2L}\le18r^L
\]
to the error of the smaller circuit. There are fewer than \(J\) levels (Lemma 2.2 of [A contracting block](a-contracting-block.md)). Bernoulli's inequality gives \((4/3)^L\ge1+L/3\), hence \(r^L\le3/L\), and the total error is at most
\[
18Jr^L\le\frac{54J}L=\frac{54}{10000}<\frac1{100}.
\]
In particular all working qubits, also those of the inner levels, return to zero in the ideal comparison map.

*Resources.* Write \(N=n+1\). Then \(J,L=O(N^3)\), \(b=O(N^4)\), \(K=O(N^7)\) and \(h=O(N)\). A pair of encoders uses \(O(K+n+h)\) fresh qubits and \(O(L(K+n+h)+K)\) slots; the pre- and post-processing \(P_{\mathrm R}^*\), \(P_{\mathrm L}^*\) adds \(O(n)\) qubits and slots. All registers of an outer level stay allocated during the inner call, including the phase labels, so over the fewer than \(J\) levels there are
\[
t+O(J(K+n+h))=t+O(N^{10})
\]
qubits and
\[
\begin{aligned}
&O\bigl(J[L(K+n+h)+K+n]\bigr)\\
&\quad=O(N^{13})
\end{aligned}
\]
slots. These sums are enough because each level calls the next one only once.

*Uniformity.* The skeleton is generated without computing any table. The successive orders \(d\), \(q\), \(s\), \(k\) have \(O(n)\)-bit descriptions and are computed in polynomial time; the register layout, the order of the state preparations, the Fourier transforms, the reflections and the \(L\) amplification rounds depend only on these numbers. Everything that depends on \(U_\lambda\) (the signs, the permutations, the amplitudes of the state preparations, the lists \(I_u\) and the recursively prescribed unitaries) changes only tables. A control list has at most \(t+O(N^{10})\) entries, so writing the lists of all \(O(N^{13})\) slots takes polynomial time in \(n+t\). \(\blacksquare\)

## 5. Exercises

**5.1.** In Lemma 1.1 with \(L=1\), compute \(\theta\), \(t_0\) and the amplification angle, and check that one round sends the angle \(\beta\) of a direction with \(\sigma=1\) to \(\pi/2\).

**5.2.** Show that \(2\sin(x/2)\le x\) for \(x\ge0\), as used for the distance on the unit circle.

**5.3.** Where would the proof of Lemma 1.1 fail if the rows of \(T\) had more than \(L\) nonzero entries?

**5.4.** Check the arithmetic of the error bound: \(8r^L+10r^{2L}\le18r^L\) and \(18J\cdot3/(10000J)<1/100\).

**5.5.** Why may the label register grow by \(K\) qubits at every level without destroying the polynomial bounds?

## 6. Solutions

**5.1.** \(\theta=\pi/6\), \(t_0=1/2\); for \(\sigma=1\), \(\beta=\arcsin(1/2)=\pi/6\), and one round gives \(3\beta=\pi/2\): the vector is exactly \(e_j\).

**5.2.** The function \(x-2\sin(x/2)\) vanishes at \(0\) and has derivative \(1-\cos(x/2)\ge0\).

**5.3.** In step (ii) a row \(u\) needs a list \(I_u\) of \(L\) indices containing all \(i\) with \(a_{ui}\ne0\); with more than \(L\) of them the amplitude \(1/\sqrt L\) of the inverse state preparation cannot reach all columns of the row, and a smaller amplitude would change \(t_0\) row by row.

**5.4.** \(r^{2L}\le r^L\), and \(18\cdot3/10000=0.0054<0.01\).

**5.5.** There are fewer than \(J=O(N^3)\) levels, each adding \(K=O(N^7)\) label qubits, so the labels add \(O(N^{10})\) qubits in all, and the control lists stay of polynomial length.

## References

- [OpenAI-US] OpenAI, *Polynomial-Time Unitary Synthesis from a Boolean Oracle*, OpenAI Math Release preprint, 5 October 2026, Sections 5 and 6. https://github.com/openai/math/tree/main/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026
- [BHMT] G. Brassard, P. Høyer, M. Mosca and A. Tapp, *Quantum amplitude amplification and estimation*, arXiv:quant-ph/0005055. https://arxiv.org/abs/quant-ph/0005055
