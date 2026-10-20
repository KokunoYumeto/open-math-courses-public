# Logarithmic phases at polynomial scales

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Sums of \(n^{it}\) over a progression appear twice in this course: in the rough part of the prime coefficient (Lesson 6) and in a Gram matrix of evaluations of a Dirichlet polynomial (Lesson 17). In both places the progression has length at least \(x^{\delta}\) for a fixed \(\delta>0\), and the frequency \(t\) is at most a fixed power of \(x\). In this regime the ratio \(\log|t|/\log(\text{length})\) is bounded, and classical van der Corput differencing gives a saving of a fixed power of the length. This lesson proves that saving with full uniformity in the shift and the residue class.

**Prerequisites.** [*Exponential sums and a subconvex bound*](course:NT-ZETA/NT-ZETA-07), Theorems 2.1 (Kusmin–Landau), 2.2 (second-derivative sum test) and 3.1 (van der Corput's inequality); [*Primes, divisors, mean squares and rough numbers*](primes-divisors-mean-squares-and-rough-numbers.md), Lemma 5.1.

Throughout, \(H\ge2\), \(0\le u\le1\), \(t\) is real, \(J\subseteq[H,2H]\) is an interval, and

\[
\begin{gathered}
S=\sum_{n\in J}(n+u)^{it}=\sum_{n\in J}e\bigl(f(n)\bigr),\\
f(y)=\frac t{2\pi}\log(y+u).\quad(0.1)
\end{gathered}
\]

The derivatives of the phase are

\[
\begin{gathered}
f^{(j)}(y)=\frac t{2\pi}\cdot\frac{(-1)^{j-1}(j-1)!}{(y+u)^j}\\
(j\ge1).\quad(0.2)
\end{gathered}
\]

## 1. Small frequencies

**Lemma 1.1.** If \(0<|t|\le\pi H\), then \(|S|\ll H/|t|\), with an absolute implied constant.

**Proof.** Replacing \(t\) by \(-t\) conjugates \(S\), so let \(t>0\). For consecutive integers \(n,n+1\in J\) the increment of the phase is \(\delta_n=f(n+1)-f(n)=\int_n^{n+1}f'(y)\,dy\). By (0.2), \(f'(y)=t/(2\pi(y+u))\) decreases and lies in \([t/(2\pi(2H+2)),\,t/(2\pi H)]\) on \([H,2H+1]\). So the increments decrease and lie in \([\Delta,1-\Delta]\) with \(\Delta=t/(4\pi(H+1))\le\frac14\), because \(t/(2\pi H)\le\frac12\le1-\Delta\). The Kusmin–Landau inequality (Theorem 2.1 of [*Exponential sums and a subconvex bound*](course:NT-ZETA/NT-ZETA-07)) gives \(|S|\ll\Delta^{-1}\ll H/t\). \(\square\)

## 2. Repeated differencing

For a finite sequence \(z=(z_n)\) of complex numbers indexed by an interval of integers and an integer \(k\ge1\), let \(\Delta_kz\) be the sequence \(n\mapsto z_{n+k}\overline{z_n}\), indexed by those \(n\) for which both \(n\) and \(n+k\) are indices of \(z\). For \(\mathbf k=(k_1,\dots,k_d)\) put \(\Delta_{\mathbf k}z=\Delta_{k_d}\cdots\Delta_{k_1}z\) and \(S_{\mathbf k}=\sum_n(\Delta_{\mathbf k}z)_n\).

**Lemma 2.1 (iterated van der Corput inequality).** Let \(L_0\ge1\) be an integer and \(z\) a sequence with \(|z_n|\le1\) indexed by at most \(L_0\) consecutive integers. For every integer \(d\ge1\) and \(1\le K\le L_0\),

\[
\begin{gathered}
\Bigl(\frac{|S_\varnothing|}{L_0}\Bigr)^{2^d}
\le c_d\Bigl(\frac1K\\
+\frac1{K^d}\sum_{\mathbf k\in[1,K)^d}\frac{|S_{\mathbf k}|}{L_0}\Bigr),\quad(2.1)
\end{gathered}
\]

where \(S_\varnothing=\sum_nz_n\), the sum is over integer vectors \(\mathbf k\) with \(1\le k_i<K\), and \(c_1=4\), \(c_{d+1}=8c_d^2\).

**Proof.** Extend \(z\) by zeros to exactly \(L_0\) consecutive indices; this changes none of the sums \(S_{\mathbf k}\). Van der Corput's inequality (Theorem 3.1 of [*Exponential sums and a subconvex bound*](course:NT-ZETA/NT-ZETA-07)) with \(H=K\), in the form with moduli, gives

\[
\begin{aligned}
K^2|S_\varnothing|^2&\le(L_0+K-1)\\
&\quad\times\Bigl(KL_0+2K\sum_{k<K}|S_k|\Bigr),
\end{aligned}
\]

because \(\sum|z_n|^2\le L_0\) and \(K-k\le K\). Since \(L_0+K-1\le2L_0\), dividing by \(K^2L_0^2\) gives (2.1) for \(d=1\) with \(c_1=4\). Each \(\Delta_{\mathbf k}z\) again has terms of modulus at most \(1\) and at most \(L_0\) indices, so the case \(d=1\) applies to it. Assume (2.1) for \(d\). Squaring, using \((a+b)^2\le2a^2+2b^2\) and Cauchy's inequality for the average over the at most \(K^d\) vectors \(\mathbf k\),

\[
\begin{aligned}
&\Bigl(\frac{|S_\varnothing|}{L_0}\Bigr)^{2^{d+1}}\\
&\quad\le2c_d^2\Bigl(\frac1{K^2}+\frac1{K^d}\sum_{\mathbf k}\frac{|S_{\mathbf k}|^2}{L_0^2}\Bigr)\\
&\quad\le2c_d^2\Bigl(\frac1{K^2}+\frac2K\\
&\qquad+\frac4{K^{d+1}}\sum_{\mathbf k,k'}\frac{|S_{(\mathbf k,k')}|}{L_0}\Bigr).
\end{aligned}
\]

This is (2.1) for \(d+1\) with \(c_{d+1}=8c_d^2\). \(\square\)

For the sequence \(z_n=e(f(n))\), \(n\in J\), the differenced sequence is \((\Delta_{\mathbf k}z)_n=e(g_{\mathbf k}(n))\), where \(g_{\mathbf k}=\Delta_{k_d}\cdots\Delta_{k_1}f\) and \(\Delta_kg(y)=g(y+k)-g(y)\). Since \(\Delta_kg(y)=k\int_0^1g'(y+k\theta)\,d\theta\), induction gives

\[
\begin{gathered}
g_{\mathbf k}(y)=k_1\cdots k_d\\
\times\int_{[0,1]^d}f^{(d)}\bigl(y+\textstyle\sum_ik_i\theta_i\bigr)\,d\theta,\quad(2.2)
\end{gathered}
\]

and the same formula holds for every derivative of \(g_{\mathbf k}\), with \(f^{(d)}\) replaced by the corresponding derivative of \(f^{(d)}\).

## 3. The power saving

**Theorem 3.1 (logarithmic phases with bounded height ratio).** Fix \(\Lambda\ge1\) and put \(d_\Lambda=\lceil\Lambda\rceil\) and \(c_\Lambda=1/(d_\Lambda2^{d_\Lambda+2})\). There is \(C_\Lambda\) such that, for all \(H\ge2\), \(0\le u\le1\), real \(t\) with \(1\le|t|\le H^\Lambda\), and every interval \(J\subseteq[H,2H]\),

\[
\begin{gathered}
\Bigl|\sum_{n\in J}(n+u)^{it}\Bigr|\\
\le C_\Lambda\Bigl(\frac H{|t|}+H^{1-c_\Lambda}\Bigr).\quad(3.1)
\end{gathered}
\]

**Proof.** If \(|t|\le\pi H\), Lemma 1.1 applies. Let \(|t|>\pi H\) and put \(\lambda=\log|t|/\log H\), so \(1<\lambda\le\Lambda\), and let \(d=\lceil\lambda\rceil-1\). Then \(1\le d<d_\Lambda\) and \(d<\lambda\le d+1\). Put

\[
\begin{gathered}
K=\Bigl\lfloor\frac{H^{1/(2d)}}{2d}\Bigr\rfloor,\qquad L_0=\lfloor H\rfloor+2 .
\end{gathered}
\]

If \(K<1\), then \(H\) is bounded in terms of \(\Lambda\), and (3.1) holds trivially after enlarging \(C_\Lambda\). Let \(K\ge1\). The interval \(J\) contains at most \(L_0\) integers, and \(L_0\le2H\). Apply Lemma 2.1 to \(z_n=e(f(n))\), \(n\in J\).

Fix \(\mathbf k\in[1,K)^d\). The sum \(S_{\mathbf k}\) runs over an interval of integers \(n\) of length at most \(2H\), and in (2.2) the arguments \(y+\sum_ik_i\theta_i+u\) lie in \([H,2H+dK+1]\subseteq[H,3H]\). By (0.2) and (2.2), \(g_{\mathbf k}''\) has constant sign and

\[
\begin{gathered}
k_1\cdots k_d\,m_0\le|g_{\mathbf k}''|\le3^{d+2}k_1\cdots k_d\,m_0,\\
m_0=\frac{|t|\,(d+1)!}{2\pi(3H)^{d+2}}.
\end{gathered}
\]

The second-derivative sum test (Theorem 2.2 of [*Exponential sums and a subconvex bound*](course:NT-ZETA/NT-ZETA-07)) with \(M=k_1\cdots k_dm_0\) and \(A=3^{d+2}\) gives

\[
\begin{gathered}
|S_{\mathbf k}|\ll_d H\sqrt{m_0\,k_1\cdots k_d}\\
+\frac1{\sqrt{m_0\,k_1\cdots k_d}} .
\end{gathered}
\]

Average over \(\mathbf k\), using \(\sum_{k<K}\sqrt k\le K^{3/2}\) and \(\sum_{k<K}1/\sqrt k\le2\sqrt K\):

\[
\begin{gathered}
\frac1{K^d}\sum_{\mathbf k}|S_{\mathbf k}|\ll_d HK^{d/2}\sqrt{m_0}\\
+\frac{2^d}{K^{d/2}\sqrt{m_0}} .
\end{gathered}
\]

Here \(m_0\asymp_dH^{\lambda-d-2}\) and \(K^d\asymp_dH^{1/2}\). Since \(\lambda\le d+1\), the first term is \(\ll_dH^{1+(\lambda-d-2)/2+1/4}\le H^{3/4}\). Since \(\lambda>d\), the second is \(\ll_dH^{(d+2-\lambda)/2-1/4}\le H^{3/4}\). Inserting these into (2.1), with \(L_0\ge H\) and \(1/K\ll_dH^{-1/(2d)}\),

\[
\begin{gathered}
\Bigl(\frac{|S|}{L_0}\Bigr)^{2^d}\ll_dH^{-1/(2d)}+H^{-1/4}\\
\le2H^{-1/(4d)} .
\end{gathered}
\]

Hence \(|S|\ll_\Lambda H^{1-1/(d2^{d+2})}\le H^{1-c_\Lambda}\), because \(d<d_\Lambda\). \(\square\)

The saving comes from comparing two scales: the differencing lowers the effective size of the phase by a factor \(K\) at each step, until its second derivative is small enough for the second-derivative test to win. The number of steps is about \(\log|t|/\log H\), and each step halves the exponent of the saving; this is why the method needs a bounded ratio \(\log|t|/\log H\).

## 4. Progressions and weights

**Corollary 4.1 (logarithmic phases on progressions).** Fix \(\delta_1>0\), \(C_0>0\) and \(\Lambda_1\ge1\). There are \(c>0\) and \(C\), depending only on \(\delta_1\) and \(\Lambda_1\), such that for large \(x\), uniformly for \(x^{\delta_1}\le N\le x^{\Lambda_1}\), moduli \(1\le q\le L^{C_0}\), integers \(a\), intervals \(J\subseteq[N,2N]\) and real \(t\) with \(1\le|t|\le x^{\Lambda_1}\),

\[
\begin{gathered}
\Bigl|\sum_{\substack{n\in J\\ n\equiv a\ (q)}}n^{it}\Bigr|\le C\,\frac Nq\Bigl(\frac1{|t|}+x^{-c}\Bigr).\quad(4.1)
\end{gathered}
\]

**Proof.** Let \(a_0\in[1,q]\) satisfy \(a_0\equiv a\ (q)\), and write \(n=qb+a_0\). Then \(n^{it}=q^{it}(b+u)^{it}\) with \(u=a_0/q\in(0,1]\), and \(b\) runs over the integers of an interval contained in \([H_0,2H_0+2]\), where \(H_0=N/q-1\ge N/(2q)\ge x^{\delta_1/2}\) for large \(x\). At most three values of \(b\) exceed \(2H_0\). Apply Theorem 3.1 to the rest, with \(H=H_0\) and \(\Lambda=4\Lambda_1/\delta_1\); this is admissible because \(|t|\le x^{\Lambda_1}\le H_0^{2\Lambda_1/\delta_1}\). The result is \(|\cdot|\le C(H_0/|t|+H_0^{1-c_\Lambda})+3\), and \(H_0^{-c_\Lambda}\le x^{-c_\Lambda\delta_1/2}\). \(\square\)

**Lemma 4.2 (partial summation).** Let \(J\) be an interval, \(a_n\) complex numbers for the integers \(n\in J\), and \(g\) a function of bounded variation \(V_J(g)\) on \(J\). Then

\[
\begin{gathered}
\Bigl|\sum_{n\in J}a_ng(n)\Bigr|\le\Bigl(\sup_J|g|+V_J(g)\Bigr)\\
\times\max_{J'}\Bigl|\sum_{n\in J'}a_n\Bigr|,
\end{gathered}
\]

the maximum over the initial segments \(J'\) of \(J\).

**Proof.** Let \(n_1<\cdots<n_s\) be the integers of \(J\) and \(A_j=\sum_{i\le j}a_{n_i}\). Abel summation gives \(\sum_ja_{n_j}g(n_j)=A_sg(n_s)\)\(-\sum_{j<s}A_j\bigl(g(n_{j+1})-g(n_j)\bigr)\), and \(\sum_j|g(n_{j+1})-g(n_j)|\le V_J(g)\). \(\square\)

Combining Corollary 4.1 with Lemma 4.2, the bound (4.1) holds for \(\sum_{n\in J,\,n\equiv a}g(n)n^{it}\), multiplied by \(\sup|g|+V_J(g)\).

## 5. Exercises

**5.1.** Let \(H\ge9\) and \(1\le t\le\sqrt H/4\). Show that \(|\sum_{H<n\le2H}n^{it}|\ge H/(8t)\), so the term \(H/|t|\) in (3.1) cannot be omitted.

**5.2.** Prove (2.2) by induction on \(d\).

**5.3.** In the proof of Theorem 3.1, check that the case \(d=1\) (that is, \(H<|t|\le H^2\)) gives \(|S|\ll H^{7/8}\), and that this is the bound of the van der Corput process with one differencing step.

**5.4.** Let \(N=\exp(L/(\log L)^2)\) and \(|t|=x^3\). Compute \(\lambda=\log|t|/\log N\) and explain why Theorem 3.1 gives no saving uniform in \(x\) for this choice.

**5.5.** Let \(x^{\delta_1}\le N\le x\), \(q\le L^{C_0}\), and \(g(y)=1/\log y\) on \([N,2N]\). Use Lemma 4.2 and Corollary 4.1 to bound \(\sum_{n\in J,\,n\equiv a\,(q)}n^{it}/\log n\) for \(1\le|t|\le x^2\).

## 6. Solutions

**5.1.** By Lemma 5.1 of [*Primes, divisors, mean squares and rough numbers*](primes-divisors-mean-squares-and-rough-numbers.md) with \(q=1\), the sum differs from \(\int_H^{2H}y^{it}dy=H^{1+it}(2^{1+it}-1)/(1+it)\) by at most \(3+t\). Since \(|2^{1+it}-1|\ge1\) and \(|1+it|\le2t\), the integral has modulus at least \(H/(2t)\). Hence the sum has modulus at least \(H/(2t)-3-t\). For \(t\le\sqrt H/4\) we have \(3H/(8t)\ge\frac32\sqrt H\ge3+\frac14\sqrt H\ge3+t\), because \(\sqrt H\ge3\). So \(H/(2t)-3-t\ge H/(8t)\).

**5.2.** For \(d=1\), \(g(y+k)-g(y)=\int_0^kg'(y+s)\,ds\)\(=k\int_0^1g'(y+k\theta)\,d\theta\). If (2.2) holds for \(d\), apply the case \(d=1\) to \(g_{\mathbf k}\) and differentiate (2.2) under the integral sign.

**5.3.** For \(d=1\), \(K\asymp H^{1/2}\), and (2.1) gives \((|S|/L_0)^2\ll H^{-1/2}+H^{-1/4}\), so \(|S|\ll H^{7/8}\). This is the classical bound obtained from one application of van der Corput's inequality followed by the second-derivative test.

**5.4.** Here \(\log N=L/(\log L)^2\) and \(\log|t|=3L\), so \(\lambda=3(\log L)^2\to\infty\). Theorem 3.1 needs \(\Lambda\ge\lambda\), and its saving exponent \(c_\Lambda\) is about \(2^{-\Lambda}/\Lambda\); then \(N^{c_\Lambda}\) is \(\exp\bigl(L(\log L)^{-2}c_\Lambda\bigr)\), and \(c_\Lambda\) decreases faster than any power of \(1/L\). The next lesson treats this range by a mean value theorem whose cost grows only polynomially with the degree.

**5.5.** Lemma 4.2 with \(g(y)=1/\log y\), for which \(\sup|g|+V(g)\le2/\log N\), gives the bound \(\frac{2}{\log N}\cdot C\frac Nq(1/|t|+x^{-c})\), that is \(O\bigl(N/(qL)\cdot(1/|t|+x^{-c})\bigr)\) with an implied constant depending on \(\delta_1\).

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Section 2 and Appendix (Lemma 9.5 there covers a wider range by a different method). https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
