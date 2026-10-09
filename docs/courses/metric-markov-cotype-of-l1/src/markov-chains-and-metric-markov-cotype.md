# Markov chains and metric Markov cotype

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Ball introduced *Markov type* and *Markov cotype* in 1992 to study when a Lipschitz map from a subset of one space into another extends to the whole space with a bounded loss in its Lipschitz constant. Markov type compares how far a stationary random walk moves in \(t\) steps with \(t\) times the size of one step. Markov cotype runs the other way: given values \(x_i\) at the states of a Markov chain, it asks for new values \(y_i\), not too far from the \(x_i\), whose one-step variation is small compared with the variation of the \(x_i\) over many steps. Mendel and Naor gave the metric formulation below and asked whether the space \(\ell_1\) satisfies it with exponent two [MN, Question 1.15]. OpenAI answered this in October 2026 [OpenAI-C]:

**Theorem** (OpenAI). The real space \(\ell_1\) has metric Markov cotype two, with constant \(N_2(\ell_1)\le12\sqrt{21}\).

This course proves the theorem. The new points \(y_i\) are built from the data by an explicit nonlinear recipe: each \(y_i\) is the expected coordinatewise median of three independent endpoints of a random walk from \(i\) stopped at a random geometric time. The present lesson sets up finite Markov chains, states the definition, and proves a comparison between geometric and uniform averages of the time (Lemma 3.1), valid in every metric space. The lesson [Cuts and a flat cubic](cuts-and-a-flat-cubic.md) writes finite subsets of \(\ell_1\) through cuts and proves the key inequality for the cubic \(3r^2-2r^3\); the lesson [A stopped walk and the cotype of ℓ₁](a-stopped-walk-and-the-cotype-of-l1.md) proves the theorem.

Nothing beyond finite sums and convergent series of nonnegative numbers is used.

## 1. Finite Markov chains

A *stochastic matrix* \(A=(a_{ij})_{i,j\in[n]}\) has nonnegative entries and row sums \(1\). A probability vector \(\pi\) on \([n]\) is *stationary* for \(A\) if \(\pi A=\pi\), and \(A\) is *reversible* with respect to \(\pi\) if \(\pi_ia_{ij}=\pi_ja_{ji}\) for all \(i,j\); summing over \(i\) shows that reversibility implies stationarity. Zero entries of \(\pi\) are allowed.

The *Markov chain* with initial law \(\pi\) and transitions \(A\) is the random sequence \(X_0,X_1,\dots\) in \([n]\) with
\[
\mathbb P(X_0=i_0,X_1=i_1,\dots,X_s=i_s)=\pi_{i_0}a_{i_0i_1}\cdots a_{i_{s-1}i_s};
\]
these numbers are consistent in \(s\) because the rows of \(A\) sum to \(1\). Expectations of functions of \((X_0,\dots,X_s)\) are finite sums. Summing over intermediate states, \(\mathbb P(X_r=i,X_{r+s}=j)=(\pi A^r)_i(A^s)_{ij}\). If \(\pi\) is stationary, then \(\pi A^r=\pi\), so each \(X_r\) has law \(\pi\) and
\[
\mathbb P(X_r=i,X_{r+s}=j)=\pi_i(A^s)_{ij}\qquad(r,s\ge0):\tag{1.1}
\]
the pair \((X_r,X_{r+s})\) has the law of \((X_0,X_s)\).

## 2. The definition

**Definition 2.1** (Mendel–Naor). A metric space \((X,d)\) has *metric Markov cotype two with constant \(C\)* if for all \(n,t\ge1\), every probability vector \(\pi\) on \([n]\), every stochastic matrix \(A\) reversible with respect to \(\pi\), and all \(x_1,\dots,x_n\in X\), there are \(y_1,\dots,y_n\in X\) with
\[
\sum_i\pi_i\,d(x_i,y_i)^2+t\sum_{i,j}\pi_ia_{ij}\,d(y_i,y_j)^2\le C^2\sum_{i,j}\pi_i\Bigl(\frac1t\sum_{s=1}^tA^s\Bigr)_{ij}d(x_i,x_j)^2.\tag{2.1}
\]
The least such \(C\) is \(N_2(X)\).

By (1.1), the right-hand side of (2.1) is \(C^2\) times
\[
W=\frac1t\sum_{s=1}^t\mathbb E\,d(x_{X_s},x_{X_0})^2,
\]
the mean squared displacement of the data along the stationary chain, averaged over the times \(1,\dots,t\). The left-hand side pays for moving the data and for the one-step variation of the new values, the latter multiplied by \(t\). Keeping \(y_i=x_i\) does not work in general (Exercise 4.2): the points must be moved, and the theorem allows them to move anywhere in the space.

Ball proved that Hilbert spaces have Markov cotype two, with linear averages of the data as the new points; Mendel and Naor showed that \(\ell_1\) does not satisfy Ball's linear version and that a certain closed subspace of \(\ell_1\) fails the metric version [MN, Section 1]. So the new points of the theorem cannot in general be linear averages of the data, and they need not lie in a given subspace containing the data.

## 3. Geometric and uniform averages of time

The proof in the third lesson controls the displacement at a random geometric time. The next lemma compares it with \(W\).

**Lemma 3.1** (geometric and uniform times). Let \(X_0,X_1,\dots\) be a Markov chain with stationary initial law, let \(x_1,\dots,x_n\) lie in a metric space, and let \(t\ge1\), \(p=\frac1{t+1}\) and \(q=1-p\). Let \(D(s)=\mathbb E\,d(x_{X_s},x_{X_0})^2\) and \(W=\frac1t\sum_{s=1}^tD(s)\). Then
\[
\sum_{s=0}^\infty pq^s\,D(s)\le28\,W.\tag{3.1}
\]
If \(S\) is a random time independent of the chain with \(\mathbb P(S=s)=pq^s\), the left side is \(\mathbb E\,d(x_{X_S},x_{X_0})^2\).

**Proof.** *Subadditivity.* For \(r,s\ge0\), \(d(x_{X_{r+s}},x_{X_0})\le d(x_{X_{r+s}},x_{X_r})+d(x_{X_r},x_{X_0})\). Taking the square root of the mean square of both sides and using Minkowski's inequality and (1.1) for the pair \((X_r,X_{r+s})\),
\[
\sqrt{D(r+s)}\le\sqrt{D(s)}+\sqrt{D(r)}.\tag{3.2}
\]

*The time \(t\).* By (3.2) and \((a+b)^2\le2a^2+2b^2\), \(D(t)\le2D(r)+2D(t-r)\) for \(1\le r\le t\). Averaging over \(r\) and using \(D(0)=0\),
\[
D(t)\le\frac2t\sum_{r=1}^tD(r)+\frac2t\sum_{r=0}^{t-1}D(r)\le4W.
\]

*All times.* Write \(s=jt+r\) with \(j\ge0\) and \(0\le r<t\). Applying (3.2) \(j\) times, \(\sqrt{D(s)}\le j\sqrt{D(t)}+\sqrt{D(r)}\), so \(D(s)\le2j^2D(t)+2D(r)\le8j^2W+2D(r)\).

*The geometric weights.* Let \(J(s)=\lfloor s/t\rfloor\) and \(R(s)=s-tJ(s)\). Since \(\sum_spq^ss=\frac qp=t\) and \(\sum_spq^ss(s-1)=\frac{2q^2}{p^2}=2t^2\),
\[
\sum_spq^sJ(s)^2\le\frac1{t^2}\sum_spq^ss^2=\frac{2t^2+t}{t^2}\le3.
\]
For \(0\le r<t\), \(\sum_{s:R(s)=r}pq^s=\frac{pq^r}{1-q^t}\le2p\le\frac2t\), because \(q^t=(1+\frac1t)^{-t}\le\frac12\). Hence \(\sum_spq^sD(R(s))\le\frac2t\sum_{r=0}^{t-1}D(r)\le2W\). Altogether
\[
\sum_spq^sD(s)\le8W\cdot3+2\cdot2W=28W.
\]
For the last statement, \(\mathbb P(S=s,X_0=i,X_s=j)=pq^s\pi_i(A^s)_{ij}\). \(\square\)

Only stationarity of \(\pi\) was used, not reversibility.

## 4. Exercises

**Exercise 4.1** (easy). Show that reversibility implies stationarity, and give a stochastic matrix with a stationary vector with respect to which it is not reversible.

**Exercise 4.2** (medium). Let \(X\) be the real line, \(n=2\), \(\pi=(\frac12,\frac12)\), \(A=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), \(x_1=0\), \(x_2=1\) and \(t\) even. Compute the right-hand side of (2.1). Show that \(y_i=x_i\) satisfies (2.1) only if \(C^2\ge2t\), and that \(y_1=y_2=\frac12\) satisfies it with \(C^2=\frac12\).

**Exercise 4.3** (easy). For \(\mathbb P(S=s)=pq^s\), \(s\ge0\), show that \(\mathbb ES=q/p\) and \(\mathbb ES(S-1)=2q^2/p^2\).

**Exercise 4.4** (medium). Show that (3.2) can fail if the initial law is not stationary.

## 5. Solutions

**4.1.** \(\sum_i\pi_ia_{ij}=\sum_i\pi_ja_{ji}=\pi_j\). The cyclic matrix on three states, \(a_{12}=a_{23}=a_{31}=1\), has the stationary vector \((\frac13,\frac13,\frac13)\) but \(\pi_1a_{12}=\frac13\neq0=\pi_2a_{21}\).

**4.2.** For \(t\) even, \(\frac1t\sum_{s=1}^tA^s=\frac12(I+A)\), and the double sum on the right of (2.1) is \(\sum_i\pi_i\cdot\frac12\cdot1=\frac12\), so the right-hand side is \(\frac{C^2}2\). With \(y=x\) the left side is \(t\sum_{i,j}\pi_ia_{ij}|x_i-x_j|^2=t\), so \(C^2\ge2t\). With \(y_1=y_2=\frac12\) the left side is \(\frac14\le\frac{C^2}2\) for \(C^2=\frac12\).

**4.3.** \(\sum_ss\,q^s=q/(1-q)^2\) and \(\sum_ss(s-1)q^s=2q^2/(1-q)^3\); multiply by \(p=1-q\).

**4.4.** Take \(n=3\), \(a_{12}=a_{23}=a_{33}=1\) and the other entries \(0\), the initial law \((1,0,0)\), and \(x_1=x_2=0\), \(x_3=1\) on the real line. Then \(X_1=2\) and \(X_2=3\) with probability one, so \(D(1)=0\) and \(D(2)=1\), while (3.2) with \(r=s=1\) would give \(\sqrt{D(2)}\le2\sqrt{D(1)}=0\).

## References

- [MN] M. Mendel and A. Naor, *Spectral calculus and Lipschitz extension for barycentric metric spaces*, Anal. Geom. Metr. Spaces 1 (2013); arXiv:1301.3963. https://arxiv.org/abs/1301.3963
- [OpenAI-C] OpenAI, *Metric Markov cotype two of \(\ell_1\)*, OpenAI Math Release preprint, 5 October 2026, Sections 1 and 4. https://github.com/openai/math/tree/main/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026
