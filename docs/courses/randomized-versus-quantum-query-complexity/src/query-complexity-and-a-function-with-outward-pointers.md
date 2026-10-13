# Query complexity and a function with outward pointers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Boolean function of \(n\) bits can be computed by reading input bits one at a time, each choice depending on the bits read before. The least number of bits that must be read in the worst case is a measure of the difficulty of the function. It depends on the kind of algorithm: deterministic, randomized, or quantum. For functions that are defined on all inputs, the three numbers are related by polynomial inequalities, and the best known one for the randomized number \(R\) and the quantum number \(Q\) is \(R(f)\le C\,(1+Q(f))^4\). [OpenAI-Q] shows that the exponent \(4\) cannot be lowered. It constructs functions \(F_{k,m}\) with \(Q\) about \(\sqrt m\) and \(R\) about \(m^{2-1/k}\).

This lesson defines the deterministic and the randomized numbers, states the theorems of the course, and constructs the functions \(F_{k,m}\). The quantum number is defined in the next lesson.

- Decision trees, \(D(f)\) and \(R(f)\) (Section 1).
- The theorems of the course and the hypothesis (BS) (Sections 2 and 3).
- The Forrelation function and an exact circuit for it (Lemma 4.1).
- The function \(F_{k,m}\): columns, addresses, cells, pointers, winners (Section 5).
- A winner at a given address is recognized by local tests (Lemma 6.1).

The lesson follows [OpenAI-Q, Sections 1 and 2]. It needs only finite probability and matrices.

## 1. Decision trees

An *input* is a string \(x=(x_1,\dots,x_n)\in\{0,1\}^n\). A *partial Boolean function* is a function \(f:\mathcal D\to\{0,1\}\) on a subset \(\mathcal D\subseteq\{0,1\}^n\), its *domain*. It is *total* if \(\mathcal D=\{0,1\}^n\).

A *decision tree* is a finite rooted tree in which every inner vertex carries a position \(j\in\{1,\dots,n\}\) and has two children, one for each value of \(x_j\), and every leaf carries an output. On an input \(x\) the tree is followed from the root: at an inner vertex with the position \(j\) the bit \(x_j\) is read (a *query*), and the path continues to the child for this value. The output of the leaf that is reached is the output \(A(x)\) of the tree \(A\). The *depth* of the tree is the largest number of queries on a path. A decision tree is the same as a deterministic algorithm that reads bits adaptively; the outputs may be bits or elements of any set.

**Definition.** \(D(f)\) is the least depth of a decision tree \(A\) with \(A(x)=f(x)\) for all \(x\in\mathcal D\).

A *randomized algorithm of cost \(T\)* is a probability distribution on a finite set of decision trees of depth at most \(T\). On an input it draws a tree and runs it. It *computes \(f\) with error at most \(\tfrac13\)* if for every \(x\in\mathcal D\) the probability of the output \(f(x)\) is at least \(\tfrac23\).

**Definition.** \(R(f)\) is the least cost of a randomized algorithm that computes \(f\) with error at most \(\tfrac13\).

A single tree is a randomized algorithm, so \(R(f)\le D(f)\le n\). The cost is a worst case over the inputs and over the random choices. For a partial function nothing is required outside the domain.

The quantum number \(Q(f)\) is defined in [The quantum query model](the-quantum-query-model.md): the least number of queries of a quantum algorithm that computes \(f\) with error at most \(\tfrac13\) on every input of the domain.

## 2. The theorems of the course

**Theorem 2.1** (Aaronson, Ben-David, Kothari, Rao and Tal, with Huang's theorem). There is a number \(C\) such that for every \(n\) and every total function \(f:\{0,1\}^n\to\{0,1\}\),
\[
R(f)\le D(f)\le C\,(1+Q(f))^4 .
\]

It is proved in [The quartic upper bound and the optimal exponent](the-quartic-upper-bound-and-the-optimal-exponent.md), with \(C=1.5\cdot10^6\).

**Theorem 2.2** ([OpenAI-Q]). For every integer \(k\ge2\) and every power of four \(m\) there is a total Boolean function \(F_{k,m}\), defined in Section 5, with the following properties.

1. There is a number \(C_k\) with
\[
Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^4
\]
for all \(m\).
2. Assume the hypothesis (BS) of Section 3. Then for all large \(m\),
\[
\begin{gathered}
R(F_{k,m})>\Bigl\lfloor\frac{mL}{100}\Bigr\rfloor,\\
L=\Bigl\lfloor\frac{m^{1-1/k}}{(\log_2m)^2}\Bigr\rfloor .
\end{gathered}
\]

Part 1 is proved in [A tournament with probabilistic comparisons](a-tournament-with-probabilistic-comparisons.md), Part 2 in [The randomized lower bound](the-randomized-lower-bound.md). Part 1 uses no hypothesis.

**Corollary 2.3** (the optimal exponent). Assume (BS). Let \(\alpha<4\). Then there is no number \(C\) with \(R(f)\le C\,(1+Q(f))^\alpha\) for all total Boolean functions \(f\).

**Proof.** Choose \(k\ge2\) with \(2-\tfrac1k>\tfrac\alpha2\). By Theorem 2.2, for large \(m\),
\[
\frac{R(F_{k,m})}{(1+Q(F_{k,m}))^\alpha}\ge c\,\frac{m^{2-1/k-\alpha/2}}{(\log_2m)^{2+4\alpha}}
\]
with a number \(c>0\) that depends on \(k\) and \(\alpha\) only. The right side tends to infinity with \(m\). \(\blacksquare\)

So \(4\) is the least exponent for which an inequality \(R(f)\le C(1+Q(f))^\alpha\) holds for all total functions: Theorem 2.1 gives it for \(\alpha=4\), and Corollary 2.3 excludes every smaller one, under (BS). An inequality with the exponent \(3\) had been conjectured.

## 3. Forrelation and the hypothesis

Let \(m=2^\ell\). Index the coordinates of \(\mathbb R^m\) by the strings \(a\in\{0,1\}^\ell\), and let \(H\) be the matrix with the entries
\[
\begin{gathered}
H_{a,b}=m^{-1/2}(-1)^{a\cdot b},\\
a\cdot b=a_1b_1+\dots+a_\ell b_\ell .
\end{gathered}
\]
It is symmetric, and \(H^2=I\): the entry of \(H^2\) at \((a,c)\) is \(m^{-1}\sum_b(-1)^{(a+c)\cdot b}\), which is \(1\) for \(a=c\) and \(0\) otherwise. So \(H\) is an orthogonal matrix. Let \(u=m^{-1/2}(1,\dots,1)\); it is a unit vector, and \(u=He_0\) for the basis vector \(e_0\) of the string \(0\dots0\).

A string \(z\in\{0,1\}^m\) is also read as the vector of the signs \((-1)^{z_a}\); let \(D_z\) be the diagonal matrix with these signs. For \(k\ge2\) strings \(z=(z_1,\dots,z_k)\) put
\[
\Phi(z)=u^{\mathsf T}D_{z_1}HD_{z_2}H\cdots HD_{z_k}u .
\]
Since \(u\) is a unit vector and all the matrices are orthogonal, \(|\Phi|\le1\). Put \(\delta=2^{-5k}\).

**Definition.** The *Forrelation function* \(P=P_{k,m}\) is the partial Boolean function on \(km\) bits with
\[
\begin{gathered}
P(z)=1\quad\text{if }\Phi(z)\ge\delta,\\
P(z)=0\quad\text{if }|\Phi(z)|\le\delta/2,
\end{gathered}
\]
and not defined for the other inputs \(z=(z_1,\dots,z_k)\).

**Hypothesis (BS)** (Bansal and Sinha [BS, Corollary 1.4]). For every integer \(k\ge2\) there are numbers \(c_k>0\) and \(m_k\) such that for all powers of two \(m\ge m_k\),
\[
R(P_{k,m})\ge c_k\Bigl(\frac m{\log_2(km)}\Bigr)^{1-1/k}.
\]

This is a theorem of [BS], with \(c_k\) a constant times \(k^{-29}\). Its proof uses Gaussian interpolation and bounds for Fourier coefficients of decision trees, and it is not given in this course: the course uses it as a named hypothesis. The function, the normalization of \(H\) and the two thresholds \(\delta\) and \(\delta/2\) with \(\delta=2^{-5k}\) are those of [BS, (1.2), (1.3) and Theorem 1.3].

Quantum algorithms compute \(P_{k,m}\) with a number of queries that does not depend on \(m\) ([Amplitude amplification and the Forrelation test](amplitude-amplification-and-the-forrelation-test.md)). So \(P_{k,m}\) separates \(R\) from \(Q\) very strongly, but it is a partial function. The construction of Section 5 turns it into a total function and keeps a part of the separation.

## 4. An exact circuit

A *Boolean circuit* is a finite sequence of *gates*. Each gate computes a Boolean function of at most two earlier values; an earlier value is an input bit, a constant, or the value of an earlier gate. The *size* is the number of the gates. Some gates are marked as outputs.

**Lemma 4.1.** Let \(k\ge2\). There is a number \(C_k'\) such that for every power of four \(m\) there is a Boolean circuit \(C_{k,m}\) on \(km\) input bits of a size
\[
S=S_{k,m}\le C_k'\,m\,(\log_2m)^2
\]
with two output gates \(d\) and \(b\) such that on every input: \(d=1\) if and only if \(P_{k,m}\) is defined, and if \(d=1\), then \(b=P_{k,m}\).

**Proof.** *Integers.* Let \(W=\sqrt m\,H\), a matrix with the entries \(\pm1\), and let \(\mathbf 1\) be the vector of ones. Put
\[
N=z_1^{\mathsf T}\,W D_{z_2}W\cdots WD_{z_k}\mathbf 1,
\]
where \(z_1\) is read as a vector of signs. This is an integer, and
\[
\Phi=\frac NM,\qquad M=m\,(\sqrt m)^{k-1},
\]
because \(\Phi\) contains \(k-1\) factors \(H=W/\sqrt m\) and twice the factor \(m^{-1/2}\) of \(u\). Since \(m\) is a power of four, \(M\) is an integer. The two conditions of the definition of \(P\) are
\[
2^{5k}N\ge M\qquad\text{and}\qquad2^{5k+1}|N|\le M .
\]

*The computation.* Put \(y_k=D_{z_k}\mathbf 1\) and \(y_j=D_{z_j}Wy_{j+1}\) for \(j=k-1,\dots,2\); then \(N=z_1^{\mathsf T}Wy_2\). All entries of the vectors \(y_j\) and \(Wy_j\) are integers of absolute value at most \(m^k\). They and the numbers in the two comparisons are written in binary, with a sign, with \(B=\lceil k\log_2m\rceil+5k+3\) bits.

The product \(Wy\) for a vector \(y\) with \(m=2^\ell\) entries is computed in \(\ell\) rounds: by \(W_{2m'}=\begin{pmatrix}W_{m'}&W_{m'}\\W_{m'}&-W_{m'}\end{pmatrix}\), the transform of a vector \((y',y'')\) is \((W_{m'}y'+W_{m'}y'',\ W_{m'}y'-W_{m'}y'')\), so the transform of length \(2m'\) needs two transforms of length \(m'\) and \(2m'\) additions or subtractions. In all, \(Wy\) needs \(m\ell\) additions or subtractions.

*Gates.* Two integers of \(B\) bits are added or subtracted by a circuit of at most \(c_0B\) gates with two inputs each, for an absolute constant \(c_0\): one bit after the other, with a carry. The same holds for changing the sign of an integer if a given bit is \(1\), and for comparing two integers. So the \(k-1\) products with \(W\), the \(k-1\) products with the matrices \(D_{z_j}\), the sum \(z_1^{\mathsf T}(Wy_2)\) of \(m\) terms and the two comparisons need at most
\[
\begin{aligned}
&c_0B\,\bigl(k\,m\ell+k\,m+m+2\bigr)\\
&\qquad\le C_k'\,m\,(\log_2m)^2
\end{aligned}
\]
gates. Let \(b\) be the gate of the first comparison and \(d\) the gate that computes "the first or the second comparison holds". \(\blacksquare\)

The circuit does not help to compute \(P\) with few queries: it reads all its inputs. Its role is different. A list of the values of all gates, a *transcript*, can be checked gate by gate, and each check reads three bits. A correct transcript proves what the value of \(P\) is, or that \(P\) is not defined.

## 5. The function \(F_{k,m}\)

Fix \(k\ge2\) and a power of four \(m\ge4\). Put
\[
\ell=\log_2m,\qquad r=\lceil20\log_2m\rceil ,
\]
and let \(S=S_{k,m}\) be the size of the circuit of Lemma 4.1. The input of \(F_{k,m}\) consists of \(m\) *columns*. The column \(i\in\{1,\dots,m\}\) contains:

1. a string \(X_i\in\{0,1\}^m\);
2. strings \(A_{i,1},\dots,A_{i,r}\in\{0,1\}^{km}\), each an input of the Forrelation function;
3. for every *address* \(s\in\{0,1\}^r\) a *cell* \(B_{i,s}\). The cell contains, for every \(j\ne i\), a *pointer* \(p_{i,s,j}\in\{1,\dots,m\}\), written with \(\ell\) bits; and for every \(h\in\{1,\dots,r\}\) a string of \(S\) bits, the *transcript* for \(A_{i,h}\), one bit for every gate of \(C_{k,m}\).

So a column has \(n_1\) bits and the input has \(n\) bits, with
\[
\begin{gathered}
n_1=m+rkm+2^r\bigl((m-1)\ell+rS\bigr),\\
n=m\,n_1 .
\end{gathered}
\]
The number \(n\) is very large, of the order \(m^{22}\) up to logarithms, because there are \(2^r\ge m^{20}\) cells in every column.

**Definition.** The column \(i\) is a *winner* if:

1. \(X_i\) consists of ones only;
2. \(P(A_{i,h})\) is defined for every \(h\); the address \(s_i=(P(A_{i,1}),\dots,P(A_{i,r}))\) is the *true address* of the column;
3. in the cell \(B_{i,s_i}\), the transcript for every \(A_{i,h}\) is the list of the values of the gates of \(C_{k,m}\) on the input \(A_{i,h}\);
4. in the cell \(B_{i,s_i}\), every pointer points to a zero: \(X_j[p_{i,s_i,j}]=0\) for all \(j\ne i\).

\(F_{k,m}(x)=1\) if the input \(x\) has a winner, and \(F_{k,m}(x)=0\) otherwise.

Here \(X_j[p]\) is the bit of \(X_j\) at the position \(p\). The function is total: nothing is assumed about the strings \(A_{i,h}\), the pointers or the transcripts. If some \(P(A_{i,h})\) is not defined, the column \(i\) is not a winner.

**Lemma 5.1.** An input has at most one winner.

**Proof.** If \(i\) is a winner and \(j\ne i\), the pointer \(p_{i,s_i,j}\) shows a zero of \(X_j\). So \(X_j\) does not consist of ones only, and \(j\) is not a winner. \(\blacksquare\)

The pointers of a column point outward, into the other columns. A winner holds, in one cell, a proof against every other column. No cell of another column can hold a proof against the winner, because the winner's string has no zero. The quantum algorithm of the course uses this to compare two columns cheaply: a winner beats every other column in such a comparison.

The cell of the true address is one of \(2^r\) cells. To find it, the \(r\) values \(P(A_{i,h})\) must be known. A quantum algorithm computes them with few queries, if they are defined. A randomized algorithm needs more than \(L\) queries for one of them, by (BS), and cannot guess \(r\) of them.

## 6. Local tests

For a column \(i\) and an address \(s\in\{0,1\}^r\) we say that *\(i\) wins at \(s\)* if \(i\) is a winner and \(s=s_i\).

Fix \((i,s)\). Consider the following *tests*, each a condition on a few input bits:

- for every position \(j\) of \(X_i\): the bit \(X_i[j]\) is \(1\) (\(m\) tests, one query each);
- for every \(j\ne i\): the pointer \(p=p_{i,s,j}\) of the cell \(B_{i,s}\) satisfies \(X_j[p]=0\) (\(m-1\) tests, \(\ell+1\) queries each: the \(\ell\) bits of the pointer and one bit of \(X_j\));
- for every \(h\) and every gate of \(C_{k,m}\): the bit of this gate in the transcript for \(A_{i,h}\) in \(B_{i,s}\) is the value that the gate computes from its at most two earlier values, where the value of an earlier gate is read from the same transcript and an input bit is read from \(A_{i,h}\) (\(rS\) tests, at most three queries each);
- for every \(h\): the bit of the output gate \(d\) in the transcript for \(A_{i,h}\) is \(1\), and the bit of the output gate \(b\) is \(s_h\) (\(2r\) tests, one query each).

Their number is
\[
K=m+(m-1)+r(S+2),
\]
the same for all \((i,s)\), and \(K\le C_k''\,m\,(\log_2m)^3\) by Lemma 4.1.

**Lemma 6.1.** The column \(i\) wins at the address \(s\) if and only if all \(K\) tests for \((i,s)\) pass.

**Proof.** Fix \(h\). If all gate tests for \(h\) pass, then by induction along the sequence of the gates every bit of the transcript is the value of its gate on the input \(A_{i,h}\): the earlier values that the test of a gate uses are input bits or, by induction, correct values. Conversely the list of the true values passes all gate tests. So the gate tests for \(h\) pass if and only if the transcript is the true one. If it is, the two output tests say \(d=1\) and \(b=s_h\) for the true values, that is, by Lemma 4.1: \(P(A_{i,h})\) is defined and equal to \(s_h\).

So the tests of the last two kinds pass for all \(h\) if and only if \(s\) is the true address of \(i\) and the transcripts in \(B_{i,s}\) are correct. The tests of the first two kinds are the conditions 1 and 4 of a winner for the cell \(B_{i,s}\). \(\blacksquare\)

**Corollary 6.2.** \(F_{k,m}(x)=1\) if and only if there are a column \(i\) and an address \(s\) for which all tests pass. A column that is not a winner fails a test at every address.

So a proposed pair \((i,s)\) can be checked against the definition, whatever the input is. If the pair is wrong, at least one of \(K\) tests fails; to find a failing test among \(K\) is a search problem, which a quantum algorithm solves with about \(\sqrt K\) queries.

## 7. Exercises

**7.1.** Let \(\mathrm{OR}_n(x)=1\) if \(x\ne0\dots0\). Show \(D(\mathrm{OR}_n)=n\).

**7.2.** Show \(\Phi(z_1,\dots,z_k)=m^{-1/2}\) if all \(z_j\) are the string \(0\dots0\) and \(k\) is even, and compute it for odd \(k\). For which \(m\) is \(P_{2,m}(0,0)\) defined?

**7.3.** Let \(m=4\). Compute \(N\) and \(\Phi\) for \(k=2\), \(z_1=0000\), \(z_2=0110\), with the strings \(a\in\{0,1\}^2\) in the order \(00,01,10,11\).

**7.4.** Show \(n\le m^{24}\) for the number of the input bits of \(F_{k,m}\), for all large \(m\).

**7.5.** An input has the column \(1\) with \(X_1\) all ones, all \(P(A_{1,h})\) defined, a correct cell at the true address, but one pointer of this cell, for \(j=2\), points to a one of \(X_2\). The string \(X_2\) has a zero elsewhere. Is the column \(1\) a winner? Can the column \(2\) be a winner?

## 8. Solutions

**7.1.** \(D\le n\) always. Let a tree of depth less than \(n\) be given. Follow the path on which every answer is \(0\). It reads fewer than \(n\) positions, so the inputs \(0\dots0\) and the input with a single one at a position that is not read reach the same leaf. They have different values of \(\mathrm{OR}_n\).

**7.2.** For the zero strings all \(D_{z_j}=I\), so \(\Phi=u^{\mathsf T}H^{k-1}u\). For even \(k\) the power is \(H\), and \(u^{\mathsf T}Hu=u^{\mathsf T}e_0=m^{-1/2}\). For odd \(k\) the power is \(I\), and \(\Phi=1\). For \(k=2\): \(\delta=2^{-10}\); \(P\) is defined if \(m^{-1/2}\ge2^{-10}\) or \(m^{-1/2}\le2^{-11}\), that is for \(m\le2^{20}\) (value \(1\)) and for \(m\ge2^{22}\) (value \(0\)); for \(m=2^{21}\) it is not defined.

**7.3.** \(y_2=D_{z_2}\mathbf 1=(1,-1,-1,1)\). The rows of \(W\) are \((1,1,1,1)\), \((1,-1,1,-1)\), \((1,1,-1,-1)\), \((1,-1,-1,1)\), so \(Wy_2=(0,0,0,4)\). With \(z_1=(1,1,1,1)\) as signs, \(N=4\), \(M=4\cdot2=8\) and \(\Phi=\tfrac12\).

**7.4.** \(2^r<2m^{20}\), \(r\le20\ell+1\), \(S\le C_k'm\ell^2\). So \(n\le m\bigl(m+rkm+2m^{20}(m\ell+rS)\bigr)\), which is at most a constant times \(m^{22}\ell^3\), and this is below \(m^{24}\) for large \(m\).

**7.5.** The column \(1\) is not a winner: condition 4 fails for \(j=2\), although \(X_2\) has a zero. The pointer itself must show a zero. The column \(2\) is not a winner either, because \(X_2\) has a zero. So \(F_{k,m}=0\) unless another column wins, and no other column can win, because \(X_1\) has no zero to point to.

## References

- [OpenAI-Q] OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, OpenAI Math Release preprint, 5 October 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026
- [BS] N. Bansal and M. Sinha, *k-Forrelation optimally separates quantum and classical query complexity*, arXiv:2008.07003, version 3, Theorem 1.3 and Corollary 1.4. https://arxiv.org/abs/2008.07003
