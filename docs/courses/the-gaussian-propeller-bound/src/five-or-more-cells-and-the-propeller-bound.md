# Five or more cells and the propeller bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the Gaussian propeller bound stated in [Gaussian first moments of partitions](gaussian-first-moments-of-partitions.md), using the bounds of the three lessons before it. We are in the standing setting (S1)–(S6) of that lesson: a hypothetical optimal partition with value \(C>9/(8\pi)\) and \(m\ge5\) active cells. The earlier lessons provide two kinds of information about the normalized lengths \(r_j\) and the cell measures \(P_j\).

*Scalar bounds* ([Rearrangement bounds for one cell](rearrangement-bounds-for-one-cell.md), Proposition 2.4, and [Ehrhard concavity and the loss of one score](ehrhard-concavity-and-the-loss-of-one-score.md), Proposition 5.2). With \(A=0.929\) if \(m=5\) and \(A=0.884\) if \(m\ge6\),
\[
\begin{gathered}
r_j<\frac23,\qquad P_j>Ar_j^2,\\
P_j>0.415\,r_j+0.15\,r_j^2,
\end{gathered}
\]
and \(\sum_jP_j=\sum_jr_j^2=1\).

*Geometric constraints* ([Two competing scores](two-competing-scores.md), Corollary 3.1). With the lengths ordered as \(r_1\ge\dots\ge r_m=t\), \(L=r_1^2+r_2^2\) and \(c=r_3^2\), the inequalities (C1), on the first line, and (C2), on the second, hold:
\[
\begin{aligned}
(c-t^2)(L-c-2t^2)&\le8(3/\pi)^2t^2,\\
\tfrac32(c-t^2)^2&\le10(3/\pi)^2t^2.
\end{aligned}
\]

We show that they are incompatible. First the smallest length is confined to \(0.066<t<0.12\); then the third length is shown to satisfy \(c>2.6t\), which contradicts (C2).

## 1. The probability budget

Put
\[
\begin{gathered}
d=A-0.15,\qquad s=\frac{0.415}d,\\
e(u)=0.415u-du^2 ,
\end{gathered}
\]
so \(d=0.779\) for \(m=5\) and \(d=0.734\) for \(m\ge6\). The *excesses* \(\delta_j=P_j-Ar_j^2\) satisfy the *budget* (1.1):
\[
\begin{gathered}
\delta_j>\max\{0,e(r_j)\}\quad(1\le j\le m),\\
\sum_{j=1}^m\delta_j=1-A .
\end{gathered}
\]
Indeed \(\delta_j>0\) is the second scalar bound, and the third gives \(\delta_j>0.415r_j+0.15r_j^2-Ar_j^2=e(r_j)\). The function \(e\) is a concave quadratic with roots \(0\) and \(s\) and maximum at \(s/2\).

All finite comparisons below are stated with exact rationals or strict rational bounds, obtained with the enclosures of [Rearrangement bounds for one cell](rearrangement-bounds-for-one-cell.md), Section 3.

## 2. The third length

**Step 1.** \((1-L)\bigl(0.415/\sqrt c-0.734\bigr)\le0.116\), and \(\sqrt c>0.23\).

**Proof.** For \(j\ge3\), \(r_j\le\sqrt c\), so \(e(r_j)=r_j^2(0.415/r_j-d)\), which is at least \(r_j^2(0.415/\sqrt c-d)\). Summing over \(j\ge3\) and using (1.1) and \(\sum_{j\ge3}r_j^2=1-L\),
\[
(1-L)\Bigl(\frac{0.415}{\sqrt c}-d\Bigr)\le1-A .
\]
For \(A=0.884\) this is the first claim. For \(A=0.929\), add \(0.045(1-L)\le0.045\) to both sides: \(0.779-0.045=0.734\) and \(0.071+0.045=0.116\).

Since \(r_1,r_2<\frac23\), \(L<\frac89\) and \(1-L>\frac19\). If \(\sqrt c\le0.23\), then \(0.415/\sqrt c-0.734\) is at least \(0.415/0.23-0.734>0\), and the left side of the first claim exceeds its right side by at least
\[
\begin{aligned}
&\frac19\Bigl(\frac{0.415}{0.23}-0.734\Bigr)-0.116\\
&\quad=\frac{101}{34500}>0 ,
\end{aligned}
\]
a contradiction. \(\square\)

## 3. The smallest length from below

**Step 2.** \(t>0.066\).

**Proof.** Suppose \(t\le q_0=0.066\). We contradict (C1), whose right side is at most \(8(3/\pi)^2q_0^2\).

If \(\sqrt c\ge0.44\), then \(L\ge2c\) (because \(r_1,r_2\ge r_3\)), so \(L-c-2t^2\ge c-2t^2\), and
\[
\begin{aligned}
&(c-t^2)(L-c-2t^2)\\
&\quad\ge(0.44^2-q_0^2)(0.44^2-2q_0^2).
\end{aligned}
\]
Both factors on the right are positive, and
\[
\begin{aligned}
&(0.44^2-q_0^2)(0.44^2-2q_0^2)\\
&\quad-8(3/\pi)^2q_0^2>0.00321132 .
\end{aligned}
\]

If \(0.23<\sqrt c<0.44\), then \(\sqrt c\) lies in one of the intervals \([a,b]\) of Table 1. There \(0.415/\sqrt c-0.734\) is at least \(0.415/b-0.734>0\), so Step 1 gives \(1-L\le0.116/(0.415/b-0.734)\). With \(c\le b^2\) and \(t\le q_0\) this gives \(L-c-2t^2\ge M(b)\), where
\[
\begin{aligned}
M(b)&=1-\frac{0.116}{0.415/b-0.734}\\
&\quad-b^2-2q_0^2 .
\end{aligned}
\]
Also \(c-t^2\ge a^2-q_0^2>0\). Every \(M(b)\) is positive, and the last column of Table 1 shows \((a^2-q_0^2)M(b)>8(3/\pi)^2q_0^2\), contradicting (C1). \(\square\)

*Table 1. Excluding \(t\le0.066\) when \(\sqrt c<0.44\).*

| \([a,b]\) | \(M(b)>\) | \((a^2-q_0^2)M(b)-8(3/\pi)^2q_0^2>\) |
|---|---|---|
| \([0.23,0.30]\) | 0.72264 | 0.00330237 |
| \([0.30,0.35]\) | 0.61198 | 0.02063552 |
| \([0.35,0.41]\) | 0.40621 | 0.01621418 |
| \([0.41,0.44]\) | 0.24314 | 0.00803616 |

## 4. The lengths after the third

**Step 3.** \(r_j\le0.42\) for every \(j\ge4\).

**Proof.** Suppose \(r_4>0.42\); then \(r_1,\dots,r_4>0.42\). Put \(K=d\cdot0.42/(s+0.42)\). For \(u\ge0.42\) the following inequality (4.1) holds:
\[
\max\{0,e(u)\}\ge K(s^2-u^2).
\]
Indeed, for \(0.42\le u\le s\) we have \(e(u)=\frac{du}{s+u}(s^2-u^2)\) and \(\frac u{s+u}\ge\frac{0.42}{s+0.42}\) (here \(0.42<s\)); for \(u>s\) the right side of (4.1) is negative. Applying (4.1) to \(r_1,\dots,r_4\) and using \(\sum_{j\le4}r_j^2=1-\sum_{j\ge5}r_j^2\le1-(m-4)t^2\),
\[
\begin{aligned}
\sum_{j=1}^4\delta_j&\ge K\Bigl(4s^2-\sum_{j\le4}r_j^2\Bigr)\\
&\ge K\bigl(4s^2-1+(m-4)t^2\bigr).
\end{aligned}
\]
For \(j\ge5\) the ordering gives \(5r_j^2\le\sum_{i\le5}r_i^2\le1\), and Step 2 gives \(r_j>0.066\); so \(r_j\in[0.066,1/\sqrt5]\). By concavity \(e(r_j)\) is at least the smaller of \(e(0.066)\) and \(e(1/\sqrt5)\), which is \(e(0.066)\) by Table 2; so \(\delta_j>e(0.066)\). With \(t>0.066\), (1.1) gives the inequality (4.2):
\[
\begin{aligned}
1-A&\ge K\bigl(4s^2-1+(m-4)(0.066)^2\bigr)\\
&\quad+(m-4)\,e(0.066).
\end{aligned}
\]
The right side increases with \(m\), by \(K(0.066)^2+e(0.066)>0\) per unit. At the smallest admissible \(m\) (five for \(A=0.929\), six for \(A=0.884\)) it already exceeds \(1-A\), by the last column of Table 2. \(\square\)

*Table 2. Excluding four lengths above \(0.42\).*

| \(A\) | smallest \(m\) | \(e(0.066)\) | \(e(1/\sqrt5)>\) | right side of (4.2) minus \(1-A\), \(>\) |
|---|---|---|---|---|
| 0.929 | 5 | 0.023996676 | 0.02979364 | 0.00092980 |
| 0.884 | 6 | 0.024192696 | 0.03879364 | 0.02229774 |

## 5. The smallest length from above

Put \(k=2\) if \(m=5\) and \(k=3\) if \(m\ge6\). The indices \(4,\dots,m\) are at least \(k\) in number, and by Step 3 their lengths lie in \([t,0.42]\).

**Step 4.** \(ke(t)\le1-A\), \(t\le t_0\), and \(t<0.12\), where \(t_0\) is the smaller root of \(ke(u)=1-A\):
\[
t_0=\frac{0.415-\sqrt{0.415^2-4d(1-A)/k}}{2d}.
\]

**Proof.** By concavity, each of \(k\) indices among \(4,\dots,m\) has \(\delta_j>e(r_j)\ge\min\{e(t),e(0.42)\}\). Exactly, \(ke(0.42)-(1-A)\) equals \(0.0027688\) for \(A=0.929\) and \(0.0184672\) for \(A=0.884\), so the minimum cannot be \(e(0.42)\); hence \(ke(t)\le1-A\), and also \(e(0.42)>(1-A)/k\ge e(t)\). Since \(ke(0.42)>1-A\), the point \(0.42\) lies strictly between the two roots of the concave quadratic \(ke(u)-(1-A)\), and \(t\le0.42\) with \(ke(t)\le1-A\) forces \(t\le t_0\). The enclosures \(0.1070554<t_0<0.1070555\) for \(A=0.929\) and \(0.1176565<t_0<0.1176566\) for \(A=0.884\) give \(t_0<0.12\). \(\square\)

The function \(e\) is increasing on \([0,t_0]\), since \(t_0<s/2\), the abscissa of its maximum.

## 6. The final contradiction

**Step 5.** \(c>2.6t\).

**Proof.** Suppose \(c\le2.6t\). By Step 1, \(\sqrt c\in[0.23,\sqrt{2.6t}]\). The index \(3\) is distinct from the \(k\) indices charged in Step 4, so (1.1) and concavity of \(e\) give the inequality (6.1):
\[
\begin{aligned}
1-A&\ge\min\bigl\{e(0.23),\,e(\sqrt{2.6t})\bigr\}\\
&\quad+ke(t).
\end{aligned}
\]
By Steps 2 and 4, \(t\in[0.066,t_0]\). We show that both alternatives exceed \(1-A\) on this whole interval.

First, \(e\) is increasing on \([0.066,t_0]\), so
\[
\begin{aligned}
&e(0.23)+ke(t)-(1-A)\\
&\quad\ge e(0.23)+ke(0.066)-(1-A)\\
&\quad>0
\end{aligned}
\]
by Table 3. Second, the function
\[
\begin{aligned}
F(t)&=e(\sqrt{2.6t})+ke(t)\\
&=0.415\sqrt{2.6t}-2.6dt\\
&\quad+k(0.415t-dt^2)
\end{aligned}
\]
is strictly concave for \(t>0\), since \(F''(t)=-\frac{0.415\sqrt{2.6}}{4t^{3/2}}-2kd<0\). Its minimum on \([0.066,t_0]\) is attained at an endpoint. Table 3 gives \(F(0.066)>1-A\) and \(2.6t_0<s^2\). The latter means \(\sqrt{2.6t_0}<s\), so \(e(\sqrt{2.6t_0})>0\); since \(ke(t_0)=1-A\), also \(F(t_0)>1-A\). Both alternatives contradict (6.1). \(\square\)

*Table 3. Margins for (6.1). The first numerical column is exact.*

| \(A\) | \(e(0.23)+ke(0.066)-(1-A)\) | \(F(0.066)-(1-A)>\) | \(s^2-2.6t_0>\) |
|---|---|---|---|
| 0.929 | 0.031234252 | 0.01522916 | 0.00546157 |
| 0.884 | 0.013199488 | 0.00253590 | 0.01376450 |

**Step 6.** The contradiction. By Step 5 and Step 4, \(c-t^2>2.6t-t^2=t(2.6-t)\), and \(t(2.6-t)>(2.6-0.12)\,t>0\). With (C2),
\[
\begin{aligned}
10(3/\pi)^2t^2&\ge1.5(c-t^2)^2\\
&>1.5\,(2.6-0.12)^2t^2 .
\end{aligned}
\]
But \(1.5(2.6-0.12)^2-10(3/\pi)^2\) exceeds \(0.10667806\), a contradiction. \(\square\)

## 7. The theorem

**Theorem 7.1** (the Gaussian propeller bound). For all positive integers \(d\) and \(k\), every measurable partition \((A_1,\dots,A_k)\) of \(\mathbb R^d\) satisfies \(\sum_i|z(A_i)|^2\le9/(8\pi)\), with equality for the propeller when \(d\ge2\) and \(k\ge3\). The proof uses the named statement (HJN) and Ehrhard's inequality (EHR), which is proved in the course [Ehrhard's inequality for convex sets](course:ehrhards-inequality-for-convex-sets/gaussian-heat-semigroups-and-a-gradient-bound#the-theorem).

**Proof.** If \(C(n,n+1)>9/(8\pi)\) for some \(n\ge4\), Theorem 4.3 of [Gaussian first moments of partitions](gaussian-first-moments-of-partitions.md), which uses (HJN), gives an optimal partition with \(m\ge5\) active cells satisfying (S1)–(S6), and Steps 1–6 derive a contradiction; Proposition 5.2 of [Ehrhard concavity and the loss of one score](ehrhard-concavity-and-the-loss-of-one-score.md), used in Step 1 onwards, rests on (EHR). Hence \(C(n,n+1)\le9/(8\pi)\) for all \(n\ge4\), and Lemma 1.1(c) of the first lesson transfers the bound to all \(d\) and \(k\). Corollary 2.2 of the first lesson gives the equality case. \(\square\)

The two inputs enter at different places. (HJN) is needed only for optimal partitions with at most four active cells, whose cones lie in a space of dimension at most three. (EHR) is needed only for the linear–quadratic bound; Exercise 6.2 of [Ehrhard concavity and the loss of one score](ehrhard-concavity-and-the-loss-of-one-score.md) shows that the weaker log-concavity of gap probabilities does not suffice for Step 4.

## 8. Gaussian maxima

By the duality of [Gaussian first moments of partitions](gaussian-first-moments-of-partitions.md), Lemma 3.1, the theorem is an inequality for maxima of Gaussian scores. For four scores in its uncentered form it is [HJN, Theorem 1.2]; in the following centered form it holds for any number of scores [OpenAI-GP, Corollary 1.2].

**Corollary 8.1.** Let \(g\) be standard Gaussian in \(\mathbb R^d\), let \(v_1,\dots,v_k\in\mathbb R^d\) and \(\bar v=\frac1k\sum_iv_i\). Then
\[
\begin{aligned}
&\mathbb E\max_{1\le i\le k}\langle v_i,g\rangle\\
&\quad\le\frac3{2\sqrt{2\pi}}\Bigl(\sum_{i=1}^k|v_i-\bar v|^2\Bigr)^{1/2}.
\end{aligned}
\]
The constant is sharp already for three vectors in the plane.

**Proof.** Put \(u_i=v_i-\bar v\). Subtracting the common score \(\langle\bar v,g\rangle\), whose mean is zero, does not change the expected maximum. Let \(z_i\) be the moments of the score partition of \(u_1,\dots,u_k\). By Lemma 3.1 of the first lesson, the Cauchy–Schwarz inequality and Theorem 7.1,
\[
\begin{aligned}
&\mathbb E\max_i\langle v_i,g\rangle=\sum_i\langle u_i,z_i\rangle\\
&\quad\le\Bigl(\sum_i|u_i|^2\Bigr)^{1/2}\Bigl(\sum_i|z_i|^2\Bigr)^{1/2}\\
&\quad\le B\Bigl(\sum_i|u_i|^2\Bigr)^{1/2}.
\end{aligned}
\]
For sharpness take the three moments of the propeller: they sum to zero, their score partition is the propeller, and both inequalities are equalities (the first because each \(u_i\) is a positive multiple of \(z_i\) with the same factor). \(\square\)

A centered Gaussian vector \((X_1,\dots,X_k)\), possibly with singular covariance, has the form \((\langle v_i,g\rangle)_i\): take for \(v_i\) the rows of a square root of the covariance matrix. With \(\bar X=\frac1k\sum_iX_i\), the corollary therefore reads
\[
\begin{aligned}
&\mathbb E\max_iX_i\\
&\quad\le B\Bigl(\sum_i\operatorname{Var}(X_i-\bar X)\Bigr)^{1/2}.
\end{aligned}
\]

## 9. Exercises

**9.1** (easy). Deduce from Corollary 8.1 the uncentered form \(|\mathbb E\max_iX_i|\le B\bigl(\sum_i\mathbb EX_i^2\bigr)^{1/2}\) for centered jointly Gaussian \(X_1,\dots,X_k\).

**9.2** (easy). For \(k=2\), compute \(\mathbb E\max(X_1,X_2)\) exactly and compare it with Corollary 8.1.

**9.3** (medium). Show that with \(A=0.884\) in place of \(0.929\) the argument of Step 4 fails for \(m=5\): compute \(2e(0.42)-(1-A)\) with \(d=0.734\). Which lesson supplies the larger constant?

**9.4** (medium). Where in Steps 1–6 is \(m\ge5\) used?

## 10. Solutions

**9.1.** \(\sum_i\operatorname{Var}(X_i-\bar X)\) equals \(\sum_i\mathbb EX_i^2-k\,\mathbb E\bar X^2\), which is at most \(\sum_i\mathbb EX_i^2\), and \(\mathbb E\max_iX_i\ge\mathbb EX_1=0\).

**9.2.** \(\max(X_1,X_2)\) equals \(\frac12(X_1+X_2)+\frac12|X_1-X_2|\), so \(\mathbb E\max=\frac12\mathbb E|X_1-X_2|=\sigma/\sqrt{2\pi}\) with \(\sigma^2=\operatorname{Var}(X_1-X_2)\). The corollary gives \(B\sigma/\sqrt2=\frac{3}{2\sqrt2}\cdot\frac{\sigma}{\sqrt{2\pi}}\approx1.06\,\sigma/\sqrt{2\pi}\): true but not sharp, since two cells give at most \(1/\pi\) (Exercise 5.4 of the first lesson).

**9.3.** With \(d=0.734\), \(e(0.42)=0.0448224\), so \(2e(0.42)=0.0896448\) is less than \(1-A=0.116\). Then the budget does not exclude that the minimum \(\min\{e(t),e(0.42)\}\) is \(e(0.42)\), and Step 4 gives no upper bound for \(t\). The constant \(0.929\) comes from the comparison with caps on the three-sphere in [Rearrangement bounds for one cell](rearrangement-bounds-for-one-cell.md), Section 2.

**9.4.** In (S1)–(S6) and Lemma 1.1(d) of [Two competing scores](two-competing-scores.md) (the indices \(1,2,3,m\) are distinct and three moments form a proper subset); in Step 3, which needs four lengths and the bound \(r_j\le1/\sqrt5\) for \(j\ge5\); and in Step 4, which needs \(k\ge2\) indices after the third.

## References

- [OpenAI-GP] OpenAI, *The Gaussian propeller bound in every dimension*, OpenAI Math Release preprint, 24 September 2026, Section 5 and Corollary 1.2. https://github.com/openai/math/tree/main/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026
- [HJN] S. Heilman, A. Jagannath and A. Naor, *Solution of the propeller conjecture in \(\mathbb R^3\)*, Discrete & Computational Geometry 50 (2013), 263–305; arXiv:1112.2993. https://arxiv.org/abs/1112.2993
- [KhNa] S. Khot and A. Naor, *Approximate kernel clustering*, Mathematika 55 (2009), 129–165; arXiv:0807.4626. https://arxiv.org/abs/0807.4626
