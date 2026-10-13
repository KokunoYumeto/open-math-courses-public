# The quartic upper bound and the optimal exponent

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a Boolean function that is defined on all inputs, a quantum algorithm cannot be arbitrarily much faster than a deterministic one: \(D(f)\le C\,Q(f)^4\). This lesson proves it. The proof has three parts. A quantum algorithm with few queries cannot distinguish many pairs of inputs that differ in few places; this bounds two combinatorial numbers of \(f\), the block sensitivity and the largest eigenvalue of the sensitivity graph, by powers of \(Q(f)\). The degree of \(f\) as a polynomial is at most the square of that eigenvalue; this is Huang's theorem on induced subgraphs of the cube. And a deterministic algorithm needs at most block sensitivity times degree queries. With the functions \(F_{k,m}\) of the earlier lessons, the exponent \(4\) is the best possible.

- Block sensitivity, the sensitivity graph, the degree (Section 1).
- The adversary bound (Lemma 2.1) and its two consequences (Corollary 2.2).
- \(\deg(f)\le\lambda(f)^2\) (Lemma 3.2).
- \(D(f)\le\operatorname{bs}(f)\deg(f)\) (Lemma 4.1).
- \(D(f)\le1.5\cdot10^6\,Q(f)^4\) (Theorem 5.1), and the optimal exponent.

The lesson follows [OpenAI-Q, Appendix A], which gives the argument of Aaronson, Ben-David, Kothari, Rao and Tal with complete proofs. It uses query algorithms from [The quantum query model](the-quantum-query-model.md), decision trees from [Query complexity and a function with outward pointers](query-complexity-and-a-function-with-outward-pointers.md), and the eigenvalues of real symmetric matrices ([Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40), core course).

## 1. Three numbers of a Boolean function

Let \(f:\{0,1\}^n\to\{0,1\}\) be a total function. For an input \(x\) and a set \(B\subseteq\{1,\dots,n\}\) let \(x^B\) be the input \(x\) with the bits at the positions of \(B\) changed.

**Block sensitivity.** A nonempty set \(B\) is a *sensitive block at \(x\)* if \(f(x^B)\ne f(x)\). The *block sensitivity* \(\operatorname{bs}(f)\) is the largest number \(b\) such that some input has \(b\) pairwise disjoint sensitive blocks. It is \(0\) exactly for the constant functions.

**The sensitivity graph.** Its vertices are the inputs, and \(x\) and \(y\) are adjacent if they differ in exactly one position and \(f(x)\ne f(y)\). Let \(S_f\) be its adjacency matrix, a symmetric matrix with entries \(0\) and \(1\), and \(\lambda(f)=\|S_f\|\) its norm.

Here and below, \(\|M\|\) is the operator norm of a real matrix for the Euclidean norm. For a real symmetric matrix \(M\) it is the largest absolute value of an eigenvalue, and
\[
\begin{gathered}
\|M\|=\max_{\|w\|=1}|w^{\mathsf T}Mw|,\\
|w^{\mathsf T}Mw'|\le\|M\|\,\|w\|\,\|w'\| .
\end{gathered}
\]

**Lemma 1.1.** Let \(\Gamma\) be a real symmetric matrix with entries \(\ge0\). There is a unit vector \(v\) with entries \(\ge0\) and \(v^{\mathsf T}\Gamma v=\|\Gamma\|\).

**Proof.** Take a unit vector \(w\) with \(|w^{\mathsf T}\Gamma w|=\|\Gamma\|\) and let \(v\) be the vector of the absolute values of its entries. Then
\[
\begin{aligned}
\|\Gamma\|\ge v^{\mathsf T}\Gamma v&=\sum_{x,y}\Gamma_{xy}|w_x||w_y|\\
&\ge|w^{\mathsf T}\Gamma w| .
\end{aligned}
\]
\(\blacksquare\)

**The degree.** Write \(y_i=(-1)^{x_i}\) for the sign of the bit \(x_i\), and \(y_S=\prod_{i\in S}y_i\) for a set \(S\) of positions. Every real function \(g\) on \(\{0,1\}^n\) has a unique form
\[
\begin{gathered}
g=\sum_S\widehat g(S)\,y_S,\\
\widehat g(S)=2^{-n}\sum_xg(x)\,y_S(x),
\end{gathered}
\]
where \(S\) runs through all sets of positions.
Indeed, for the inner product \(\langle g,h\rangle=2^{-n}\sum_xg(x)h(x)\) the \(2^n\) functions \(y_S\) are orthonormal: \(y_Sy_T\) is the function \(y_{S\triangle T}\) of the symmetric difference, whose mean is \(0\) unless \(S=T\). So they are a basis of the space of all functions, which has the dimension \(2^n\). The *degree* of \(g\) is the largest \(|S|\) with \(\widehat g(S)\ne0\), and \(0\) for \(g=0\). For a Boolean function \(f\), \(\deg(f)\) is the degree of the function \((-1)^f\). It is \(0\) exactly for the constant functions. If some variables are fixed to values, the function of the other variables has at most the same degree: fixing \(y_i\) replaces \(y_S\) by \(\pm y_{S\setminus\{i\}}\).

## 2. The adversary bound

**Lemma 2.1** ([OpenAI-Q]; Barnum, Saks and Szegedy). Let \(f\) be a total Boolean function that is not constant. Let \(\Gamma\ne0\) be a real symmetric matrix whose rows and columns are indexed by the inputs, with entries \(\ge0\) and with \(\Gamma_{xy}=0\) whenever \(f(x)=f(y)\). For a position \(i\) let \(\Gamma_i\) be the matrix with the entries \(\Gamma_{xy}\) if \(x_i\ne y_i\), and \(0\) if \(x_i=y_i\). Then
\[
\begin{gathered}
Q(f)\ \ge\ c_0\,\frac{\|\Gamma\|}{\max_i\|\Gamma_i\|},\\
c_0=\frac{3-2\sqrt2}6 .
\end{gathered}
\]

Some \(\Gamma_i\) is not \(0\): a pair with \(\Gamma_{xy}>0\) has \(f(x)\ne f(y)\), so \(x\ne y\).

**Proof.** Let a query algorithm with \(T\) queries compute \(f\) with error at most \(\tfrac13\), with the maps \(U_0,\dots,U_T\). For an input \(x\) and \(0\le t\le T\) let
\[
\psi^t_x=U_t\,O_x\,U_{t-1}\cdots O_x\,U_0|\beta_0\rangle
\]
be the state after \(t\) queries. Let \(v\) be the vector of Lemma 1.1 for \(\Gamma\), and
\[
W_t=\sum_{x,y}v_xv_y\,\Gamma_{xy}\,\langle\psi^t_x,\psi^t_y\rangle .
\]
This number is real, because \(\Gamma\) is symmetric and \(\langle\psi_y,\psi_x\rangle\) is the complex conjugate of \(\langle\psi_x,\psi_y\rangle\).

*The start.* \(\psi^0_x=U_0|\beta_0\rangle\) does not depend on \(x\), so \(W_0=v^{\mathsf T}\Gamma v=\|\Gamma\|\).

*One query.* Since \(U_{t+1}\) is unitary, \(\langle\psi^{t+1}_x,\psi^{t+1}_y\rangle=\langle O_x\psi^t_x,O_y\psi^t_y\rangle\). Write \(\psi_x=\psi^t_x=\sum_i|i\rangle\otimes\psi_{x,i}\) with the index register in front. The query acts on \(|i\rangle\otimes\chi\) as \(|i\rangle\otimes\chi\) if \(x_i=0\), and as \(|i\rangle\otimes E\chi\) if \(x_i=1\), where \(E\) changes the bit register. \(E\) is unitary, \(E^2=I\), and \(\langle E\chi,\chi'\rangle=\langle\chi,E\chi'\rangle\). So
\[
\begin{aligned}
&\langle O_x\psi_x,O_y\psi_y\rangle-\langle\psi_x,\psi_y\rangle\\
&\quad=\sum_{i:\ x_i\ne y_i}\langle\psi_{x,i},(E-I)\psi_{y,i}\rangle ,
\end{aligned}
\]
and each term has an absolute value of at most \(2\|\psi_{x,i}\|\|\psi_{y,i}\|\). Let \(u_i\) be the vector with the entries \(v_x\|\psi_{x,i}\|\). Then
\[
\begin{aligned}
|W_{t+1}-W_t|&\le2\sum_iu_i^{\mathsf T}\Gamma_iu_i\\
&\le2\max_i\|\Gamma_i\|\sum_i\|u_i\|^2\\
&=2\max_i\|\Gamma_i\| ,
\end{aligned}
\]
because \(\sum_i\|u_i\|^2=\sum_xv_x^2\sum_i\|\psi_{x,i}\|^2\), and this is \(\sum_xv_x^2=1\).

*The end.* Let \(\Pi_1\) be the projection onto the span of the basis states with the output \(1\), and \(\Pi_0=I-\Pi_1\). Let \(f(x)=1\) and \(f(y)=0\), and \(\psi_x=\psi^T_x\), \(\psi_y=\psi^T_y\). Then \(\|\Pi_1\psi_x\|^2\ge\tfrac23\) and \(\|\Pi_1\psi_y\|^2\le\tfrac13\). Write \(\|\Pi_1\psi_x\|=\cos a\) and \(\|\Pi_1\psi_y\|=\cos a'\) with angles between \(0\) and \(\tfrac\pi2\); then \(a\le a_0\) and \(a'\ge\tfrac\pi2-a_0\), where \(\cos a_0=\sqrt{2/3}\). By the Cauchy–Schwarz inequality in the images of \(\Pi_1\) and \(\Pi_0\),
\[
\begin{aligned}
|\langle\psi_x,\psi_y\rangle|&\le\cos a\cos a'+\sin a\sin a'\\
&=\cos(a'-a)\\
&\le\cos\bigl(\tfrac\pi2-2a_0\bigr)\\
&=\sin2a_0=\frac{2\sqrt2}3 .
\end{aligned}
\]
Since \(\Gamma_{xy}=0\) for \(f(x)=f(y)\), it follows that \(|W_T|\le\tfrac{2\sqrt2}3\,v^{\mathsf T}\Gamma v=\tfrac{2\sqrt2}3\|\Gamma\|\).

*Together.*
\[
\begin{aligned}
\Bigl(1-\frac{2\sqrt2}3\Bigr)\|\Gamma\|&\le|W_0-W_T|\\
&\le2T\max_i\|\Gamma_i\| .
\end{aligned}
\]
\(\blacksquare\)

The matrix \(\Gamma\) is a weighted set of pairs of inputs with different values, which the algorithm must tell apart. At the start all states are equal; at the end the states of such a pair are far from each other. One query changes the weighted sum of the inner products by little, if no single position distinguishes much of the weight.

**Corollary 2.2.** For every total Boolean function \(f\) that is not constant,
\[
\operatorname{bs}(f)\le\frac{Q(f)^2}{c_0^2},\qquad\lambda(f)\le\frac{Q(f)}{c_0}.
\]

**Proof.** *Block sensitivity.* Let \(x\) have the pairwise disjoint sensitive blocks \(B_1,\dots,B_b\), \(b=\operatorname{bs}(f)\). Let \(\Gamma\) have the entry \(1\) at the pairs \((x,x^{B_j})\) and \((x^{B_j},x)\), and \(0\) elsewhere. For a unit vector \(w\),
\[
\begin{aligned}
w^{\mathsf T}\Gamma w&=2w_x\sum_jw_{x^{B_j}}\\
&\le2|w_x|\sqrt b\,\Bigl(\sum_jw_{x^{B_j}}^2\Bigr)^{1/2}\\
&\le\sqrt b ,
\end{aligned}
\]
with equality for a suitable \(w\); so \(\|\Gamma\|=\sqrt b\). A position \(i\) lies in at most one block, so \(\Gamma_i\) has at most two entries \(1\), at one pair and its transpose, and \(\|\Gamma_i\|\le1\). By Lemma 2.1, \(Q(f)\ge c_0\sqrt b\).

*The sensitivity graph.* Take \(\Gamma=S_f\); it is not \(0\) because \(f\) is not constant. The matrix \(\Gamma_i\) is the adjacency matrix of the edges in the direction \(i\). Every input lies on at most one of them, so \(|w^{\mathsf T}\Gamma_iw|\le\sum_{\{x,y\}}2|w_xw_y|\le\|w\|^2\), and \(\|\Gamma_i\|\le1\). By Lemma 2.1, \(Q(f)\ge c_0\lambda(f)\). \(\blacksquare\)

## 3. The degree and the sensitivity graph

Define symmetric matrices \(H'_j\) with \(2^j\) rows by
\[
\begin{gathered}
H'_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\\
H'_{j+1}=\begin{pmatrix}H'_j&I\\I&-H'_j\end{pmatrix}.
\end{gathered}
\]

**Lemma 3.1.** (1) If the rows of \(H'_j\) are indexed by \(\{0,1\}^j\) in a suitable way, the absolute values of the entries of \(H'_j\) are the entries of the adjacency matrix of the cube: \(1\) for two strings that differ in exactly one position, \(0\) otherwise.

(2) \((H'_j)^2=j\,I\).

(3) The eigenvalues of \(H'_j\) are \(\sqrt j\) and \(-\sqrt j\), each with the multiplicity \(2^{j-1}\).

**Proof.** (1) Index the first half of the rows of \(H'_{j+1}\) by the strings \((x',0)\) and the second half by the strings \((x',1)\), with \(x'\) as for \(H'_j\). The blocks \(\pm H'_j\) join strings with the same last bit that are joined for \(H'_j\); the blocks \(I\) join \((x',0)\) with \((x',1)\).

(2) By induction, with \(X=H'_j\) and \(X^2=jI\):
\[
\begin{aligned}
\begin{pmatrix}X&I\\I&-X\end{pmatrix}^2&=\begin{pmatrix}X^2+I&0\\0&I+X^2\end{pmatrix}\\
&=(j+1)\,I .
\end{aligned}
\]

(3) By (2) every eigenvalue is \(\pm\sqrt j\). The trace of \(H'_j\) is \(0\), so both occur equally often. \(\blacksquare\)

**Lemma 3.2** (Huang; in this form Aaronson, Ben-David, Kothari, Rao and Tal). For every total Boolean function \(f\),
\[
\deg(f)\le\lambda(f)^2 .
\]

**Proof.** Let \(d=\deg(f)\ge1\) and \(F=(-1)^f\). Choose a set \(S\) with \(|S|=d\) and \(\widehat F(S)\ne0\).

*Restriction.* Fix the variables outside \(S\) to any values, and let \(g\) be the resulting function of the \(d\) signs \(y_i\), \(i\in S\); its values are \(\pm1\). The coefficient of \(y_S\) in \(g\) is \(\widehat F(S)\): another term \(\widehat F(T)y_T\) of \(F\) contributes to it only if \(T\) contains \(S\) and is larger, and then \(\widehat F(T)=0\) because \(|T|>d\). So
\[
\widehat g(S)=2^{-d}\sum_yg(y)\,y_S\ne0 ,
\]
and the numbers of the \(y\) with \(g(y)=y_S\) and with \(g(y)=-y_S\) are different. Let \(\sigma\in\{1,-1\}\) be the sign for which
\[
U=\{y:\ g(y)=\sigma\,y_S\}
\]
has more than \(2^{d-1}\) elements.

*Edges inside \(U\).* If \(y,y'\in U\) differ in exactly one position, then \(y'_S=-y_S\), so \(g(y')=-g(y)\). The two inputs of \(f\) that belong to \(y\) and \(y'\) differ in one position and have different values: they are adjacent in the sensitivity graph of \(f\).

*An eigenvector.* Index the rows of \(H'_d\) by the \(y\in\{1,-1\}^S\) as in Lemma 3.1. The eigenspace of \(H'_d\) for \(\sqrt d\) has the dimension \(2^{d-1}\), and the space of the vectors that are \(0\) outside \(U\) has the dimension \(|U|>2^{d-1}\). The two dimensions add up to more than \(2^d\), so the spaces have a common vector \(w\ne0\). Then
\[
\begin{aligned}
\sqrt d\,\|w\|^2&=w^{\mathsf T}H'_dw\\
&=\sum_{y,y'\in U}(H'_d)_{yy'}\,w_yw_{y'}\\
&\le\sum_{\substack{y,y'\in U\\ \mathrm{adjacent}}}|w_y||w_{y'}| .
\end{aligned}
\]
Let \(\widetilde w\) be the vector indexed by the inputs of \(f\) that has the entry \(|w_y|\) at the input that belongs to \(y\), and \(0\) at the inputs with other values of the fixed variables. By the preceding step the last sum is at most \(\widetilde w^{\mathsf T}S_f\widetilde w\le\lambda(f)\|\widetilde w\|^2=\lambda(f)\|w\|^2\). So \(\sqrt d\le\lambda(f)\). \(\blacksquare\)

The core of the proof is a statement about the cube: a set of more than half of the vertices of the \(d\)-dimensional cube spans a subgraph whose adjacency matrix has a norm of at least \(\sqrt d\). The signs in \(H'_d\) make all eigenvalues equal to \(\pm\sqrt d\); the adjacency matrix of the cube itself has the eigenvalues \(d,d-2,\dots,-d\), which would give nothing.

## 4. A deterministic algorithm

**Lemma 4.1** (Midrijānis). For every total Boolean function \(f\),
\[
D(f)\le\operatorname{bs}(f)\,\deg(f).
\]

**Proof.** *The algorithm.* Let \(F=(-1)^f\). The algorithm works in rounds. At the beginning of a round, some positions have been read. Let \(F_\rho\) be the function of the other variables that arises from \(F\) when the read variables are fixed to the values read. If \(F_\rho\) is constant, the algorithm outputs the value of \(f\) that belongs to it. Otherwise it chooses a set \(S\) of unread positions of the largest size with a coefficient \(\ne0\) in \(F_\rho\); so \(|S|=\deg F_\rho\ge1\). It reads all positions of \(S\).

*A sensitive block in every round.* Let \(x\) be the input. Consider a round with the set \(S\). Fix, in \(F_\rho\), all unread variables outside \(S\) to their values in \(x\), and let \(g\) be the resulting function of the variables in \(S\). The coefficient of \(y_S\) in \(g\) is the coefficient of \(y_S\) in \(F_\rho\), because no set with a coefficient \(\ne0\) in \(F_\rho\) is larger than \(S\). It is not \(0\), and \(S\) is not empty, so \(g\) is not constant. So there is an assignment of the variables in \(S\) at which \(g\) differs from its value at the assignment given by \(x\). Let \(B\subseteq S\) be the set of the positions at which the two assignments differ. It is not empty, and \(f(x^B)\ne f(x)\): \(B\) is a sensitive block at \(x\).

*The count.* The sets \(S\) of different rounds are disjoint, so the blocks are pairwise disjoint sensitive blocks at \(x\). So there are at most \(\operatorname{bs}(f)\) rounds on the input \(x\). A round reads \(\deg F_\rho\le\deg F=\deg(f)\) positions. \(\blacksquare\)

## 5. The theorem

**Theorem 5.1** (Aaronson, Ben-David, Kothari, Rao and Tal). For every \(n\) and every total function \(f:\{0,1\}^n\to\{0,1\}\),
\[
\begin{aligned}
R(f)\le D(f)&\le c_0^{-4}\,Q(f)^4\\
&\le1.5\cdot10^6\,Q(f)^4 .
\end{aligned}
\]

**Proof.** For a constant function \(D(f)=0\). Let \(f\) not be constant. By Lemma 4.1, Corollary 2.2 and Lemma 3.2,
\[
\begin{aligned}
D(f)&\le\operatorname{bs}(f)\,\deg(f)\\
&\le\operatorname{bs}(f)\,\lambda(f)^2\\
&\le\frac{Q(f)^2}{c_0^2}\cdot\frac{Q(f)^2}{c_0^2}.
\end{aligned}
\]
And \(c_0^{-1}=6\,(3+2\sqrt2)<34.98\), so \(c_0^{-4}<1.5\cdot10^6\). \(\blacksquare\)

This is Theorem 2.1 of the first lesson.

**The optimal exponent.** The course has proved, for total Boolean functions:

- \(R(f)\le D(f)\le1.5\cdot10^6\,Q(f)^4\), with no hypothesis (Theorem 5.1);
- \(Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^4\), with no hypothesis (Theorem 5.1 of the lesson on the tournament);
- \(R(F_{k,m})>\lfloor mL/100\rfloor\) with \(L=\lfloor m^{1-1/k}/(\log_2m)^2\rfloor\) for large \(m\), under the hypothesis (BS) (Proposition 4.1 of the lesson on the randomized lower bound).

So, under (BS), for every \(\alpha<4\) the quotient \(R(f)/(1+Q(f))^\alpha\) is unbounded on the total Boolean functions (Corollary 2.3 of the first lesson), while \(R(f)/(1+Q(f))^4\) is bounded. The exponent \(4\) is optimal for the randomized number, and so also for the deterministic number.

**How sharp the bounds for \(F_{k,m}\) are.** By Theorem 5.1 and the lower bound, under (BS),
\[
\begin{aligned}
Q(F_{k,m})&\ge c_0\,R(F_{k,m})^{1/4}\\
&\ge c\,\frac{m^{1/2-1/(4k)}}{(\log_2m)^{1/2}}
\end{aligned}
\]
for large \(m\), with a number \(c>0\). So the quantum algorithm of the course is optimal up to the factor \(m^{1/(4k)}\) and logarithms. On the other side \(D(F_{k,m})\le2m^2\) for large \(m\) (Exercise 5.5 of the lesson on the randomized lower bound), so the randomized lower bound is optimal up to the factor \(m^{1/k}\) and logarithms.

**What remains open in the course.** The hypothesis (BS), the randomized lower bound of Bansal and Sinha for the Forrelation function, is not proved here. Everything else is proved in the six lessons from linear algebra and finite probability.

## 6. Exercises

**6.1.** Let \(\mathrm{OR}_n(x)=1\) if \(x\ne0\dots0\). Find \(\operatorname{bs}(\mathrm{OR}_n)\) and conclude \(Q(\mathrm{OR}_n)\ge c_0\sqrt n\).

**6.2.** Write down \(H'_2\) and check \((H'_2)^2=2I\).

**6.3.** Let \(f\) be the parity of \(n\) bits. Find \(\deg(f)\), \(\lambda(f)\) and \(\operatorname{bs}(f)\), and the bounds for \(Q(f)\) that Corollary 2.2 gives.

**6.4.** Let \(f(x)=x_1\wedge x_2\) on two bits. Write \((-1)^f\) as a polynomial in the signs, and follow the algorithm of Lemma 4.1.

**6.5.** Show that the statement at the end of Section 3 is sharp in the following sense: the \(d\)-dimensional cube has a set of exactly \(2^{d-1}\) vertices without any edge.

## 7. Solutions

**6.1.** At \(x=0\dots0\) every single position is a sensitive block, so \(\operatorname{bs}\ge n\); and \(n\) pairwise disjoint nonempty blocks are the largest possible number. So \(\operatorname{bs}(\mathrm{OR}_n)=n\), and \(Q\ge c_0\sqrt n\) by Corollary 2.2. Search among \(n\) positions needs about \(\sqrt n\) quantum queries; the amplification lemma of the course gives an algorithm with a constant times \(\sqrt n\) queries.

**6.2.**
\[
H'_2=\begin{pmatrix}0&1&1&0\\1&0&0&1\\1&0&0&-1\\0&1&-1&0\end{pmatrix}.
\]
The rows are orthogonal to each other, and each has the squared norm \(2\).

**6.3.** \((-1)^f=y_1\cdots y_n\), so \(\deg(f)=n\). Every edge of the cube changes \(f\), so \(S_f\) is the adjacency matrix of the cube, and \(\lambda(f)=n\) (the vector of ones is an eigenvector). Every single position is a sensitive block at every input: \(\operatorname{bs}(f)=n\). Corollary 2.2 gives \(Q(f)\ge c_0\,n\) from \(\lambda\) and \(Q(f)\ge c_0\sqrt n\) from \(\operatorname{bs}\). Lemma 3.2 says \(n\le n^2\).

**6.4.** \((-1)^f\) is \(-1\) for \(y_1=y_2=-1\) and \(1\) otherwise: \((-1)^f=\tfrac12(1+y_1+y_2-y_1y_2)\). The largest set with a coefficient \(\ne0\) is \(\{1,2\}\). The algorithm reads both bits in the first round; then the function is constant. It uses \(2\) queries; the bound of the lemma is \(\operatorname{bs}(f)\deg(f)=2\cdot2\).

**6.5.** The strings with an even number of ones: two of them differ in at least two positions.

## References

- [OpenAI-Q] OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, OpenAI Math Release preprint, 5 October 2026, Section 5 and Appendix A. https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026
- [BS] N. Bansal and M. Sinha, *k-Forrelation optimally separates quantum and classical query complexity*, arXiv:2008.07003, version 3. https://arxiv.org/abs/2008.07003
