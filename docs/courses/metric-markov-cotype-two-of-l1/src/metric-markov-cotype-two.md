# Metric Markov cotype two

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Attach points \(x_1,\dots,x_n\) of a metric space to the states of a Markov chain. Can the points be moved a little so that states that follow each other in the chain carry points that are close together? *Metric Markov cotype two* is a quantitative form of this question: the cost of moving the points, plus \(t\) times the one-step variation of the new points, is to be bounded by a constant times the variation of the old points over the times \(1,\dots,t\). The notion goes back to Ball; the form used here is due to Mendel and Naor [MN, Definition 1.2]. They asked whether the sequence space \(\ell_1\) has this property [MN, Question 1.15]. [OpenAI-MC] proves that it does, with the constant \(12\sqrt{21}\). This course gives the proof.

This lesson gives the definition, examples, and two general facts. In a Hilbert space the averages of the points along the chain can be taken as the new points (Proposition 3.4). In every metric space the average over the times \(1,\dots,t\) can be replaced by an average over a geometric random time with mean \(t\) (Proposition 4.3).

- Stochastic matrices, stationary and reversible vectors, the energy of a family of points (Section 1).
- The definition, two examples, the statement of the theorem (Section 2).
- Hilbert space has metric Markov cotype two with the constant \(\sqrt5\) (Proposition 3.4).
- Geometric and Cesàro averages (Proposition 4.3).

The lesson follows [OpenAI-MC, Sections 1 and 4]. Section 3 is not taken from that text. The lesson uses finite sums, the Cauchy–Schwarz inequality and the geometric series; Section 3 uses the spectral theorem for symmetric matrices (core course [Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40)).

## 1. Stationary and reversible matrices

Let \(n\ge1\) and \([n]=\{1,\dots,n\}\). A *probability vector* is a vector \(\pi=(\pi_i)_{i\in[n]}\) with \(\pi_i\ge0\) and \(\sum_i\pi_i=1\); entries equal to \(0\) are allowed. A *stochastic matrix* is a matrix \(A=(a_{ij})_{i,j\in[n]}\) with \(a_{ij}\ge0\) and \(\sum_ja_{ij}=1\) for every \(i\).

**Definition.** Let \(A\) be a stochastic matrix and \(\pi\) a probability vector. The vector \(\pi\) is *stationary* for \(A\) if
\[
\sum_i\pi_ia_{ij}=\pi_j\qquad\text{for all }j .
\]
The matrix \(A\) is *reversible* for \(\pi\) if
\[
\pi_ia_{ij}=\pi_ja_{ji}\qquad\text{for all }i,j .
\]

Summing the second condition over \(i\) gives the first: if \(A\) is reversible for \(\pi\), then \(\pi\) is stationary for \(A\). The converse is false. For \(n=3\) let \(A\) send \(1\) to \(2\), \(2\) to \(3\) and \(3\) to \(1\), each with probability \(1\). The uniform vector is stationary, and \(\pi_1a_{12}=\tfrac13\) while \(\pi_2a_{21}=0\).

For a stochastic matrix \(A\) and \(t\ge1\) put
\[
M_t=\frac1t\sum_{s=1}^tA^s ,
\]
the *Cesàro average* of the powers of \(A\). For \(0<q<1\) put
\[
G=(1-q)\sum_{s=0}^\infty q^sA^s ,
\]
with \(A^0=I\), the *geometric average* with the ratio \(q\). The series converges in every entry, because the entries of \(A^s\) lie in \([0,1]\) (they are entries of a stochastic matrix, by the next lemma).

**Lemma 1.1.** Let \(A\) and \(A'\) be stochastic matrices and let \(\pi\) be stationary for both.

1. The product \(AA'\) is stochastic and \(\pi\) is stationary for it. The same holds for every power \(A^s\), for \(M_t\) and for \(G\).
2. If \(A\) is reversible for \(\pi\), then so are \(A^s\), \(M_t\) and \(G\).
3. \(G=(1-q)I+qAG\).

**Proof.** *Part 1.* The entries of \(AA'\) are \(\ge0\), and \(\sum_j\sum_ka_{ik}a'_{kj}=\sum_ka_{ik}=1\). Further \(\sum_i\pi_i(AA')_{ij}=\sum_k\pi_ka'_{kj}=\pi_j\). By induction the powers are stochastic with the stationary vector \(\pi\). Both properties are kept by averages with nonnegative weights of sum \(1\), finite or infinite; the weights of \(G\) are \((1-q)q^s\), with the sum \(1\).

*Part 2.* Assume \(\pi_i(A^s)_{ij}=\pi_j(A^s)_{ji}\) for all \(i,j\). Then
\[
\begin{aligned}
\pi_i(A^{s+1})_{ij}&=\sum_k\pi_i(A^s)_{ik}a_{kj}\\
&=\sum_k(A^s)_{ki}\,\pi_ka_{kj}\\
&=\sum_k(A^s)_{ki}\,\pi_ja_{jk}\\
&=\pi_j(A^{s+1})_{ji} ,
\end{aligned}
\]
where the last step uses \(A^{s+1}=A\,A^s\). The condition is linear in the matrix, so it passes to \(M_t\) and \(G\).

*Part 3.* The matrix \(qAG\) is \((1-q)\sum_{s\ge1}q^sA^s\), and this is \(G-(1-q)I\). \(\blacksquare\)

**The walk.** A stochastic matrix with a stationary vector describes a random walk \(X_0,X_1,X_2,\dots\) on \([n]\): the state \(X_0\) has the distribution \(\pi\), and from \(X_s=i\) the next state is \(j\) with probability \(a_{ij}\). Then \(X_0=i\) and \(X_s=j\) hold together with probability \(\pi_i(A^s)_{ij}\), and every \(X_s\) has the distribution \(\pi\). The proofs of this course work with the sums; the walk is used to describe what the sums mean.

**Definition.** Let \(P\) be a stochastic matrix with the stationary vector \(\pi\), and let \(x=(x_1,\dots,x_n)\) be points of a metric space \((X,d)\). The *energy* of \(x\) for \(P\) is
\[
\mathcal E_P(x)=\sum_{i,j}\pi_iP_{ij}\,d(x_i,x_j)^2 .
\]

For \(P=A^s\) this is the mean of \(d(x_{X_0},x_{X_s})^2\): the mean squared distance between the points at time \(0\) and at time \(s\). The energy is linear in \(P\):
\[
\begin{aligned}
\mathcal E_{M_t}(x)&=\frac1t\sum_{s=1}^t\mathcal E_{A^s}(x),\\
\mathcal E_G(x)&=(1-q)\sum_{s\ge0}q^s\,\mathcal E_{A^s}(x),
\end{aligned}
\]
and \(\mathcal E_I(x)=0\).

## 2. The definition and the theorem

**Definition 2.1** (Mendel and Naor). A metric space \((X,d)\) has *metric Markov cotype two with the constant \(C>0\)* if for all \(n,t\ge1\), every probability vector \(\pi\), every stochastic matrix \(A\) that is reversible for \(\pi\), and all \(x_1,\dots,x_n\in X\) there are \(y_1,\dots,y_n\in X\) with
\[
\begin{aligned}
&\sum_i\pi_i\,d(x_i,y_i)^2+t\,\mathcal E_A(y)\\
&\qquad\le C^2\,\mathcal E_{M_t}(x) .
\end{aligned}
\]
The infimum of these constants is \(N_2(X)\).

The first term on the left is the cost of replacing each \(x_i\) by \(y_i\). The second term is \(t\) times the one-step energy of the new points. The right side is the energy of the old points, averaged over the times \(1,\dots,t\). The new points have to lie in \(X\); they are otherwise free. In particular they need not be averages of the old points, and a subspace of a space with metric Markov cotype two need not have it, because the new points may leave the subspace. Mendel and Naor constructed a closed linear subspace of \(\ell_1\) that does not have metric Markov cotype two [MN, Theorem 1.14]; that statement is not used in this course.

**Example 2.2** (one step). For \(t=1\) the choice \(y_i=x_i\) gives \(0+\mathcal E_A(x)\) on the left and \(C^2\,\mathcal E_A(x)\) on the right. So for \(t=1\) every metric space satisfies the inequality with \(C=1\).

**Example 2.3** (two states that are exchanged). Let \(n=2\), \(\pi=(\tfrac12,\tfrac12)\), and let \(A\) exchange the two states: \(a_{12}=a_{21}=1\). This matrix is reversible for \(\pi\). Its powers are \(A^s=A\) for odd \(s\) and \(A^s=I\) for even \(s\). So \((M_t)_{12}=(M_t)_{21}=\lceil t/2\rceil/t\) and, with \(D=d(x_1,x_2)\),
\[
\mathcal E_{M_t}(x)=\frac{\lceil t/2\rceil}{t}\,D^2,\qquad
\mathcal E_A(x)=D^2 .
\]
The choice \(y_i=x_i\) gives \(t\,D^2\) on the left side. This is larger than the right side by the factor \(t^2/(C^2\lceil t/2\rceil)\), which is at least \(t/C^2\) for \(t\ge2\). So no constant works for all \(t\) with \(y=x\). The choice \(y_1=y_2=x_1\) gives \(\tfrac12D^2\) on the left side, and the right side is at least \(\tfrac12C^2D^2\). So \(C=1\) suffices for this chain in every metric space.

The two examples show the two extreme choices. If the chain barely moves in \(t\) steps, the points can stay. If the chain forgets its start within \(t\) steps, all points can be moved to one place. The definition asks for a choice that works for every chain with one constant.

**Theorem 2.4** ([OpenAI-MC, Section 1]). The real space \(\ell_1\) has metric Markov cotype two with the constant \(12\sqrt{21}\):
\[
N_2(\ell_1)\le12\sqrt{21} .
\]
The square of this constant is \(3024\).

Here \(\ell_1\) is the space of real sequences \(x=(x(k))_{k\ge1}\) with \(\|x\|_1=\sum_k|x(k)|<\infty\), with the metric \(d(x,y)=\|x-y\|_1\). The proof is given in [The stopped walk and the cotype inequality](the-stopped-walk-and-the-cotype-inequality.md) (Theorem 3.1 there); it uses the tools of [Cuts, the cubic map and a quartic potential](cuts-the-cubic-map-and-a-quartic-potential.md) and Proposition 4.3 below. The proof uses only that \(\pi\) is stationary for \(A\).

## 3. Hilbert space

In a Hilbert space the new points can be taken as the Cesàro averages of the old points along the chain:
\[
y_i=\sum_j(M_t)_{ij}\,x_j .
\]
This section proves that claim. It is an illustration of the definition; the proof for \(\ell_1\) does not use it, and the points \(y_i\) for \(\ell_1\) are not averages of this kind.

**Lemma 3.1.** Let \(H\) be a real inner product space, \(P\) a stochastic matrix with the stationary vector \(\pi\), and \(x_1,\dots,x_n\in H\). Then
\[
\begin{aligned}
\mathcal E_P(x)&=2\sum_i\pi_i\|x_i\|^2\\
&\quad-2\sum_{i,j}\pi_iP_{ij}\langle x_i,x_j\rangle .
\end{aligned}
\]

**Proof.** Expand \(\|x_i-x_j\|^2=\|x_i\|^2+\|x_j\|^2-2\langle x_i,x_j\rangle\). The first term gives \(\sum_i\pi_i\|x_i\|^2\) because the rows of \(P\) have the sum \(1\); the second gives \(\sum_j\pi_j\|x_j\|^2\) because \(\pi\) is stationary. \(\blacksquare\)

**Lemma 3.2.** Let \(A\) be reversible for \(\pi\) and let \(\pi_i>0\) for all \(i\). On \(\mathbb R^n\) use the inner product \(\langle f,g\rangle_\pi=\sum_i\pi_if_ig_i\). Then \(\langle Af,g\rangle_\pi=\langle f,Ag\rangle_\pi\), and \(\mathbb R^n\) has a basis \(\varphi_1,\dots,\varphi_n\) of eigenvectors of \(A\) that is orthonormal for this inner product, with real eigenvalues \(\lambda_1,\dots,\lambda_n\in[-1,1]\).

**Proof.** \(\langle Af,g\rangle_\pi=\sum_{i,j}\pi_ia_{ij}f_jg_i\), and by reversibility this is \(\sum_{i,j}\pi_ja_{ji}f_jg_i=\langle f,Ag\rangle_\pi\). A linear map of a finite-dimensional real inner product space that is self-adjoint has an orthonormal basis of eigenvectors with real eigenvalues (spectral theorem; in the coordinates \(\sqrt{\pi_i}\,f_i\) the map has the symmetric matrix \(\sqrt{\pi_i}\,a_{ij}/\sqrt{\pi_j}\)). If \(A\varphi=\lambda\varphi\) with \(\varphi\ne0\), choose \(i\) with \(|\varphi_i|\) largest; then \(|\lambda|\,|\varphi_i|=|\sum_ja_{ij}\varphi_j|\le|\varphi_i|\), so \(|\lambda|\le1\). \(\blacksquare\)

**Lemma 3.3.** Let \(-1\le\lambda\le1\), \(t\ge1\) and \(c=\frac1t\sum_{s=1}^t\lambda^s\). Then:

1. \(|c|\le1\), and \(c\le0\) if \(\lambda<0\);
2. \(t(1-\lambda)\,c=\lambda(1-\lambda^t)\);
3. \((1-c)^2+2t(1-\lambda)\,c^2\le10\,(1-c)\).

**Proof.** *Part 1.* Each \(|\lambda^s|\le1\). Let \(\lambda<0\). The terms can be grouped in pairs \(\lambda^{2k-1}+\lambda^{2k}=\lambda^{2k-1}(1+\lambda)\le0\); if \(t\) is odd, the term \(\lambda^t\le0\) remains.

*Part 2.* \((1-\lambda)\sum_{s=1}^t\lambda^s=\lambda-\lambda^{t+1}\).

*Part 3.* By part 1, \(0\le1-c\le2\), so \((1-c)^2\le2(1-c)\). By part 2,
\[
t(1-\lambda)\,c^2=\lambda\,c\,(1-\lambda^t) .
\]
*Case \(\lambda\ge0\).* Then \(0\le c\le1\), so the right side is at most \(1-\lambda^t\). Put \(m=\lceil t/2\rceil\). There are \(t-m+1\ge t/2\) indices \(s\) with \(m\le s\le t\), and for each of them \(1-\lambda^s\ge1-\lambda^m\). All terms \(1-\lambda^s\) are \(\ge0\), so
\[
1-c=\frac1t\sum_{s=1}^t(1-\lambda^s)\ge\frac12\,(1-\lambda^m) .
\]
Because \(2m\ge t\),
\[
\begin{aligned}
1-\lambda^t&\le1-\lambda^{2m}\\
&=(1-\lambda^m)(1+\lambda^m)\\
&\le2\,(1-\lambda^m)\le4\,(1-c) .
\end{aligned}
\]
So \(2t(1-\lambda)c^2\le8(1-c)\).

*Case \(\lambda<0\).* Then \(c\le0\), so \(\lambda c=|\lambda|\,|c|\le1\), and \(0\le1-\lambda^t\le2\). So \(t(1-\lambda)c^2\le2\le2(1-c)\), because \(1-c\ge1\). So \(2t(1-\lambda)c^2\le4(1-c)\).

In both cases the left side of part 3 is at most \(2(1-c)+8(1-c)\). \(\blacksquare\)

**Proposition 3.4.** Every real Hilbert space \(H\) has metric Markov cotype two with the constant \(\sqrt5\). For \(\pi\), \(A\), \(t\) and \(x_1,\dots,x_n\in H\) as in Definition 2.1, the points \(y_i=\sum_j(M_t)_{ij}x_j\) satisfy
\[
\begin{aligned}
&\sum_i\pi_i\|x_i-y_i\|^2+t\,\mathcal E_A(y)\\
&\qquad\le5\,\mathcal E_{M_t}(x) .
\end{aligned}
\]

**Proof.** *Reduction to positive \(\pi\).* Let \(S\) be the set of the \(i\) with \(\pi_i>0\). For \(i\in S\) and \(j\notin S\), reversibility gives \(\pi_ia_{ij}=\pi_ja_{ji}=0\), so \(a_{ij}=0\). So the matrix \(A_S=(a_{ij})_{i,j\in S}\) is stochastic and reversible for \((\pi_i)_{i\in S}\), and for \(i\in S\) the row \(i\) of \(A^s\) is the row \(i\) of \(A_S^s\), filled with zeros outside \(S\). Every term of the three sums of the inequality has a factor \(\pi_i\). So only \(i\in S\) contributes, and then only \(j\in S\), and for \(i\in S\) the point \(y_i\) is the average formed with \(A_S\). So it suffices to prove the inequality for \(A_S\). Assume from here on that all \(\pi_i>0\).

*Reduction to real numbers.* Choose an orthonormal basis \(\epsilon_1,\dots,\epsilon_m\) of the span of \(x_1,\dots,x_n\) and write \(x_i=\sum_lf^l_i\epsilon_l\). Then \(y_i=\sum_l(M_tf^l)_i\,\epsilon_l\), and each of the three sums of the inequality is the sum over \(l\) of the same sum for the real numbers \(f^l_1,\dots,f^l_n\) with the new numbers \((M_tf^l)_i\). So it suffices to treat \(H=\mathbb R\).

*The case of real numbers.* Let \(f\in\mathbb R^n\) and write \(f=\sum_kc_k\varphi_k\) with the basis of Lemma 3.2. For \(\lambda\in[-1,1]\) let \(c(\lambda)=\frac1t\sum_{s=1}^t\lambda^s\). Then \(M_t\varphi_k=c(\lambda_k)\varphi_k\) and \(y=M_tf=\sum_kc_k\,c(\lambda_k)\,\varphi_k\). The basis is orthonormal for \(\langle\cdot,\cdot\rangle_\pi\), so
\[
\sum_i\pi_i(f_i-y_i)^2=\sum_kc_k^2\bigl(1-c(\lambda_k)\bigr)^2 .
\]
By Lemma 3.1 for \(P=A\), in the form \(\mathcal E_A(y)=2\langle y,y\rangle_\pi-2\langle Ay,y\rangle_\pi\),
\[
\mathcal E_A(y)=2\sum_kc_k^2\,c(\lambda_k)^2\,(1-\lambda_k) ,
\]
and by Lemma 3.1 for \(P=M_t\),
\[
\mathcal E_{M_t}(f)=2\sum_kc_k^2\bigl(1-c(\lambda_k)\bigr) .
\]
By Lemma 3.3, part 3, for every \(k\) the number
\[
\bigl(1-c(\lambda_k)\bigr)^2+2t(1-\lambda_k)\,c(\lambda_k)^2
\]
is at most \(10\,(1-c(\lambda_k))\). Multiply by \(c_k^2\) and sum over \(k\). \(\blacksquare\)

For \(\ell_1\) the situation is different. According to [OpenAI-MC, Section 1], a condition of Ball that prescribes linear averages as the new points fails in \(\ell_1\); that statement is not used and not proved in this course. The points \(y_i\) of the proof of Theorem 2.4 are obtained from the points \(x_j\) by a nonlinear operation, a mean of coordinatewise medians.

## 4. Two averages over time

In this section \(A\) is a stochastic matrix with a stationary vector \(\pi\) (reversibility is not needed), \(x_1,\dots,x_n\) are points of a metric space \((X,d)\), and \(t\ge1\). Put
\[
p=\frac1{t+1},\qquad q=1-p=\frac t{t+1} ,
\]
and let \(G_t\) be the geometric average with this ratio:
\[
G_t=p\sum_{s=0}^\infty q^sA^s .
\]
In terms of the walk: let \(S\) be a random time, independent of the walk, with \(\mathbb P(S=s)=pq^s\) for \(s\ge0\). Then \(\mathcal E_{G_t}(x)\) is the mean of \(d(x_{X_0},x_{X_S})^2\). The mean of \(S\) is \(t\) (Lemma 4.2). The time \(S\) arises if after every step the walk stops with probability \(p\); this is the form in which it is used in the proof of Theorem 2.4. The result of this section compares the stopped walk with the average over the times \(1,\dots,t\) of the definition.

Write
\[
\begin{aligned}
D(s)&=\mathcal E_{A^s}(x),\\
W&=\mathcal E_{M_t}(x)=\frac1t\sum_{s=1}^tD(s) .
\end{aligned}
\]
So \(D(0)=0\) and \(\mathcal E_{G_t}(x)=\sum_{s\ge0}pq^sD(s)\).

**Lemma 4.1.** For all \(r,s\ge0\),
\[
\sqrt{D(r+s)}\le\sqrt{D(r)}+\sqrt{D(s)} .
\]

**Proof.** For \(i,j,k\in[n]\) let \(\omega_{ijk}=\pi_i(A^r)_{ij}(A^s)_{jk}\). These numbers are \(\ge0\). Summing \(\omega_{ijk}\) over \(j\) gives \(\pi_i(A^{r+s})_{ik}\); summing over \(k\) gives \(\pi_i(A^r)_{ij}\); summing over \(i\) gives \(\pi_j(A^s)_{jk}\), because \(\pi\) is stationary for \(A^r\). So with \(\alpha_{ijk}=d(x_i,x_j)\) and \(\beta_{ijk}=d(x_j,x_k)\):
\[
\begin{aligned}
\sum\omega_{ijk}\,d(x_i,x_k)^2&=D(r+s),\\
\sum\omega_{ijk}\,\alpha_{ijk}^2&=D(r),\\
\sum\omega_{ijk}\,\beta_{ijk}^2&=D(s).
\end{aligned}
\]
By the triangle inequality \(d(x_i,x_k)\le\alpha_{ijk}+\beta_{ijk}\). So
\[
\begin{aligned}
D(r+s)&\le\sum\omega\,(\alpha+\beta)^2\\
&=D(r)+D(s)+2\sum\omega\,\alpha\beta ,
\end{aligned}
\]
and \(\sum\omega\,\alpha\beta\le\sqrt{D(r)D(s)}\) by the Cauchy–Schwarz inequality. So \(D(r+s)\le(\sqrt{D(r)}+\sqrt{D(s)})^2\). \(\blacksquare\)

**Lemma 4.2.** With \(p\) and \(q\) as above:

1. \(p\sum_{s\ge0}q^s=1\) and \(p\sum_{s\ge0}s\,q^s=t\);
2. \(p\sum_{s\ge0}s^2q^s=2t^2+t\);
3. \(q^t\le\tfrac12\).

**Proof.** Let \(S_0=\sum q^s=1/(1-q)=1/p\), \(S_1=\sum s\,q^s\) and \(S_2=\sum s^2q^s\); the series converge because \(0<q<1\). Subtract \(q\) times each series from the series; the coefficient of \(q^s\) becomes \(s-(s-1)=1\) for \(S_1\) and \(s^2-(s-1)^2=2s-1\) for \(S_2\):
\[
\begin{aligned}
(1-q)S_1&=\sum_{s\ge1}q^s=\frac q{1-q},\\
(1-q)S_2&=\sum_{s\ge1}(2s-1)\,q^s\\
&=2S_1-\frac q{1-q} .
\end{aligned}
\]
So \(S_1=q/p^2\) and \(S_2=(2q/p^2-q/p)/p=q(1+q)/p^3\). With \(q/p=t\) and \((1+q)/p=2t+1\) this gives \(pS_1=t\) and \(pS_2=t(2t+1)\). For part 3, \(1/q=1+1/t\) and \((1+1/t)^t\ge1+t\cdot\frac1t=2\) by Bernoulli's inequality. \(\blacksquare\)

**Proposition 4.3** (geometric against Cesàro). For every stochastic matrix \(A\) with a stationary vector \(\pi\), all points \(x_1,\dots,x_n\) of a metric space and every \(t\ge1\),
\[
\mathcal E_{G_t}(x)\le28\,\mathcal E_{M_t}(x) .
\]

**Proof.** *Step 1: \(D(t)\le4W\).* For \(1\le r\le t\), Lemma 4.1 and \((\alpha+\beta)^2\le2\alpha^2+2\beta^2\) give \(D(t)\le2D(r)+2D(t-r)\). Average over \(r=1,\dots,t\):
\[
D(t)\le\frac2t\sum_{r=1}^tD(r)+\frac2t\sum_{r=0}^{t-1}D(r) .
\]
The first term is \(2W\). In the second, \(D(0)=0\), so the sum is \(\sum_{r=1}^{t-1}D(r)\le tW\). So \(D(t)\le4W\). The same remark gives
\[
\sum_{r=0}^{t-1}D(r)\le tW .
\]

*Step 2: blocks of length \(t\).* Let \(s=jt+r\) with \(j\ge0\) and \(0\le r<t\). Applying Lemma 4.1 repeatedly,
\[
\begin{aligned}
D(s)&\le\bigl(j\sqrt{D(t)}+\sqrt{D(r)}\bigr)^2\\
&\le2j^2D(t)+2D(r) .
\end{aligned}
\]

*Step 3: the sum.* Multiply by \(pq^s\) and sum over \(s\ge0\). All terms are \(\ge0\), so the order of summation is free. For the first part use \(j=\lfloor s/t\rfloor\le s/t\) and Lemma 4.2:
\[
\begin{aligned}
\sum_{s\ge0}pq^s\,j^2&\le\frac1{t^2}\,p\sum_{s\ge0}s^2q^s\\
&=2+\frac1t\le3 .
\end{aligned}
\]
For the second part collect the \(s\) with the same remainder \(r\):
\[
\sum_{j\ge0}pq^{jt+r}=\frac{pq^r}{1-q^t}\le2p\le\frac2t ,
\]
because \(q^t\le\tfrac12\) and \(q^r\le1\). So
\[
\begin{aligned}
\mathcal E_{G_t}(x)&=\sum_{s\ge0}pq^sD(s)\\
&\le2\cdot3\cdot D(t)+2\cdot\frac2t\sum_{r=0}^{t-1}D(r)\\
&\le24\,W+4\,W .
\end{aligned}
\]
\(\blacksquare\)

In terms of the walk, \(j\) is the number of complete blocks of \(t\) steps before the time \(S\) and \(r\) is the rest. The second moment of \(j\) is at most \(3\), and the rest takes each value \(0,\dots,t-1\) with a probability of at most \(2/t\).

A comparison in the other direction, with the constant \(2e\), is Exercise 5.4. So the two averages can replace each other in the definition, at the cost of the constant.

## 5. Exercises

**5.1.** Let \((X,d)\) be a metric space with at least two points. Show that \(N_2(X)\ge1/\sqrt5\). Use the matrix of Example 2.3 with \(t=1\).

**5.2.** Let \(H\) be a real Hilbert space, \(\pi\) a probability vector and let every row of \(A\) be equal to \(\pi\). Show that \(A\) is reversible for \(\pi\), that \(M_t=A\), and that the points \(y_i=m\) with \(m=\sum_j\pi_jx_j\) give equality in Definition 2.1 with \(C^2=\tfrac12\).

**5.3.** Show that \(D(2s)\le4D(s)\) for all \(s\), and give an example in which \(D(s)\) is not monotone in \(s\).

**5.4.** Show that \(\mathcal E_{M_t}(x)\le2e\,\mathcal E_{G_t}(x)\) in the setting of Section 4.

**5.5.** Show that the matrix \(A\) of the example after the first definition (the cyclic shift of three states) has eigenvalues that are not real. Which step of the proof of Lemma 3.2 fails?

## 6. Solutions

**5.1.** Let \(x_1\ne x_2\), \(D=d(x_1,x_2)\), and take the matrix of Example 2.3 with \(t=1\). Then \(M_1=A\) and the right side is \(C^2D^2\). For any \(y_1,y_2\) put \(\alpha=d(x_1,y_1)\), \(\beta=d(x_2,y_2)\), \(\gamma=d(y_1,y_2)\). The left side is \(\tfrac12\alpha^2+\tfrac12\beta^2+\gamma^2\), and \(D\le\alpha+\gamma+\beta\) by the triangle inequality. By the Cauchy–Schwarz inequality for the vectors \((\sqrt2,\sqrt2,1)\) and \((\alpha/\sqrt2,\ \beta/\sqrt2,\ \gamma)\),
\[
(\alpha+\beta+\gamma)^2\le5\,\Bigl(\frac{\alpha^2}2+\frac{\beta^2}2+\gamma^2\Bigr) .
\]
So the left side is at least \(D^2/5\) for every choice of \(y_1,y_2\), and \(C^2\ge\tfrac15\).

**5.2.** \(\pi_ia_{ij}=\pi_i\pi_j=\pi_ja_{ji}\). \(A^2=A\) because \(\sum_k\pi_k\pi_j=\pi_j\); so all powers are \(A\) and \(M_t=A\). By Lemma 3.1,
\[
\begin{aligned}
\mathcal E_A(x)&=2\sum_i\pi_i\|x_i\|^2-2\|m\|^2\\
&=2\sum_i\pi_i\|x_i-m\|^2 .
\end{aligned}
\]
With \(y_i=m\) the left side of Definition 2.1 is \(\sum_i\pi_i\|x_i-m\|^2+0\), which is \(\tfrac12\mathcal E_{M_t}(x)\).

**5.3.** Lemma 4.1 with \(r=s\) gives \(\sqrt{D(2s)}\le2\sqrt{D(s)}\). In Example 2.3 with \(x_1\ne x_2\): \(D(s)=d(x_1,x_2)^2\) for odd \(s\) and \(D(s)=0\) for even \(s\).

**5.4.** All entries of the matrices \(A^s\) are \(\ge0\), so entry by entry
\[
G_t\ge p\sum_{s=1}^tq^sA^s\ge p\,q^t\,t\,M_t .
\]
Here \(pt=t/(t+1)\ge\tfrac12\), and \(q^t=(1+1/t)^{-t}\ge e^{-1}\) because \(1+u\le e^u\). So \(G_t\ge\frac1{2e}M_t\) entry by entry, and the energy is a sum with nonnegative coefficients of the entries.

**5.5.** \(A^3=I\) and the characteristic polynomial of \(A\) is \(\lambda^3-1\), with the roots \(1\) and \(-\tfrac12\pm\tfrac{\sqrt3}2\,i\). In the proof of Lemma 3.2 the first step fails: \(\langle Af,g\rangle_\pi=\langle f,Ag\rangle_\pi\) needs \(\pi_ia_{ij}=\pi_ja_{ji}\), which is false for this matrix.

## References

- [OpenAI-MC] OpenAI, *Metric Markov Cotype Two of \(\ell_1\)*, OpenAI Math Release preprint, 5 October 2026, Sections 1 and 4. https://github.com/openai/math/tree/main/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026
- [MN] M. Mendel and A. Naor, *Spectral calculus and Lipschitz extension for barycentric metric spaces*, arXiv:1301.3963, version 2, Definition 1.2, Theorem 1.14 and Question 1.15. https://arxiv.org/abs/1301.3963
