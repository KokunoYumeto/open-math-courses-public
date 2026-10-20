# A mean value theorem and logarithmic phases at large height

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The zero-free region of [*A zero-free strip at large height*](a-zero-free-strip-at-large-height.md) needs cancellation in \(\sum n^{iv}\) over progressions of length about \(\exp(L/(\log L)^2)\) at heights \(|v|\) up to \(x^3\). Then \(\log|v|/\log(\text{length})\) is of order \((\log L)^2\), and repeated differencing (Lesson 3) gives no useful saving. Vinogradov's method expands the phase into a polynomial of degree \(k\approx4\log|v|/\log(\text{length})\) and controls the resulting polynomial sums on average by a mean value theorem. What matters here is that every constant depends on \(k\) only through a factor \(\exp(Ck^{C})\). This lesson proves such a mean value theorem by Linnik's \(p\)-adic iteration and deduces the required cancellation.

**Prerequisites.** [*Primes, divisors, mean squares and rough numbers*](primes-divisors-mean-squares-and-rough-numbers.md), Lemma 1.3; [*Logarithmic phases at polynomial scales*](logarithmic-phases-at-polynomial-scales.md), Lemma 1.1; [*Measure and Hilbert space tools for Haar integration*](course:harmonic-analysis-on-locally-compact-groups/reader/measure-and-hilbert-space-tools), Theorem 3.1 (Hölder's inequality).

## 1. A mean value theorem with uniform constants

For integers \(k\ge2\), \(s\ge1\) and real \(M\ge1\), let \(J_{s,k}(M)\) be the number of pairs of \(s\)-tuples \(\mathbf u,\mathbf v\in\{1,\dots,\lfloor M\rfloor\}^s\) with

\[
\begin{gathered}
\sum_{i=1}^su_i^j=\sum_{i=1}^sv_i^j\qquad(1\le j\le k),
\end{gathered}
\]

and put \(\kappa=k(k+1)/2\). For \(\boldsymbol\alpha\in\mathbb R^k\) let

\[
\begin{gathered}
f(\boldsymbol\alpha)=\sum_{n\le M}e\Bigl(\sum_{j=1}^k\alpha_jn^j\Bigr).
\end{gathered}
\]

**Lemma 1.1 (basic properties).**

1. \(J_{s,k}(M)=\int_{[0,1]^k}|f(\boldsymbol\alpha)|^{2s}\,d\boldsymbol\alpha\).
2. The system \(\sum_iu_i^j=\sum_iv_i^j\) \((j\le k)\) is invariant under the translation of all variables by one integer, so the number of its solutions with all variables in any set of \(\lfloor M\rfloor\) consecutive integers is \(J_{s,k}(M)\).
3. For every integer vector \(\mathbf c\) and every set \(I\) of \(\lfloor M\rfloor\) consecutive integers, the number of \(\mathbf u,\mathbf v\in I^s\) with \(\sum_i(u_i^j-v_i^j)=c_j\) for all \(j\le k\) is at most \(J_{s,k}(M)\).

**Proof.** 1. Expand \(|f|^{2s}=f^s\overline f^{\,s}\) and use \(\int_0^1e(m\alpha)\,d\alpha=\mathbf 1_{m=0}\) for integers \(m\). 2. By the binomial theorem, \(\sum_i(u_i+b)^j-\sum_i(v_i+b)^j\) is a combination of the differences \(\sum_iu_i^l-\sum_iv_i^l\), \(l\le j\), because both sides have \(s\) terms. 3. With \(g\) the exponential sum over \(I\), the count is \(\int|g|^{2s}e(-\boldsymbol\alpha\cdot\mathbf c)\,d\boldsymbol\alpha\le\int|g|^{2s}\), which is \(J_{s,k}(M)\) by parts 1 and 2. \(\square\)

**Lemma 1.2 (power sums modulo prime powers).** Let \(r>k\) be prime and \(h\ge1\). The \(k\)-tuples \(\mathbf z\in(\mathbb Z/r^h\mathbb Z)^k\) whose entries are pairwise distinct modulo \(r\) and whose power sums \(\sum_iz_i^j\) \((1\le j\le k)\) take prescribed values modulo \(r^h\) are at most \(k!\) in number; any two of them are permutations of each other.

**Proof.** Let \(e_j\) be the elementary symmetric functions of \(\mathbf z\) and \(p_j=\sum_iz_i^j\). Newton's identities \(je_j=\sum_{l=1}^j(-1)^{l-1}e_{j-l}p_l\), with \(e_0=1\), determine \(e_1,\dots,e_k\) modulo \(r^h\) from the \(p_j\), since \(j\le k<r\) is invertible. So all such tuples share the polynomial \(F(X)=\prod_i(X-z_i)\) modulo \(r^h\). Let \(\mathbf z,\mathbf z'\) be two of them. Modulo \(r\), \(F\) splits over the field \(\mathbb F_r\) with the roots \(z_1,\dots,z_k\), so each \(z_i'\) is congruent modulo \(r\) to exactly one \(z_{\sigma(i)}\), and \(\sigma\) is a permutation because the \(z_i'\) are distinct modulo \(r\). In \(0\equiv F(z_i')=\prod_l(z_i'-z_l)\pmod{r^h}\), every factor with \(l\ne\sigma(i)\) is a unit modulo \(r\), so \(z_i'\equiv z_{\sigma(i)}\pmod{r^h}\). \(\square\)

**Lemma 1.3 (the congruence step).** Let \(k\ge2\), \(s\ge1\), let \(r>k\) be a prime with \(r^k\ge M\) and \(r\le M\), and let \(N_r\) be the number of solutions counted by \(J_{s+k,k}(M)\) in which the first \(k\) coordinates of \(\mathbf u\) are pairwise distinct modulo \(r\), and likewise for \(\mathbf v\). Then

\[
\begin{gathered}
N_r\le k!\,r^{2s+\kappa-k}M^k\,J_{s,k}(\lceil M/r\rceil).\quad(1.1)
\end{gathered}
\]

**Proof.** Let \(F_r(\boldsymbol\alpha)\) be the sum of \(e(\sum_j\alpha_j\sum_{i\le k}z_i^j)\) over \(\mathbf z\in\{1,\dots,\lfloor M\rfloor\}^k\) with entries distinct modulo \(r\), and \(f_a\) the part of \(f\) with \(n\equiv a\ (r)\). Then \(N_r=\int|F_r|^2|f|^{2s}\). Since \(f=\sum_{a\bmod r}f_a\), Hölder's inequality for the counting measure on the \(r\) residues (Theorem 3.1 of [*Measure and Hilbert space tools for Haar integration*](course:harmonic-analysis-on-locally-compact-groups/reader/measure-and-hilbert-space-tools)) gives \(|f|^{2s}\le r^{2s-1}\sum_a|f_a|^{2s}\), so \(N_r\le r^{2s}\max_a\int|F_r|^2|f_a|^{2s}\).

Fix \(a\). The integral counts solutions in which the last \(s\) coordinates on each side are \(\equiv a\ (r)\). Translate every variable by \(-a\) (Lemma 1.1(2)). The last coordinates become \(r\tilde u_i\), \(r\tilde v_i\), so the first parts \(\mathbf z=(u_i-a)_{i\le k}\) and \(\mathbf z'=(v_i-a)_{i\le k}\) satisfy

\[
\begin{gathered}
\sum_{i\le k}z_i^j\equiv\sum_{i\le k}{z'_i}^{\,j}\pmod{r^j}\\
(1\le j\le k).
\end{gathered}
\]

There are at most \(M^k\) choices of \(\mathbf z\). Given \(\mathbf z\), the power sums of \(\mathbf z'\) are prescribed modulo \(r^j\); lifting them to residues modulo \(r^k\) can be done in \(\prod_{j\le k}r^{k-j}=r^{\kappa-k}\) ways, and for each lift Lemma 1.2 leaves at most \(k!\) residue vectors \(\mathbf z'\bmod r^k\). Since \(M\le r^k\), each residue class modulo \(r^k\) has at most one representative among the \(\lfloor M\rfloor\) admissible values. Given both first parts, the variables \(\tilde u_i,\tilde v_i\) run over a set of at most \(\lceil M/r\rceil\) consecutive integers and satisfy \(\sum_i(\tilde u_i^j-\tilde v_i^j)=c_j\) for integers \(c_j\) determined by \(\mathbf z,\mathbf z'\); Lemma 1.1(3) bounds their number by \(J_{s,k}(\lceil M/r\rceil)\). Multiplying the three counts proves (1.1). \(\square\)

**Theorem 1.4 (mean value with uniform constants).** There are absolute constants \(C_1,C_2\) such that for every \(k\ge2\) some integer \(s\) with \(k\le s\le C_1k^3\) satisfies

\[
\begin{gathered}
J_{s,k}(M)\le\exp(C_1k^{C_2})\\
\times M^{2s-\kappa+1/100}\quad(M\ge1).\quad(1.2)
\end{gathered}
\]

**Proof.** We prove by induction along \(s=k,2k,3k,\dots\) bounds

\[
\begin{gathered}
J_{s,k}(M)\le C_sM^{E_s}\quad(M\ge1),\\
E_s=2s-\kappa+\epsilon_s,\\
\epsilon_{s+k}=\Bigl(1-\frac1k\Bigr)\epsilon_s,\quad(1.3)
\end{gathered}
\]

starting from \(C_k=1\), \(\epsilon_k=\kappa\), which is the trivial bound \(J_{k,k}(M)\le M^{2k}\). Note that \(E_k=2k\) and \(E_{s+k}-E_s=2k-\epsilon_s/k\)\(\ge2k-(k+1)/2>0\), so \(E_s\ge2k\) throughout.

By Lemma 1.3 of Lesson 2 there is an absolute \(A_1\) such that for every \(k\ge2\) and every \(y\ge A_1k^6\) the interval \([y,2y]\) contains at least \(k^3\) primes, all larger than \(k\). Fix \(s\) and let \(M\ge1\).

*Small \(M\).* If \(M^{1/k}<A_1k^6\), the trivial bound \(J_{s+k,k}(M)\le M^{2(s+k)}=M^{E_{s+k}}M^{\kappa-\epsilon_{s+k}}\) gives (1.3) with a constant at most \(M^\kappa\le(A_1k^6)^{k\kappa}=\exp(O(k^3\log2k))\).

*Large \(M\).* Let \(M^{1/k}\ge A_1k^6\) and choose primes \(r_1,\dots,r_{k^3}\in[M^{1/k},2M^{1/k}]\), all larger than \(k\); then \(r^k\ge M\) and \(r\le2M^{1/k}\le M\). Call an \((s+k)\)-tuple *degenerate* if it has fewer than \(k\) distinct coordinates. Such a tuple is described by a list of \(k-1\) values and an assignment of each coordinate to one of them, so there are at most \(M^{k-1}k^{s+k}\) of them. The solutions with a degenerate \(\mathbf u\) number \(\int G\overline f^{\,s+k}\), where \(G\) is the exponential sum over degenerate tuples, and

\[
\begin{gathered}
\Bigl|\int G\overline f^{\,s+k}\Bigr|\le M^{k-1}k^{s+k}\int|f|^{s+k}\\
\le M^{k-1}k^{s+k}J_{s+k,k}(M)^{1/2}.
\end{gathered}
\]

The same holds for degenerate \(\mathbf v\). In a solution with both sides nondegenerate, choose \(k\) positions with distinct entries on each side and permute them to the front; this shows that such solutions number at most \((s+k)^{2k}\) times those whose first \(k\) entries are distinct on both sides. The product of the two Vandermonde determinants of these entries is a nonzero integer of modulus less than \(M^{k(k-1)}\), so at most \(k^2(k-1)<k^3\) of the primes \(r_l\ge M^{1/k}\) divide it, and some \(r_l\) separates both sets of entries. By Lemma 1.3,

\[
\begin{gathered}
J_{s+k,k}(M)\\
\le2M^{k-1}k^{s+k}J_{s+k,k}(M)^{1/2}\\
+k^3(s+k)^{2k}k!\max_lr_l^{2s+\kappa-k}\\
\times M^kJ_{s,k}(\lceil M/r_l\rceil).
\end{gathered}
\]

Insert (1.3) for \(s\), with \(\lceil M/r\rceil\le2M/r\). Since \(2s+\kappa-k-E_s=k^2-\epsilon_s\ge0\) and \(r\le2M^{1/k}\),

\[
\begin{aligned}
&r^{2s+\kappa-k}M^k\Bigl(\frac{2M}r\Bigr)^{E_s}\\
&\quad\le2^{E_s+k^2}M^{k+E_s+k-\epsilon_s/k}\\
&\quad=2^{E_s+k^2}M^{E_{s+k}}.
\end{aligned}
\]

An inequality \(J\le a\sqrt J+b\) implies \(J\le a^2+2b\). Here \(a^2=4k^{2(s+k)}M^{2k-2}\le4k^{2(s+k)}M^{E_{s+k}}\), because \(E_{s+k}\ge2k\). Thus (1.3) holds for \(s+k\) with

\[
\begin{gathered}
\log C_{s+k}\le\log(1+C_s)\\
+O\bigl((s+k^3)\log2k\bigr),
\end{gathered}
\]

which also covers the small-\(M\) constant; here \(E_s\le2s+\kappa\) was used for the factor \(2^{E_s}\).

After \(n\) steps, \(\epsilon=\kappa(1-1/k)^n\le\kappa e^{-n/k}\), which is at most \(1/100\) once \(n=\lceil k\log(100\kappa)\rceil\). Then \(s=k+nk=O(k^2\log2k)\le C_1k^3\), and the constants satisfy \(\log C_s\)\(=O(n(k^2\log2k+k^3)\log2k)\)\(=O(k^5)\). Since \(M\ge1\) and \(E_s\le2s-\kappa+1/100\), this proves (1.2). \(\square\)

The exponent \(2s-\kappa\) cannot be lowered: the vector of power sums takes at most \(\prod_j(sM^j+1)\) values, and Cauchy's inequality gives \(J_{s,k}(M)\ge\lfloor M\rfloor^{2s}/\prod_j(sM^j+1)\) (Exercise 4.2). Theorem 1.4 loses only \(1/100\) in the exponent, at a cost \(\exp(C_1k^{C_2})\) that is polynomial in \(k\) after taking logarithms. Much sharper results are known, but this weak form with explicit uniformity is all that is needed below.

## 2. Logarithmic phases on short progressions

Put \(T=\log L=\log\log x\).

**Theorem 2.1 (logarithmic phases at large height).** Fix \(C_0>0\). There is an absolute constant \(C_3\) such that, for \(x\) large in terms of \(C_0\), uniformly for

\[
\begin{gathered}
\exp(L/T^2)\le N\le2x^5,\qquad q\le L^{C_0},\\
\exp\bigl(L/(2T^2)\bigr)\le|v|\le4x^3,
\end{gathered}
\]

every residue \(a\) modulo \(q\) and every interval \(I\subseteq[N,2N]\),

\[
\begin{gathered}
\Bigl|\sum_{\substack{n\in I\\ n\equiv a\ (q)}}n^{iv}\Bigr|\le\frac Nq\exp\Bigl(-\frac L{T^{C_3}}\Bigr).\quad(2.1)
\end{gathered}
\]

One can take \(C_3=10\).

**Proof.** Let \(a_0\in[1,q]\) with \(a_0\equiv a\ (q)\), and write \(n=qb+a_0\), \(u=a_0/q\in(0,1]\) and \(H=N/q\). Then \(n^{iv}=q^{iv}(b+u)^{iv}\), and \(b\) runs over the integers of an interval \(\mathcal I\) on which \(b+u\in[H,2H]\). Let \(S=\sum_{b\in\mathcal I}e(F(b))\) with \(F(y)=(v/2\pi)\log(y+u)\), and

\[
\begin{gathered}
y_*=\frac{\log|v|}{\log H}.
\end{gathered}
\]

For large \(x\), \(\log H\ge L/T^2-C_0T\ge L/(2T^2)\) and \(\log|v|\le3L+2\), so \(y_*\le7T^2\).

*The case \(y_*<4/5\).* Then \(|v|<H^{4/5}<\pi H\), and the proof of Lemma 1.1 of [*Logarithmic phases at polynomial scales*](logarithmic-phases-at-polynomial-scales.md), which uses only \(b+u\in[H,2H]\), gives \(|S|\ll H/|v|\le H\exp(-L/(2T^2))\).

*The case \(y_*\ge4/5\).* Put

\[
\begin{gathered}
M=\lfloor H^{3/4}\rfloor,\qquad k=\lceil4y_*+8\rceil,
\end{gathered}
\]

so that \(12\le k\le28T^2+9\). Shifting the summation by \(h\in[1,M]\) changes \(S\) by at most \(2h\) terms, so

\[
\begin{gathered}
\Bigl|S-\frac1M\sum_{h=1}^M\sum_{b\in\mathcal I}e\bigl(F(b+h)\bigr)\Bigr|\le2M.
\end{gathered}
\]

Taylor's formula with \(\alpha_j(b)=F^{(j)}(b)/j!\)\(=(-1)^{j-1}v/(2\pi j(b+u)^j)\) gives \(F(b+h)=F(b)+\sum_{j\le k}\alpha_j(b)h^j+R\), where

\[
\begin{gathered}
|R|\le\frac{|v|}{2\pi}\Bigl(\frac MH\Bigr)^{k+1}\\
\le H^{y_*-(k+1)/4}\le H^{-9/4},
\end{gathered}
\]

because \(M\le H^{3/4}\) and \((k+1)/4\ge y_*+9/4\). With \(S_k(\boldsymbol\alpha)=\sum_{h\le M}e(\sum_{j\le k}\alpha_jh^j)\) this yields

\[
\begin{gathered}
|S|\le\frac1M\sum_{b\in\mathcal I}\bigl|S_k(\boldsymbol\alpha(b))\bigr|\\
+2M+1.\quad(2.2)
\end{gathered}
\]

*Occupancy.* Divide \([0,1)^k\) into the \(M^\kappa\) boxes that are products of intervals of length \(M^{-j}\) in the \(j\)th coordinate. We claim that each box contains \(\boldsymbol\alpha(b)\bmod1\) for at most \(e^{O(k)}H^{4/5}\) values of \(b\). Let \(j_0=\lceil y_*+3/20\rceil\), so \(1\le j_0\le y_*+23/20\le k\). The coordinate \(\alpha_{j_0}(b)\) has modulus at most \(H^{y_*-j_0}\le H^{-3/20}<\frac12\) and is monotone in \(b\), with

\[
\begin{gathered}
\Bigl|\frac{d\alpha_{j_0}}{db}\Bigr|=\frac{|v|}{2\pi(b+u)^{j_0+1}}\ge\frac{H^{y_*-j_0-1}}{2\pi\,2^{j_0+1}} .
\end{gathered}
\]

An interval of length \(M^{-j_0}\le2^{j_0}H^{-3j_0/4}\) on the circle meets \((-\frac12,\frac12)\) in at most two intervals of total length \(M^{-j_0}\), whose preimage under \(\alpha_{j_0}\) has total length at most \(e^{O(k)}H^{1+j_0/4-y_*}\). Since \(y_*\ge4/5\),

\[
\begin{gathered}
1+\frac{j_0}4-y_*\le1-\frac{3y_*}4+\frac{23}{80}\\
\le1-\frac5{16},
\end{gathered}
\]

and the preimage contains at most \(e^{O(k)}H^{11/16}+2\) integers, which proves the claim.

*Suprema over boxes.* For every \(s\ge1\),

\[
\begin{gathered}
\sum_Q\sup_{\boldsymbol\alpha\in Q}|S_k(\boldsymbol\alpha)|^{2s}\\
\le(4\pi)^{2sk}M^\kappa J_{s,k}(M).\quad(2.3)
\end{gathered}
\]

To see this, rescale a box \(Q\) to the unit cube by \(\alpha_j=\beta_j+\theta_jM^{-j}\) and let \(\Phi(\boldsymbol\theta)\) be \(S_k\) in these coordinates. In one variable, \(\phi(\theta)=\phi(\theta')+\int_{\theta'}^\theta\phi'\) and averaging over \(\theta'\in[0,1]\) give \(|\phi(\theta)|\le\int_0^1|\phi|+\int_0^1|\phi'|\). Applying this in each coordinate, \(\sup|\Phi|\le\sum_{\boldsymbol\epsilon\in\{0,1\}^k}\int_{[0,1]^k}|\partial^{\boldsymbol\epsilon}\Phi|\), and by Hölder's inequality

\[
\begin{gathered}
\sup|\Phi|^{2s}\le2^{k(2s-1)}\sum_{\boldsymbol\epsilon}\int_{[0,1]^k}|\partial^{\boldsymbol\epsilon}\Phi|^{2s}.
\end{gathered}
\]

Each \(\partial^{\boldsymbol\epsilon}\Phi\) is an exponential sum of the same shape as \(S_k\) whose coefficients \(\prod_{j:\epsilon_j=1}2\pi i(h/M)^j\) have modulus at most \((2\pi)^k\). Summing over the boxes undoes the rescaling at the cost of the factor \(M^\kappa\), and the full-torus moment of such a sum is at most \((2\pi)^{2sk}J_{s,k}(M)\) by Lemma 1.1(1). This proves (2.3).

*Conclusion.* Take \(s\) from Theorem 1.4. By Hölder's inequality, the occupancy bound, (2.3) and (1.2),

\[
\begin{aligned}
&\frac1M\sum_{b\in\mathcal I}|S_k(\boldsymbol\alpha(b))|\\
&\quad\le\frac{(2H)^{1-1/(2s)}}M\\
&\qquad\times\Bigl(\sum_b|S_k(\boldsymbol\alpha(b))|^{2s}\Bigr)^{1/(2s)}\\
&\quad\le2H\bigl(e^{O(sk+k^{C_2})}H^{-1/5}M^{1/100}\bigr)^{1/(2s)} .
\end{aligned}
\]

Here \(H^{-1/5}M^{1/100}\le H^{-77/400}\), \(sk+k^{C_2}\ll T^{2\max(4,C_2)}\), \(2s\ll T^6\), and \(\log H\ge L/(2T^2)\). Since \(L/T^2\) exceeds every fixed power of \(T\) for large \(x\), the right side is at most \(H\exp(-L/T^9)\). The other terms in (2.2) are \(O(H^{3/4})\), which is smaller. Hence \(|S|\le H\exp(-L/T^{10})\) for large \(x\), and \(|\sum_{n\in I,\,n\equiv a}n^{iv}|=|S|\). \(\square\)

## 3. Exercises

**4.1.** Show that \(J_{k,k}(M)\le k!\lfloor M\rfloor^k\). (Two \(k\)-tuples of integers with the same first \(k\) power sums are permutations of each other.)

**4.2.** Show that \(J_{s,k}(M)\ge\lfloor M\rfloor^{2s}/\prod_{j\le k}(s\lfloor M\rfloor^j+1)\), and deduce that the exponent \(2s-\kappa\) in (1.2) cannot be lowered.

**4.3.** Show that Lemma 1.2 fails for \(r=k=2\) and \(h=2\): find two pairs with distinct residues modulo \(2\), equal power sums modulo \(4\), that are not permutations of each other modulo \(4\).

**4.4.** In the proof of Theorem 2.1, take \(y_*=1\). Compute \(k\) and \(j_0\), and check the occupancy exponent \(1+j_0/4-y_*\).

**4.5.** Deduce from Theorem 2.1 and partial summation that, under its hypotheses, \(\sum_{n\in I,\,n\equiv a}n^{-\sigma+iv}\)\(\ll N^{1-\sigma}q^{-1}\exp(-L/T^{C_3})\) uniformly for \(|\sigma-1|\le1/L\).

## 4. Solutions

**4.1.** If \(\mathbf u\) and \(\mathbf v\) have the same power sums \(p_1,\dots,p_k\), Newton's identities over \(\mathbb Q\) give the same elementary symmetric functions, hence the same polynomial \(\prod(X-u_i)=\prod(X-v_i)\), so \(\mathbf v\) is a permutation of \(\mathbf u\). For each of the \(\lfloor M\rfloor^k\) choices of \(\mathbf u\) there are at most \(k!\) choices of \(\mathbf v\).

**4.2.** Let \(R(\mathbf c)\) be the number of \(\mathbf u\in\{1,\dots,\lfloor M\rfloor\}^s\) with power-sum vector \(\mathbf c\). Then \(\sum R=\lfloor M\rfloor^s\) and \(J_{s,k}(M)=\sum R^2\). The vector \(\mathbf c\) takes at most \(\prod_j(s\lfloor M\rfloor^j+1)\) values, so Cauchy's inequality gives the bound. The denominator is \(\asymp_{s,k}M^\kappa\), so \(J_{s,k}(M)\gg_{s,k}M^{2s-\kappa}\), and a bound \(M^{2s-\kappa-\eta}\) with \(\eta>0\) is impossible for large \(M\).

**4.3.** Take \(\mathbf z=(0,1)\) and \(\mathbf z'=(2,3)\). Both have entries \(0,1\) modulo \(2\). Their sums are \(1\) and \(5\equiv1\) modulo \(4\), and their sums of squares are \(1\) and \(13\equiv1\) modulo \(4\). But \(\{2,3\}\ne\{0,1\}\) modulo \(4\). The proof breaks at Newton's identity \(2e_2=e_1p_1-p_2\), which cannot be divided by \(2\).

**4.4.** For \(y_*=1\), \(k=\lceil12\rceil=12\) and \(j_0=\lceil1.15\rceil=2\). Then \(1+j_0/4-y_*=1/2\le11/16\), so each box contains \(e^{O(k)}H^{1/2}\) points.

**4.5.** By Lemma 4.2 of Lesson 3 with \(g(n)=n^{-\sigma}\), whose supremum plus variation on \([N,2N]\) is at most \(2N^{-\sigma}\), the sum is at most \(2N^{-\sigma}\) times the maximum of (2.1) over initial segments of \(I\).

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Appendix, Lemmas 9.2–9.5. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
- T. D. Wooley, *Vinogradov's mean value theorem via efficient congruencing*, Annals of Mathematics 175 (2012), 1575–1627, Section 2, explains Linnik's \(p\)-adic form of the classical iteration. Free version: arXiv:1101.0574. https://arxiv.org/abs/1101.0574
